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
- {}: Exactly the specified number of occurrences

```python
txt = "The rain in Spain faalls all mainly in the plain!"
x = re.findall("aal{2}", txt)
#Check if the string contains "aa" followed by exactly two "l" characters

```

### Regex 8:
- | either or

```python
txt = "98The rain in Spain falls ABmainly in the plain!"
pat=re.compile('^[0-9]+|[A-Z]{2}[a-z]{4}')
#number start at the begining of string or string with 'AB' followed by four charecters from a-z
x=pat.findall(txt)
['98', 'ABmain']

```

### Regex 9:
- \d Check if the string contains any digits (numbers from 0-9):
```python
txt = "I love you 3000 , I love you 4000"
x = re.findall("\d", txt)
['3', '0', '0', '0', '4', '0', '0', '0']
x = re.findall("\d+", txt)
['3000', '4000']

```

### Regex 10:
- \D Return a match at every no-digit character:
```python
x = re.findall("\D", txt)
['I', ' ', 'l', 'o', 'v', 'e', ' ', 'y', 'o', 'u', ' ', ' ', ',', ' ', 'I', ' ', 'l', 'o', 'v', 'e', ' ', 'y', 'o', 'u', ' ']
x = re.findall("\D+", txt)
['I love you ', ' , I love you ']



```

### Regex 11:
- \s white space
```python
#Return a match at every white-space character
txt = "I love you \n 3000 , I love \t you,  4000!"
x = re.findall("\s", txt)
[' ', ' ', ' ', '\n', ' ', ' ', ' ', ' ', ' ', '\t', ' ', ' ', ' ']
```

### Regex 12:
- \S	Returns a match where the string DOES NOT contain a white space character
```python
txt = "I love you \n 3000 , I love \t you 4000"
x = re.findall("\S", txt)
['I', 'l', 'o', 'v', 'e', 'y', 'o', 'u', '3', '0', '0', '0', ',', 'I', 'l', 'o', 'v', 'e', 'y', 'o', 'u', '4', '0', '0', '0']
x = re.findall("\S+", txt)
['I', 'love', 'you', '3000', ',', 'I', 'love', 'you', '4000']
```

### Regex 13:
- \w: #Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character)
- \w is \S without punctuations '!', ',', '.', ';'
```python
txt = "I love you \n 3000 , I love \t you 4000"
x = re.findall("\w", txt)
['I', 'l', 'o', 'v', 'e', 'y', 'o', 'u', '3', '0', '0', '0', 'I', 'l', 'o', 'v', 'e', 'y', 'o', 'u', '4', '0', '0', '0']

```

### Regex 14:
- \W: Return a match at every NON word character i.e white space \s with punctuations ',', '!', '?'
```python
txt = "I love you \n 3000 , I love \t you,  4000!"
x = re.findall("\W", txt)
[' ', ' ', ' ', '\n', ' ', ' ', ',', ' ', ' ', ' ', '\t', ' ', ',', ' ', ' ', '!']
```

### Regex 15:
-  (): Any subpattern inside a pair of parentheses will be captured as a group using ( and ). In practice, this can be used to extract information like phone numbers or emails from all sorts of data.

```python
file_name='IMG2024.png'
x=re.findall("^IMG\d+\.png$",file_name)
['IMG2024.png']
#to capture the filename without the extension, which matches a particular pattern
x=re.findall("^(IMG\d+)\.png$",file_name) 
['IMG2024']


```

### Regex 16:
- \\ escaping special character

```python
 #special characters [ \ ^ $ . | ? * + ( ) have special meaning in a regex engine. Let’s say we want to find literally a dot. Not “any character”, but just a dot. To use a special character as a regular one, prepend it with a backslash: \..
#That’s also called “escaping a character”.
txt="open chapter 3.21, page 221"
x=re.findall('\d\.\d+',txt)
['3.21']

```

### Regex 17:
- Back reference

```python
#Backreferences match the same text as previously matched by a capturing group
txt ='they say no pain no gain' \1 back refernces to same pattern inside capyuring group and if the pattern matches returns whats inside capture group
x=re.findall(r'(ai)\D+\1',txt) # raw string
 ['ai']
txt='they say no pain no profit'
x=re.findall(r'(ai)\D+\1',txt)
[]

```
### Regex 18:
- Raw string
- when we use r"abc" we tell python interpreter to interpret as it is withut special meanings eg. print("\n") interpreted as new line where  print(r"\n")  prints "\n" regex engine has some extra special charecter additional to python
- findall(r"[\w]", s) and findall("[\w]", s) have exactly same effect as \w is regex special charecter but has no special meaning for python interpreter, so using raw or not inputs exactly same string to regex engine from python interpreter
- problem arises when a charecter has special meaning in both python interpreter and regex engine. Example '\b', which means backspace in python interpreter but regex interprets as specified characters are at the beginning or at the end of a word
- We have to tell the python interpreter to ignore special meaning using raw string, so it would be interpreted as raw \b without the meaning 'backspace', but then it's special meaning would be interpreted by regex engine.
\b specified characters are at the beginning or at the end of a word. In "john's jeans" , \b matches between (",j),(n,'),(',s),(s," "), (" ",j), (s,")

```python
txt = "I love glove embeddings"
x = re.findall(r"\blove", txt)
['love']

txt = "The rain in Spain"
#Check if "ain" is present at the end of a WORD:
x = re.findall(r"ain\b", txt)
['ain', 'ain']
# \B for not the beginning or the end of a word 
x = re.findall(r"ain\B", txt)
x = re.findall(r"\Bain", txt)

```
### Regex 19:
- Look around (Look ahead and look backward)
- Look around do not consume characters in the string, but only assert whether a match is possible or not.

**Look Ahead**

- The lookahead itself is not a capturing group. It is not included in the count towards numbering the backreferences.
- In order to store the match of the regex inside a lookahead, one has to put capturing parentheses around the regex : (?=(regex))

*Positive Look Ahead*

- It matches something that is followed by something else eg. ol(?=k) it matches 'ol' that is followed by 'k' without making the capturing group 'k' as part of the match 

```python
txt='I live in kolkata'
#Positive Look Ahead
re.findall('ol(?=ka)',txt)
 ['ol']
re.findall('ol(?=(ka))',txt)
['ka']
```
*Negative Lookahead*
- To match something not followed by something else eg. ol(?!k) it matches 'ol' that is not followed by 'k' without making the capturing group 'k' as part of the match 
```python
re.findall('ol(?!ka)',txt)
[]
re.findall('ol(?!ki)',txt)
['ol']
```
- As the name suggest look ahead looks ahead and after matching regex engine goes back to actual position so 'ol(?=k)a' expression first matches 'ol' then look ahead to match 'k' and regex engine then goes back to actual position i.e 'l' now the token 'a' is matched to 'l', so basically it tries to match 'k' and 'a' to the same position in the string and always fail, this not not issue with look behind and Look behind can be used in any position.

**Look behind**

- It tells the regex engine to temporarily step backwards in the string, to check if the text inside the lookbehind can be matched there. (?<!a)b matches a “b” that is not preceded by an “a”, using negative lookbehind.

*Positive look behind (?<=a)b*
```python
txt='I live in kolkata'
re.findall('(?<=ka)ta',txt)
['ta']
```
*Negative look behind (?<!a)b*
```python
re.findall('(?<!ka)ta',txt)
[]
re.findall('(?<!ki)ta',txt)
['ta']
re.findall(r'\b\w+(?<!s)\b',"john's jeans")
['john']
#(Hint: \b matches between the apostrophe and the s)
```
### Function : split
```python
#split at white space
txt = "I love you \n 3000 , I love \t you,  4000!"
x = re.split("\s", txt)
['I', 'love', 'you', '', '', '3000', ',', 'I', 'love', '', '', 'you,', '', '4000!']
#Split the string at the first white-space character
x = re.split("\s", txt, 1)
['I', 'love you \n 3000 , I love \t you,  4000!']
```
### Function : sub
```python
#Replace every white-space character with the number XX
txt = "I love you \n 3000 , I love \t you,  4000!"
x = re.sub("\s", "XX", txt)
print(x)
IXXloveXXyouXXXXXX3000XX,XXIXXloveXXXXXXyou,XXXX4000!

#Replace the first 2 occurrences:
x = re.sub("\s", "XX", txt,2)
print(x)
IXXloveXXyou 
 3000 , I love 	 you,  4000!
```
### Function : search
```python
#A Match Object is an object containing information about the search and the result.
#If there is no match, the value None will be returned, instead of the Match Object.
txt = "I love you 3000, I love you 4000"
x = re.search("love", txt)
print(x)
<_sre.SRE_Match object; span=(2, 6), match='love'>
x = re.search("hate", txt)
print(x)
None
```
