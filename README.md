# useful-tools
Some useful tools


## 1 ALL SCORES: ## 
--all_score0.py calculates : ["Bleu_1", "Bleu_2", "Bleu_3", "Bleu_4"]),"METEOR", "ROUGE_L", "CIDEr")
--Before Running install pycocoevalcap :
 --To install pycocoevalcap and the pycocotools dependency, run:
 ```
  pip install git+https://github.com/salaniz/pycocoevalcap
 ```
 --this program uses pycocoevalcap from https://github.com/salaniz/pycocoevalcap
  #(if single reference) run:
  ```
  python  python all_score0.py candidateb.txt referenceb.txt 
  ```
  if (multiple references) run:
  ```
  python all_score0.py candidateb.txt reference1.txt reference2.txt reference3.txt 
  ```
  ################################################################################################
