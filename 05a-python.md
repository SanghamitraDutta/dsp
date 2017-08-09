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
  - Both are collection of elements separated by commas
  - Both are mutable
* Dissimilarities:
  - List is a sequence of comma seperated elements that supports efficient access using indices
  - Set is a collection of unordered(no fixed sequence) elemets and the elements accessed by hash numbers that are mapped to each element
  - Lists are enclosed within square brackets ([and]) whereas sets are enclosed within curly branckets ({and}).
  - Lists can contain values of any type but sets can contain only immutable data types.
  - Elements or values in a list are ordered whereas in a set there is no order.
  - Unlike lists, sets can't have duplicate occurance of the same element.  
 
 Example of List:    
 ```  
 List1=[1,3,[4,'a'],'Priya','b','a',{"first":124,"second": 43}]    #Can have any data type as elements 
 print(List1[6][1])                                                #Supports indexing  
 ```
 Example of Set:  
 ```  
 x={1,3,'Priya','b','a',("Agra","Delhi")}        #Can have only immutable elements. No list nor dict
 y=set(["Hi","Hello",1,2,('a','b'),"Hi"])        #Converts list argument into a set.But elements of the list can't be mutable.
 print(y)                                        #Doesn't support indexing
 >>>{1, 2, ('a', 'b'), 'Hello', 'Hi'}            #Set has no duplicate elements present in the list above
 ```
 * Performance comparision for finding elements:
   - To find an element in list, just check for the element with the 'in' keyword. Here the whole list is searched for the element.
     ```
     l1=["Agra","Delhi","Lucknow","Mumbai","Agra",1,2,('q')]
     print("Agra" in l1)
     ```
   - To find an element in a set, just check for the element with the 'in' keyword. Here the hash value attached to the element is used to look up the position of the element. 
     ```
     y={"Agra","Delhi","Lucknow","Mumbai","Agra",1,2,('q')}
     print("Agra" in y)
     ```
   Sets are implemented by using hash tables. When you add an object to a set, the position within the memory of the set object is          determined using the hash of the object to be added. When testing for membership, one checks whether the object is at the position determined by its hash, so the speed of this operation does not depend on the size of the set. For lists, in contrast, the whole list needs to be searched, which will become slower as the list grows.

   Note: Usually sets aren't faster than lists. Membership test is faster for sets, and so is removing an element. As long as you don't need these operations, lists are often faster.
---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

* Lambda function is a way to create small functions without a name.
  Example 1:
  ```
  def ABC(n):
    return lambda x: x+n
    
  a=ABC(9)
  result1=a(10)
  print(result1)
  
  result2=ABC(20)(21)
  print(result2) 
  ```
  Example 2 (lambda fn. syntax can be written in just 1 line):
  ```
  f =  lambda input_list: [i for i in input_list if i%2==0]

  my_list = [3,4,7,2,9,170]
  for x in f(my_list):
    print(x)
  ```
* Lambda can be very useful when used in combination with the functions like filter(), map() and reduce().
  - Lambda used with filter() can apply the lambda function to elements of an enitre list and then filter out only the elements that return a True value on applying lambda function.   
     Example:  
     ```
     number = [0,1,1,2,3,5,8,13,21,34,55]
     Odd= list(filter(lambda x: x % 2, number))
     print(Odd)
     Even = list(filter(lambda x: x % 2 == 0, number))
     print(Even)
     ```
  - Lambda used with map() can apply the lambda function to all elements of sequence/s(like list) one by one and then return a single list with the results of the lambda function.  
     Example:  
     ```
     p = [10,20,33]
     q = [-14,12,-10]
     r = [2,1,2]
     s = list(map(lambda x,y,z: x+y-z, p,q,r))
     print(s)
     ```
* Using Lambda in the key argument to sorted: Here key argument will first appply the lambda function to all the elements to be sorted in the iterable. Then the sorting of elements occurs based on the result returned by the lambda function.
     Example:  
     ```
     student_info= {("Andrew",'A',20), ("Patrick",'B',19),("Carol",'C',24)}
     sorted_age = sorted(student_info, key = lambda student: student[2])       #Elements sorted based on age
     print(sorted_age)
     ```

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

* List comprehensions provide a concise way to create lists. Common applications are to make new lists where each element is the result of some operations applied to each member of another sequence or iterable, or to create a subsequence of those elements that satisfy a certain condition.Example:
 ```
 list_pythagoras=[(x,y,z) for x in range(1,30) for y in range(x,30) for z in range(y,30) if x**2+y**2==z**2]
 print(list_pythagoras)
 ```
* List comprehension is a complete substitute for the lambda function as well as the functions map(), filter() and reduce(). For most people the syntax of list comprehension is easier to be grasped.    
  - Examples of how list comprehension is equivalent to to map() and filter():   
    Map function:
    ```
     p = [10,20,33]
     q = [-14,12,-10]
     r = [2,1,2]
     s = list(map(lambda x,y,z: x+y-z, p,q,r))
     print(s)
    ```
    Equivalent list comprehension:
    ```
     p = [10,20,33]
     q = [-14,12,-10]
     r = [2,1,2]
     s = [ p[i]+q[i]-r[i] for i in range(len(p)]
     print(s)
    ```   
    Filter function:
    ```
     number = [0,1,1,2,3,5,8,13,21,34,55]
     Odd= list(filter(lambda x: x % 2, number))
     print(Odd)
     Even = list(filter(lambda x: x % 2 == 0, number))
     print(Even)
    ```
    Equivalent list comprehension:
    ```
     number = [0,1,1,2,3,5,8,13,21,34,55]
     Odd = [ x for x in number if x % 2 != 0 ]
     print(Odd)
     Even = [ x for x in number if x not in Odd]
     print(Even)
    ```  
  - Comparing capabilities of list comprehension with map() and filter():
    - List Comprehension is faster when lambda is used with map() and filter()
    - If you already have a function defined, it is simpler to use map or filter. For example, map(sum, myLists) is more crisp than [sum(x) for x in myLists]. You do not have to make a dummy variable (e.g. x) which you have to type twice, just to iterate.
    - If you will not be using all your data, or do not know ahead of time how much data you need, map in python3 (and generator expressions in python2 or python3) will avoid calculating their values until the last moment necessary.This saves memory.
* Set comprehension example:
  ```
  a = {x for x in 'abracadabra' if x not in 'abc'}
  print(a)
  ```
* Dictionary comprehension example:
  ```
  matrix_dictionary=[['a',10],['b',20],['cd',40]]
  d = {k:v for k, v in matrix_dictionary}
  print(d)
  
  #Alternatively   

  dictionary_key=['a','b','cd']
  dictionary_value=[10,20,40]
  d = {k:v for k in dictionary_key for v in dictionary_value}
  print(d)
  ```
---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 days

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





