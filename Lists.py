#                                                          PYTHON LISTS

'''
  Lists are used to to store multiple items in a single variable
  These are just like dynamically sized arrays. A list is collection of things [] and separated by comma 
'''
List1 = [] #blank list
print("This is a blank list :", List1)
List2 = ['Asha', 'Anil', 'Ankit']  
List3 = [['Nisha','Sanjana','Sufiyana'], [1,2,3]] #multi - dimensional list 
print("One dimensional List : ", List2)
print("An example of multi- dimensional list :", List3)

# accessing elements from the list 
print("Element at index one in list2 that is one dimensional list :", List2[1])
print("Element at index 1 in list at index 0 in list 3 , that is multi dimensional list : ",List3[0][1])

#List items are ordered, changeable and allow duplicate values and indexed as well first element is at index 0 and so on....

# We can determine the no. of items in a list using len function as follows : 

print("Length of List 2 is : ",len(List2))
print("Type of list2 : ",type(List2))

# NEGATIVE INDEXING 
# this is done to access elements from the end of the list
#index -1 is the last element of the list 

print("Element at the index 2 in list  at index 2 from the last in multi dimensional list : ", List3[-2][-2])

# Range of indexing 
print("The lements in list 2 from index 1 to 3 : ", List2[1:3])
print("Elements from starting to index 2 but it will not mention element at index 2 :", List2[:2])

#changing the value 

List2[1] = "Neelu"
print("Updated list 2 : ", List2)

#Adding more elements 

List2[1:2]= ["Neelie", "Nisha"]

print("list 2 after achanging element at index 1 with 2 others : ", List2)

List2.insert(4,"Shakuntla") #insert function is used to insert any element at specified index

print("List 2 after inserting one more element :",List2)

#To add an element at the end of the list use append function 

List3.append(["Excellent", "Good", "Outstanding"])
print("List 3 after adding an another element using append : ",List3)

# To append elements from one list to another list using extend function 

List2.extend(List3)
print("updated list after appending list and list 3 using extend :", List2)

#To remove elements use remove function

List2.remove("Asha")
print("List2 after removing Sanjana : ", List2)
List2.pop(2) #use pop to remove element at specified index in List and if you won't specify the index then it will remove the last element
print("list 2 after removing element at index 2 is : ", List2)

# Another way of removing the element at specified index is using del keyword, it also removes the element at specified index and complete list as well

del List2[1]
del List1

print("List 2 :",List2)

# clear empties the list 

List2.clear()
print("List 2 after emptiying it using clear is : ",List2)

#loop through a list 

for x in List3: 
    print(x)

#loop through the list by referring to their index number

for i in range(len(List2)):
  print(List2[i])