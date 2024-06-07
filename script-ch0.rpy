label ch0_main:
    stop music fadeout 2.0
    scene bg classroom_day
    with dissolve_scene_full
    play music t6
    mc "What's this? A strange folder hidden within the game files?"
    mc "I've never seen it before. Maybe I should take a closer look."

    menu:
        "Open the folder":
            jump open_folder
        "Ignore it for now":
            jump ignore_folder

label open_folder:
    "As I explore the folder, memories flood back."
    "Snapshots of moments I thought were lost forever."
    mc "Could these be alternate paths I never took?"

    $ hidden_memories = True

    jump next_scene

label ignore_folder:
    mc "Maybe it's best not to delve into this mystery right now."
    mc "I'll leave it alone for the time being."

    jump next_scene

label next_scene:
    mc "Little do I know, these hidden files will change everything."
    mc "The blurred lines between reality and fiction are about to unravel."

    return
