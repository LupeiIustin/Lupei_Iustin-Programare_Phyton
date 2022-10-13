from collections import defaultdict

def word_count(text): #ex 10
    words = 1
    for i in text:
        if i == " ":
            words += 1
    return words


def find_gcd(arr):   # ex 1
    if len(arr) <= 1:
        return arr
    else:
        for i in range(len(arr)-1):
            a = arr[i]
            b = arr[i+1]
            while b:
                a, b = b, a%b
            arr[i+1] = a
        return a


def count_vowels(text):   # ex 2
    vowels = "aeiouAEIOU"
    count = 0
    for let in text:
        if let in vowels:
            count +=1
    return count


def count_substrings(string, substring):  # ex3
    count = 0
    substring_len = len(substring)
    for i in range(len(string)):
        if string[i:i + substring_len] == substring:
            count += 1
    return count


def upper_camel_case(text):  #ex 4
    result = []
    for index in range(len(text)):
        if index != 0 and text[index].isupper():
            result.append("_" + text[index])
        elif index == 0:
            result.append(text[index])
        else:
            result.append(text[index])
    return "".join(result)




def is_palindrome(number):  #ex 6
    if str(number)[::-1] == str(number):
        return True
    return False


def common_letter(text):    #ex 9
    letters = defaultdict(int)
    for letter in text:
        letters[letter] += 1

    return max(letters, key=letters.get)


def find_first_number(text):        # ex 7
    result = []
    index = 0
    while index < len(text):
        while index < len(text) and text[index].isnumeric():
            result.append(text[index])
            index += 1
        index += 1

    return result

def count_bits(number): #ex 8 
    result = []
    while number > 0:
        if number % 2 == 0:
            result.append('0')
            number //= 2
        else:
            result.append('1')
            number //= 2
    return "".join(result).count("1")




if __name__ == "__main__":
    print(word_count("ana are mere"))
    print(find_gcd([10, 15, 20]))
    print(count_vowels("Ana are mere"))
    print(count_substrings("Ana are Ana mere", "Ana"))
    print(upper_camel_case("AnaAreMere"))
    print(is_palindrome(10013))
    print(common_letter("aabbccc"))
    print(find_first_number("Eu am 10"))\
    print(count_bits(24))
   