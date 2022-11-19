
from ast import Try
from inspect import getclosurevars
import os
from socket import if_nametoindex

def main():
    foo = list(range(10))
    print(
        get_item_from_list(foo, 9),
        get_item_from_list(foo, -1),
        get_item_from_list(foo, 10),
    )
    ...


def add(x, y):
    try:
        return x + y
    except TypeError:
        return 0
                    

def read_file(filename):
    try:
        return open(filename, "r").read()
    except FileNotFoundError:
        return ""

def get_item_from_list(l, index):
    max_index = len(l) - 1
    min_index = -1 - max_index
    try:
        return l[index]
    except IndexError:
        return None
    except TypeError:
        return None

print(get_item_from_list("456",'55'))    
    
if index <= max_index and index >= min_index:
        return l[index]
    else:
        return None


if __name__ == "__main__":
    main()
