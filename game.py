import math
import random

WIDTH = 800
HEIGHT = 480
TITLE = "Pixel Jumper"


game_state = "menu"
music_on = True

class Player(Actor):
    def __init__(self, pos):
        super().__init__("idle1", pos)

        self.original_width = self.width
        self.original_height = self.height


        self.height = 56

        self.vx = 0
        self.vy = 0
        self.on_ground = False
        self.facing_right = True
        self.frame = 0
        self.anim_timer = 0

    def update(self):
        self.apply_gravity()
        self.move()
        self.animate()

    def apply_gravity(self):
        self.vy += 0.6
        if self.vy > 10:
            self.vy = 10

    def move(self):
        self.x += self.vx
        self.y += self.vy

        self.on_ground = False
        for p in platforms:
            if self.colliderect(p) and self.vy >= 0:
                self.y = p.top - self.height / 2
                self.vy = 0
                self.on_ground = True

        # limites de tela
        if self.x < 0: self.x = 0
        if self.x > WIDTH: self.x = WIDTH
        if self.y > HEIGHT:
            reset_game()

    def jump(self):
        if self.on_ground:
            self.vy = -12
            if music_on:
                sounds.jump.play()

    def animate(self):
        self.anim_timer += 1
        if abs(self.vx) > 0.1:
            if self.anim_timer % 10 == 0:
                self.frame = (self.frame + 1) % 3
                self.image = f"run ({self.frame+1})"
        else:
            if self.anim_timer % 60 == 0:
                self.frame = (self.frame + 1) % 2
                self.image = f"idle{self.frame+1}"


        if not self.facing_right:
            self.image = transform_image_hflip(self.image)
        self.height = 56

def transform_image_hflip(name):
    return name

class Enemy(Actor):
    def __init__(self, pos, direction=1, patrol_limits=None):
        super().__init__("enemy1", pos)

        if patrol_limits:
            self.limit_left = patrol_limits[0]
            self.limit_right = patrol_limits[1]
        else:
            self.limit_left = 50
            self.limit_right = WIDTH - 50


        self.start_pos = pos
        self.start_dir = direction

        self.direction = direction
        self.frame = 0
        self.anim_timer = 0

    def update(self):
        self.x += self.direction * 2
        if self.x < self.limit_left or self.x > self.limit_right:
            self.direction *= -1
        self.animate()

    def animate(self):
        self.anim_timer += 1
        if self.anim_timer % 15 == 0:
            self.frame = (self.frame + 1) % 2
            self.image = f"enemy{self.frame+1}"
    
    def reset(self):
        self.pos = self.start_pos
        self.direction = self.start_dir

player = Player((60, 400))
platforms = [
    Actor("platform", (60, 460)),
    Actor("platform", (320, 460)),
    Actor("platform", (448, 460)),
    Actor("platform", (576, 460)),
    Actor("platform", (704, 460)),
    Actor("platform", (832, 460)),
]
enemies = [
    Enemy((500, 380), patrol_limits=(350, 550)),
]

goal_door = Actor("door", (750, 325))

buttons = [
    {"text": "Start Game", "rect": Rect((300, 200), (200, 50)), "action": "start"},
    {"text": "Sound: OFF", "rect": Rect((300, 270), (200, 50)), "action": "sound"},
    {"text": "Exit", "rect": Rect((300, 340), (200, 50)), "action": "exit"},
]

win_button = {
    "text": "Back to Menu", 
    "rect": Rect((300, 300), (200, 50)),
    "action": "back_to_menu"
}

def go_to_win_screen():
    global game_state
    game_state = "win"
    music.stop()

def go_to_menu():
    global game_state
    game_state = "menu"
    reset_game()

def start_game():
    global game_state
    game_state = "playing"
    if music_on:
        music.play("bg_music")
        music.set_volume(0.5)

def reset_game():
    global player
    player.x, player.y = 100, 400
    player.vx, player.vy = 0, 0
    for e in enemies:
        e.reset()

def toggle_music():
    global music_on
    music_on = not music_on
    if music_on:
        music.play("bg_music")
        music.set_volume(0.5)
        buttons[1]["text"] = "Sound: ON"
    else:
        music.stop()
        buttons[1]["text"] = "Sound: OFF"

def exit_game():
    quit()

def on_mouse_down(pos):
    global game_state
    if game_state == "menu":
        for b in buttons:
            if b["rect"].collidepoint(pos):
                sounds.blip.play()
                if b["action"] == "start":
                    start_game()
                elif b["action"] == "sound":
                    toggle_music()
                elif b["action"] == "exit":
                    exit_game()
    elif game_state == "win":
        if win_button["rect"].collidepoint(pos):
            sounds.blip.play()
            if win_button["action"] == "back_to_menu":
                go_to_menu()

def on_key_down(key):
    if game_state == "playing":
        if key == keys.SPACE:
            player.jump()

def on_key_up(key):
    if game_state == "playing":
        if key in (keys.LEFT, keys.RIGHT):
            player.vx = 0

def update():
    if game_state == "playing":
        handle_input()
        player.update()
        for e in enemies:
            e.update()
            if player.colliderect(e):
                sounds.hit.play()
                reset_game()
        if player.colliderect(goal_door):
            go_to_win_screen()
            sounds.powerup.play()

def handle_input():
    if keyboard.left:
        player.vx = -4
        player.facing_right = False
    elif keyboard.right:
        player.vx = 4
        player.facing_right = True
    else:
        player.vx = 0

def draw():
    if game_state == "menu":
        screen.blit("background", (0, 0))
        screen.draw.text("PIXEL JUMPER", center=(WIDTH/2, 100), fontsize=60, color="white")
        for b in buttons:
            screen.draw.filled_rect(b["rect"], (50, 50, 150))
            screen.draw.text(b["text"], center=b["rect"].center, fontsize=32, color="white")

    elif game_state == "playing":
        screen.blit("background", (0, 0))
        for p in platforms:
            p.draw()
        for e in enemies:
            e.draw()

        goal_door.draw()
        
        player.draw()

        screen.draw.text("→ GOAL", (750, 50), color="yellow")

    elif game_state == "win":
        screen.blit("background", (0, 0)) 
        
        screen.draw.text("You Win!", center=(WIDTH/2, 150), fontsize=80, color="yellow")
        
        b = win_button
        screen.draw.filled_rect(b["rect"], (50, 50, 150))
        screen.draw.text(b["text"], center=b["rect"].center, fontsize=32, color="white")