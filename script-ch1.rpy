label ch1_main:
    stop music fadeout 2.0
    scene bg classroom_day
    with dissolve_scene_full
    play music t6
    "As I explore the hidden files further, vivid memories flood my mind."
    "I see glimpses of moments that never happened in the original game."
    mc "Alternate paths, forgotten choices, and secrets buried deep."

    menu:
        "Remember Sayori's hidden talent":
            jump sayori_talent
        "Uncover Yuri's intricate past":
            jump yuri_past
        "Explore Natsuki's family situation":
            jump natsuki_family

label sayori_talent:
    mc "Sayori... She was always cheerful, but there's more to her."
    mc "In this alternate path, she discovers a hidden talent for painting."
    mc "Her room is filled with canvases, each capturing raw emotions."

    $ sayori_painting = True

    jump next_scene

label yuri_past:
    mc "Yuri's mysterious demeanor hides a complex history."
    mc "In these hidden memories, I see her as a talented pianist."
    mc "Music becomes her refuge, a way to express feelings she can't put into words."

    $ yuri_pianist = True

    jump next_scene

label natsuki_family:
    mc "Natsuki's tough exterior masks a painful reality."
    mc "In this alternate path, I learn about her troubled home life."
    mc "Her love for baking becomes an escape from the chaos."

    $ natsuki_baking = True

    jump next_scene

label next_scene:
    mc "These hidden memories intertwine with our present."
    mc "The blurred lines between reality and fiction grow even more fragile."

    return
