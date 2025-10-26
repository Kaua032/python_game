# Pixel Jumper

Um jogo de plataforma 2D simples criado em Python com a biblioteca Pygame Zero.

Este projeto foi desenvolvido como um exercício prático e inclui um personagem animado (parado, correndo, pulando), inimigos com patrulha, um menu principal, música, efeitos sonoros e uma tela de vitória.

## Recursos

  * **Personagem Animado:** Animações completas para parado (idle), correndo e pulando.
  * **Inimigos:** Inimigos que patrulham áreas pré-definidas e reiniciam suas posições quando o jogador colide com eles.
  * **Estados de Jogo:** Múltiplos estados de jogo (Menu Principal, Jogando, Tela de Vitória).
  * **Áudio Completo:**
      * Música de fundo (com botão para ligar/desligar).
      * Efeitos sonoros para pulo, clique de botão e colisão com inimigo.
  * **Ciclo de Jogo:** O jogador pode começar pelo menu, jogar o nível, chegar à porta (objetivo) para vencer, e voltar ao menu.

## Requisitos

  * Python 3.7+
  * Biblioteca Pygame Zero (`pgzero`)

## Instalação

Antes de executar, você precisa garantir que tem o Pygame Zero instalado.

1.  Abra o seu terminal (PowerShell, CMD, Prompt de Comando, etc.).

2.  Instale o Pygame Zero usando o `pip`. Este comando instala tanto o `pgzero` quanto a biblioteca `pygame` da qual ele depende:

    ```bash
    python -m pip install pgzero
    ```

## Estrutura de Pastas Obrigatória

O Pygame Zero **exige** que os ficheiros de recursos (assets) estejam em pastas com nomes específicos. O jogo não encontrará as imagens ou sons se a estrutura não for exatamente esta:

```
project_python_game/
├── game.py            # O código principal do jogo
│
├── images/            # Pasta para TODAS as imagens
│   ├── background.png
│   ├── player_idle1.png
│   ├── player_run1.png
│   ├── player_jump1.png
│   ├── platform.png
│   ├── enemy1.png
│   ├── door.png
│   └── ... (e todas as outras imagens de animação)
│
├── music/             # Pasta para a MÚSICA de fundo (longa)
│   └── bg_music.mp3   # (ou .wav, .ogg)
│
└── sounds/            # Pasta para EFEITOS sonoros (curtos)
    ├── jump.wav
    ├── click.wav
    └── hit.wav
```

## Como Executar o Jogo

1.  Abra o seu terminal.

2.  Navegue (usando o comando `cd`) até à pasta onde o seu projeto está guardado:

    ```bash
    # Exemplo de caminho:
    cd C:\Users\user\Documentos\project_python_game
    ```

3.  Use o seguinte comando para executar o jogo através do módulo `pgzrun`:

    ```bash
    python -m pgzrun game.py
    ```

### Solução de Problemas

**Erro de Acentos (`UnicodeDecodeError`):**
Se você adicionar comentários em português (com acentos como `ç` ou `ã`) ao seu código `game.py`, o `pgzrun` pode falhar ao lê-lo. Se isso acontecer, use este comando alternativo que força a codificação UTF-8:

```bash
python -X utf8 -m pgzrun game.py
```

## Controles

  * **Seta Esquerda:** Mover para a esquerda
  * **Seta Direita:** Mover para a direita
  * **Barra de Espaço:** Pular
  * **Clique do Mouse:** Selecionar botões no menu e na tela de vitória
