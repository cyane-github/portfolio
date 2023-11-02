# custom renpy and python functions
init:
    python:
        # declare imports
        import random

        # declare constants
        COMIC_TRANSITION_EASE_DURATION_DEFAULT = 1.6
        COMIC_TRANSITION_EASE_DURATION_FAST = COMIC_TRANSITION_EASE_DURATION_DEFAULT/2
        COMIC_TRANSITION_PAUSE_DURATION_NEW_DAY = COMIC_TRANSITION_EASE_DURATION_DEFAULT/2

        COMIC_DISSOLVE_DURATION = 0.7
        COMIC_FLASHBACK_FADE_DURATION = [0.1, 0, 0.1]

        COMIC_DISSOLVE = Dissolve(COMIC_DISSOLVE_DURATION)
        COMIC_FLASHBACK_FADE = Fade(*COMIC_FLASHBACK_FADE_DURATION)

        COMIC_TRANSITION_DIRECTION = {
            "ENTER": {
                "RIGHT": [1920, 0],
                "DOWN_LEFT": [-1920, 1080],
                "DOWN": [0, -1080]
                },
            "LEAVE": {
                "LEFT": [-1920, 0],
                "UP_RIGHT": [1920, -1080],
                "UP": [0, 1080]
                }
            }

        # declare variables

        # define functions
        def randShakingOffset():
            return random.randint(-4, 4)

        def pauseHard(pauseDuration):
            pauseDuration > 0 and renpy.pause(pauseDuration, hard=True)

    # define custom transforms
    transform comicTransitionEnter(start_xy=[1920, 1080], end_xy=[0, 0], ease_duration=COMIC_TRANSITION_EASE_DURATION_DEFAULT):
        xpos start_xy[0] ypos start_xy[1]
        ease ease_duration xpos end_xy[0] ypos end_xy[1]

    transform comicTransitionLeave(end_xy=[-1920, -1080], ease_duration=COMIC_TRANSITION_EASE_DURATION_DEFAULT):
        ease ease_duration xpos end_xy[0] ypos end_xy[1]

    transform shaking:
        linear 0.1 xoffset randShakingOffset() yoffset randShakingOffset()
        linear 0.1 xoffset randShakingOffset() yoffset randShakingOffset()
        linear 0.1 xoffset randShakingOffset() yoffset randShakingOffset()
        linear 0.1 xoffset randShakingOffset() yoffset randShakingOffset()
        linear 0.1 xoffset randShakingOffset() yoffset randShakingOffset()
        linear 0.1 xoffset randShakingOffset() yoffset randShakingOffset()
        repeat


# declare characters
define CHAR_TOCATA = Character(_("Tocata"), color=PALETTE['TOCATA']['WHITE'], what_outlines=[(2, PALETTE['TOCATA']['PURPLE'])])
define CHAR_OLD_BOSS = Character(_(None), what_outlines=[(2, PALETTE['TOCATA']['BROWN'])], window_style="old_boss")

# declare images
image COMIC_CHAPTER_ONE_MOCKUP = "comics/chapter-one-mockup.jpg"

# The game starts here.
label start:

    # prologue
    jump CHAPTER_PROLOGUE_START
    label CHAPTER_PROLOGUE_END:

    # chapter one
    jump CHAPTER_ONE
    label CHAPTER_ONE_END:

    # Return to the main menu
    return
