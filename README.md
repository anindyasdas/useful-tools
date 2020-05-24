# useful-tools
Some useful tools


# 1 ALL SCORES: 
all_score0.py calculates :
(Bleu(4), ["Bleu_1", "Bleu_2", "Bleu_3", "Bleu_4"]),"METEOR", "ROUGE_L", "CIDEr")
  Before Running install pycocoevalcap :
  To install pycocoevalcap and the pycocotools dependency, run:
  pip install git+https://github.com/salaniz/pycocoevalcap
  this program uses pycocoevalcap from https://github.com/salaniz/pycocoevalcap
  
  python  python all_score0.py candidateb.txt referenceb.txt #(if single reference)
  python all_score0.py candidateb.txt reference1.txt reference2.txt reference3.txt (multiple references)
  ################################################################################################
