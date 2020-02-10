%pwd(Will let you know in which drive your python files are stored)
'C:\\Users\\Shubhangi sakarkar'
Data Types
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
type(a)
Data Science
str
This Python Tut
This is

this is point 1
this is point 2
​
​
​
type(a)
str
z = True
type(z)
bool
#Autotypecasting
3 + 4.5
7.5
True + 2
3
False+6
False+6
6
int(5.6)
Forced Typecasting
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
​
# bool -> int -> float -> string
bool(-18)
​
​
name = 'ashok'
type(name)
str
Type Casting
3 + 6.5
# bool -> int -> float -> str
True + 6 + 7.5
int(7.9) + 3
bool(0)
​
​
​
​
​
​
#Auto typecasting
True + 3 + int(4.5)
8
# Bool -> int -> float -> str
True + 18
19
str(3) + 'Ashok'
'3Ashok'
​
​
#Manual / forced type casting
4 + float('9.5')
13.5
4.5 + 5 + bool(-8) + int('6') + 3.5 + True
21.0
%pwd
'C:\\Users\\Shubhangi sakarkar'
float('6.5')
6.5
int('7') + 5
12
int('ashok')
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
5 + 6.7
11.7
# bool --> int --> float --->str
a= 3
b = 4.5
print(type(a))
print(type(b))
<class 'int'>
<class 'float'>
a + int(b)
7
3 + int('4')
7
# True -> 1, False -> 0
False + 4
4
#Anything not zero is taken as booleon True
bool(-18)
True
3 + int('6')
9
3 + int('4.5')
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-32-08365561c7ff> in <module>
----> 1 3 + int('4.5')

ValueError: invalid literal for int() with base 10: '4.5'

3 + int(4.5)
7
int(float('4.5'))
4
bool(4.5)
True
3.5 + bool(-18) + int('3')
7.5
name = "ashok"
type(name)
str
type(a)
int
b = 4.5
type(b)
float
z = True
type(z)
bool
a = 3
b = 5.4
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

​
​
float(3)
3.0
bool(-18.9)
True
int(3.4 + bool(-20)+int(8.4))
12
%pwd
'C:\\Users\\Shubhangi sakarkar'
Slicing
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
# : -> slicing operator
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
# Slicing Operator :  Gives you Range
a[7:21:1]
print(a)
a[0:15:2]
​
a[-5:]
​
​
# :  is a slicing operator
a[7:11]
a[7:]
a[:11]
print(a)
bool(a)
d = '32'
print(d)
type(d)
float(d)
b = 0
bool(b)
​
​
False
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
message[10:3]
​
​
message[5:10]
​
​
​
​
message[45:34]
This is to test
a='I am a Data Scientist'
type(a)
c = 20/6
c
d = 'This is interesting'
d
len(d)
​
​
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
​
import datetime as dt
td = dt.date.today()
print(td.month)
print(dt.datetime.now())
td =dt.date.today()
christmas_day = dt.date(2018,12,25)
print(christmas_day -td)
dt.date.today()
tday = dt.date.today()
tday
someday = dt.date(2018,12,20)
someday
print(someday - tday)
# dt is alias name of datetime
import datetime as dt
sometime = dt.datetime.strptime('27-11-2018','%d-%m-%Y')
sometime
dt.date(2018,9,29)
tday = dt.date.today()
tday
someday = dt.date(2018,12,20)
someday
someday - tday
print(dta.date.today())
td = dt.date.today()
type(td)
print(datetime.date.today())
tday.day
datetime.date.today()
tday = dt.date.today()
print(tday)
type(tday)
type(tday)
someday = dt.date(2019,10,20)
print(someday)
​
someday.month
someday - tday
dt.datetime.strptime('03-1900',"%m-%Y")
​
print(someday - td)
datetime.date.today()
import datetime as dt
dt.date.today()
from datetime import date
date.today()
print(dt.date.today())
from datetime import date
a = 3
type(a)
td = date.today()
print(td)
td.month
td = date.today()
type(td)
a = '2018-7-20'
type(a)
from datetime import date
someday = date(2018,7,20)
print(someday)
print(someday - td)
someday = dt.date(2016,5,25)
​
td - dt.timedelta(days=100,hours=100)
tday+dt.timedelta(days=350,hours=100)
dt.datetime.now()-dt.timedelta(days=-350,hours=95)
​
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

Math Operators
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
​
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
​
print(5 > 3 and 6 < 3 )
print(5 > 3 or 5 < 3 )
False
True
True == 1
True
True == bool(-18)
True
a=3
b=2
(a<3 and b>1) 
(5 >= 3 or 6 > 100) and (True == bool(23))
Conditional Statement
if (5 < 3):
    print("This is true")
    print("I am in True block")
else:
    print("This is false")
    
print("I am out of IF block")
​
​
​
x = 2
​
if (x>0):
    print("Positive number")
    print("In the IF block")
else:
    print("Negative number")
    print("In the else block")
    
​
​
​
x=5
if (x>0):
    print("X is a positive")
    print("I m if True Block")
else:
    print("X is a Negative")
    print("I m if Else/False Block")
    
print("I am out of IF-ELSE block")
​
​
​
​
​
​
​
​
​
if 5 < 3:
    print("I am in if block")
    print("So the statement is TRUE")
else:
    print("I am in ELSE block")
    
print("I am anyway printed, out of IF")
    
​
​
​
​
​
False or -18
if (5<3) :
    print("True")
    print("another statement")
else :
    print("False")
    print("another else st")
print("This prints anyway")    
​
    
    
​
​
​
Conditional Statements
x=12
if (x>10) :
    print("This is True or IF block")
    print("I am still in IF")
else :
    print("This is else block")
    
print("\n ---- \n I am out of IF block")
​
​
if (5<3):
    print("This is IF block")
else :
    print("This is Else Block")
​
if (5<3) :
    print("True block statement 1")
    print("True block statement 2")
    print("True block statement 3")
else:
    print("False block")
​
​
​
​
​
x = 0
if (x > 0) :
    print("X is Positive")
​
elif (x<0):
    print("X is Negative")   
else:
    print("X is ZERO")
​
          
​
​
​
​
​
x=-100
​
if ((x>0) or (x==-100)):
    print("X is positive Value or -100")
    print("I am if loop")
elif (x<0):
    print("I am in else if block")
    print("X is negative")
else:
    print("X is Zero")
    
print("I am out of IF looP")
    
x = 6
​
if x%2 == 0 :
    print(x, " is even number")
    print("hello..")
else :
    print(x, " is ODD number")
​
print("this is out of IF else block")
​
​
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
​
# single-line if statement (sometimes discouraged) 
x=5
if x > 0: print('positive') 
​
Lists
Python lists are very flexible and can hold completely heterogeneous, arbitrary data, and they can be appended to very efficiently.

a = [3,4,6.5,True,[4,5],'Ashok']
a
a[4][1]
type(a)
​
a = [ 3, 4, 'ashok',[12,14,22],True]
a
a[3][1]
​
a = [2,True,3.4,4,'data science',[50,60]]
a
a[5][1]
type(a[1])
myfamily = ['mom','dad','me']
myfamily
myfamily.sort()
myfamily
myfamily.append('wife')
myfamily
myfamily.extend(['bro','sis','grandma'])
myfamily
myfamily.remove('bro')
myfamily
myfamily.pop(-1)
myfamily
myfamily.insert(1,'uncle')
myfamily
myfamily[-3:]
myfamily.
​
​
z = [3,4.0,True]
z
a = [3,4.0,True,'ashok',[56,78,89]]
a
a[4][2]
myfamily = ['dad','mom','me']
myfamily.append('wife')
myfamily.extend(['bro','sis','grandma','grandfa'])
myfamily
myfamily.remove('bro')
myfamily
myfamily.pop(-1)
myfamily
myfamily.insert(4,'sis-in-law')
myfamily
​
myfamily.extend(['wife','sis-in-law','daughter'])
myfamily
myfamily.append('grand ma')
myfamily
myfamily.pop(0)
myfamily
my_list = [3,4,15,5.9]
print(my_list)
type(my_list)
my_list.sort()
my_list
myfamily = ['mom','dad','me']
myfamily
myfamily.extend(['wife','brother'])
myfamily.append('sis')
myfamily
​
myfamily.extend(['wife','bro','daughter'])
myfamily
myfamily.insert(0,'grandma')
myfamily.
myfamily.sort(reverse=True)
myfamily
myfamily
myfamily
myfamily
myfamily.pop(4)
myfamily
myfamily.remove('brother')
myfamily
myfamily
family.extend(['bro','uncle','aunt'])
family
myfamily
family.append('wife')
family
family.insert(4,"sis")
family
​
​
family.pop(3)
family
family.remove('me')
## properties: ordered, iterable, mutable, can contain multiple data types       
# create an empty list (two ways) 
empty_list = [] 
empty_list = list() 
# create a list 
simpsons = ['homer', 'marge', 'bart']
# examine a list 
print(simpsons[0])        # print element 0 ('homer’) 
print(len(simpsons))    # returns the length (3)
 # modify a list (does not return the list) 
simpsons.append('lisa') # append element to end 
simpsons.extend(['itchy', 'scratchy'])  # append multiple elements to end 
print(simpsons)
​
family.remove('me')
family.pop(2)
​
myfamily.sort()
z = [3, 4.5,True]
z.sort()
z
Tuples
A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists. The differences between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets. Creating a tuple is as simple as putting different comma-separated values.

simpsons.insert(0, 'maggie')  # insert element at index 0 (shifts ˓→everything right) 
print(simpsons)
simpsons.remove('bart')  # searches for first instance and removes it 
print(simpsons)
simpsons.pop(0) # removes element 0 and returns it del
print(simpsons)
simpsons[0] = 'krusty' # replace element 0
print(simpsons)
# create a tuple 
digits = (0, 1, 'two',0,1,1,1)  # create a tuple directly 
#recommend way to by using tuple function
digits = tuple([0, 1, 'two'])  # create a tuple from a list 
# examine a tuple 
print(digits[2])  # returns ‘two’ 
print(len(digits)) # returns 3 
print(digits.count(0))  # counts the number of instances of that value (0) digits.index(1)  # returns the index of the first instance of that value (1) 
# create a tuple 
digits1 = (0, 1, 'two',0,1,1,1)  # create a tuple directly 
# examine a tuple 
print(digits1.count(1))  # counts the number of instances of that value (0) digits.index(1)  # returns the index of the first instance of that value (1) 
len(digits1)
digits[1]= 'one' #returns an assignment error
my_tuple = (1,3.0,'works')
my_tuple
my_tuple2 = tuple(["this works too",8,10,True])
type(my_tuple2)
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
Dictionaries
Python dictionary is an unordered collection of items. While other compound data types have only value as an element, a dictionary has a key: value pair.

Dictionaries are optimized to retrieve values when the key is known.

​
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
A set contains an unordered collection of unique and immutable objects. The set data type is, as the name implies, a Python implementation of the sets as they are known from mathematics. This explains, why sets unlike lists or tuples can't have multiple occurrences of the same element.

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
