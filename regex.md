# Important Regular Expressions #

## Functions:
- findall:	Returns a list containing all matches
- search:	Returns a Match object if there is a match anywhere in the string
- sub:	Replaces one or many matches with a string

### Regex 0:
- ^ works as complement
```python
txt = "The rain in Spain"
#Check if the string has other characters than a, r, or n:
x = re.findall("[^arn]", txt)
['T', 'h', 'e', ' ', 'i', ' ', 'i', ' ', 'S', 'p', 'i']
```
### Regex 1:
- ^carrot beginning of string
- {}	Exactly the specified number of occurrences
- $ end of string
```python
pattern=re.compile('^[A-Z]{5}[0-9]{4}[A-Z]{4}[0-9]{1}$')
pattern.findall(string)
#or 
re.findall('^[A-Z]{5}[0-9]{4}[A-Z]{4}[0-9]{1}$', 'ABCDE1234DGHI9')
#match: 'ABCDE1234DGHI9'
#not_match: 'ABCDE1234DGHI9l', 'aABCDE1234DGHI9'
```
### Regex 2:
```python
txt = "The rain in Spain"
#Find all lower case characters alphabetically between "a" and "m":
re.findall("[a-m]", txt)
#output: ['h', 'e', 'a', 'i', 'i', 'a', 'i']
```
### Regex 3:

- . Any character (except newline character)
```python
txt = "welcomehello world"
x = re.findall("he..o", txt)
#output: ['hello']
#Search for a sequence that starts with "he", followed by two (any) characters, and an "o"
```
