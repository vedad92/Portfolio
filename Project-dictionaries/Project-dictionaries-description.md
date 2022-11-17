**passport

Write in main.py a function create_passport that takes as its arguments, in this order:

A name
A date of birth 
A place A height 
A nationality And returns a passport dict containing this information with the keys:

name date_of_birth place_of_birth height nationality Note:

We express a nationality as a country (str) from the list returned by get_countries. Part 2: Add Stamp Whenever a person travels to another country, they get a stamp in their passport that shows that they have been there. Implement add_stamp in main.py, which takes as its arguments, in this order:

A passport (dict) like the one returned by create_passport A country (str) And:

Adds or updates a key-value pair: (key) 'stamps' (value) a list of countries (str) that the person has been to. Finally: add_stamp returns the (possibly) stamped passport. Note:

Any stamp may be a person's first stamp, in which case the 'stamps' key in their passport dict is not present yet. You will have to create it in that case. But beware not to overwrite people's existing stamps list! Travellers don't need stamps of their home country. No duplicate stamps! If a traveler already has a stamp for a country, don't give them another stamp. Part 3: Add biometric data Passport technology advances and security has become more of a concern for a lot of countries. Quite a few countries have added "biometric data" to passports. See this Wikipedia article for more information (you won't need that for this exercise).

Because the software you're writing will be used by different countries that want to add different kinds of biometric data your code needs to be able to handle all kinds of different biometric data.

Write a function add_biometric_data in main.py that takes as its arguments, in this order:

A passport (dict) like the one returned by create_passport A name (str) for the type of biometric data that will be added. The value, or values of the to-be-added biometric data. A date in ISO format YYYY-MM-DD (str) for when the biometric data was recorded. The biometric data should live in a dictionary inside of the passport. In other words: a nested dictionary. The key for the biometric data dictionary is biometric.

If the passport did not yet have any biometric data: add the key for it, you can assume you'll only get passports with a chip to save biometric data. If the type of biometric data was not yet in the passport: add it to the passport. The value for the specific type of biometric data should again be a dictionary (so nested again). This dictionary should have two keys: date and value. See examples below for specific examples. If the type of biometric data was already in the passport: update the biometric data in the passport, overwriting the previous value and date.
