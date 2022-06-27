import random

#All_team = ['TeamA' ,'TeamB','TeamC','TeamD']
TeamA = []
TeamB = []
TeamC = []
TeamD = []
All_team = [TeamA,TeamB,TeamC,TeamD]

All_Allrounder = ['test1','test2','test3','test4','test5','test6','test7','test8','test9','test10']
All_Allrounder_rating =[9,8,8,8,7,7,7,7,6,6]


All_Allrounder_dic =dict(zip(All_Allrounder, All_Allrounder_rating))

print(All_Allrounder_dic)



for rating in All_Allrounder_rating :
    'Getting postion of rating'
    postion = All_Allrounder_rating.index(rating)
    'Conut same rating player'
    n= All_Allrounder_rating.count(rating)

    if n==1 :

        'select any random team'
        select_random_team = random.choice(All_team)
        'Add player name in random team list'
        select_random_team.append(All_Allrounder[postion])
        'Remove selected player'
        All_Allrounder.remove(All_Allrounder[postion])
        'Remove selected player rating'
        All_Allrounder_rating.remove(rating)

    if n >1:
        A = TeamA.count()
        B = TeamB.count()
        C = TeamC.count()
        D = TeamD.count()

        if A or B or C or D:
            pass







print(f'TeamA  :  {TeamA} ')
print(f'TeamB  :  {TeamB} ')
print(f'TeamC  :  {TeamC} ')
print(f'TeamD  :  {TeamD} ')

print(All_Allrounder)
print(All_Allrounder_rating)
