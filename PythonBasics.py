%pwd(Will let you know in which drive your python files are stored)
'C:\\Users\\Shubhangi sakarkar'


#Data Types
bool: Boolean (true/false) types. Supported precisions: 8 (default) bits.
int: Signed integer types. Supported precisions: 8, 16, 32 (default) and 64 bits.
float: Floating point types. Supported precisions: 16, 32, 64 (default) bits and extended precision floating point (see note on floating point types).
string: Raw string types. Supported precisions: 8-bit positive multiples.
bool -> True, False / 1,0
int -> 3,5,-1,-9
float -> 3.45
str -> 'data scientist'
# bool, int, float, str


a = 'Data Science'
print(a)  [print function helps to print the output]
type(a)   [Type function is used to check the datatype of varibale]
type(a)
str

z = True
type(z)
bool


#Autotypecasting
3 + 4.5
7.5
True + 2  (True=1,False=0)
3
False+6
6

#Forced Typecasting
3 + int(4.5)
7
bool(-18)
True
10
bool(10)
True
0
bool(0)
False

# bool -> int -> float -> string (Order of conversion)
bool(-18)
True
name = 'shubhangi'
type(name)
str
#Type Casting
3 + 6.5
True + 6 + 7.5
14.5
int(7.9) + 3
10

#Auto typecasting
True + 3 + int(4.5)
8

True + 18
19
str(3) + 'shubhangi'
'3shubhangi'

#Manual / forced type casting

int('shubhangi')
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-21-1a3577233c62> in <module>
----> 1 int('ashok')

ValueError: invalid literal for int() with base 10: 'ashok'

bool(-1)
True
a = 3.4
type(a)
float
#forced / manual typecasting
int(a)
3
#auto type casting

c = a+b
c
7.5
type(c)
float
3.0 + False
3.0
int(3.4)
3
​
4 + int('a')
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-47-2aa9310fc2c8> in <module>
----> 1 4 + int('a')

ValueError: invalid literal for int() with base 10: 'a'
        
#Slicing
a = 'I am a Data Scientist'
print(a)
a[3] # selector operator []
I am a Data Scientist
'm'
a
a[0:4] # : is slicing operation
'I am'
a[5:] # : is slicing operation
'a Data Scientist'
a[:5]
'I am '
a[7:]
'Data Scientist'
a[:7]
'I am a '
a
a[7:21:2]   # [start:end:step]
a[-9:-12]
#Index starts from ZERO 0
a[7]
a
# Slicing Operator :  Gives you start stop step
a[7:21:1]
print(a)
a[0:15:2]

a[-5:] [Reverse order]

a[7:11]
a[7:]
a[:11]
print(a)
bool(a)

## Examples
3 + 2.5
5.5
bool("Me")
True
bool("Me")
int('3') + 6.7 + bool("Me")
10.7
a = 3
b = 5.9
a+b
8.9
b = 3.9
c = False
b+c
3.9
d
d='3'
d
'3'
d = '3'
d
a= 6
a+int(d)
9
a=3.5
b=5
print(type(a))
print(type(b))
<class 'float'>
<class 'int'>
​
int(a) +b
8
bool(-10) * 3
3
z = False
a*z
a = "I am a DataScientist"
len(a)

a='I am a Data Scientist'
type(a)
c = 20/6
c
d = 'This is interesting'
d
len(d)

a = 3
b = 5
print(a)
print(b)
type(3)
type(4.0)
print(type(2))  # returns 'int’ 
print(type(2.0)) # returns 'float’ 
print(type('two')) # returns 'str’ 
print(type(True)) # returns 'bool’ 
print(type(None)) # returns 'NoneType'
a=3.0
print(a)
type(a)
print(a)

#import datetime as dt (datetime is package present in python for datetime calculation)
td = dt.date.today() [This will give current date]
print(td.month)      [This will give current month]
print(dt.datetime.now()) [This will give current date and time]

christmas_day = dt.date(2020,12,25) [Defining the christmas day]
print(christmas_day -td)  [It will give you how many days left for christmas]

import datetime as dt
sometime = dt.datetime.strptime('27-11-2018','%d-%m-%Y') [new datetime parsed from a string]
# timedelta function
td - dt.timedelta(days=100,hours=100) [This function provide time gap calculation]
tday+dt.timedelta(days=350,hours=100)
dt.datetime.now()-dt.timedelta(days=-350,hours=95)

date.today() + dt.timedelta(hours=40)
today = dt.date.today()
today
startdate = date(2018,1,1)
tday + dt.timedelta(days=-40,hours=200)
​
​
print(dt.datetime.now())
print(today-startdate)
from datetime import date
today = date.today()
​
from datetime import date
from datetime import datetime
​
today = date.today()
print(dt.datetime.now())
​
​
td + dt.timedelta(days=100, hours=48)
tday
tday.month
tday.isoweekday()
print(tday + datetime.timedelta(days=20, hours=72))
print(someday)
someday.isoweekday()
from datetime import date
day1 = date(2010, 6, 20)
day100 = today + dt.timedelta(days=100)
day100.isoweekday()
import datetime as dt
day1 = date(2010, 6, 20)
print(day1)
​
newdate = day1 + dt.timedelta(hours=10,minutes=40)
​
​
import datetime
​
otherday = day1 + datetime.timedelta(days=400)
print(otherday)
​
my_bday = date(1978, 6, 10)
​
print(date.today()-my_bday)
my_birthday = date(today.year, 6, 24)
my_birthday = my_birthday.replace(year=today.year + 1)
print(my_birthday)
​
time_to_birthday = abs(my_birthday - today)
print(time_to_birthday.days)
print(date.today())
print(date.weekday(date.today()))
print(date.isoweekday(date.today()))
print(date.today())
date.today()

#Math Operators
print(10 + 4) # add (returns 14) 
print(10 - 4) # subtract (returns 6) 
print(10 * 4) # multiply (returns 40) 
print(10**4) # exponent (returns 10000) 
print(10 / 4) # divide (returns 2.5) 
print(5 % 4) # modulo (returns 1) - also known as the remainder
print(22//4) # Floor Division you get, 5

Comparision / Logical Operators
# comparisons (these return True) 
print(5 > 3 )
print(5 >= 3)
print(5 < 3 )
print(5 <= 3)
print(5 != 5)
print(5 == 5) # boolean operations (these return True) 

# evaluation order: not, and, or
Logical Operators
T and T --> T
T and F --> F
F and T --> F
F and F --> F

AND is only True if all are True
T or T --> T
T or F --> T
F or T --> T
F or F --> F

OR is only False if all are False
5>7 or 10<9
False
# Logical operators and or
(5<3) or (10<12)
True

print(5 > 3 and 6 < 3 )
False
print(5 > 3 or 5 < 3 )
True
True == 1
True
True == bool(-18)
True
a=3
b=2
(a<3 and b>1) 
(5 >= 3 or 6 > 100) and (True == bool(23))


#Conditional Statement
if (5 < 3):
    print("This is true")
    print("I am in True block")
else:
    print("This is false")
    
print("I am out of IF block")
O/P:-This is false
     I am out of IF block

        
  x=2      
 if (x>0):
    print("Positive number")
    print("In the IF block")
else:
    print("Negative number")
    print("In the else block")
O/P:- Positive number
      In the IF block

x=5
if (x>0):
    print("X is a positive")
    print("I m if True Block")
else:
    print("X is a Negative")
    print("I m if Else/False Block")
    
print("I am out of IF-ELSE block")
O/P:-X is a positive
    I m if True Block
    I am out of IF-ELSE block
    
    
if 5 < 3:
    print("I am in if block")
    print("So the statement is TRUE")
else:
    print("I am in ELSE block")
    
print("I am anyway printed, out of IF")
    O/P:-I am in ELSE block
         I am anyway printed, out of IF
    
 False or -18
 O/P:- -18
    
if (5<3) :
    print("True")
    print("another statement")
else :
    print("False")
    print("another else st")
print("This prints anyway")    
O/P:-False
another else st
This prints anyway
Conditional Statements


x=12
if (x>10) :
    print("This is True or IF block")
    print("I am still in IF")
else :
    print("This is else block")
    
print("\n ---- \n I am out of IF block")
 O/P:-This is True or IF block
I am still in IF

 ---- 
 I am out of IF block

if (5<3):
    print("This is IF block")
else :
    print("This is Else Block")
O/P:-This is Else Block

    if (5<3) :
    print("True block statement 1")
    print("True block statement 2")
    print("True block statement 3")
else:
    print("False block")
    O/P:-False block
0
if (x > 0) :
    print("X is Positive")

elif (x<0):
    print("X is Negative")   
else:
    print("X is ZERO")
    O/P:-X is ZERO
x=-100
if ((x>0) or (x==-100)):
    print("X is positive Value or -100")
    print("I am if loop")
elif (x<0):
    print("I am in else if block")
    print("X is negative")
else:
    print("X is Zero")
    
print("I am out of IF looP")
O/P:-X is positive Value or -100
I am if loop
I am out of IF looP
    
x = 6

if x%2 == 0 :
    print(x, " is even number")
    print("hello..")
else :
    print(x, " is ODD number")

print("this is out of IF else block")
O/P:-6  is even number
hello..
this is out of IF else block
x = -20
# if/elif/else statement
if x > 0:
    print('positive') 
    print('hello')
elif x == 0: 
    print('zero') 
else: 
    print('negative') 
print("I am out of IF block")

# single-line if statement (sometimes discouraged) 
x=5
if x > 0: print('positive') 
    
#### Python Data Object
1)List
2)Tuple
3)String
4)Dictonary
5)Set
6)Function and Loop


##Lists
Python lists arecollection which are very flexible and can hold completely heterogeneous, arbitrary data, and they can be appended to very efficiently.

a = [3,4,6.5,True,[4,5],'Shubhangi'] [Defining a list]
print(a)
a[4][1]
O/P:-5
type(a)
O/P:-type(a)
a = [ 3, 4, 'shubhangi',[12,14,22],True]
a
a[3][1]
O/P:-14
a = [2,True,3.4,4,'data science',[50,60]]
a
a[5][1]
O/P:-60
type(a[1])
O/P:-bool
    
    
myfamily = ['mom','dad','me']
myfamily
O/p:-['mom','dad','me']
    
myfamily.sort() [sort function will arrange list objects in ascending order ]
myfamily
O/P:-['dad','me','mom']
    
myfamily.append('wife') [append function will add new object to lsit from end position]
myfamily
O/P:-['dad', 'me', 'mom', 'wife']
    
myfamily.extend(['bro','sis','grandma']) [extend function helps to add multiple member in one shot]
myfamily
O/P:-['dad', 'me', 'mom', 'wife', 'bro', 'sis', 'grandma']

myfamily.remove('bro') [remove function to used to remove said object from list]
myfamily
O/P:-['dad', 'me', 'mom', 'wife','sis', 'grandma']
    
myfamily.pop(-1) [Pop function removes object from list at end position but if index is well defined,it will pop only that object]
myfamily
O/P:-['dad', 'me', 'mom', 'wife','sis']
    
myfamily.insert(1,'uncle') [Insert function will insert object at specified index]
myfamily
O/P:-
['dad', 'uncle','me', 'mom', 'wife', 'sis', 'grandma', 'sis']

myfamily[-3:] [Selecting objects from end to start]
myfamily
O/P:-['sis', 'grandma', 'sis']

a = [3,4.0,True,'ashok',[56,78,89]]
a
a[4][2]
O/P:-89
    

## properties: ordered, iterable, mutable, can contain multiple data types       
# create an empty list (two ways) 
empty_list = [] 
empty_list = list() 

Tuples
A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists. 
The differences between tuples and lists are, the tuples cannot be changed unlike lists 
and tuples use parentheses, whereas lists use square brackets. Creating a tuple is as simple 
as putting different comma-separated values.

# create a tuple 
digits = (0, 1, 'two',0,1,1,1)  # create a tuple directly 
#recommend way to by using tuple function
digits = tuple([0, 1, 'two'])  # create a tuple from a list 
# examine a tuple 
print(digits[2])  # returns ‘two’ 
print(len(digits)) # returns 3 
print(digits.count(0))  # counts the number of instances of that value (0) digits.index(1)  # returns the index of the first instance of that value (1) 


Strings
# create a string 
s = 'I like you' # examine a string 
s[0] # returns 'I’ 
len(s) # returns 10 
# string slicing like lists
s[:6] # returns 'I like’
s[7:] # returns 'you’
s[-1] # returns 'u' 
s = 'I am a Data Scientist'
s[-9:]
snew = 'Hello Data Science World'
snew[-5:]
s1[6:3]


##Dictionaries
Python dictionary is an unordered collection of items. While other compound data types have only 
value as an element, a dictionary has a key: value pair.

Dictionaries are optimized to retrieve values when the key is known.


cust = dict(name='Rakesh',type='premier',loc ='Bangalore')
cust['loc']
​
# create an empty dictionary (two ways) 
empty_dict = {} 
empty_dict = dict() 
# create a dictionary (two ways) 
cust_profile = dict(cust_id = 24,name='Anand', age=30, 
                    job=['programmer','CEO','Data Scientist'],
                    location="bangalore", years_Exp=17) 
cust_profile.keys()
cust = dict( name = 'ashok',job = "DS Trainer", exp = 17)
cust['job']
​
Sets
A set contains an unordered collection of unique and immutable objects. 
The set data type is, as the name implies, a Python implementation of the sets
as they are known from mathematics. This explains, why sets unlike lists or tuples
can't have multiple occurrences of the same element.

# create an empty set
empty_set = set()
# create a set
lang = {'python', 'r', 'java'} # create a set directly 
snakes = set(['cobra', 'viper', 'python','viper']) # create a set from a list 
print(lang)
print(snakes)
snakes.union(lang)
snakes.intersection(lang)
# examine a set 
​
lang.intersection(snakes)
languages.union(snakes)
​
Functions
#args weight in kilograms,height in cms 
def bmi(w,h):
    bmi = w/(h/100)**2
    if bmi>25:
        print(int(bmi)," This is above normal. Workout")
    else:
        print(int(bmi),"  Perfect!")
​
​
bmi(90,165)
​
​
​
def hello():
    print("Hello Data Science world")
hello()
def hello(name):
    print("Hello ",name)
hello("Ashok")
​
def squareit(x=0):
    if(x==0):
        print("please give a number for squaring")
    else:
        return x**2
​
​
squareit(3)
def helloo():
    print('Hi , I am from ABC corp Hello')
    print('function end')
helloo()
​
​
bmi(70,175)
mybmi
​
def sayhello():
    return print("HELOOOOO")
​
​
    
bmi(76,179.8)
sayhello()
def c2f(deg):
    return deg*(9/5)+32
​
​
​
​
​
def bmi(weight,height):
     return weight / (height/100)**2
​
​
bmi(78,182)
​
ban_temp=c2f(23)
ban_temp
def iseven(x):
    if x%2==0: 
        print("It is even")
    else:
        print("it is odd")
iseven(6)
def iseven(x=''):
    if (x==''):
        return print("please provide arg")
    elif (x%2==0):
        return True
    else:
        return False
    
​
z = iseven(7)
z
# define a function with one argument and no return values 
def print_this(x): print(x) 
​
print_this(2)
Loops
# alternative for loop (recommended style)
fruits = ['apple', 'banana', 'kiwi','gauva','mango'] 
​
for x in fruits:
    if x == 'kiwi':
        print('Hi its Kiwi')
    print(x)
        
for x in range(4):
    print("Hello",x)
​
​
for fruit in fruits: 
        if (fruit!='banana'):
            print(fruit)
a = range(10)
type(a)
fruit
for x in range(55,60):
    print(x,' hello')
print(range(10))
now = dt.datetime.now()
now.replace()
​
