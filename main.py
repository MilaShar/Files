__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

# use liberaries

import os
import shutil
import zipfile

def clean_cache():
   
    folder_cache = ("cache")
    check_folder = os.path.isdir(folder_cache)
    
    if not check_folder:
        os.makedirs(folder_cache)
    
    else:
        shutil.rmtree(folder_cache)
        os.makedirs(folder_cache)
    return
clean_cache()

#2
def cache_zip(zip_file_path,cache_dir_path):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(cache_dir_path)
    return

cache_zip('data.zip','cache')
    
def cached_files():
    list_new = []
    for file in os.listdir(os.path.abspath("cache")):
        list_new.append(f"{os.path.abspath('cache')}\{file}")
    print(list_new)
    return list_new


def find_password(file_path):
    for file_name in file_path:
        file = open(file_name, 'r')
        for line in file:
            if 'password' in line:
                print(line[line.find(' ')+1:-1])
                return line
            
find_password(cached_files())







