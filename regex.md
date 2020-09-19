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
### Regex 4:
- \* Zero or more occurrences
```python
txt = "m ma mab mabi mabin mabii mabiiii mabiiiinlp"
#Check if the string contains "ab" followed by 0 or more "i" characters
x = re.findall("abi*", txt)
['ab', 'abi', 'abi', 'abii', 'abiiii', 'abiiii']
```

### Regex 5:
- .* any charecter (except new line) any number of occurance
```python
txt = "welcomehello world hxxo hehhhhhlllllodhdh"
x = re.findall("he.*o", txt)
#output: ['hello world hxxo hehhhhhlllllo']
#starts with 'he' any number of charecters in between then ends with 'o'

```

### Regex 6:
- \+ one or more occurrences
```python
txt = "m ma mab mabi mabin mabii mabiiii mabiiiinlp"
#Check if the string contains "ab" followed by 1 or more "i" characters
x = re.findall("abi+", txt)
['abi', 'abi', 'abii', 'abiiii', 'abiiii']
txt='hello ab98hgl'
x=re.findall('[0-9]+',txt)
#check if string contains 1 or more numbers i.e [0-9]
['98445962']
#if we remove '+'
x=re.findall('[0-9]',txt)
#output:['9', '8', '4', '4', '5', '9', '6', '2']

```

### Regex 7:

```python

```

### Regex 8:

```python

```

### Regex 9:

```python

```

### Regex 10:

```python

```

### Regex 11:

```python

```

### Regex 12:

```python

```

### Regex 13:

```python

```

### Regex 14:

```python

```

### Regex 15:

```python

```

### Regex 16:

```python

```

### Regex 17:

```python

```
### Regex 18:

```python

```
