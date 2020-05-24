# -*- coding: utf-8 -*-
"""
Created on Sat May 23 22:58:40 2020

@author: Anindya
"""

from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
#from nltk.translate.meteor_score import single_meteor_score
import pandas as pd
import numpy as np


def compute_bleu(candidate, reference, ngramm_weights=None,
                 smoothing=SmoothingFunction().method1):
    reference = [reference.split()]
    candidate = candidate.split()
    score = sentence_bleu(reference, candidate, weights=ngramm_weights, smoothing_function=smoothing)
    return score





file_name='\\Users\\Anindya\\Desktop\\Backup\\afterpretrain.txt'
fl=pd.read_csv(file_name, delimiter='\t')
fl.columns=['ref', 'can'] #actual gen


if __name__=='__main__':
    
    score_1 =[]
    score_2=[]
    score_3=[]
    score_4=[]
    meteor= []
    hypo={}
    refs={}
    for i in range(len(fl)):
        reference=fl['ref'][i].strip()
        candidate=fl['can'][i].strip()
        hypo[i] = [candidate.strip()]
        raw_ref = map(str.strip,(reference))
        refs[i] = raw_ref
        #print(candidate)
        score_1.append(compute_bleu(candidate, reference, ngramm_weights=(1, 0, 0, 0)))
        score_2.append(compute_bleu(candidate, reference, ngramm_weights=(0.5, 0.5, 0, 0)))
        score_3.append(compute_bleu(candidate, reference, ngramm_weights=(0.33, 0.33, 0.33, 0)))
        score_4.append(compute_bleu(candidate, reference, ngramm_weights=(0.25, 0.25, 0.25, 0.25)))
        #meteor.append(single_meteor_score(candidate, reference))
        
    print('Bleu_1 score', round(np.mean(score_1),4))
    print('Bleu_2 score', round(np.mean(score_2),4))
    print('Bleu_3 score', round(np.mean(score_3),4))
    print('Bleu_4 score', round(np.mean(score_4),4))
    #print('METEOR score', round(np.mean(meteor),4))
    