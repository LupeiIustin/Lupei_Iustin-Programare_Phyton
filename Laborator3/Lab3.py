from collections import defaultdict


def operations(data_1, data_2):  # ex 1
    result = []
    inter = set()
    for element in data_1:
        if element in data_2:
            inter.add(element)
    result.append(inter)

    reunion = set()
    reunion.update(data_1)
    reunion.update(data_2)
    result.append(reunion)

    a_b = set()
    for element in data_1:
        if element not in data_2:
            a_b.add(element)
    result.append(a_b)

    b_a = set()
    for element in data_2:
        if element not in data_1:
            b_a.add(element)
    result.append(b_a)

    return result


def count_occurences(data):  # ex2
    counter = defaultdict(int)
    for element in data:
        counter[element] += 1
    return counter


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


def get_all_operations(data):  # ex 7
    result = defaultdict(set)

    for index in range(len(data) - 1):
        for jindex in range(index + 1, len(data)):
            operaration_res = operations(data[index], data[jindex])
            result[f"{data[index]} & {data[jindex]}"] = operaration_res[0]
            result[f"{data[index]} | {data[jindex]}"] = operaration_res[1]
            result[f"{data[index]} - {data[jindex]}"] = operaration_res[2]
            result[f"{data[jindex]} - {data[index]}"] = operaration_res[3]

    return result


def find_a_loop(data):  # ex 8
    condition = True
    current_key = 'start'
    next_key = None
    result = []

    while condition:
        next_key = data[current_key]
        result.append(data[current_key])
        if current_key == next_key:
            condition = False
        if data[next_key] == current_key:
            condition = False

        current_key = next_key

    return result


def get_specified_optional_param(param_1, param_2, param_3, param_4, karg_1=1, kaerg_2=2, karg_3=3, karg_4=5):  # ex 9
    # I can t understand
    pass


def get_xml_format(tag, content, href="http://python.org", _class=" my-link ", id=" someid "):      #ex 4
    return f"""<{tag} href=\"{href} \ "_class = \" {_class} \ "id = \" {id} \ "> {content} </a>"""


if __name__ == "__main__":
    print(operations([1, 2, 3, 4], [1, 2, 0]))
    print(count_occurences("alex are mere"))
    print(count_unique_and_more([1, 1, 2, 2, 3, 4, 5, 0]))
    print(get_all_operations([{1, 2, 3}, {1, 2}, {0}, {1, 1}]))
    print(find_a_loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))
    print(get_xml_format("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid "))
