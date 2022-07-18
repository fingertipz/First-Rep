import random
def pick_power_ball():
    print('\n')
    pb_num = [x for x in range(1,70)]
    #Creates a list of powerball numbers
    p_balls = [x for x in range(1,27)]
    #Creates a list of powerballs
    print("Powerball Picks:\n")
    runs = 0
    pb_picks=[]
    p_ballpick=[]
    while runs < 5:
        count = 0
        while count < 5:
            for num in pb_num:
                pb_picks = random.sample(pb_num, 5)
                count = count + 1
#Creates five lists of five random numbers
        for num in p_balls:
            p_ballpick = random.choice(p_balls)
#Chooses a random powerball number for each list 
        print(sorted(pb_picks),' ',p_ballpick)
#Shows those five random numers ordered least to greatest for each list        
        runs += 1
#Same actions take place in the function below
#Small difference in range of numbers from one game to the other
#Aside from that it does the same thing
def pick_mega_mil():
    print('\n')
    lot_num = [x for x in range(1,71)]
    megaplier = [x for x in range(1,26)]


    pick_1=[]
    pick_1mega=[]
    print("MegaMillions Picks:\n")
    runs = 0
    
    while runs < 5:
        for num in lot_num:
            pick_1 = random.sample(lot_num, 5)
            
        for num in megaplier:
            pick_1mega = random.choice(megaplier)
        
        print(sorted(pick_1),' ',pick_1mega)
        
        
        runs += 1

pick_power_ball()
pick_mega_mil()