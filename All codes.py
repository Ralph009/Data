#Variables
result = 2+1
print(result)
type(result)

#Strings
#We can use indexing []
my_string= 'Hi there'
print(my_string[-1]) #grabs last letter of the variable my_string.
#Slicing on a string
#Slicing [start:stop:step] 
#start is the numerical index for the slice start.
#start is the index you will go up to (but not include).
#step is the size of the jump we want to take.
#Escape sequence print(Hello \n--> This is for new line World)


#String doesn't support item assingment
#Lists

my_list = [1,2,3,4,5,6,'Hi','Ankyiee']

my_list.append('Yo') #to add at last
my_list.pop() #to delete at last
print(my_list[-1])





#Dictionaries in Python
#Unordered mapping to store objects in an ordered sequence
#Dictionary: Objects retrieved by key name
#Unordered and cannot be sorted
#Hello = {'Key1':'Yo'}

#print(Hello.items())
#print(Hello.keys())




#List
#Objects are retrieved by location
#Indexing and slicing available
#Tuples in Python
#Immutable cannot be changed 
#Slicing and Indexing available
#tuple1 = (1,2,3)-->Tuple
#tuple2 = [1,2,3]-->List

#Some Functions for Tuples
#t = (1,1,1,1,12,13)
#rint(t.count(1))

#Sets in Python
#Unordered collection of UNIQUE elements
#Can have same objects

#myset = set()
#myset.add(1)
#print(myset)

mylist = [1,1,2,2,3,3]
print(set(mylist))







#Map Function
def square(num):
  return num**2

mynums = [1,2,3,4,5,6]

for item in map(square,mynums):
  print(item)

#Filter Function

def goo(num):
  return num%2 == 0

my_numbers = [1,2,3,4,5,6]

for item in filter(goo,my_numbers):
  print(item)


#Lambda..Anonymous  function


list1 = [1,2,4,5,6]
for item in map(lambda num:num**2,list1):
  print(item)


#LEGB Rules Local ,Enclosing function locals, Global, Built-in
lambda num:num**2 #local

#for example

name = 'Global String' #Global
def aba():
  name = 'SAM' #Localy enclosed 

  def hello():
    name = 'Local' #local 
    print('Hello'+name)

  hello()

