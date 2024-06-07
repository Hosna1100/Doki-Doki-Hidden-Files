label ch2_main:
    stop music fadeout 2.0
    scene bg classroom_day
    with dissolve_scene_full
    play music t6
    "The hidden files continue to unravel secrets."
    "In this alternate path, the blurred lines between reality and fiction blur further."
    "I see glimpses of events that never occurred in the original game."

    menu:
        "Unlock Monika's hidden abilities":
            jump monika_abilities
        "Reveal a different fate for MC":
            jump mc_fate
        "Uncover the truth about the game world":
            jump game_world_truth

label monika_abilities:
    mc "Monika... She's more than just the club president."
    "In these memories, she possesses extraordinary powers."
    "She can manipulate the game world itself."

    $ monika_powers = True

    jump next_scene

label mc_fate:
    "In this path, my fate takes a different turn."
    "Choices I never made lead to unexpected outcomes."
    mc "Is this the real me, or just another possibility?"

    $ mc_different_fate = True

    jump next_scene

label game_world_truth:
    mc "The game world isn't what it seems."
    mc "There's a hidden layer beyond the visual novel."
    "Characters are aware of their existence."

    $ game_world_revelation = True

    jump next_scene

label next_scene:
    "The hidden files pull me deeper into their web."
    mc "What's real? What's fiction? I'm no longer sure."

    return
