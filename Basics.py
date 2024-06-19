print('Hello World') #It Will print Hello World And # initiates comments 

#Created By Guido Van Rossum in 1991

#Indentation matters in python

#Python has no command for declaring a variable 

x=75
print(x)
print(type(x)) #it will print the type of variable x

'''
this is 
a multi line comments
we can write multi line comment using triple quotes 
dear 

'''

# Second way of writing
#multi line comment is to write 
#it in different line
#beginning with hash sign

# A variable is created as soon as you assign value to it 

x=54
y='Asha'
X=90
print('The value of X is : ' , x) # concatenate string with another type using comma
print('The value of y: ',y)
print('The value of X : ',X)

#Variable names in python are case sensitive as x and X are different in the above statements 

'''
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.

'''

# Multi word varibles name can be written using various Techniques : camelCaseTechnique, PascalCaseTechnique, snake_case_technique.

fruit1, fruit2, fruit3 = "Apple" , "Banana" , "Orange" #Assigning many values to various varibles in one line 
print("fruit2 is : ", fruit2)

OnlyAvailableFruit = FruitToStore = "Pineapple" #Assigning same value to multiple varibles
print("The avalable fruit is : ", OnlyAvailableFruit)

# Note : "+" acts as way to combining for two string but we can't combine two different types using it 
# Also "+" acts as operator for intgers print(6+7) will show output 13

'''
GLOBAL VARIABLES : The variables that are created outside the function but can be used by everyone both outside and inside the function 

Even if we create a varible with same name inside the function that would be used only within the function and called local varible

And global varible will remain unchanged
'''
GlobalVariable1 = 79 #this is global variable

def myfunc():
    GlobalVariable1 = 80 #this is local varible with same name as global varible
    print("The local variable that was created inside the function with same name as global varible :", GlobalVariable1)

myfunc()
print("Global Variable is : ", GlobalVariable1)

# Now to make the local variable a global varible use global keyword as follows : 

GlobalVariable2 = 45 

def myfunc():
    global GlobalVariable2
    GlobalVariable2 =50
    print("The local variable is : ", GlobalVariable2)

myfunc()
print("The value of gobal variable is : ", GlobalVariable2)

# As you can see from the output now the value of global variable is same as the local varible with global keyword 
# Hence global keyword is also used to change the value of global variable

'''
Built-in Data Types
In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType

'''
