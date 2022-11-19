from helpers import get_countries

countries = get_countries()

def takeSecond(elem):
    return elem[1]

def most_vowels(listofcountries):
    vowels = 'aeiou'
    leader_board = []
    leader_board_name = []
      
    for country in countries:
        vowel_count = 0
        for i in country:
            if i.lower() in vowels:
                vowel_count = vowel_count + 1   
        leader_board.append([country,vowel_count])
        leader_board.sort(key=takeSecond, reverse=True)    
        top_three = leader_board[:3]

    for country,vowel_count in top_three:
        leader_board_name.append([country])

    return leader_board_name

print(most_vowels(countries))

def alphabet_set(countrylist):   
    alphabetical_list = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    char_set = []
    
    for country in countries:
        for i in country:
            if i.lower() in alphabet and country not in alphabetical_list:
                char_set.append(i)
                alphabetical_list.append(country)
            if str(char_set) == alphabet:
                break    
    return alphabetical_list
print(alphabet_set(countries))

def alphabet_set(listofcountries):
    total_list = []
    alphabet_set = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    

    for country in countries:
        for i in country:
            if i.lower() in alphabet and country not in total_list:



def alphabet_set(countries):   
    alphabetical_list = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for country in countries:
        for i in country:
            if i.lower() in alphabet and country not in alphabetical_list:
                alphabet = alphabet.replace(i.lower(),'')
                alphabetical_list.append(country)
            if alphabet == '':
                break    
    return alphabetical_list
print(alphabet_set(countries)) 

txns = [1.09, 23.56, 57.84, 4.56, 6.78]
TAX_RATE = .08
def get_price_with_tax(txn):
    return txn * (1 + TAX_RATE)
final_prices = map(get_price_with_tax, txns)
'''print(list(final_prices))'''

n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('Loop ended.')














def shortest_name(list):
    short_country = min(countries, key=len) 
    return short_country

print(shortest_name(countries))




# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()
    """ Write the calls to your functions here. """
    # print(shortest_names(countries))
    # print(most_vowels(countries))
    # print(alphabet_set(countries))
    # print(len(alphabet_set(countries)))
