# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Narrator")
define mc= Character ("MC")
define m= Character ("Michael")
define s= Character ("Salina")
define r= Character ("Rose")
define x= Character ("Xel")
define s= Character ("Susie")
define sh= Character ("Shane")
define k= Character ("Kasey")
define q= Character ("???")

                            


# The game starts here.

label start:

   
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

     



    scene black background

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show zap neutral
    hide zap neutral


    q "Sadness. Pain. Lackluster. "
     
    q "These are the descriptive word for my everyday life."
     
    q "Go to work, go home, eat."
     
    q "Day in and day out."
    
    scene town square
     
    mc "That’s the normal, everyday life for me."
    
    mc "The tireless trudge of another work day."
     
    mc "It’s not that i hate my job, rather I hate the idea of having to leave."
     
    mc "Why waste the day with fake smiles and small talk, when I could pursue my true passion?"
    
    mc "I live in the bustling city of tokyfrancisco."
    
    mc "It's a large town, full of vibrant people, bright lights, and glittering attractions."
    
    mc "It's not really my place though. As beautiful as it is, I would rather go somewhere else..."
    
    scene black background
    
    mc "...indoors"
     
    mc "Nothing beat the loneliness of the day like playing an online game full of strangers who will most likely throw a bucket of salt at you and say things about your mom!"
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # This ends the game.
    return
