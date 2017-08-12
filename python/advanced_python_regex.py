
# Q1
import csv

with open('faculty.csv') as f:
    data = list(csv.DictReader(f))
    list1 = [ dict(x) for x in data ]
    for x in list1:
        print (x)

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

print("No. of different degress: ",len(dict1),'\n') 

print("Degrees and their frequencies:")
for i in dict1:
    print(i,':', dict1[i])

#Q1 using re

import csv
import re 

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

# or use the simple method below to create the dictionary with unique degrees and their frequencies in just 1 step
dict1 = {}

for i in list_all_degrees:
    degree = re.sub('\.','',i)  # degree string without any '.'
    if degree in dict1:
        dict1[degree] += 1
    else:
        dict1.update({degree:1})  # if degree is not in dictionary then add as a new item        
    
print("No. of different degress: ",len(dict1),'\n') 
print("Degrees and their frequencies:")
for i in dict1:
    print(i,':', dict1[i])


    
# Q2
import csv

with open('faculty.csv') as f:
    data = list(csv.DictReader(f))
    list1 = [ dict(x) for x in data ]
    for x in list1:
        print (x)

  
# Creating a list of all the titles   
list_all_titles = [ x[' title'] for x in list1]    
print("\nList of all titles: ", list_all_titles,'\n')


# Creating a list of all the unique titles by removing duplicates
list_unique_titles=list(set(list_all_titles))
print("List of all unique titles: ", list_unique_titles,'\n')


# Creating a dictionary with unique title as the key and their frequencies as values
dict1 = { i:list_all_titles.count(i) for i in list_unique_titles } 
print("Dictionary of all unique titles with their frequencies: ", dict1,'\n')        


# Cleaning dictionary data by removing various versions of a title and adding their frequencies to a single key
for i in dict1:
    if  i == 'Assistant Professor is Biostatistics':
        dict1['Assistant Professor of Biostatistics'] += dict1[i]
   
del dict1['Assistant Professor is Biostatistics']

print("Cleaned dictionary: ", dict1,'\n')

print("Titles and their frequencies:")
for i in dict1:
    print(i,':', dict1[i])

#Q2 using re

import csv
import re 

with open('faculty.csv') as f:
    data = list(csv.DictReader(f))
    list1 = [ dict(x) for x in data ]
    
# Creating a dicitonary of all titles and their frequencies and cleaning title data
dict1 = {}
for row in list1:
    title = re.sub(r'\bis\b','of',row[' title'])  
    if title in dict1:
        dict1[title] += 1
    else:
        dict1.update({title:1})  # if title is not in dictionary then add as a new item
          
print("Titles and their frequencies:")
for i in dict1:
    print(i,':', dict1[i])

    
# Q3

import csv

with open('faculty.csv') as f:
    data = list(csv.DictReader(f))
    list1 = [ dict(x) for x in data ]
    
# Creating a list of all the email addressess   
list_all_emails = [ x[' email'] for x in list1]    
print("\nList of all email addresses: \n",list_all_emails,'\n')

# Q4

import csv

with open('faculty.csv') as f:
    data = list(csv.DictReader(f))
    list1 = [ dict(x) for x in data ]
  
# Creating a list of all the email addressess   
list_all_emails = [ x[' email'] for x in list1]    
print("\nList of all email addresses: \n",list_all_emails,'\n')

# Creating a list of all the email domains   
list_all_domains = [ x[' email'].split('@')[1] for x in list1]    
print("List of all email domains: \n",list_all_domains,'\n')

# Creating a list of all the unique domains by removing duplicates
list_unique_domains=list(set(list_all_domains))
print("No. of unique email domains: ",len(list_unique_domains))
print("List of all unique email domains: ", list_unique_domains,'\n')

#Q4 using re

import csv
import re 

with open('faculty.csv') as f:
    data = list(csv.DictReader(f))
    list1 = [ dict(x) for x in data ]  
  
# Creating a list of all the email addressess   
list_all_emails = [ x[' email'] for x in list1]    
print("\nList of all email addresses: \n",list_all_emails,'\n')

# Creating a list of all unique email domains
list_unique_domains = []
for x in list_all_emails:
    domain = x.split('@')[1]
    if domain not in list_unique_domains:
        list_unique_domains.append(domain)

print("No. of unique email domains: ",len(list_unique_domains))
print("List of all unique email domains: ", list_unique_domains,'\n')


    
    
    
