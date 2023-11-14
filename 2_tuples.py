#Author: Naman Goyal
#Youtube Channel : https://www.youtube.com/@CSFactoryIn/videos

#Tuples : ordered , immutable, allows duplicate elements
#Immutable means: Tuple cannot be changed after its creation
#Usually tuples are used for objects that belong together
#closed in parantheses or not

mytuple = ("Naman", 10, "July") #with parantheses
print(mytuple)

mytuple2 = "Naman", 10, "July" #without parantheses
print(mytuple2)

#Check Immutability of a tuple - trying to change 'July' to 11

# mytuple[2] = 11
# print(mytuple) #It will give error "'tuple' object does not support item assignment"

 
#NOTE: If you have a single value in the tuple, then it is not a tuple
mytuple3 = ("Naman")
print(mytuple3)
print(type(mytuple3))#It is an string, not a tuple

mytuple4 = (5)
print(mytuple4)
print(type(mytuple4)) #It is an int, not a tuple

#If you want to consider single element as a tuple, then use comma afetr that element
mytuple5 = ("Naman",)
print(mytuple5)
print(type(mytuple5))#It is a tuple, not a string

mytuple6 = (5,)
print(mytuple6)
print(type(mytuple6)) #It is a tuple, not an int

#Creating a tuple from a list using tuple method
#List is also called as an iterable

mylist = ["Naman", "Python", 2.0]
mytuple7 = tuple(mylist)
print(mylist)
print(mytuple7)

#Accessing elements from a tuple using [] square brackets.
item = mytuple7[0]
print(item)

#tuple index out of range error : if you put a large value than the length of the tuple
# item = mytuple7[78]
# print(item)

#-1 to  access last item in the list
item = mytuple7[-1]
print(item)

#Iterate over a tuple using a for loop
for element in mytuple:
    print(element)

#Check whether an element is present in the tuple or not using in operator
if "Naman" in mytuple:
    print("Yes")
else:
    print("No")

#Length of a tuple or how many elements are present in the tuple using len method
tuple_len = len(mytuple)
print(tuple_len)

#Count the frequency of the charactors or words in a tuple using count method
char_tuple = ('n','a','m','a','n')
print(char_tuple.count('n'))

word_tuple = ('naman','goyal','naman','rid')
print(word_tuple.count('naman'))
print(word_tuple.count('rid'))

#Finding first index of a recurring/non-recurring charactor or word using index method
print(char_tuple.index('n'))
print(word_tuple.index('naman'))

print(char_tuple.index('a'))
print(word_tuple.index('rid'))

#If we check for the index of a char/word i.e. not present in the tuple
#Then an error pops up "Value error: tuple.index(x): x not in tuple"
# print(char_tuple.index('t'))

#If you want MUTABILITY in tuple, then you need to convert a tuple into a list
#modify that list
#convert that list again into a tuple

tuple_to_list = list(word_tuple)
print(tuple_to_list)

#Change values in the list
tuple_to_list[2] = "Sunam"
print(tuple_to_list) 

#Convert list to tuple
list_to_tuple = tuple(tuple_to_list)
print(list_to_tuple)

#Slicing in tuples : To access sub-parts of the input tuple using colon (:)
print(list_to_tuple[:2]) #It will print elements present at 0th and 1st index
print(list_to_tuple[1:])#It will print elements present at 1st till last index
print(list_to_tuple[:-1])#It will print elements present at 2nd last index till 0th index

#Take every 2nd element from the tuple using double colon (::)
print(list_to_tuple[::2]) #It will print 2nd and 3rd element of the input tuple

#Reverse the tuple
print(list_to_tuple[::-1])

#Unpacking or bifurcating a tuple into multiple variables
first_name, last_name, city, misc = list_to_tuple
print(first_name)
print(last_name)
print(city)
print(misc)

#NOTE: If the number of variables on Left hand side is different
#From number of elements present in the tuple
#Then an error pops up "ValueError : too many values to unpack"

# first_name, last_name, city = list_to_tuple

#If you donot want to create so many variables, but still needs unpacking, Use *
test0, *test1, test3 = list_to_tuple
print(test0) #It will contain the first element
print(test1) #It will contain LIST of middle elements
print(test3) #It will contain the last element

#Comparing a tuple and a list
#NOTE: Working with large data, Use tuples. Because If you take same elements in a list
# and same elements in a tuple, the overall size of the tuple is lesser than that of list
#So space optimization

import sys
size_list = ["naman", "goyal", 10, "July"]
size_tuple = ("naman", "goyal", 10, "July")
print(sys.getsizeof(size_list), "bytes") #Outputs 88 bytes
print(sys.getsizeof(size_tuple), "bytes") #Outputs 72 bytes

#Tuple also supports processing-time optimization over lists
#So iteration is faster in tuples than lists
#User timeit, stmt is a list or tuple, number is iterations i.e 1 million

import timeit 
print(timeit.timeit(stmt = "[1,2,3,4,5]", number = 1000000)) #List #Outputs five times slower than tuple processing time approx
print(timeit.timeit(stmt = "(1,2,3,4,5)", number = 1000000)) #Tuple #Outputs five times faster than tuple processing time approx