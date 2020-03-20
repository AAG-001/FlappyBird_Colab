import os
os.environ["SDL_VIDEODRIVER"] = "dummy"
import pygame
import sys

def load():
    # path of player with different states
    PLAYER_PATH = (
            'DeepLearningFlappyBird/assets/sprites/redbird-upflap.png',
            'DeepLearningFlappyBird/assets/sprites/redbird-midflap.png',
            'DeepLearningFlappyBird/assets/sprites/redbird-downflap.png'
    )

    # path of background
    BACKGROUND_PATH = 'DeepLearningFlappyBird/assets/sprites/background-black.png'

    # path of pipe
    PIPE_PATH = 'DeepLearningFlappyBird/assets/sprites/pipe-green.png'

    IMAGES, SOUNDS, HITMASKS = {}, {}, {}

    pygame.display.init()
    # numbers sprites for score display
    IMAGES['numbers'] = (
        pygame.image.load('DeepLearningFlappyBird/assets/sprites/0.png').convert_alpha(),
        pygame.image.load('DeepLearningFlappyBird/assets/sprites/1.png').convert_alpha(),
        pygame.image.load('DeepLearningFlappyBird/assets/sprites/2.png').convert_alpha(),
        pygame.image.load('DeepLearningFlappyBird/assets/sprites/3.png').convert_alpha(),
        pygame.image.load('DeepLearningFlappyBird/assets/sprites/4.png').convert_alpha(),
        pygame.image.load('DeepLearningFlappyBird/assets/sprites/5.png').convert_alpha(),
        pygame.image.load('DeepLearningFlappyBird/assets/sprites/6.png').convert_alpha(),
        pygame.image.load('DeepLearningFlappyBird/assets/sprites/7.png').convert_alpha(),
        pygame.image.load('DeepLearningFlappyBird/assets/sprites/8.png').convert_alpha(),
        pygame.image.load('DeepLearningFlappyBird/assets/sprites/9.png').convert_alpha()
    )

    # base (ground) sprite
    IMAGES['base'] = pygame.image.load('DeepLearningFlappyBird/assets/sprites/base.png').convert_alpha()

    # sounds
    if 'win' in sys.platform:
        soundExt = '.wav'
    else:
        soundExt = '.ogg'

    pygame.mixer.init()
    SOUNDS['die']    = pygame.mixer.Sound('DeepLearningFlappyBird/assets/audio/die' + soundExt)
    SOUNDS['hit']    = pygame.mixer.Sound('DeepLearningFlappyBird/assets/audio/hit' + soundExt)
    SOUNDS['point']  = pygame.mixer.Sound('DeepLearningFlappyBird/assets/audio/point' + soundExt)
    SOUNDS['swoosh'] = pygame.mixer.Sound('DeepLearningFlappyBird/assets/audio/swoosh' + soundExt)
    SOUNDS['wing']   = pygame.mixer.Sound('DeepLearningFlappyBird/assets/audio/wing' + soundExt)

    # select random background sprites
    IMAGES['background'] = pygame.image.load(BACKGROUND_PATH).convert()

    # select random player sprites
    IMAGES['player'] = (
        pygame.image.load(PLAYER_PATH[0]).convert_alpha(),
        pygame.image.load(PLAYER_PATH[1]).convert_alpha(),
        pygame.image.load(PLAYER_PATH[2]).convert_alpha(),
    )

    # select random pipe sprites
    IMAGES['pipe'] = (
        pygame.transform.rotate(
            pygame.image.load(PIPE_PATH).convert_alpha(), 180),
        pygame.image.load(PIPE_PATH).convert_alpha(),
    )

    # hismask for pipes
    HITMASKS['pipe'] = (
        getHitmask(IMAGES['pipe'][0]),
        getHitmask(IMAGES['pipe'][1]),
    )

    # hitmask for player
    HITMASKS['player'] = (
        getHitmask(IMAGES['player'][0]),
        getHitmask(IMAGES['player'][1]),
        getHitmask(IMAGES['player'][2]),
    )

    return IMAGES, SOUNDS, HITMASKS

def getHitmask(image):
    """returns a hitmask using an image's alpha."""
    mask = []
    for x in range(image.get_width()):
        mask.append([])
        for y in range(image.get_height()):
            mask[x].append(bool(image.get_at((x,y))[3]))
    return mask
