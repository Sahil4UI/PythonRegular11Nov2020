Python 3.7.9 (v3.7.9:13c94747c7, Aug 15 2020, 01:31:08) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #String MEthods
>>> x="ankur"
>>> x.upper()
'ANKUR'
>>> x="AnKuR"
>>> x.lower()
'ankur'
>>> x.casefold()
'ankur'
>>> x
'AnKuR'
>>> x=x.lower()
>>> x
'ankur'
>>> x="Ankur Nain"
>>> x.replace("Nain","Kumar")
'Ankur Kumar'
>>> x
'Ankur Nain'
>>> x.lower()
'ankur nain'
>>> print(x)
Ankur Nain
>>> x=x.lower()
>>> x
'ankur nain'
>>> x="welcome to our python programming class"
>>> x.capitalize()
'Welcome to our python programming class'
>>> x.title()
'Welcome To Our Python Programming Class'
>>> x
'welcome to our python programming class'
>>> x.index("w")
0
>>> x.index("e")
1
>>> x.index("o")
4
>>> x.index("o",0)
4
>>> x.index("o",5)
9
>>> x.find("o",5)
9
>>> x.index("x")
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    x.index("x")
ValueError: substring not found
>>> x.find("x")
-1
>>> x
'welcome to our python programming class'
>>> x.split(" ")
['welcome', 'to', 'our', 'python', 'programming', 'class']
>>> x.split("o")
['welc', 'me t', ' ', 'ur pyth', 'n pr', 'gramming class']
>>> x="Ankur"
>>> len(x)
5
>>> x.center(3)
'Ankur'
>>> x.center(5)
'Ankur'
>>> x.center(6)
'Ankur '
>>> x.center(7)
' Ankur '
>>> x.center(10)
'  Ankur   '
>>> x.center(10,"*")
'**Ankur***'
>>> x.center(30,"/")
'////////////Ankur/////////////'
>>> x.center(40,"+")
'+++++++++++++++++Ankur++++++++++++++++++'
>>> x="               Ankur           "
>>> x.rstrip()
'               Ankur'
>>> x.lstrip()
'Ankur           '
>>> x.strip()
'Ankur'
>>> x='+++++++++++++++++Ankur++++++++++++++++++'
>>> x.strip()
'+++++++++++++++++Ankur++++++++++++++++++'
>>> x.strip("+")
'Ankur'
>>> x="AnKuR NaIn"
>>> x.swapcase()
'aNkUr nAiN'
>>> x="ankur"
>>> len(x)
5
>>> x.zfill(4)
'ankur'
>>> x.zfill(5)
'ankur'
>>> x.zfill(10)
'00000ankur'
>>> x
'ankur'
>>> x.startswith('k')
False
>>> x.endswith("r")
True
>>> #ASCII code ->American Standard Code for Information Interchange
>>> #ord & chr
>>> ord("A")
65
>>> ord("%")
37
>>> ord("~")
126
>>> ord("#@")
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    ord("#@")
TypeError: ord() expected a character, but string of length 2 found
>>> ord("x")
120
>>> chr(125)
'}'
>>> chr(65)
'A'
>>> chr(96)
'`'
>>> chr(100)
'd'
>>> 