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


def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
          return False
    return True


def return_prime_numbers(numbers):      #ex2
    result = []
    for number in numbers:
        if is_prime(number):
            result.append(number)
    return result

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

if __name__ == "__main__":
    # Driven code
    printFibonacciNumbers(7)
    print(return_prime_numbers([1,2,3,4,5,6,7,8,9,11]), end="\n")
    print_operations([123] , [2])