

import random
bricks = []
no_bricks = []
def setup_bricks():
    
    for i in range(1,61):
        x = random.randint(1,61)
        bricks.append(i)
    tuple3 =(bricks,no_bricks)
    return tuple3 
    
print(setup_bricks())
#how do i add an empty list here that is returned by the function
#why is this list looping severally in an array
#when to use return and when to use print in a function
def shuffle_bricks(bricks):
    shuffled_bricks = random.shuffle(bricks)
    
shuffle_bricks(bricks)  
 #random.sample(bricks, len(bricks))   
 #print(bricks)
 