from collections import defaultdict


def operations(data_1, data_2):     #ex 1
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


def count_occurences(data):      #ex2
   counter = defaultdict(int)
   for element in data:
      counter[element] += 1
   return counter


def count_unique_and_more(data):    #ex 6
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

if name == "main":
   print(operations([1,2,3,4], [1,2,0]))
   print(count_occurences("alex are mere"))
   print(count_unique_and_more([1,1,2,2,3,4,5,0]))