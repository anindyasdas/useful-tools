# Important Regular Expressions #

## Functions:
- findall:	Returns a list containing all matches
- search:	Returns a Match object if there is a match anywhere in the string
- sub:	Replaces one or many matches with a string

### Regex 0:
- ^ works as complement
```
txt = "The rain in Spain" <br>
#Check if the string has other characters than a, r, or n:
x = re.findall("[^arn]", txt)
['T', 'h', 'e', ' ', 'i', ' ', 'i', ' ', 'S', 'p', 'i']
```
