import random

def print_introductory_message():
    '''This function prints out the introduction message of the game.'''
    print '''Congratulations, you are the newest ruler of ancient Samaria, elected
for a ten year term of office. Your duties are to dispense food, direct farming,
and buy and sell land as needed to support your people. Watch out for rat
infestation and the plague! Grain is the general currency, measured in bushels.
The following will help you in your decisions:

     * Each person needs at least 20 bushels of grain per year to survive.

     * Each person can farm at most 10 acres of land.

     * It takes 2 bushels of grain to farm an acre of land.

     * The market price for land fluctuates yearly.

Rule wisely and you will be showeredwith appreciation at the end of your term.
Rule poorly and you will be kicked out of office!'''

def hammurabi():
    '''This function holds the main circle of the game.'''
    starved = 0
    immigrants = 5
    population = 100
    harvest = 3000 # bushels
    bushels_per_acre = 3 # amount harvested
    acres_planted = 1000 # acres planted
    rats_ate = 200 # bushels
    bushels_in_storage = 2800
    acres_owned = 1000
    cost_per_acre = 19 #bushels per acre
    plague_deaths = 0
    print_introductory_message()
    term = 10 #the term of the office

    for year in range(0,term + 1):
        print 'O great Hammurabi!'
        print 'You are in year', year, 'of your ten year rule.'
        print 'In the previous year', starved, 'people starved to death.'
        print 'In the previous year', immigrants, 'people entered the kingdom.'
        print 'The population is now', population,'.'
        print 'We harvested', harvest, 'bushels at', bushels_per_acre, 'bushels per acre.'
        print 'Rats destroyed', rats_ate, 'bushels, leaving', bushels_in_storage, 'bushels in storage.'
        print 'The city owns', acres_owned, 'acres of land.'
        print 'Land is currently worth', cost_per_acre, 'bushels per acre.'
        print 'There were', plague_deaths, 'deaths from the plague.'
        if year == 10:
            office_assess(population, bushels_in_storage)
            break
        else:
            pass

        land_bought = ask_to_buy_land(bushels_in_storage, cost_per_acre)
        if land_bought == 0:
            land_sold = ask_to_sell_land(acres_owned)
        else:
            land_sold = 0
        acres_owned = acres_owned + land_bought - land_sold
        bushels_in_storage = bushels_in_storage + (land_sold - land_bought) * cost_per_acre

        bushels_fed = ask_to_feed_people(bushels_in_storage)
        bushels_in_storage = bushels_in_storage - bushels_fed

        acres_planted = ask_to_plant(population, bushels_in_storage, acres_owned)
        bushels_in_storage = bushels_in_storage - acres_planted * 2

        plague_deaths = people_die_in_plague(population)
        starved = people_starve(population, bushels_fed)
        if starved != None:
            population = population - (plague_deaths + starved)

            immigrants = people_immigrate(acres_owned, bushels_in_storage, population, starved)

            if population * 10 < acres_planted:
                acres_planted = population * 10
            else:
                pass
            bushels_per_acre = grain_harvested_per_acre()
            harvest = bushels_per_acre * acres_planted

            bushels_in_storage = bushels_in_storage + harvest
            rats_ate = rat_ate_grain(bushels_in_storage)
            bushels_in_storage = bushels_in_storage - rats_ate

            population = population + immigrants

            cost_per_acre = land_cost()
        else:
            break
            
def ask_to_buy_land(bushels, cost):
    '''Ask user how many bushels to spend buying land.'''
    acres = get_int('How many acres will you buy, great Hammurabi?')
    while acres * cost > bushels:
        print 'O great Hammurabi, we have but', bushels, 'bushels of grain!'
        acres = get_int('How much land will you buy?')
    return acres

def ask_to_sell_land(acres_owned):
    '''Ask user how many acres of land to sell.'''
    acres = get_int('How many acres of land will you sell?')
    while acres > acres_owned:
        print 'O great Hammurabi, we have but', acres_owned, 'acres of land.'
        acres = get_int('How much land will you sell?')
    return acres

def ask_to_feed_people(bushels_in_storage):
    '''Ask how many bushels of grain to feed the people.'''
    bushels = get_int('How many bushels of grain will you feed the people?')
    while bushels > bushels_in_storage:
        print 'O great Hammurabi, we have but', bushels_in_storage, 'bushels of grain.'
        bushels = get_int('How much grain will you feed the people?')
    return bushels

def ask_to_plant(population, bushels_in_storage, acres_owned):
    '''Ask how many acres of land to plant.'''
    acres = get_int('How many acres of land will you plant?')
    while acres > acres_owned:
        print 'O great Hammurabi, we only have but', acres_owned, 'of land.'
        acres = get_int('How much land will you plant?') 
    while population * 10 < acres:
        print 'O great Hammurabi, we only have but', population, 'people to plant.'
        acres = get_int('How much land will you plant?')
    while acres * 2 > bushels_in_storage:
        print 'O great Hammurabi, we have but', bushels_in_storage, 'bushels of grain.'
        acres = get_int('How much land will you plant?')
    return acres

def people_die_in_plague(population):
    '''Calculates whether there is a plague this year and how many people die.'''
    rand_num = random.randint(1,100)
    if rand_num <= 15:
        people_die = population / 2;
    else:
        people_die = 0
    return people_die

def people_starve(population, bushels_to_feed):
    '''Calculates the number of people starving after hammurabi decides the feeding policy.'''
    people_starve = population - bushels_to_feed / 20
    if people_starve < 0: people_starve = 0
    if people_starve > population * 0.45:
        print 'You are thrown out of office! Game Over!'
        return None
    else:
        return people_starve

def people_immigrate(acres_owned, bushels_in_storage, population, starved):
    '''Calculate the number of people who immigrate into the city.'''
    if starved > 0:
        return 0
    else:
        return (20 * acres_owned + bushels_in_storage) / (100 * population) +1

def grain_harvested_per_acre():
    '''Calculate the grain harvested in a year.'''
    rand_num = random.randint(1,8)
    return rand_num

def rat_ate_grain(bushels_in_storage):
    '''Calculates the amount of grain ate by rats.'''
    rand_num = random.randint(1,100)
    if rand_num <= 40:
        rand_num_ratio = random.randint(1,3)
        grain_infested = rand_num_ratio * bushels_in_storage / 10
    else:
        grain_infested = 0
    return grain_infested

def land_cost():
    rand_num = random.randint(17,23)
    return rand_num

def get_int(message):
    '''Print the message as prompt, and require the user to enter an integer.'''
    answer = None
    while answer == None:
        try:
            answer = int(input(message))
        except:
            print 'Please enter a number.'
    return answer

def office_assess(population, bushels_in_storage):
    print 'You have finished your term of office!'
    if population > 200 and bushels_in_storage > 6000:
        print 'You are doing great! We hope you can take another term!'
    elif population > 100 and bushels_in_storage > 3000:
        print 'You are doing fine! Thank you!'
    else:
        print 'You are a terrible leader!'

hammurabi()
    
