# -*- coding: utf-8 -*-
"""
Created on Fri May  8 10:52:14 2020

@author: Anindya
#This code removes unnecessary files from Flower dataset keeping only images and 
caption data
Please follow the steps before running the code:
    1. Download flower dataset from http://www.robots.ox.ac.uk/~vgg/data/flowers/102/ and save them in 102flowers/iamges/*.jpg
    2.Download captions from https://drive.google.com/file/d/0B0ywwgffWnLLcms2WWJQRFNSWXM/view and 
    Extract the archive, copy the text_c10 folder and paste it in 102flowers/text_c10
    3.copy testclasses.txt and put in 102flowers/testclasses.txt 20 class
    4.copy trainvalclasses.txt and put in 102flowers/trainvalclasses.txt 82 class
    5. remove .t7 files run the below code with appropriate folder name to remove .h5 files

"""
import glob
import os

floc = '\\Users\\Anindya\\Desktop\\Backup\\102flowers\\102flowers\\text_c10\\*'
files = glob.glob(floc)



for file in files:
    h5_files = glob.glob(os.path.join(file, '*.h5'))
    for h5_file in h5_files:
        os.remove(h5_file)
        print('file: {} removed'.format(h5_file))
