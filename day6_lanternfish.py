import sys
attributes = sys.argv

state  = [0,0,0,0,0,0,0,0,0]

attributes.pop(0)
days = int(attributes.pop(0))


startState = list(map(int,attributes))
for fish in startState:
    print(fish)
    state[fish] +=1

print(state)

counter = 0;


while counter < days:
    reproducing = state.pop(0);
    state.append(reproducing)
    state[6] += reproducing
    counter +=1
    print(state)
    print("After %i days: %i fish" %(counter, sum(state)))
