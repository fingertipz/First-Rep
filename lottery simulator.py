import random
import time
pb1picks = [14,19,25,39,68]
pb2picks = [3,43,47,57,67]
pb3picks = [1,3,53,54,61]
pb4picks = [2,37,46,50,68]
pb5picks = [5,10,21,63,65]
pb6picks = [5,6,35,51,56]
pb7picks = [2,27,58,61,69]
pb8picks = [24,30,53,54,62]
pb9picks = [7,18,19,27,39]
pb10picks = [8,20,35,54,56]
pb11picks = [19,25,42,57,61]
pb12picks = [7,18,34,45,49]
pb13picks = [13,14,51,61,66]
pb14picks = [14,24,31,38,46]
pb15picks = [19,23,29,46,56]
pb16picks = [9,25,35,46,55]
pb17picks = [3,11,23,33,59]
pb18picks = [8,13,30,56,62]
pb19picks = [20,25,35,45,64]
pb20picks = [7,13,18,33,61]

pb1 =[21]
pb2 =[7]
pb3 =[16]
pb4 =[23]
pb5 =[23]
pb6 =[1]
pb7 =[6]
pb8 =[5]
pb9 =[2]
pb10 =[1]
pb11 =[1]
pb12 =[15]
pb13 =[10]
pb14 =[10]
pb15 =[15]
pb16 =[4]
pb17 =[16]
pb18 =[2]
pb19 =[14]
pb20 =[16]
pb_list = [pb1picks,pb1],[pb2picks,pb2],[pb3picks,pb3],[pb4picks,pb4],[pb5picks,pb5],[pb6picks,pb6],[pb7picks,pb7],[pb8picks,pb8],[pb9picks,pb9],[pb10picks,pb10],[pb11picks,pb11],[pb12picks,pb12],[pb13picks,pb13],[pb14picks,pb14],[pb15picks,pb15],[pb16picks,pb16],[pb17picks,pb17],[pb18picks,pb18],[pb19picks,pb19],[pb20picks,pb20]
#POWERBALL PICKS ABOVE
#I have double the amount of powerball picks to see the effect of results
#MEGAMILLION PICKS BELOW
mm1 = [17,22,30,60,50,]
mm2 = [13,28,43,61,66]
mm3 = [7,11,33,43,67]
mm4 = [9,24,44,53,63]
mm5 = [21,29,41,46,67]
mm6 = [16,17,18,41,57]
mm7 = [46,52,59,62,64]
mm8 = [9,49,57,61,66]
mm9 = [5,13,38,56,61]
mm10 = [30,31,66,68,70]

mb1 =[4]
mb2 =[7]
mb3 =[14]
mb4 =[23]
mb5 =[19]
mb6 = [25]
mb7 = [1]
mb8 = [13]
mb9 = [18]
mb10 = [12]

ls1 = [mm1,mb1],[mm2,mb2],[mm3,mb3],[mm4,mb4],[mm5,mb5],[mm6,mb6],[mm7,mb7],[mm8,mb8],[mm9,mb9],[mm10,mb10]



mm_num = [x for x in range(1,71)]
megaballs = [x for x in range(1,26)] 

pb_num = [x for x in range(1,70)]
powerballs = [x for x in range(1,27)]

print("POWERBALL SIMULATOR RUNNING....")
def zigzag(counter, maximum):
    iteration, step = divmod(counter, maximum)
    if iteration % 2 == 1:  # go backwards every other iteration
        return maximum - step
    return step

#THIS LOADING STUFF I THOUGHT LOOKED NICE BUT I THINk IT ACTUALLY SLOWS THE PROGRAM DOWN
#BECAUSE IT HAS TO ITERATE THROUGH THE LOOP TO DISPLAY THE LOADING INFO BEFORE THE ACTUAL SIMULATION TAKES PLACE


for x in range(20):
    n_dots = zigzag(x, 4)  # up to 4 dots
    message = f"Loading {'.' * n_dots}"
    print(message.ljust(12), end='\r')
    time.sleep(.1)

def powerball_simulation():
    match1_wpb = 0
    match2_wpb = 0
    match3 = 0
    match3_wpb = 0
    match4 = 0
    match4_wpb = 0
    match5 = 0
    match5_wpb = 0
    match_mb = 0
    
    runs = 0
    
    while runs < 25000:
    
        for num in pb_num:
            lot_nums = random.sample(pb_num, 5)


        for num in powerballs:
            powerball = random.choice(powerballs)
#above code picks a set of winning numbers and a single powerball


        i = 0
        k = 0
#run through every set of powerball picks and powerball to check for matches
        while i < 20: 
            matches = [element for element in lot_nums if element in pb_list[i][k]]
            for x in pb_list[i][1]:
                if x == powerball:
                    continue
                else:
                    continue
            if matches == lot_nums and x == powerball:
                match5_wpb += 1
            elif len(matches) == 5 and x != powerball:
                match5 += 1
            elif len(matches) == 4 and x == powerball:
                match4_wpb += 1
            elif len(matches) == 4 and x != powerball:
                match4 += 1
            elif len(matches) == 3 and x == powerball:
                match3_wpb += 1
            elif len(matches) == 3 and x != powerball:
                match3 += 1
            elif len(matches) == 2 and x == powerball:
                match2_wpb += 1
            elif len(matches) == 1 and x == powerball:
                match1_wpb += 1
            elif len(matches) == 0 and x == powerball:
                match_mb += 1
            i += 1
    #type of matches determined above
    #results displayed after the loop is finished below

        runs += 1
    print("Simulations Executed:\n")
    print(runs,'\n')  
    print ("Match 5 Plus Powerball:",match5_wpb,'\n')
    print ("Match 5:",match5,'\n')
    print ("Match 4 Plus Powerball:",match4_wpb,'\n')
    print ("Match 4:",match4,'\n')
    print ("Match 3 Plus Powerball:",match3_wpb,'\n')
    print ("Match 3",match3,'\n')
    print ("Match 2 Plus Powerball:",match2_wpb,'\n')
    print ("Match 1 Plus Powerball:",match1_wpb,'\n')
    print ("Powerball Match Only:",match_mb,'\n')

def megamillions_simulation():
    
    match1_wpb = 0
    match2_wmb = 0
    match3 = 0
    match3_wpb = 0
    match4 = 0
    match4_wpb = 0
    match5 = 0
    match5_wpb = 0
    match_mb = 0
    runs = 0
    
    while runs < 25000:
    
        for num in mm_num:
            lot_nums = random.sample(mm_num, 5)


        for num in megaballs:
            megaball = random.choice(megaballs)

        i = 0
        k = 0

        while i < 10: 
            matches = [element for element in lot_nums if element in ls1[i][k]]
            for x in ls1[i][1]:
                if x == megaball:
                    continue
                else:
                    continue
            if matches == lot_nums and x == megaball:
                match5_wpb += 1
            elif len(matches) == 5 and x != megaball:
                match5 += 1
            elif len(matches) == 4 and x == megaball:
                match4_wpb += 1
            elif len(matches) == 4 and x != megaball:
                match4 += 1
            elif len(matches) == 3 and x == megaball:
                match3_wpb += 1
            elif len(matches) == 3 and x != megaball:
                match3 += 1
            elif len(matches) == 2 and x == megaball:
                match2_wmb += 1
            elif len(matches) == 1 and x == megaball:
                match1_wpb += 1
            elif len(matches) == 0 and x == megaball:
                match_mb += 1
            i += 1
    

        runs += 1
    print("Simulations Executed:\n")
    print(runs,'\n')  
    print ("Match 5 Plus Megaball:",match5_wpb,'\n')
    print ("Match 5:",match5,'\n')
    print ("Match 4 Plus Megaball:",match4_wpb,'\n')
    print ("Match 4:",match4,'\n')
    print ("Match 3 Plus Megaball:",match3_wpb,'\n')
    print ("Match 3",match3,'\n')
    print ("Match 2 Plus Megaball:",match2_wmb,'\n')
    print ("Match 1 Plus Megaball:",match1_wpb,'\n')
    print ("Megaball Match Only:",match_mb,'\n')


powerball_simulation()
    
print("MEGAMILLIONS SIMULATOR RUNNING....")
def zigzag(counter, maximum):
    iteration, step = divmod(counter, maximum)
    if iteration % 2 == 1:  # go backwards every other iteration
        return maximum - step
    return step

#THIS LOADING STUFF I THOUGHT LOOKED NICE BUT I THING IT ACTUALLY SLOWS THE PROGRAM DOWN
#BECAUSE IT HAS TO ITERATE THROUGH THE LOOP TO DISPLAY THE LOADING INFO BEFORE THE ACTUAL SIMULATION TAKES PLACE

for x in range(20):
    n_dots = zigzag(x, 4)  # up to 4 dots
    message = f"Loading {'.' * n_dots}"
    print(message.ljust(12), end='\r')
    time.sleep(.1)
    
megamillions_simulation()
