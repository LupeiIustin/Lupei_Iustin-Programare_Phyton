
# 2) Create a function and an anonymous function that receive a variable number of arguments. Both will return the sum
#  of the values of the keyword arguments.

def my_function(*args, **kwargs):
    sum = 0
    for i in kwargs:
        sum += kwargs[i]
    return sum
    


x = lambda *args,**kwargs: sum(kwargs[i] for i in kwargs)



# 3) Using functions, anonymous functions, list comprehensions and filter, implement three methods to generate a list 
# with all the vowels in a given string.


def vowels(s):
    v = []
    for i in range(len(s)-1):
        if s[i] in "aeiouAEIOU":
            v.append(s[i])
    return v

v = lambda s: list(s[i] for i in range(len(s)) if s[i] in "aeiouAEIOU")

v2 = list(filter(lambda i: i in "aeiouAEIOU", "Programming in Python is fun"))

# 4) Write a function that receives a variable number of arguments and keyword arguments. The function returns a list
#  containing only the arguments which are dictionaries, containing minimum 2 keys and at least one string key with 
#  minimum 3 characters.

def dictionaryArgument(*args, **kwargs):
    list = []
    for a in args:
        if isinstance(a, dict):
            if len(a) >= 2:
                for element in a:
                    if isinstance(element, str):
                        if len(element) >= 3:
                            list.append(a)
                            break
    for a in kwargs:
        if isinstance(kwargs[a], dict):
            if len(kwargs[a]) >= 2:
                for element in kwargs[a]:
                    if isinstance(element, str):
                        if len(element) >= 3:
                            list.append(kwargs[a])
                            break
    return list

 

# 5) Write a function with one parameter which represents a list. The function will return a new list containing all 
# the numbers found in the given list.


def numbers(x):
    list = []
    for i in x:
        if isinstance(i, int) or isinstance(i, float):
            list.append(i)
        
    return list


# 6) Write a function that receives a list with integers as parameter that contains an equal number of even and odd 
# numbers that are in no specific order. The function should return a list of pairs (tuples of 2 elements) of numbers
#  (Xi, Yi) such that Xi is the i-th even number in the list and Yi is the i-th odd number


def numberList(x):
    l = []
    odd = list(filter(lambda i: i%2==0, x))
    even = list(filter(lambda i: i%2==1, x))

    for i in range(0, len(odd)):
        t = (odd[i], even[i])
        l.append(t)

    return l



# 7) Write a function called process that receives a variable number of keyword arguments

# The function generates the first 1000 numbers of the Fibonacci sequence and then processes them in the following way:

# If the function receives a parameter called filters, this will be a list of predicates (function receiving an argument and returning True/False) and will retain from the generated numbers only those for which the predicates are True. 

# If the function receives a parameter called limit, it will return only that amount of numbers from the sequence. 

# If the function receives a parameter called offset, it will skip that number of entries from the beginning of the result list. 

# The function will return the processed numbers.

def process(**kwargs):
    fib = [0]*100
    fib[1] = 1

    for i in range(2, 100):
        fib[i] = fib[i-1]+fib[i-2]
    
    valid = fib

    filters = kwargs["filters"]
    for f in filters:
        x = list(filter(f, valid))
        valid = x

    limit = kwargs["limit"]
    offset = kwargs["offset"]

    res = []
    for i in range(offset, offset+limit):
        res.append(valid[i])


    return res


def sum_digits(x):
    return sum(map(int, str(x)))

# 9) Write a function that receives a list of pairs of integers (tuples with 2 elements) as parameter (named pairs). The function
#  should return a list of dictionaries for each pair (in the same order as in the input list) that contain the following keys
#   (as strings): sum (the value should be sum of the 2 numbers), prod (the value should be product of the two numbers), 
#   pow (the value should be the first number raised to the power of the second number) 


def f9(pairs):
    def sum(a,b):
        return a + b

    def prod(a, b):
        return a * b

    def pow(a, b):
        return a ** b

    list = []
    for p in pairs:
        d = dict()
        d["sum"] = sum(p[0], p[1])
        d["prod"] = prod(p[0], p[1])
        d["pow"] = pow(p[0], p[1])
        list.append(d)

    return list

#############################

if __name__ == "__main__":

    print(my_function(1, 2, c=3, d=4))                                                                         
    print(v2)                                                                                                         
    print(dictionaryArgument({1: 2, 3: 4, 5: 6},               
                            {'a': 5, 'b': 7, 'c': 'e'}, 
                            {2: 3}, 
                            [1, 2, 3],
                            {'abc': 4, 'def': 5},
                            3764,
                            dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},
                            test={1: 1, 'test': True}))
    print(numbers([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))    
    print(numberList([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))         
    print(process(filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20],  
                limit=2,
                offset=2))  
    print(f9(pairs = [(5, 2), (19, 1), (30, 6), (2, 2)] ))   


    # 2 3 4 5 6 7 9   
