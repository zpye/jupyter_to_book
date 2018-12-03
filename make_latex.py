import sys
import os
import subprocess

if __name__ == '__main__':
    # delete book.ipynb
    file = 'book.ipynb'
    if(os.path.exists(file)):
        os.remove(file)
    
    # run notebooks
    p = subprocess.Popen('jupyter nbconvert --allow-errors --inplace --execute *.ipynb')
    p.communicate()

    # merge notebooks
    p = subprocess.Popen('python merge_chapters.py')
    p.communicate()

    # generate latex
    p = subprocess.Popen('jupyter nbconvert --to latex --template book book.ipynb')
    p.communicate()