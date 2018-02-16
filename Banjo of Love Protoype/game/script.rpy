# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e =Character("Bob")
define f =Character(" ")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show bob neutral
    with fade

    # These display lines of dialogue.

    e "Hello."

    e "My name is 'placeholder guy until we get actual art'. But you can call me Bob!"
    
    e "I'm currently being made in Python using the engine Renpy in Unity!"
    
    show bob happy
    
    e "Isn't that exciting?!"
    
    show bob neutral
    
    e "Though I AM just a placeholder at the moment."
    
    show bob happy
    
    e "But I'm good at it, right?!"
    
    show bob neutral
    
    e "In any case, this will be a visual novel with a choice making aspect."
    
    e "Do you like choices?"
    
menu:
        "Yes, I do! ":
            jump yes

        "No, I don't.":
            jump no
label yes:
    show bob happy
    
    e "Yay! Then you're in the right place!"
    
    jump end
    
label no:
    show bob confused
    
    e "Then why are you here?!"
    
    jump end

label end:
    
    show bob happy
    
    e "In any case, this is our prototype! I hope that it gave you some insight!"
    
    hide bob happy
    
    f "Note that any stickfigures in this game is purely fictional, and is no way a likeness to anyone"

    # This ends the game.

    return
