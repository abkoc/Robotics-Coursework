
import numpy as np

'''==================================================
Initial set up
=================================================='''

#Hyperparameters
SMALL_ENOUGH = 0.005
GAMMA = 0.5         
NOISE = 0.0  

#Define all states
all_states=[]
for i in range(3):
    for j in range(3):
            all_states.append((i,j))

#Define rewards for all states
rewards = {}
for i in all_states:
    if i == (0,2):
        rewards[i] = 1
    else:
        rewards[i] = 0

#Dictionnary of possible actions. We have two "end" states (1,2 and 2,2)
actions = {
    (0,0):('D', 'R'), 
    (0,1):('D', 'R', 'L'),    
    (1,0):('D', 'R', 'U'),
    (1,1):('D', 'R', 'L', 'U'),
    (1,2):('D', 'L', 'U'),
    (2,0):('R', 'U'),
    (2,1):('R', 'L', 'U'),
    (2,2):('L', 'U'),
    }

#Define an initial policy
policy={}
for s in actions.keys():
    policy[s] = np.random.choice(actions[s])

#Define initial value function 
V={}
for s in all_states:
    if s in actions.keys():
        V[s] = 0
    if s == (0,2):
        V[s] = 1



'''==================================================
Value Iteration
=================================================='''

iteration = 0
while (iteration<10):
    # Display current values
    print(f"\n iteration number {iteration}")
    print(f"optimal policy is \n{policy}\n")
    for s in all_states:
        print(f"Value of state {s} is {V[s]}")

    biggest_change = 0
    for s in all_states:            
        if s in policy:
            
            old_v = V[s]
            new_v = 0
            
            for a in actions[s]:
                if a == 'U':
                    nxt = [s[0]-1, s[1]]
                if a == 'D':
                    nxt = [s[0]+1, s[1]]
                if a == 'L':
                    nxt = [s[0], s[1]-1]
                if a == 'R':
                    nxt = [s[0], s[1]+1]

                #Choose a new random action to do (transition probability)
                random_1=np.random.choice([i for i in actions[s] if i != a])
                if random_1 == 'U':
                    act = [s[0]-1, s[1]]
                if random_1 == 'D':
                    act = [s[0]+1, s[1]]
                if random_1 == 'L':
                    act = [s[0], s[1]-1]
                if random_1 == 'R':
                    act = [s[0], s[1]+1]

                #Calculate the value
                nxt = tuple(nxt)
                act = tuple(act)
                v = rewards[s] + (GAMMA * ((1-NOISE)* V[nxt] + (NOISE * V[act]))) 
                if v > new_v: #Is this the best action so far? If so, keep it
                    new_v = v
                    policy[s] = a

       #Save the best of all actions for the state                                 
            V[s] = new_v
            biggest_change = max(biggest_change, np.abs(old_v - V[s]))
         
   #See if the loop should stop now         
    #if biggest_change < SMALL_ENOUGH:
        #break
    iteration += 1

