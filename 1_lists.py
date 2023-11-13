#Lists: ordered, mutable, allows duplicate elements

mylist = ["banana", "cherry", "apple"]
print(mylist)

#Create an empty list and later on, you can append items

mylist2 = list()
print(mylist2)

#list allows for multiple datatypes objects and duplicates also

mylist2 = [5, 7, 6.9, "mango", "mango"]
print(mylist2)

#Accessing an element of a list using an index
#Index start at 0
item = mylist2[2]
print(item)

#Accessing an index which is not present
# item = mylist2[10]
# print(item)

# item = mylist2[-10]
# print(item)

#Accessing an item from last index of the list 
#last item of the list starts from -1
item = mylist2[-4]
print(item)

#Iterate over a list
#Using for loop
for i in mylist2: #Note the usage of 'in' operator
    print(i)

#Check if a particular item (number (without quotes)) is present in the input list or not
if 6.9 in mylist2:
    print("yes")
else:
    print("no")

#Check if a particular item ("string" (with quotes)) is present in the input list or not
if "mango" in mylist2:
    print("yes")
else:
    print("no")
    
#How many elements are present in your list using len method
length_of_list = len(mylist2)
print(length_of_list)

#Add or append more items to an existing list using append method
mylist2.append(7.4)
print(mylist2)

#Insert an item at the specific position/index in the existing list using insert method
#Use index and item to be inserted
mylist2.insert(2, "custard apple")
print(mylist2)

#Delete the last item from the list using pop method
item = mylist2.pop()
print(item)
print(mylist2) #list without the last item of that list

#Remove a particular element from the list using the remove method
print(mylist2)
mylist2.remove("custard apple")
print(mylist2)

#Try to remove an element which is not present in the list
# mylist2.remove("guava") 
#It will throw an error "x not in list"

#Reverse the list using reverse method
mylist2.reverse()
print(mylist2)

#Sort the list in ascending order using sort method
# mylist2.sort()
# print(mylist2) #It will throw an error because mylist2 contains both string and float elements

#NOTE : Sorting only sorts similar datatype elements
#FLOAT AND INTEGER WORKS, BUT NUMBER AND STRING DO NOT WORK
#So, let's create a new list with similar datatype based elements
#Sort method sorts the lists in-place, means it changes your original input list
mylist3 = [45, 66, 1, 2.5, 7.09]
# mylist3.sort()
# print(mylist3)

#If you want to keep your original list as it is, and want to create a new sorted list
#Then use sorted method
print(mylist3)
mylist4 = sorted(mylist3)
print(mylist4)

#Remove all elements from a list using clear method
mylist2.clear()
print(mylist2) #It will return an empty list, with only square brackets

#Create a list with same items
#Create a list of 10 elements containing 10 5's.
mylist5 = [5] * 10;
print(mylist5)

#Concatenate two lists using '+' operator
mylist6 = [10, 23, 46]
mylist7 = mylist6 + mylist5
print(mylist7)

#Slicing: accessing sub parts of your list using a colon (:) operator
new_list = mylist7[1:5] #start from index 1 and ending element at index 4
print(new_list)

#Starts from 0th index
new_list_1 = mylist7[:5]
print(new_list_1)

#Give only a start index and goes upto end of the input list
new_list_2 = mylist7[2:]
print(new_list_2)

#Takes every third (stepsize (3)) item from the list using double colon (::)
new_list_3 = mylist7[1::3] #start from first index till last index with step = 3
print(new_list_3)

#Trick to reverse your list, without using reverse method
new_list_4 = mylist7[::-1]
print(new_list_4)

#Copy a list to another list variable using copy method
copiedList = mylist4.copy()
print(copiedList)
#Another technique to create a copy of the list is using slicing and list methods
#Slicing
copiedList1 = mylist4[:]
print(copiedList1)
#Using list method
copiedList2 = list(mylist4)
print(copiedList2)

#List Comprehension : Create a new list from squaring the elements of existing list
test1 = [1, 2,  3, 4, 5] #input list
test2 = [element*element for element in test1] # created list of squares of elements of input list

print(test1)
print(test2)