from audioop import add
from helpers import get_countries

def create_passport(name, date_of_birth, place_of_birth, height, nationality):

    passport_dict = {
        "name": name,
        "date_of_birth": date_of_birth,
        "place_of_birth": place_of_birth,
        "height": height,
        "nationality": nationality,
    }

    return passport_dict


print(create_passport("Vedad", "07-08-1992", "Rotterdam", 182, "Netherlands"))


passport_vedad = {
    "name": "vedad",
    "date_of_birth": "07-01-1992",
    "place_of_birth": "brcko",
    "height": 182,
    "nationality": "dutch",
}


"""def add_stamp(passport, country):
    stamps = []
   
    if country not in stamps and passport['nationality'] is not country:
        stamps.append(country)
    
    passport['stamps'] = stamps

    return passport




print(add_stamp(passport_vedad, 'Germany'))"""


def add_stamp(passport, country):
    stamps = []
    if country not in stamps and passport["nationality"] is not country:
        stamps.append(country)
    passport.update({"stamps": stamps})
    return passport


print(add_stamp(passport_vedad, "Belgium"))


fingerprint_data = {
    "left_pinky": "2378945",
    "left_ring": "2349081",
    "left_middle": "132890",
    "left_index": "9823234",
    "left_thumb": "0924131",
    "right_thumb": "6234923",
    "right_index": "13249734",
    "right_middle": "34023784",
    "right_ring": "12332538",
    "right_pinky": "32458970",
}

fingerprint_data2 = {
    "x": "00000000078945",
    "y": "000002349081"
    }

    
def add_biometric_data(passport, datatype, value, date):
    
    biometric_data = {datatype : {"date": date, "value": value}}

    if 'biometric' not in passport:
        passport['biometric'] = {} 

    if 'biometric' in passport:
        passport['biometric'][datatype] = {"date": date, "value": value}
 
    return passport

print(add_biometric_data(passport_vedad, 'fingerprint data', fingerprint_data, '04-03-2020'))
print(add_biometric_data(passport_vedad, 'fingerprint data2', fingerprint_data2, '04-03-2020'))
