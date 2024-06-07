label ch4_main:
    stop music fadeout 2.0
    scene bg classroom_day
    with dissolve_scene_full
    play music t6
    "The hidden files have led me to this moment."
    "Paths intertwine, memories collide, and reality fractures."
    "I stand at the crossroads of existence."

    menu:
        "Embrace the meta-narrative":
            jump embrace_meta_narrative
        "Restore the original game":
            jump restore_original_game

label embrace_meta_narrative:
    mc "I choose to embrace the meta-narrative."
    "I step beyond the boundaries of the visual novel."
    "The game acknowledges my presence."

    $ special_ending_meta = True

    jump end_game

label restore_original_game:
    mc "I decide to restore the original game."
    "The hidden files fade away, leaving only memories."
    "The characters return to their scripted paths."

    $ special_ending_restore = True

    jump end_game

label end_game:
    "And so, the hidden files close their story."
    "Reality reasserts itself, and the blurred lines vanish."

    return
