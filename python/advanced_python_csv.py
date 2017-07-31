PLACE YOUR CODE HERE
import csv

with open('faculty.csv') as f:
    data = list(csv.DictReader(f))
    list1 = [ dict(x) for x in data ]
  
# Creating a list of all the email addressess   
list_all_emails = [ x[' email'] for x in list1]    
print("\nList of all email addresses: \n",list_all_emails,'\n')

# Creating a new file 'email.csv and writing the list of emails in the new file
with open('email.csv', 'w') as fwrite:
    data_writer = csv.writer(fwrite, delimiter='\n')
    data_writer.writerow(list_all_emails)
