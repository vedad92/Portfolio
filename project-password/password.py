from importlib.resources import path
import os
import shutil

cache_path = os.path.join(os.getcwd(), 'cache')

def clean_cache():
    if os.path.isdir(cache_path):
        for f in os.listdir(cache_path):
            file_path = os.path.join(cache_path, f)
            os.remove(file_path)       
    else:
        print('Folder created')
        os.makedirs("cache")
    return      

def cache_zip(zip_file, cache_dir):
    shutil.unpack_archive(zip_file, cache_dir)
    return


def cached_files():
    files = [os.path.join(cache_path, f) for f in os.listdir(cache_path)]
    return files


def find_password(file_list):
    for file in file_list:
        with open(file, "r") as f: #contents = f.readlines()
            for line in f:
                if "password" in line:
                    line.split()
                    return line[10:]
    return 'Password not found'


def main():
    clean_cache()
    cache_zip('data.zip',cache_path) #os.path.join(os.getcwd(), 'cache')
    print(cached_files())
    print(find_password(cached_files()))
    return


if __name__ == "__main__":
    main()
