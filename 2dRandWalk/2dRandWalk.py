import random
def TwoDRandWalk():
    '''This program simulates the 2 dimensional random walk process.'''
    times = [None]*11
    for i in range(0,11):
        times[i] = [0]*11 #cannot use [[0]*11]*11 to initialize times
    step = [5,5]
    print step
    while step[0] != 0 and step[1] != 0 and step[0] != 10 and step[1] != 10:
        ran = random.randint(1,4)
        if ran == 1:
            step[1] += 1
        elif ran == 2:
            step[1] -= 1
        elif ran == 3:
            step[0] += 1
        elif ran == 4:
            step[0] -= 1
        else:
            pass
        print step
        times[step[0]][step[1]] += 1
    print times

TwoDRandWalk()



    
