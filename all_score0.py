# -*- coding: utf-8 -*-
"""
Created on Sun May 24 16:35:01 2020

@author: Anindya
"""

"""
Computes the BLEU, ROUGE, METEOR, and CIDER
using the COCO metrics scripts
"""
import argparse
import logging

# this requires the coco-caption package, https://github.com/tylin/coco-caption
from pycocoevalcap.bleu.bleu import Bleu
from pycocoevalcap.rouge.rouge import Rouge
from pycocoevalcap.cider.cider import Cider
from pycocoevalcap.meteor.meteor import Meteor


parser = argparse.ArgumentParser(
    description="""This takes two text files and a path the references (source, references),
     computes bleu, meteor, rouge and cider metrics""", formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("hypothesis", type=argparse.FileType('r'),
                help="The hypothesis files")
parser.add_argument("references", type=argparse.FileType('r'), nargs="+",
                help="Path to all the reference files")


def load_textfiles(references, hypothesis):
    print("The number of references is {}".format(len(references)))
    hypo = {idx: [lines.strip()] for (idx, lines) in enumerate(hypothesis)}
    #print(type(references))
    #print(references)
    #print(hypo)
    # take out newlines before creating dictionary
    if len(references)==1:
        raw_refs = [[r.strip()] for r in references[0]]
    else:
        raw_refs = [list(map(str.strip, r)) for r in zip(*references)]
    refs = {idx: rr for idx, rr in enumerate(raw_refs)}
    #print(type(refs[0]))
    #print(refs)
    #print(len(refs))
    #print(len(hypo))
    # sanity check that we have the same number of references as hypothesis
    if len(hypo) != len(refs):
        raise ValueError("There is a sentence number mismatch between the inputs")
    return refs, hypo


def score(ref, hypo):
    """
    ref, dictionary of reference sentences (id, sentence)
    hypo, dictionary of hypothesis sentences (id, sentence)
    score, dictionary of scores
    """
    scorers = [
        (Bleu(4), ["Bleu_1", "Bleu_2", "Bleu_3", "Bleu_4"]),
        (Meteor(),"METEOR"),
        (Rouge(), "ROUGE_L"),
        (Cider(), "CIDEr")
    ]
    final_scores = {}
    for scorer, method in scorers:
        score, scores = scorer.compute_score(ref, hypo)
        if type(score) == list:
            for m, s in zip(method, score):
                final_scores[m] = s
        else:
            final_scores[method] = score
    return final_scores

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger('Computing Metrics:')
    args = parser.parse_args()
    ref, hypo = load_textfiles(args.references, args.hypothesis)
    print(score(ref, hypo))