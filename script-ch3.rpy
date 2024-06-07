label ch3_main:
    stop music fadeout 2.0
    scene bg classroom_day
    with dissolve_scene_full
    play music t6
    "The hidden files pull me further into their web."
    "In this alternate path, the boundaries between reality and fiction blur beyond recognition."
    "I witness events that defy logic and challenge my understanding."

    menu:
        "Unlock secrets of the game engine":
            jump game_engine_secrets
        "Confront the meta-narrative":
            jump meta_narrative
        "Face the consequences of hidden choices":
            jump hidden_choices_consequences

label game_engine_secrets:
    mc "The game engine itself holds secrets."
    "I discover hidden commands that alter the fabric of the visual novel."
    mc "Is this a glitch or a deliberate design?"

    $ game_engine_revelations = True

    jump next_scene

label meta_narrative:
    "The meta-narrative transcends the characters."
    "I become aware of my role as the player."
    "Choices I make affect not only the characters but the very structure of the game."

    $ meta_narrative_awareness = True

    jump next_scene

label hidden_choices_consequences:
    "The hidden choices ripple through time."
    "I witness alternate realities branching from seemingly insignificant decisions."
    "What if I had chosen differently?"

    $ hidden_choices_impact = True

    jump next_scene

label next_scene:
    "The hidden files rewrite the very code of existence."
    "I question my own agency and the nature of storytelling."

    return
