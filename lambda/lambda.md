Target: Python self learning quick notes
Student: Harrison Mfula
Data: 31.05.2016


Topic: lambda, map, filter, reduce
       """""""""""""""""""""""""""

lambda : way to create  anonymous functions 
syntax: lambda arguments:expression
lambda is a keyword, arguments can be any number of argumenst, : is mandatory, expression can be any expression, commonly mathematical expression. 
note: a lambda function can be assigned into a variable and later be called just like a standard function, see example
>>> f = lambda x, y : x + y
>>> f(1,1)
2

map() function: applies a given  function to every element of the sequence (list)  and retuns a list containing the result of the function, see syntax
syntax:  result = map(func, seq)  
example: 
>>> Celsius = [39.2, 36.5, 37.3, 37.8]
>>> Fahrenheit = map(lambda x: (float(9)/5)*x + 32, Celsius)
>>> print Fahrenheit
[102.56, 97.700000000000003, 99.140000000000001, 100.03999999999999]
>>> C = map(lambda x: (float(5)/9)*(x-32), Fahrenheit)
>>> print C
[39.200000000000003, 36.5, 37.300000000000004, 37.799999999999997]

example 2: map function can take many lists of equal length. Like

>>> a = [1,2,3,4]
>>> b = [17,12,11,10]
>>> map(lambda x,y:x+y, a,b)
[18, 14, 14, 14]

note: in the example above, the parameter x gets its values from the list a, while y gets its values from b

filter() function : filters out all the elements of a list for which the function func returns a boolean i.e. Tue or False. Like map function, applies  the function on all elements of the list 
syntax: filter(funct, list)
example: To find even numbers in the sample list
>>>fib = [0,1,1,2,3,5,8,13,21,34,55]
>>> result = filter(lambda x: x % 2 == 0, fib)
>>> print result
[0, 2, 8, 34]

reduce() function: typically applied on a list

The function reduce(func, seq) continually applies the function func() to the sequence seq. It returns a single value. 

If seq = [ s1, s2, s3, ... , sn ], calling reduce(func, seq) works like this:
At first the first two elements of seq will be applied to func, i.e. func(s1,s2) The list on which reduce() works looks now like this: [ func(s1, s2), s3, ... , sn ]
In the next step func will be applied on the previous result and the third element of the list, i.e. func(func(s1, s2),s3)
The list looks like this now: [ func(func(s1, s2),s3), ... , sn ]
Continue like this until just one element is left and return this element as the result of reduce()
example 1:
>>> reduce(lambda x,y: x+y, [47,11,42,13])
113

example 2: calculating the sum of numbers from 1 to 100:
>>> reduce(lambda x, y: x+y, range(1,101))
5050

example 3: determining the maximum of a list of numerical values by using reduce:
>>> f = lambda a,b: a if (a > b) else b
>>> reduce(f, [47,11,42,102,13])
102
