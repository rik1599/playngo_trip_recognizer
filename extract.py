import os
import zipfile
from tqdm.auto import tqdm

os.makedirs('data', exist_ok=True)

def recursive_unzip(zip_file, path):
    with zipfile.ZipFile(zip_file, 'r') as myzip:
        for file in tqdm(myzip.namelist(), leave=False):
            myzip.extract(file, path)
            if file.endswith('.zip'):
                recursive_unzip(path + '/' + file, path)
                os.remove(path + '/' + file)

recursive_unzip('./08-08-2024-16-23-37_files_list.zip', './data')