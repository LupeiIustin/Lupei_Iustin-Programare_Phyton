from collections import defaultdict

def printFibonacciNumbers(n):   #ex 1
    f1 = 0
    f2 = 1
    if (n < 1):
        return
    print(f1, end=" ")
    for x in range(1, n):
        print(f2, end=" ")
        next = f1 + f2
        f1 = f2
        f2 = next
    print()

######################################

def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
          return False
    return True

######################################

def return_prime_numbers(numbers):      #ex2
    result = []
    for number in numbers:
        if is_prime(number):
            result.append(number)
    return result

######################################

def print_operations(group1, group2):    #ex 3
    result = []
    result.extend(group1)
    result.extend(group2)
    print(f"A reunited with be is: {result}",  end="\n")
    result.clear()

    for element in group1:
        if element in group2:
            result.append(element)
    print(f"A intersected with b is : {result}")
    result.clear()

    for element in group1:
        if element not in group2:
            result.append(element)
    print(f"A minus  b is : {result}")
    result.clear()

    for element in group2:
        if element not in group1:
            result.append(element)
    print(f"B minuns A is : {result}")
    result.clear()

######################################

def musical_notes(notes,  moves, start):        #ex4       
    result = []

    index = start
    result.append(notes[start])

    for move in moves:
        if index + move > len(notes) - 1 or index + move < 0:
            index = (index + move) % 5
        else:
            index += move
        print(index)
        result.append(notes[index])

    return result

######################################

def replace_matrix_elem(matrix):      #ex5

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j < i:
                matrix[i][j] = 0
    
    return matrix

######################################

def x_occurences(data, x):      #ex 6
    result = []
    occ = defaultdict(int)
    for element in data:
        for elem in element:
            occ[elem] += 1
    
    for key in occ:
        if occ[key] == x:
            result.append(key)
    
    return result

######################################

def is_palindrome(data):               #ex 7
    data = str(data)
    if data == data[::-1]:
        return True
    return False

def extract_palindrome_info(data):
    palindromes = []
    for element in data:
        if is_palindrome(element) and (element < 0 or element > 9):
            palindromes.append(element)
    return (len(palindromes), max(palindromes))

######################################

def check_ascii(data, x=1, flag=True):  #ex 8
    result = []
    if flag:
        for string in data:
            for character in string:
                if ord(character) % x == 0:
                    result.append(character)
    else:
        for string in data:
            for character in string:
                if ord(character) % x != 0:
                    result.append(character)

    return result

######################################

if __name__ == "__main__":
    # Driven code
    printFibonacciNumbers(7)
    print(return_prime_numbers([1,2,3,4,5,6,7,8,9,11]), end="\n")
    print_operations([123] , [2])
    print(musical_notes(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))
    print(replace_matrix_elem([[0,1,2,3], [0,1,2,3], [0,1,2,3], [0,1,2,3]]))
    print(x_occurences([ [1,2,3], [2,3,4],[4,5,6], [4,1, "test"]], 1))
    print(extract_palindrome_info([121, 2, 2223, 111, 12, 00, 777]))
    print(check_ascii(["test", "hello", "lab002"], x = 2, flag = False))

 # 0 1 2 3 4
 # 
