import random

def main(): #maybe shared
    database = test_list[:]
    create_lists_for_dict(database)
    fill_lists_for_dict(database)

def constraint_1(database):
    list_of_invite_lists = []
    print "still working"
    while len(list_of_invite_lists) != 10: #10 is number of valid lists we generate
        print "DID WE DO A BIG LOOP?!!?!?!?!?"
        invite_list = [] #list of "names" (really unique numbers)
        no_invites = [] #list of database keys
        pot_invites = [] #list of database keys
        key = random.randint(0, len(database))-1 #might end up making the same list twice?
        print "key is", key
        while len(invite_list) < len(database):
            print "little loop start \ninvite's dislikes:", database[key][2]
            append_disliked(no_invites, database[key])
            print "no_invites:", no_invites
            print "people that like him/her:", database[key][3]
            append_likes(no_invites, pot_invites, database[key][3])
            print "pot_invites:", pot_invites
            if len(pot_invites) == 0:
                break 
            invite_list.append(database[key][0]) #invites him/her
            print "invite list:", invite_list         
            pot_list_key = find_lowest_score(pot_invites) #for pot_invites, key of whom we're next going to invite 
            key = pot_invites[pot_list_key] #key = for database, key of whom we're next going to invite
            no_invites.append(pot_invites[pot_list_key]) #im not sure that this works here. keeps people from being readded to pot_invites
            pot_invites.remove(pot_invites[pot_list_key]) #need next invite off of potential invites  
            print "new key:", key
        if len(invite_list) > 1:
            list_of_invite_lists.append(invite_list)
            print "List of invite lists:", list_of_invite_lists
    print "It might have worked! Here's the list of lists:", list_of_invite_lists
    return


def find_lowest_score(pot_invites):
    """Will rank each potential invite and return the key of best-ranked""" #key works for pot_invites
    score_list = []
    for i in range(0, len(pot_invites)): #just changed it to length #this will result in a list of scores.  Each key will be granted a score, the lower the better
        score(pot_invites[i], database, pot_invites, score_list) #pot_invites[i] will be the key
        print "working"
    return score_list.index(min(score_list))
    

    #returns key of best fit
def score(pot_invite_key, database, pot_invites, score_list): #need pot_invites or database or score list in parameters?
    score = 0
    for i in range(0, len(database[pot_invite_key][4])):
        if database[pot_invite_key][4][i] in pot_invites:
            score = score + 1
            print "working"
    score_list.append(score)
    return



def append_disliked(no_invites, person): 
    for i in range(0, len(person[2])):
        if person[2][i] not in no_invites:
            no_invites.append(person[2][i])
    for i in range(0, len(person[4])): 
        if person[4][i] not in no_invites:
            no_invites.append(person[4][i])
    return
#each element in no_invites will be a database key

def append_likes(no_invites, pot_invites, likes):
    """Checks if the people that liked latest invite should be added to potential invites"""
    for i in range(0, len(likes)):
        if likes[i] not in no_invites:
            pot_invites.append(likes[i])
    return
#each element in append_likes will be a database key
                         
                    

def create_lists_for_dict(main_dict):
    for i in range (0, len(main_dict)):
        main_dict[i].append([]) #1 - x likes  #Do we ever actually use this?
        main_dict[i].append([]) #2 - x dislikes
        main_dict[i].append([]) #3 - likes x
        main_dict[i].append([]) #4 - dislikes x
    return


def fill_lists_for_dict(main_dict):
    for i in range (0, len(main_dict)):
        for j in range (0, len(main_dict[i][0])):
            if main_dict[i][0][j] == 1:
                main_dict[i][1].append(j)
                main_dict[j][3].append(i)
            if main_dict[i][0][j] == -1:
                main_dict[i][2].append(j)
                main_dict[j][4].append(i)
    return


test_list = [[[0, 1, 0, -1, 1]], [[-1, 0, -1, -1, -1]], [[1, -1, 0, -1, -1]], [[1, -1, 0, 0, 0]], [[1, 0, 0, 1, 0]]]
database = test_list[:]
create_lists_for_dict(database)
fill_lists_for_dict(database)
print "database:", database
constraint_1(database)
