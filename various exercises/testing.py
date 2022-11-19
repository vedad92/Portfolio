from cgi import test


def get_none():
    return

def flatten_dict(dictionary):
    return list(dictionary.values())


example_dict = {'a': [42, 350], 'b': 3.14}

print(flatten_dict(example_dict)) 


    


