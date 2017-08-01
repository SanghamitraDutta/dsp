# Q6
import csv

with open('faculty.csv') as f:
    data = list(csv.DictReader(f))
    list1 = [ dict(x) for x in data ]    
 
# Creating the dictionary in the specified format

faculty_dict = {}
for x in list1:
    if x['name'].split()[-1] not in faculty_dict:
        faculty_dict.update({ x['name'].split()[-1]:[[x[' degree'], x[' title'][:-17],x[' email']]]})
    else:
        faculty_dict[x['name'].split()[-1]].append([x[' degree'],x[' title'][:-17],x[' email']])                      
                              
print(faculty_dict)


# Q7
import csv

with open('faculty.csv') as f:
    data = list(csv.DictReader(f))
    list1 = [ dict(x) for x in data ]        

# Creating the dictionary in the specified format
                   
professor_dict = { (x['name'].split()[0],x['name'].split()[-1]):[x[' degree'], x[' title'][:-17], x[' email']] for x in list1 }
                   
print(professor_dict)


# Q8
import csv

with open('faculty.csv') as f:
    data = list(csv.DictReader(f))
    list1 = [ dict(x) for x in data ]         

# Creating the dictionary in the specified format
                   
professor_dict = { (x['name'].split()[-1],x['name'].split()[0]):[x[' degree'], x[' title'][:-17], x[' email']] for x in list1 }
                  
count=0
for k,v in professor_dict.items():
    if count<3:
        print(k,v)
        count += 1
        
