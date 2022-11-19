from click import argument
from main import get_none, flatten_dict

example_dict = {'a': [42, 350], 'b': 3.14}

def test_get_none():
    assert get_none() == None

def test_flatten_dict(dictionary):
    assert flatten_dict(dictionary) == list(dictionary.values())


