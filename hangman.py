import random
greeting=(
"""

  _   _                                         _ 
 | | | | __ _ _ __   __ _ _ __ ___   __ _ _ __ | |
 | |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \| |
 |  _  | (_| | | | | (_| | | | | | | (_| | | | |_|
 |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_(_)
                    |___/                         
                    
"""
)

youlose=(
"""

__  __               __                    __
\ \/ /___  __  __   / /   ____  ________  / /
 \  / __ \/ / / /  / /   / __ \/ ___/ _ \/ / 
 / / /_/ / /_/ /  / /___/ /_/ (__  )  __/_/  
/_/\____/\__,_/  /_____/\____/____/\___(_)   
                                             

"""
)

youwin=(
"""

__  __               _       ___       __
\ \/ /___  __  __   | |     / (_)___  / /
 \  / __ \/ / / /   | | /| / / / __ \/ / 
 / / /_/ / /_/ /    | |/ |/ / / / / /_/  
/_/\____/\__,_/     |__/|__/_/_/ /_(_)   
                                         

"""
)

hangman=(
"""
   _________
    |/        
    |              
    |                
    |                 
    |               
    |                   
    |___                 
    """,

"""
   _________
    |/   |      
    |              
    |                
    |                 
    |               
    |                   
    |___                 
    """,

"""
   _________       
    |/   |              
    |   (_)
    |                         
    |                       
    |                         
    |                          
    |___                       
    """,

"""
   ________               
    |/   |                   
    |   (_)                  
    |    |                     
    |    |                    
    |                           
    |                            
    |___                    
    """,


"""
   _________             
    |/   |               
    |   (_)                   
    |   /|                     
    |    |                    
    |                        
    |                          
    |___                          
    """,


"""
   _________              
    |/   |                     
    |   (_)                     
    |   /|\                    
    |    |                       
    |                             
    |                            
    |___                          
    """,



"""
   ________                   
    |/   |                         
    |   (_)                      
    |   /|\                             
    |    |                          
    |   /                            
    |                                  
    |___                              
    """,


"""
   ________
    |/   |     
    |   (_)    
    |   /|\           
    |    |        
    |   / \        
    |               
    |___           
    """)

#string dashes together

while True:
    print greeting
    print("Welcome! Let's play Hangman!")
    pokemon=["ninetails","pikachu","blaziken","vaporeon"]
    food=["apple","cherry","durian","starfruit"]
    colors=["maroon","black","white"]
    print "A) Pokemon B) Food C) Colors"
    user=raw_input("Pick a category: ").lower()
    if user=="a":
        words=pokemon
    elif user=="b":
        words=food
    elif user=="c":
        words=colors
    else:
        print "Invalid answer, try again!"
        pass
    player_guess=None
    chance=0
    chosen_word=random.choice(words).lower()
    #create empty array for chosen word
    dash = len(chosen_word)*['_']
    print hangman[chance]
    print ''.join(dash)
    
    while True:
        correct=False
        player_guess=raw_input("Guess a letter: ")
        
        #loop to check if guess is in chosen word
        for i in range (len(chosen_word)):
            if player_guess == chosen_word[i]:
                dash[i]=player_guess
                correct=True

        #if guess is incorrect, correct should still be false        
        if correct == False:
            chance=chance+1
            print 'Nope!'

        #if chances reach 8, game over
        if chance==7:
            print youlose
            break

        #check if they won by looking for dashes
        winFlag=0
        for i in range (len(chosen_word)):
            if dash[i] == "_":
                winFlag=1
        if winFlag==0:
            print youwin
            break
        
        #reprint updated dash array
        print hangman[chance]
        print ''.join(dash)
        
    #ask to play again 
    replay=raw_input("Would you like to play again (Yes/No)?: ").lower()
    if replay=='yes':
        pass
    else:
        break




