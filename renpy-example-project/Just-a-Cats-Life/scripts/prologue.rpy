# custom python specific to this chapter
init python:
    # declare imports
    import re

    # declare constants
    COMIC_PROLOGUE_PATH = "comics/prologue/"
    for path in renpy.list_files():
        if COMIC_PROLOGUE_PATH in path:
            panel_id = re.search('%s(.*).png' %
                                 (COMIC_PROLOGUE_PATH), path).group(1).upper().replace("-", "_")
            renpy.image("COMIC_PROLOGUE_%s" % (panel_id), im.Scale(
                path, 1920, 1080)) # assigns image objects for all prologue comic panels

    BUS_PAUSE_DURATION = COMIC_TRANSITION_EASE_DURATION_DEFAULT/4

    INTERVIEW_APPROACH_LIST = {
        "RATIONAL": "Rational and hard working",
        "SOCIAL": "Social and friendly",
        "KNOWLEDGABLE": "Knowledgable and blunt"
    }

    # declare variables

    # declare functions

# The chapter starts here.
label CHAPTER_PROLOGUE_START:

    scene COMIC_PROLOGUE_BACKGROUND with fade

    # page 1
    pause
    show COMIC_PROLOGUE_1_1 with dissolve:
        comicTransitionEnter(ease_duration=0)
    show COMIC_PROLOGUE_1_2 with COMIC_DISSOLVE:
        comicTransitionEnter(ease_duration=0)
    pause

    show COMIC_PROLOGUE_1_1:
        comicTransitionLeave(COMIC_TRANSITION_DIRECTION["LEAVE"]["LEFT"])
    show COMIC_PROLOGUE_1_2:
        comicTransitionLeave(COMIC_TRANSITION_DIRECTION["LEAVE"]["LEFT"])

    # page 2
    show COMIC_PROLOGUE_2_1:
        comicTransitionEnter(COMIC_TRANSITION_DIRECTION["ENTER"]["RIGHT"])
    $  pauseHard(COMIC_TRANSITION_EASE_DURATION_DEFAULT)
    show COMIC_PROLOGUE_2_2 with COMIC_DISSOLVE:
        comicTransitionEnter(ease_duration=0)
    show COMIC_PROLOGUE_2_3 with COMIC_DISSOLVE:
        comicTransitionEnter(ease_duration=0)
    show COMIC_PROLOGUE_2_4 with COMIC_DISSOLVE:
        comicTransitionEnter(ease_duration=0)
    pause

    show COMIC_PROLOGUE_2_1:
        comicTransitionLeave(COMIC_TRANSITION_DIRECTION["LEAVE"]["UP_RIGHT"])
    show COMIC_PROLOGUE_2_2:
        comicTransitionLeave(COMIC_TRANSITION_DIRECTION["LEAVE"]["UP_RIGHT"])
    show COMIC_PROLOGUE_2_3:
        comicTransitionLeave(COMIC_TRANSITION_DIRECTION["LEAVE"]["UP_RIGHT"])
    show COMIC_PROLOGUE_2_4:
        comicTransitionLeave(COMIC_TRANSITION_DIRECTION["LEAVE"]["UP_RIGHT"])

    # page 2.5
    show COMIC_PROLOGUE_2P5_2:
        comicTransitionEnter(end_xy=COMIC_TRANSITION_DIRECTION["LEAVE"]["LEFT"], ease_duration=0)
    show COMIC_PROLOGUE_2P5_1 at shaking:
        comicTransitionEnter(start_xy=COMIC_TRANSITION_DIRECTION["ENTER"]["DOWN_LEFT"], end_xy=[500, 0], ease_duration=2)
    $ pauseHard(COMIC_TRANSITION_EASE_DURATION_DEFAULT)
    pause BUS_PAUSE_DURATION
    show COMIC_PROLOGUE_2P5_2:
        comicTransitionEnter(
            start_xy=[-1920, 0], ease_duration=3)
    $ pauseHard(3) #matches ease_duration in line above
    pause COMIC_TRANSITION_PAUSE_DURATION_NEW_DAY

    show COMIC_PROLOGUE_2P5_1:
        comicTransitionLeave(end_xy=[-1920, 50], ease_duration=2)
    $  pauseHard(2)
    CHAR_TOCATA "{i}8: 21 am.\n{w}I wonder if there’s always that many people already being active at that time of the day.{/i}"
    show COMIC_PROLOGUE_2P5_2:
        comicTransitionLeave(COMIC_TRANSITION_DIRECTION["LEAVE"]["LEFT"])

    # page 3
    show COMIC_PROLOGUE_3_1:
        comicTransitionEnter(COMIC_TRANSITION_DIRECTION["ENTER"]["RIGHT"])
    show COMIC_PROLOGUE_3_1_1:
        comicTransitionEnter(COMIC_TRANSITION_DIRECTION["ENTER"]["RIGHT"])
    $  pauseHard(COMIC_TRANSITION_EASE_DURATION_DEFAULT)
    CHAR_TOCATA "{i}Someone misses their train right in front of me, and they’re annoyed for a moment.{/i}"
    show COMIC_PROLOGUE_3_2 with COMIC_DISSOLVE:
        comicTransitionEnter(ease_duration=0)
    CHAR_TOCATA "{i}I imagine them checking their phone for the next connection, only to find one within the next 13 minutes.{/i}"
    CHAR_TOCATA "{i}With how hasty they’re being, they might drop their phone.{/i}"
    show COMIC_PROLOGUE_3_3 with COMIC_DISSOLVE:
        comicTransitionEnter(ease_duration=0)
    CHAR_TOCATA "{i}Not like their screen would shatter though, being lucky it only hits the screens protective glass.{/i}"


    show COMIC_PROLOGUE_3_1:
        comicTransitionLeave(COMIC_TRANSITION_DIRECTION["LEAVE"]["UP_RIGHT"])
    show COMIC_PROLOGUE_3_1_1:
        comicTransitionLeave(COMIC_TRANSITION_DIRECTION["LEAVE"]["UP_RIGHT"])
    show COMIC_PROLOGUE_3_2:
        comicTransitionLeave(COMIC_TRANSITION_DIRECTION["LEAVE"]["UP_RIGHT"])
    show COMIC_PROLOGUE_3_3:
        comicTransitionLeave(COMIC_TRANSITION_DIRECTION["LEAVE"]["UP_RIGHT"])

    # page 5
    show COMIC_PROLOGUE_5_1:
        comicTransitionEnter(COMIC_TRANSITION_DIRECTION["ENTER"]["DOWN_LEFT"])
    $  pauseHard(COMIC_TRANSITION_EASE_DURATION_DEFAULT)
    CHAR_TOCATA "{i}In a world where 2nd chances are a given, why should I actually try to ace it the very first time?{/i}"

    # page 6
    hide COMIC_PROLOGUE_5_1
    scene COMIC_PROLOGUE_BACKGROUND_FLASHBACK
    show COMIC_PROLOGUE_6_1
    with COMIC_FLASHBACK_FADE
    pause 0.3
    CHAR_OLD_BOSS "We can’t take you like this.{w=0.75}{nw}"

    hide COMIC_PROLOGUE_6_1
    scene COMIC_PROLOGUE_BACKGROUND

    # page 7
    show COMIC_PROLOGUE_7_1
    with Fade(0.1, 0.1, 0.1)
    pause 0.5

    hide COMIC_PROLOGUE_7_1
    show COMIC_PROLOGUE_7_1:
        comicTransitionEnter(ease_duration=0) # This sets up the panel positioning correctly for the leave transition
    CHAR_TOCATA "Hm?"

    show COMIC_PROLOGUE_7_1:
        comicTransitionLeave(COMIC_TRANSITION_DIRECTION["LEAVE"]["UP"], ease_duration=COMIC_TRANSITION_EASE_DURATION_FAST)
    pause COMIC_TRANSITION_PAUSE_DURATION_NEW_DAY

    # page 8
    show COMIC_PROLOGUE_8_1:
        comicTransitionEnter(COMIC_TRANSITION_DIRECTION["ENTER"]["DOWN"], ease_duration=COMIC_TRANSITION_EASE_DURATION_FAST)
    $  pauseHard(COMIC_TRANSITION_EASE_DURATION_FAST)
    show COMIC_PROLOGUE_8_2 with COMIC_DISSOLVE:
        comicTransitionEnter(ease_duration=0)
    pause

    show COMIC_PROLOGUE_8_1:
        comicTransitionLeave(COMIC_TRANSITION_DIRECTION["LEAVE"]["LEFT"])
    show COMIC_PROLOGUE_8_2:
        comicTransitionLeave(COMIC_TRANSITION_DIRECTION["LEAVE"]["LEFT"])

    # page 9
    show COMIC_PROLOGUE_9_1:
        comicTransitionEnter(COMIC_TRANSITION_DIRECTION["ENTER"]["RIGHT"])
    $  pauseHard(COMIC_TRANSITION_EASE_DURATION_DEFAULT)
    show COMIC_PROLOGUE_9_2 with COMIC_DISSOLVE:
        comicTransitionEnter(ease_duration=0)
    show COMIC_PROLOGUE_9_3 with COMIC_DISSOLVE:
        comicTransitionEnter(ease_duration=0)
    show COMIC_PROLOGUE_9_4 with COMIC_DISSOLVE:
        comicTransitionEnter(ease_duration=0)
    pause

    show COMIC_PROLOGUE_9_1:
        comicTransitionLeave(COMIC_TRANSITION_DIRECTION["LEAVE"]["UP"], ease_duration=COMIC_TRANSITION_EASE_DURATION_FAST)
    show COMIC_PROLOGUE_9_2:
        comicTransitionLeave(COMIC_TRANSITION_DIRECTION["LEAVE"]["UP"], ease_duration=COMIC_TRANSITION_EASE_DURATION_FAST)
    show COMIC_PROLOGUE_9_3:
        comicTransitionLeave(COMIC_TRANSITION_DIRECTION["LEAVE"]["UP"], ease_duration=COMIC_TRANSITION_EASE_DURATION_FAST)
    show COMIC_PROLOGUE_9_4:
        comicTransitionLeave(COMIC_TRANSITION_DIRECTION["LEAVE"]["UP"], ease_duration=COMIC_TRANSITION_EASE_DURATION_FAST)
    pause COMIC_TRANSITION_PAUSE_DURATION_NEW_DAY

    # page 10
    show COMIC_PROLOGUE_10_1:
        comicTransitionEnter(COMIC_TRANSITION_DIRECTION["ENTER"]["DOWN"], ease_duration=COMIC_TRANSITION_EASE_DURATION_FAST)
    show COMIC_PROLOGUE_10_1_1 at shaking:
        comicTransitionEnter(COMIC_TRANSITION_DIRECTION["ENTER"]["DOWN"], ease_duration=COMIC_TRANSITION_EASE_DURATION_FAST)
    $  pauseHard(COMIC_TRANSITION_EASE_DURATION_FAST)
    show COMIC_PROLOGUE_10_2 with COMIC_DISSOLVE:
        comicTransitionEnter(ease_duration=0)
    pause

    show COMIC_PROLOGUE_10_1:
        comicTransitionLeave(COMIC_TRANSITION_DIRECTION["LEAVE"]["LEFT"])
    show COMIC_PROLOGUE_10_1_1 at shaking:
        comicTransitionLeave(COMIC_TRANSITION_DIRECTION["LEAVE"]["LEFT"])
    show COMIC_PROLOGUE_10_2:
        comicTransitionLeave(COMIC_TRANSITION_DIRECTION["LEAVE"]["LEFT"])

    # page 11
    show COMIC_PROLOGUE_11_1:
        comicTransitionEnter(COMIC_TRANSITION_DIRECTION["ENTER"]["RIGHT"])
    show COMIC_PROLOGUE_11_1_1:
        comicTransitionEnter(COMIC_TRANSITION_DIRECTION["ENTER"]["RIGHT"])
    $  pauseHard(COMIC_TRANSITION_EASE_DURATION_DEFAULT)
    show COMIC_PROLOGUE_11_2 with COMIC_DISSOLVE:
        comicTransitionEnter(ease_duration=0)
    show COMIC_PROLOGUE_11_3 with COMIC_DISSOLVE:
        comicTransitionEnter(ease_duration=0)
    pause

    show COMIC_PROLOGUE_11_1:
        comicTransitionLeave(COMIC_TRANSITION_DIRECTION["LEAVE"]["UP_RIGHT"])
    show COMIC_PROLOGUE_11_1_1:
        comicTransitionLeave(COMIC_TRANSITION_DIRECTION["LEAVE"]["UP_RIGHT"])
    show COMIC_PROLOGUE_11_2:
        comicTransitionLeave(COMIC_TRANSITION_DIRECTION["LEAVE"]["UP_RIGHT"])
    show COMIC_PROLOGUE_11_3:
        comicTransitionLeave(COMIC_TRANSITION_DIRECTION["LEAVE"]["UP_RIGHT"])

    # page 11.5
    show COMIC_PROLOGUE_11P5_1:
        comicTransitionEnter()
    $  pauseHard(COMIC_TRANSITION_EASE_DURATION_DEFAULT)
    show COMIC_PROLOGUE_11P5_2 with COMIC_DISSOLVE:
        comicTransitionEnter(ease_duration=0)
    show COMIC_PROLOGUE_11P5_3 with COMIC_DISSOLVE:
        comicTransitionEnter(ease_duration=0)
    show COMIC_PROLOGUE_11P5_4 with COMIC_DISSOLVE:
        comicTransitionEnter(ease_duration=0)
    show COMIC_PROLOGUE_11P5_5 with COMIC_DISSOLVE:
        comicTransitionEnter(ease_duration=0)
    pause

    show COMIC_PROLOGUE_11P5_1:
        comicTransitionLeave(COMIC_TRANSITION_DIRECTION["LEAVE"]["UP"], ease_duration=COMIC_TRANSITION_EASE_DURATION_FAST)
    show COMIC_PROLOGUE_11P5_2:
        comicTransitionLeave(COMIC_TRANSITION_DIRECTION["LEAVE"]["UP"], ease_duration=COMIC_TRANSITION_EASE_DURATION_FAST)
    show COMIC_PROLOGUE_11P5_3:
        comicTransitionLeave(COMIC_TRANSITION_DIRECTION["LEAVE"]["UP"], ease_duration=COMIC_TRANSITION_EASE_DURATION_FAST)
    show COMIC_PROLOGUE_11P5_4:
        comicTransitionLeave(COMIC_TRANSITION_DIRECTION["LEAVE"]["UP"], ease_duration=COMIC_TRANSITION_EASE_DURATION_FAST)
    show COMIC_PROLOGUE_11P5_5:
        comicTransitionLeave(COMIC_TRANSITION_DIRECTION["LEAVE"]["UP"], ease_duration=COMIC_TRANSITION_EASE_DURATION_FAST)
    pause COMIC_TRANSITION_PAUSE_DURATION_NEW_DAY

    # page 12
    show COMIC_PROLOGUE_12_1:
        comicTransitionEnter(COMIC_TRANSITION_DIRECTION["ENTER"]["DOWN"], ease_duration=COMIC_TRANSITION_EASE_DURATION_FAST)
    $  pauseHard(COMIC_TRANSITION_EASE_DURATION_FAST)
    show COMIC_PROLOGUE_12_2 with COMIC_DISSOLVE:
        comicTransitionEnter(ease_duration=0)
    CHAR_TOCATA "{i}Fuck, it’s already the 16th--??{/i}"
    CHAR_TOCATA "{i}I missed that one special event in my video game...{/i}"

    show COMIC_PROLOGUE_12_1:
        comicTransitionLeave(COMIC_TRANSITION_DIRECTION["LEAVE"]["LEFT"])
    show COMIC_PROLOGUE_12_2:
        comicTransitionLeave(COMIC_TRANSITION_DIRECTION["LEAVE"]["LEFT"])

    # page 12.5
    # TODO: Make these two panels slide away from each other on the horizonal axis after the pause
    show COMIC_PROLOGUE_12P5_1:
        comicTransitionEnter(COMIC_TRANSITION_DIRECTION["ENTER"]["RIGHT"])
    $  pauseHard(COMIC_TRANSITION_EASE_DURATION_DEFAULT)
    show COMIC_PROLOGUE_12P5_2 with COMIC_DISSOLVE:
        comicTransitionEnter(ease_duration=0)
    pause

    show COMIC_PROLOGUE_12P5_1:
        comicTransitionLeave(COMIC_TRANSITION_DIRECTION["LEAVE"]["UP_RIGHT"])
    show COMIC_PROLOGUE_12P5_2:
        comicTransitionLeave(COMIC_TRANSITION_DIRECTION["LEAVE"]["UP_RIGHT"])

    # page 13
    show COMIC_PROLOGUE_13_1:
        comicTransitionEnter(COMIC_TRANSITION_DIRECTION["ENTER"]["DOWN_LEFT"])
    $  pauseHard(COMIC_TRANSITION_EASE_DURATION_DEFAULT)
    show COMIC_PROLOGUE_13_2 with COMIC_DISSOLVE:
        comicTransitionEnter(ease_duration=0)
    pause

    show COMIC_PROLOGUE_13_1:
        comicTransitionLeave(COMIC_TRANSITION_DIRECTION["LEAVE"]["UP"], ease_duration=COMIC_TRANSITION_EASE_DURATION_FAST)
    show COMIC_PROLOGUE_13_2:
        comicTransitionLeave(COMIC_TRANSITION_DIRECTION["LEAVE"]["UP"], ease_duration=COMIC_TRANSITION_EASE_DURATION_FAST)
    pause COMIC_TRANSITION_PAUSE_DURATION_NEW_DAY

    # page 14
    show COMIC_PROLOGUE_14_1:
        comicTransitionEnter(COMIC_TRANSITION_DIRECTION["ENTER"]["DOWN"], ease_duration=COMIC_TRANSITION_EASE_DURATION_FAST)
    $  pauseHard(COMIC_TRANSITION_EASE_DURATION_FAST)
    CHAR_TOCATA "{i}I stayed awake all night finishing up that one videogame mission using a time cheat...{/i}"
    CHAR_TOCATA "{i}Idk what would even motivate me to stay awake now.{/i}"

    show COMIC_PROLOGUE_14_1:
        comicTransitionLeave(COMIC_TRANSITION_DIRECTION["LEAVE"]["LEFT"])

    # page 15
    show COMIC_PROLOGUE_15_1:
        comicTransitionEnter(COMIC_TRANSITION_DIRECTION["ENTER"]["RIGHT"])
    $  pauseHard(COMIC_TRANSITION_EASE_DURATION_DEFAULT)
    CHAR_TOCATA "{i}This outfit feels too tight, oof.{/i}"
    show COMIC_PROLOGUE_15_2 with COMIC_DISSOLVE:
        comicTransitionEnter(ease_duration=0)
    CHAR_TOCATA "{i}Still... I should put in some minimal effort or I'm fully wasting my time.{/i}"
    show COMIC_PROLOGUE_15_3 with COMIC_DISSOLVE:
        comicTransitionEnter(ease_duration=0)

    CHAR_TOCATA "Hmm... How to present myself for {i}this{/i} interview?{nw}"
    menu:
        CHAR_TOCATA "{cps=0}Hmm... How to present myself for {i}this{/i} interview?{/cps}" #textbox disapears without this
        "[INTERVIEW_APPROACH_LIST[RATIONAL]]":
            $ i_interview_approach = INTERVIEW_APPROACH_LIST['RATIONAL']
            pass
        "[INTERVIEW_APPROACH_LIST[SOCIAL]]":
            $ i_interview_approach = INTERVIEW_APPROACH_LIST['SOCIAL']
            pass
        "[INTERVIEW_APPROACH_LIST[KNOWLEDGABLE]]":
            $ i_interview_approach = INTERVIEW_APPROACH_LIST['KNOWLEDGABLE']
            pass

    if i_interview_approach == INTERVIEW_APPROACH_LIST['KNOWLEDGABLE']:
        $ i_interview_approach_append = "I don't know what I'm supposed to be doing but I can pretend!"
    elif i_interview_approach == INTERVIEW_APPROACH_LIST['SOCIAL']:
        $ i_interview_approach_append = "I'll be the most outgoing person they've ever seen!"
    else:
        $ i_interview_approach_append = "I can do that!"

    CHAR_TOCATA "[i_interview_approach]!{w} [i_interview_approach_append]"

    show COMIC_PROLOGUE_15_1:
        comicTransitionLeave(COMIC_TRANSITION_DIRECTION["LEAVE"]["UP_RIGHT"])
    show COMIC_PROLOGUE_15_2:
        comicTransitionLeave(COMIC_TRANSITION_DIRECTION["LEAVE"]["UP_RIGHT"])
    show COMIC_PROLOGUE_15_3:
        comicTransitionLeave(COMIC_TRANSITION_DIRECTION["LEAVE"]["UP_RIGHT"])

    # page 16
    show COMIC_PROLOGUE_16_1:
        comicTransitionEnter(COMIC_TRANSITION_DIRECTION["ENTER"]["DOWN_LEFT"])
    $  pauseHard(COMIC_TRANSITION_EASE_DURATION_DEFAULT)
    show COMIC_PROLOGUE_16_2 with COMIC_DISSOLVE:
        comicTransitionEnter(ease_duration=0)
    pause

    show COMIC_PROLOGUE_16_1:
        comicTransitionLeave(COMIC_TRANSITION_DIRECTION["LEAVE"]["LEFT"])
    show COMIC_PROLOGUE_16_2:
        comicTransitionLeave(COMIC_TRANSITION_DIRECTION["LEAVE"]["LEFT"])

    # page 17
    show COMIC_PROLOGUE_17_1:
        comicTransitionEnter(COMIC_TRANSITION_DIRECTION["ENTER"]["RIGHT"])
    $  pauseHard(COMIC_TRANSITION_EASE_DURATION_DEFAULT)
    show COMIC_PROLOGUE_17_2 with COMIC_DISSOLVE:
        comicTransitionEnter(ease_duration=0)
    show COMIC_PROLOGUE_17_3 with COMIC_DISSOLVE:
        comicTransitionEnter(ease_duration=0)
    CHAR_TOCATA "[i_interview_approach]... Now to get myself into that mindset-"

    show COMIC_PROLOGUE_17_1:
        comicTransitionLeave(COMIC_TRANSITION_DIRECTION["LEAVE"]["UP_RIGHT"])
    show COMIC_PROLOGUE_17_2:
        comicTransitionLeave(COMIC_TRANSITION_DIRECTION["LEAVE"]["UP_RIGHT"])
    show COMIC_PROLOGUE_17_3:
        comicTransitionLeave(COMIC_TRANSITION_DIRECTION["LEAVE"]["UP_RIGHT"])

    # page 18
    show COMIC_PROLOGUE_18_1:
        comicTransitionEnter(COMIC_TRANSITION_DIRECTION["ENTER"]["DOWN_LEFT"])
    $  pauseHard(COMIC_TRANSITION_EASE_DURATION_DEFAULT)
    show COMIC_PROLOGUE_18_2 with COMIC_DISSOLVE:
        comicTransitionEnter(ease_duration=0)
    pause

    show COMIC_PROLOGUE_18_1:
        comicTransitionLeave()
    show COMIC_PROLOGUE_18_2:
        comicTransitionLeave()

    # end chapter
    jump CHAPTER_PROLOGUE_END
