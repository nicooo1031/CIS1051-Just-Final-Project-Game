# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Kylo = Character('Kylo', color='#FFFF00')
define J. Doe = Character('J. Doe', color = '#FFFFFF')
define Mike = Character('Mike', color = '#ff0000')
default grace = 0

# The game starts here.

label start:

    scene bg bedroomp
    play music "audio/nipponic dimension.mp3" volume 0.5
    J. Doe "It's cold out today..."
    J. Doe "I don't want to get up, but Kylo..."

    "Kylo is my roommate, and a great one too."
    "He cleans up after himself, pays his bills, and never gives me trouble."
    "And, hes a good friend, a little too good for his own will."
    "Because of that, he gets mixed up with the wrong people sometimes."
    "Lately, he's been complaining about this new co-worker of his that gives him the creeps."
    "He says the co-worker is harmless, but I still offered to walk him home after work."
    "Just the idea of his co-worker taking advatange of him makes me paranoid..."
    
    J. Doe "I should probably get up soon..."
    scene bg daykitchen
    
    J. Doe "I mean... I have time for some food before I head out"
    "As I put my bread in the toaster and look outside, I wonder how this whole thing began."
    "I remember a couple weeks ago when Kylo first told me about Mike..."

    scene bg elevatorf
    with fade
    "Kylo and his new coworker, Mike, stand in the elevator..."
    show kylo hoodie at left 
    show mike normal at right
    Kylo "Hey! You're Mike, the new guy starting today right?"
    Kylo "My name is Kylo, it's nice to meet you!"
    Mike "... hello."
    Kylo "Sorry, I am way too excitable sometimes, I didn't mean to overwhelm you."
    Mike "..."
    Kylo "So, do you need help with anything so far? Are you confused with anything?"
    Mike "..."
    Kylo "... Well, alright. If you need anything, don't hesitate to ask. See you around!"
    hide kylo hoodie
    Mike "..."
    hide mike normal

    scene bg office
    "Chatty Coworker" "I mean, there isn't anything wrong with him, he's just off."
    "Gossipy Coworker" "If by off you mean scary, than I agree. I mean, they're hiring anyone at this point."
    "Chatty Coworker" "*laughs*"
    "Chatty Coworker" "You better hope no one hears you."
    "Gossipy Coworker" "I mean, it's not like I'm saying anything no one else is thinking. The guy's totally a creep. "
    show kylo hoodie at left
    "Gossipy Coworker" "Kylo, perfect, you just got here at the best time."
    "Gossipy Coworker" "What do you think of the new guy? Aren't you scared he's gonna haunt you in your dreams a little?"
    "Chatty Coworker" "Shut up! You're so loud..."
    Kylo "Stop talking about him like that, he's just quiet. There isn't anything wrong with that."
    "Gossipy Coworker" "C'mon, you don't have to pretend to be this nice guy, it's fine if you think he's weird."
    Kylo "If anything, I think you're being weird. I really don't think there's anything wrong with him."
    show mike normal at right
    "Gossipy Coworker" "New guy! Hey!"
    Mike "..."
    Mike "Hello Kylo..."
    hide kylo hoodie 
    show kylo normal at left
    Kylo "Hey Mike! These guys were just welcoming you into the new place, right?"
    "Chatty Coworker" "Right, Welcome Mike."
    "Gossipy Coworker" "... Yeah, welcome."
    "Gossipy Coworker" "Mike, I have a question for you?"
    Kylo "Don't start..."
    "Gossipy Coworker" "Why did you only say hi to Kylo?"
    "Gossipy Coworker" "I mean, he didn't even acknowledge you when you walked in."
    Kylo "Enough."
    Mike "He's my friend."
    "Mike proceeds to walk away"
    hide mike normal
    "Gossipy Coworker" "Well, Kylo, didn't know you and Mikey were such good buddies."
    Kylo "I mean, I just met him today, but yea, he's my friend, so enough with the talking behind his back, please?"
    
    scene bg breakroom
    show kylo hoodie at left
    show mike normal at right
    Kylo "Mike, hey, don't mind our coworkers, sometimes they're a little too nosey for their own good."
    Mike "..."
    Mike "It's fine, I hope it didn't change your opinion of me."
    Kylo "Of course not, you still seem like a stand up guy to me."
    Mike "Thank you... that means a lot to me..."
    Kylo "Yea, no worries."
    Mike "Kylo, can I ask you a question?"
    stop music
    Kylo "Of course, whats up?"
    Mike "Are you seeing someone?"
    play music "audio/do not look back.mp3" volume 0.5
    Kylo "Oh! Um, not currently, I guess."
    Mike "Would you like to be?"
    Kylo "I think those type of things happen when they happen, but I don't think anyone minds having a person."
    Mike "Kylo..."
    Mike "Can I walk you home?"
    Kylo "Thanks... I appreciate the offer, but I prefer walking home alone."
    Mike "You shouldn't be outside alone at night, Kylo..."
    Mike "I can make sure you get home safe and sound..."
    Kylo "Um, thanks again, but it's really alright."
    Kylo "Well, I'll see you around Mike..."
    Mike "I'll see you around..."
    Mike "Kylo..."
    stop music
    scene bg daykitchen 
    play music "audio/nipponic dimension.mp3" volume 0.5
    "Something just doesn't seem right about how Kylo explained everything to me..."
    "Who is Mike? And why is he so interested in Kylo?"
    "I glance at the time and notice I'll be late to get to Kylo on time if I stick around longer."
    J. Doe "Time to play bodyguard..."

    scene bg breakroom
    show mike normal
    "I'm waiting for Kylo in the office lobby when a man approaches me."
    Mike "..."
    J.Doe "..."
    J. Doe "Hey, have we met before or something?"
    Mike "..."
    J. Doe "..."
    J. Doe "Right, so I'm just gonna sit over here. I'm waiting for a friend."
    Mike "..."
    Mike "Who are you waiting for?"
    J. Doe "Um, just my roommate."
    Mike "Are you waiting for Kylo?"
    J. Doe "... why do you ask?"
    Mike "He asked me to take his roommate to his office when he got here, so they wouldn't get lost."
    J. Doe "Oh then yea, I'm his roommate."
    J. Doe "Sorry, didn't mean to come across as standoffish, I guess I'm just paranoid."
    Mike "It's fine, you can just follow me..."

    scene bg elevatorf
    show mike normal at right 
    "I notice the guy press the basement floor."
    J. Doe "So, how long have you been working with Kylo?"
    Mike "... long enough."
    J. Doe "Right..."
    Mike "..."
    Mike "Can I ask you a question, Doe?"
    J. Doe "Sure..."
    Mike "Are you Kylo's friend?"
    menu: 
        "Yes, he's my friend.":
            jump choices1_a
        "No, I just live with him.":
            jump choices1_b
    
    label choices1_a: 
        Mike "..."
        "He just stares at the door, as if waiting for something to happen..."
        jump choices1_common
    
    label choices1_b:
        Mike "..."
        Mike "So I'm his only friend..."
        jump choices1_common

    label choices1_common: 
        "As we stand in the elevator, I notice he used my name without asking for it first."



    hide bg elevatorf
    scene bg black
    stop music
    "The elevator opens and you notice that the floor is dark. "
    "You can't make out the space in front of you."
    "You can't see your hand even if it stretched out in front of you."
    Mike "You really shouldn't have come here."
    Mike "Now Kylo is gonna know one less face..."
    hide mike normal 
    "Wait wh-"

    scene basementd empty
    play music "audio/kind reminiscence.mp3"
    J. Doe "Where am I...?"
    scene basement light 
    show mike normal
    Mike "You're in the office's basement, for now..."
    Mike "Depending on how you answer my questions, I'll decide where you go from here."
    J. Doe "Who are you?"
    Mike "You know who I am, my sweet Kylo has mentioned me to you..."
    "No..."
    Mike "So, I have to evaulate if you're good enough to be around him..."
    "There's no way..."
    Mike "I'm going to ask you a series of questions..."
    Mike "If you answer them correctly, I'll let you go and we can pretend none of this happened."
    Mike "If you answer them incorrectly, well, Kylo won't miss you that much anyway."
    J. Doe "How do you know I won't just say what you want to hear..."
    Mike "..."
    Mike "I don't think you want to find out what happens Doe"
    "This is not good..."
    
    Mike "So, first question, are you scared of being alone?"
    menu: 
        "Yes.":
            jump choices2_a
        "No.":
            $ grace +=1
            jump choices2_b
            
        "Why does it matter...":
            jump choices2_c
    label choices2_a:
        Mike "..."
        "Mike did not like that answer..."
        jump choices2_common
    label choices2_b:
        Mike "..."
        Mike "Good..."
        jump choices2_common
    label choices2_c:
        Mike "This will go more smoothly if you just answer the question."
        "He seems annoyed..."
        jump choices2_common
    label choices2_common: 
        Mike "We should continue to the next question..."
    "I'm scared..."
   
    Mike "Are you an introvert or an extrovert?"
    menu: 
        "Introvert.":
            $ grace += 1
            jump choices3_a
        "Extrovert.":
            jump choices3_b
        "PLease let me go...":
            jump choices3_c
    label choices3_a:
        Mike "... Good."
        jump choices3_common
    label choices3_b:
        Mike"..."
        "Mike did not like that answer..."
        jump choices3_common
    label choices3_c: 
        Mike "Not answering the question won't help you."
        jump choices3_common
    label choices3_common:
        Mike "Let's move on."

    Mike "Next question, is your own happiness or the happiness of others more important?"
    menu: 
        "My own.":
            $ grace += 1
            jump choices4_a
        "Other people's happiness.":
            jump choices4_b
        "I dont want to die...":
            jump choices4_c
    
    label choices4_a:
        Mike "Good, it's important to want to move towards your own feats..."
        "What does this even mean...?"
        jump choices4_common
    label choices4_b:
        Mike "You're so bothersome..."
        "Mike did not like that answer..."
        jump choices4_common
    label choices4_c:
        Mike "It's annoying when you don't follow directions..."
        jump choices4_common
    label choices4_common:
        Mike "We're  up on our last question, Doe..."
        "I don't understand why this is happening..."
    
    Mike "If I told you it would be dangerous to stay in this area but you had to leave Kylo behind, would you?"
    menu: 
        "Yes, I would leave on my own.":
            $ grace += 1
            jump choices5_a

        "No, I would stay with my friend.":
            jump choices5_b
        "I just wanna get out of here.":
            jump choices5_c
    label choices5_a: 
        Mike "That's good to focus on yourself..."
        jump choices5_common
    label choices5_b:
        Mike "That's interesting..."
        jump choices5_common
    label choices5_c:
        Mike "Answering like this makes me more resolved on what I must do."
        jump choices5_common
    label choices5_common: 
        Mike "That's all of my questions..."
    Mike "Doe, do you know why I needed to ask you those questions?"
    "You sit there in silence before you answer..."
    "Somehow it feels like your response won't matter here..."
    menu: 
        "Yes.":
            jump choices6_a
        "No.":
            jump choices6_b
    label choices6_a:
        Mike "Good, I'm glad you understand..."
        jump choices6_common
    label choices6_b:
        Mike "That's unfortunate, I'll help you understand..."
        jump choices6_common
    label choices6_common:
        Mike "It's important to know why..."


    scene bg peaceful
    Mike "Have you ever felt at peace with someone?"
    Mike "Like, truly at peace and relaxed, and like you could just be yourself?"
    show kylo peaceful 
    Mike "That's how Kylo makes me feel..."
    Mike "He's kind and open, and a ball of sunshine..."
    Mike "I need him safe..."
    Mike "I need him with me..."
    hide kylo peaceful
    scene basement light
    show mike normal 
    Mike "So, you see Doe, I can't have anything jeopardize that for me..."
    Mike "Or anyone..."
    J. Doe "Please..."
    Mike "So, this is how this will be handled..."
    jump evaluation 

    label evaluation: 
        if grace >= 3:
            jump safe_game_ending
        else:
            jump dead_game_ending

    label safe_game_ending: 
        Mike "I will let you go, but you can never see Kylo again."
        Mike "If I ever catch you near Kylo again, I'll kill you..."
        Mike "You need to go far away, somewhere where I or Kylo can't find you..."
        Mike "Do you understand...?"
        menu: 
            "Yes, I'll leave.":
                jump escape_safe_ending
            "No, I won't leave.":
                jump dead_safe_ending
        label escape_safe_ending: 
                stop music
                scene bg newlife
                play music "audio/nipponic dimension.mp3" volume 0.5
                "I never heard of Kylo or Mike again..."
                "I was too scared to tell anyone what happened, or to even find a way to tell Kylo..."
                "I feel bad for leaving Kylo behind, but at least he has a new friend..."
                jump end_screen
        label dead_safe_ending: 
                stop music
                Mike "Oh, really?"
                Mike "That's too bad..."
                "Before I know what's happening, Mike jumps towards me and all I can think about is Kylo..."
                "... Good luck with your new friend..."
                jump end_screen
    label dead_game_ending: 
        stop music
        Mike "You know Doe, if you had just been someone who worried about themself..."
        Mike "This wouldn't have to happen."
        Mike "I'll make sure to take care of Kylo, so sleep peacefully okay?"
        "Wait, no!!!"
        jump end_screen
    label end_screen:
        stop music 
        play music "audio/dim existance.mp3"  volume 0.5 
        scene bg black 
        "The End"







    
    


    






    return
