PLACE YOUR CODE HERE
# Q1
import csv

with open('faculty.csv') as f:
    data = list(csv.DictReader(f))
    list1 = [ dict(x) for x in data ]

# Creating a list of all the degrees   
list_all_degrees = []  
for x in list1:
    temp = x[' degree'].split()
    x[' degree']= temp
    list_all_degrees.extend(x[' degree'])
    
print("List of all degrees: ", list_all_degrees,'\n')

# Creating a list of all the unique degrees by removing duplicates
list_unique_degrees=list(set(list_all_degrees))
print("List of all unique degrees: ", list_unique_degrees,'\n')

# Creating a dictionary with unique degree as the key and their frequencies as values
dict1 = { i:list_all_degrees.count(i) for i in list_unique_degrees } 
print("Dictionary of all unique degrees with their frequencies: ", dict1,'\n')        

# Cleaning dictionary data by removing various versions of a degree and adding their frequencies to a single key
for i in dict1:
    if  i == 'PhD' or i == 'Ph.D':
        dict1['Ph.D.'] += dict1[i]
    if i == 'ScD':
        dict1['Sc.D.'] += dict1[i]
    if i == 'MS':
        dict1['M.S.'] += dict1[i] 

del dict1['PhD']
del dict1['Ph.D']
del dict1['ScD']
del dict1['MS']
del dict1['0']

print("Cleaned dictionary: ", dict1,'\n')

print("Degrees and their frequencies:")
for i in dict1:
    print(i,':', dict1[i])
    
    
    
    
