# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

* List and tuples are similar as they are both are sequences of comma seperated values, called elements. They both can have values of any type i.e. string, float, integer, nested lists,etc.  

* Dissimilarities are as follows:
  - Lists are enclosed in square brackets ([ and ]). While Tuples may or maynot be enclosed in round brackets (( and )).
  - While lsits are mutable i.e. the elements can be modified by assignment, Tuples are immutable(elements can't be assigned). Although one tuple can be replaced with another.  
    E.g.     
    ```
    t = (1,2,'a','c')    
    t =('A',) + t[1:]    
    print(t)  
    ```
* Tuples can work as keys in dictionaries. As dictionaries are implemented by hastables. The dicitionary uses hash values(genereated by hash function which take any kind of value and return an integer) to store and look up key-value pairs. So if the key is mutable like a list, problems could arise. For example, if a key is modified then the key would be hashed and stored at a different locaiton. This would lead to either 2 entries for the same key or inability to find the key. Hence, dictionary keys should be immutable like strings or tuples. 

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

* Similarities between List and Sets:
  - Both are sequences of comma seperated values
  - Both are mutable
* Dissimilarities:
  - Lists are enclosed within square brackets ([and]) whereas sets are enclosed within curly branckets ({and}).
  - Lists can contain values of any type but sets can contain only immutable data types.
  - Elements or values in a list are ordered whereas in a set there is no order.
  - Unlike lists, sets can't have multiple occurance of the same element.
 Example of a List:
 '''
 List1=[1,3,[4,'a'],'Priya','b','a',{"first":124,"second": 43})      #Can have any data type as an element 
 print(List1[6][1])                                                  #Supports indexing as elements are in a fixed order 
 '''
 Example of a Set:
 '''
 x={1,3,'Priya','b','a',("Agra","Delhi")}                            #Can have only immutable elements
 y=set(["Hi","Hello",1,2,('a','b')],"Hi")                            #It saves only unique elements. Here multiple occurance are discarded
 print(x)                                                            #Doesn't support indexing as elements have no fixed order 
 '''
 * Performance comparision for finding elements:
   - To find an element in a set, just check for the element with the 'in' keyword .
     ```
     y={"Agra","Delhi","Lucknow","Mumbai","Agra",1,2,('q')}
     print("Agra" in y)
     ```
   - To find an element in list, just check for the element with the 'in' keyword 
     ```
     l1=["Agra","Delhi","Lucknow","Mumbai","Agra",1,2,('q')]
     print("Agra" in l1)
     ```
   Sets are implemented by using hash tables. When you add an object to a set, the position within the memory of the set object is          determined using the hash of the object to be added. When testing for membership, all that needs to be done is basically to look if the object is at the position determined by its hash, so the speed of this operation does not depend on the size of the set. For lists, in contrast, the whole list needs to be searched, which will become slower as the list grows.

   Note: Usually sets aren't faster than lists. Membership test is faster for sets, and so is removing an element. As long as you don't need these operations, lists are often faster.
---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)





