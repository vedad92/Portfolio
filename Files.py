from importlib.resources import path
import os
import shutil

def clean_cache():
    folder = os.path.join(os.getcwd(), 'cache')
    if os.path.isdir(folder):
        for f in os.listdir(folder):
            file_path = os.path.join(folder, f)
            os.remove(file_path)       
    else:
        print('Folder created')
        os.makedirs("cache")
    return      
clean_cache()

def cache_zip(zip_file, cache_dir):
    shutil.unpack_archive(zip_file, cache_dir)
    return
cache_zip('data.zip',os.path.join(os.getcwd(), 'cache'))


def cached_files():
    folder = os.path.join(os.getcwd(), 'cache')
    files = [os.path.join(folder, f) for f in os.listdir(folder)]
    return files
print(cached_files())


def find_password(file_list):
    for file in file_list:
        with open(file, "r") as f:
            contents = f.readlines()
            for text in contents:
                if "password" in text:
                    return text
    return 'Password not found'

print(find_password(cached_files()))
