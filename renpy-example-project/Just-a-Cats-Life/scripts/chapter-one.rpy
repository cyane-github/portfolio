# custom python specific to this chapter
# init python:
    #declare imports

    # declare constants

    # declare variables

    # declare functions

label CHAPTER_ONE:

    scene bg_black

    CHAR_OLD_BOSS "Beyond this point is some mock-up/outline work for what will become the first chapter."

    scene COMIC_CHAPTER_ONE_MOCKUP:
        zoom 2.2 xalign 0.93 yalign 0.1
        ease 0.4 zoom 5 xalign 0.83 yalign 0.19
    $ renpy.pause(0.3, hard=True)
    pause

    scene COMIC_CHAPTER_ONE_MOCKUP:
        zoom 5 xalign 0.83 yalign 0.19
        ease 0.4 zoom 4 xalign 0.83 yalign 0.4
    $ renpy.pause(0.3, hard=True)
    pause

    scene COMIC_CHAPTER_ONE_MOCKUP:
        zoom 4 xalign 0.83 yalign 0.4
        ease 1 zoom 3.8 xalign 0.83 yalign 0.56
    $ renpy.pause(0.9, hard=True)
    pause

    scene COMIC_CHAPTER_ONE_MOCKUP:
        zoom 3.8 xalign 0.83 yalign 0.56
        ease 1.8 zoom 3 xalign 0.9 yalign 0.75
    $ renpy.pause(1.7, hard=True)
    pause

    CHAR_TOCATA "First day of work! Now that I'm here I'll...{nw}"
    menu:
        CHAR_TOCATA "{cps=0}First day of work! Now that I'm here I'll...{/cps}"
        "play games":
            pass
        "play games":
            pass
        "play games":
            pass

    scene COMIC_CHAPTER_ONE_MOCKUP:
        zoom 3 xalign 0.9 yalign 0.75
        ease 1.8 zoom 2.5 xalign 0.99 yalign 0.99
    $ renpy.pause(1.7, hard=True)
    pause

    scene bg_black
    CHAR_OLD_BOSS "Chapter 1 Demo will now end and you will be returned to the main menu"

    jump CHAPTER_ONE_END
