####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

import random

team_name = 'team 5' # Only 10 chars displayed.
strategy_name = 'The name the team gives to this strategy'
strategy_description = 'How does this strategy decide?'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
    if len(my_history)==0: # It's the first round: collude
        return 'c'  
               
    elif my_history[-1]=='b' and their_history[-1]=='b':
            return 'b' # Betray if they betray last round  
                  
    elif my_history[-1]=='c' and their_history[-1]=='b':
            return 'b' # Betray if they betray last round
    
    elif 'c' in their_history[-1:] and random.random()<0.3: # If the other player has colluded within last round,              
      #  and 20% of the other rounds
        return 'b'         # Betray and 30% of the other rounds     
    else:
        return 'c'         # but 70% of the time collude
                

           
        

        
        
        
    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    

    


    
