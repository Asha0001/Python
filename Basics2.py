# We can convert on type to another with the int(), float() and complex() methods

x=2
y=2.3
z=45j

#now change the type 

a=float(x)
b=int(y)
c=complex(x)

print("the changes value of x is ",a)
print("the changes value of y is ",b)
print("the changes value of z is ",c)

#RANDOM : Python does not have a random function to make a random number 
# But It has a built in module called Random to generate random numbers

import random
print (random.randrange(1,10))   #this will generate a random number anywhere between 1 to 10

#In Python strings are either surrounded by single quotation marks or double quitation marks

print("Python k basics almost ho gya h keep revising")

Work = "Completed"
print("Kaam hua ki nhi :", Work)

WorkDetails = ''' "Ye multi line string dikhane ko h "
...................work has been completed . I just need to review the details'''

print("WorkDetails please : ",WorkDetails)

# Python does not have a character data type, a single character is simply a string with a length of 1.

# Square brackets can be used to access elements of the string

print("This is to show string acts as an array in python and we can access element like this . So character at position 3 is : ",Work[3])

#LOOPING THROUGH THE STRING 

for(x) in Work : 
    print(x)

# len() function returns the string length

print("The length of string Work is : ",len(Work))

print("review" in WorkDetails) #in keyword is used to check if any phrase or character is present in the string

print("review" not in WorkDetails) # not in keyword is used to check if any present is not present in the string

#SLICING STRING 

print("The character in Work string from 2 to 5 are : ",Work[2:5])

print("5 characters of string Work from the start : ", Work[:5]) #slicing the string from the start ka mtlb h sirf starting wale utne char print krna jitna mention h

print("characters of the string work after removing first 5 characters  : ", Work[5:])

#Modifying string 

print("Upper case of varible work is : ",Work.upper()) 

print("Lower case of variable work is : ", Work.lower())

print("After removing white space from the string using strip: ", WorkDetails.strip())

#Concatenating string 

a= "String"
b= "Concatenated"
c=a+" "+b #this is how string are concatenated
print(c)

#formatting strings 

#In python we use f-string to format the strings, for this just put f in front of the string 
# and add curly braces as placeholders for variables, operatios, functions and modifiers to format the string

price=60
display=f"The price is {price} dollars"
print(display)
modified_price = f"The modified price is{price : .2f} dollars"
print(modified_price)
Total_earning=f"The total earning is {20*60} dollars"
print(Total_earning)

# to insert the illegal characters in the string use an escape character

print("This is an example of \"Escape character\" used in the string") # here " " will be visible in  the output without any error

print("new line \n example") #here the string after\n will be printed in new line in the output 

print("this represents \\ backslash") #here \ will e printed in the string

# Revise string methods please from : 

'''
https://www.w3schools.com/python/python_strings_methods.asp

https://www.geeksforgeeks.org/python-string-methods/

'''
