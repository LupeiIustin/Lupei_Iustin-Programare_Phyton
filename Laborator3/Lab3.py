from collections import defaultdict

# 1.Write a function that receives as parameters two lists a and b and returns 
# a list of sets containing: (a intersected with b, a reunited with b, a - b, b - a)

def operations(data_1, data_2):  # ex 1
    result = []
    inter = set()
    for element in data_1:
        if element in data_2:
            inter.add(element)
    result.append(inter)  #daca d1 este in d2 adaugam in i

    reunion = set()
    reunion.update(data_1) #adauga doar elem din d1
    reunion.update(data_2) #same
    result.append(reunion) #adaugam setul in lista

    a_b = set()
    for element in data_1:
        if element not in data_2:
            a_b.add(element)#metoda de adaugare la seturi
    result.append(a_b)

    b_a = set()
    for element in data_2:
        if element not in data_1:
            b_a.add(element)
    result.append(b_a)

    return result

# 2. Write a function that receives a string as a parameter and
#  returns a dictionary in which the keys are the characters in the character string 
#  and the values are the number of occurrences of that character in the given text.

def count_occurences(data):  # ex2
    counter = defaultdict(int)  #dictionar cu valori default de tip int in cazul key -lor neinitializate
    for element in data:
        counter[element] += 1
    return counter

# 6. Write a function that receives as a parameter a list and returns a tuple (a, b),
#  representing the number of unique elements in the list, and b representing the number 
#  of duplicate elements in the list (use sets to achieve this objective).

def count_unique_and_more(data):  # ex 6
    result = defaultdict(int)

    for element in data:
        result[element] += 1

    unique, more = 0, 0
    for key in result:
        if result[key] == 1:
            unique += 1
        elif result[key] > 1:
            more += 1

    return (unique, more)

# 7. Write a function that receives a variable number of sets and returns a dictionary with
#  the following operations from all sets two by two: reunion, intersection, a-b, b-a.
#   The key will have the following form: "a op b", where a and b are two sets,
#    and op is the applied operator: |, &, -. 

# Ex: {1,2}, {2, 3} =>

# {

#     "{1, 2} | {2, 3}":  {1, 2, 3},

#     "{1, 2} & {2, 3}":  { 2 },

#     "{1, 2} - {2, 3}":  { 1 },

#     ...

# }

def get_all_operations(data):  # ex 7
    result = defaultdict(set)

    for index in range(len(data) - 1):
        for jindex in range(index + 1, len(data)):
            operaration_res = operations(data[index], data[jindex])
            result[f"{data[index]} & {data[jindex]}"] = operaration_res[0]  #folosim fstring pt ca e mai usor
            result[f"{data[index]} | {data[jindex]}"] = operaration_res[1]
            result[f"{data[index]} - {data[jindex]}"] = operaration_res[2]
            result[f"{data[jindex]} - {data[index]}"] = operaration_res[3]

    return result

# 8. Write a function that receives a single dict parameter named mapping. 
# This dictionary always contains a string key "start".
#  Starting with the value of this key you must obtain a list of objects by iterating 
#  over mapping in the following way: the value of the current key is the key for the next value,
#   until you find a loop (a key that was visited before). 
#   The function must return the list of objects obtained as previously described.

# Ex: loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'})
#  will return ['a', '6', 'z', '2']

def find_a_loop(data):  # ex 8
    condition = True
    current_key = 'start'
    next_key = None
    result = []

    while condition:    # mergem in loop pana cand gasim fie o pereche kay-value egale fie valoarea unei chei e egala cu o alta cheie 
        next_key = data[current_key]
        result.append(data[current_key])
        if current_key == next_key:
            condition = False
        if data[next_key] == current_key:
            condition = False

        current_key = next_key

    return result

# 9. Write a function that receives a variable number of positional arguments and 
# a variable number of keyword arguments adn will return the number of positional
#  arguments whose values can be found among keyword arguments values.

# Ex: my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5) will return returna 3

def get_specified_optional_param(param_1, param_2, param_3, param_4, karg_1=1, kaerg_2=2, karg_3=3, karg_4=5):  # ex 9
    # I can t understand
    pass

# 4. The build_xml_element function receives the following parameters: tag, content, 
# and key-value elements given as name-parameters. Build and return a string that represents the corresponding XML element. 
#  Example: build_xml_element ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid ") 
#  returns  the string = "<a href=\"http://python.org \ "_class = \" my-link \ "id = \" someid \ "> Hello there </a>"

def get_xml_format(tag, content, href="http://python.org", _class=" my-link ", id=" someid "):      #ex 4
    return f"""<{tag} href=\"{href} \ "_class = \" {_class} \ "id = \" {id} \ "> {content} </a>"""  #folosim fdocstring pentru a nu aparea erori de la ""/''


if __name__ == "__main__":
    print(operations([1, 2, 3, 4], [1, 2, 0]))
    print(count_occurences("alex are mere"))
    print(count_unique_and_more([1, 1, 2, 2, 3, 4, 5, 0]))
    print(get_all_operations([{1, 2, 3}, {1, 2}, {0}, {1, 1}]))
    print(find_a_loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))
    print(get_xml_format("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid "))
