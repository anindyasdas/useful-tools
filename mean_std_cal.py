# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 20:52:39 2019

@author: Anindya
"""
from __future__ import print_function
from __future__ import division
import os
#os.environ["HOME"] = str('/ukp-storage-1/das')#setting home environment from default home/das to ukp-storage-1/das
import torch

from torch.utils.data import DataLoader

import torchvision

import sys
from datasets1 import BirdsDataset
from torchvision import transforms
print("PyTorch Version: ",torch.__version__)
print("Torchvision Version: ",torchvision.__version__)

batch_size = 16
def online_mean_and_sd(loader):
    """Compute the mean and sd in an online fashion

        Var[x] = E[X^2] - E^2[X]
    """
    print("calculating mean and std")
    cnt = 0
    fst_moment = torch.empty(3)
    snd_moment = torch.empty(3)

    for data, _,_,_ in loader: # based on my dataloader
        #print(data)
        print("batch count:", cnt)
        b, c, h, w = data.shape
        nb_pixels = b * h * w
        sum_ = torch.sum(data, dim=[0, 2, 3])
        sum_of_square = torch.sum(data ** 2, dim=[0, 2, 3])
        fst_moment = (cnt * fst_moment + sum_) / (cnt + nb_pixels)
        snd_moment = (cnt * snd_moment + sum_of_square) / (cnt + nb_pixels)

        cnt += nb_pixels

    return fst_moment, torch.sqrt(snd_moment - fst_moment ** 2)

data_dir = sys.argv[1]



# Detect if we have a GPU available
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

#########################################################################


data_transforms = transforms.Compose([transforms.ToPILImage(), transforms.Pad(0), transforms.ToTensor()])


print("Initializing Datasets and Dataloaders...")
image_datasets = {x: BirdsDataset(os.path.join(data_dir), transform=data_transforms, split=x) for x in ['train', 'val']}
# Create training and validation dataloaders
image= image_datasets['train'] + image_datasets['val']
dataloaders = DataLoader(image, batch_size=batch_size, shuffle=True, num_workers=0)




#print('#################Eval mode##################')
#loader = dataloaders_dict['train'] + dataloaders_dict['val']
mean, std= online_mean_and_sd(dataloaders)
print('mean: {} , std: {}'.format(mean, std))
    


