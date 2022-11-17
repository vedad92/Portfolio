                                                                    #STRING MANIPULATIONS

player_1 = 'Ruud Gullit'
player_2 = 'Marco van Basten'

goal_0 = 32
goal_1 = 54

scorers = player_1 + ' ' + str(goal_0) + ', ' + player_2 + ' ' + str(goal_1)

print(scorers)

report = f"""{player_1} scored in the {goal_0}nd minute
{player_2} scored in the {goal_1}th minute""" 

print(report)

player = 'Frank Rijkaard'
first_name = player[:player.find(" ")]
print(first_name)
last_name_len = len(player[player.find('R'):]) #--> lengte 8
#last_name_len = len(player[player.find(" "):]) 
print(last_name_len)

name_short = f'{player[0]}.{player[player.find(" "):]}'
print(name_short)
chant = f'{first_name}! ' * len(first_name)
chant = chant[:-1]
print(chant)

good_chant = chant[-1] != " "
print(good_chant)

                                                                    #LIST MANIPULATIONS

def alphabetical_order(film_names):
    film_names.sort()
    return film_names

film_list = ['filmc','filmf','filmd','filmb','filma']
print(alphabetical_order(film_list))

def won_golden_globe(film_name):
    winner_list = ['Jaws', 'Star Wars', 'ET', 'Geisha']
    film_name_input = True if film_name in winner_list else False
    return film_name_input
print(won_golden_globe('Fightclub'))

def remove_toto_albums(mixed_collection):
    tidy_list = []
    if 'Old Is New' in mixed_collection:
        mixed_collection.remove('Old Is New')
        tidy_list.append('Old Is New')
    if 'Toto XX' in mixed_collection:
        mixed_collection.remove('Toto XX')
        tidy_list.append('Toto XX')
    mixed_collection.sort
    return print(tidy_list)

#def remove_toto_albums(mixed_collection):
  #  tidy_list = []
  #  mixed_collection.remove("Old Is New") 
  #  tidy_list.append('Old Is New')
  #  return print(tidy_list)

father_list = ["Because They're Young", "Checkmate", "Fahrenheit", "Old Is New", "Toto XX"]
remove_toto_albums(father_list)




                                                                    #CASTING
leek_price = 2
print(f'Leek is {str(leek_price)} euro per kilo.')

leek_order = 'Leek 4'
leek_amount = int(leek_order[leek_order.find(" "):])
sum_total = leek_amount * leek_price
print(sum_total)

broccoli_price = 2.34
broccoli_order = 'Broccoli 1.6'
total_price = round(float(broccoli_order[broccoli_order.find(" "):]) * broccoli_price,2)
print((broccoli_order[broccoli_order.find(" "):][1:]) + 'kg' + " " + 'broccoli' + ' ' + 'costs' + ' ' + str(total_price) + 'e')

                                                                
    
    
                                                                    #CONDITIONS

def farm_action(weather, time_of_day, milking_status, cow_location, season, tank_status, grass_status):
    if cow_location == 'pasture' and weather == 'rainy':
        print('take cows to cowshed')
        return 
    elif cow_location == 'cowshed' and weather == 'windy':
        print('milk cows')
        return
    elif cow_location == 'cowshed' and weather != 'sunny' and weather!='windy':
        print('fertilize pasture')
        return
    elif weather == 'sunny' and season == 'spring' and grass_status == True:
        print('mow grass')
        return
    else:
        print('wait')
        return
    
farm_action('rainy','day',False,'pasture','winter',False,False)
farm_action('windy','day',False,'cowshed','winter',False,False)
farm_action('rainy','day',False,'cowshed','winter',True,False)
farm_action('sunny','day',False,'pasture','spring',False,True)





