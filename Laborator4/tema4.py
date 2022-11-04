import os
import sys

"""1)	Să se scrie o funcție ce primeste un singur parametru, director, ce reprezintă calea către un director. 
Funcția returnează o listă cu extensiile unice sortate crescator (in ordine alfabetica) a fișierelor din directorul dat ca parametru."""

def extensions(dir):
    ext = set()
    for (root,directories,files) in os.walk(dir):
        for fileName in files:
            base_name = os.path.basename(fileName)
            dot_position = 0
            for i in range(len(base_name)):
                if base_name[i] == '.':
                    dot_position = i
                    break
            ext.add(base_name[dot_position+1:])
    return ext


# print(extensions(r"C:\Users\Alex\Desktop\Python"))


"""2)	Să se scrie o funcție ce primește ca argumente două căi: director si fișier. 
Implementati functia astfel încât în fișierul de la calea fișier să fie scrisă pe câte o linie, calea absolută a fiecărui fișier din 
interiorul directorului de la calea folder, ce incepe cu litera A. """


def paths(dir, fis):
    try:
        f = open(fis, "w")
        for (root,directories,files) in os.walk(dir):
            for name in files:
                f.write(os.path.join(root, name) + '\n')
                #f.wrtie("\n")
                 
        f.close() 
    except:
        print("Unable to open file")

# paths(r"C:\Users\Alex\Desktop\Python",r"C:\Users\Alex\Desktop\Python\laborator4\ex2.txt")


"""3)	Să se scrie o funcție ce primește ca parametru un string my_path.
Dacă parametrul reprezintă calea către un fișier, se vor returna ultimele 20 de caractere din conținutul fișierului. Dacă parametrul
 reprezintă calea către un director, se va returna o listă de tuple (extensie, count), sortată descrescător după count, unde extensie 
 reprezintă extensie de fișier, iar count - numărul de fișiere cu acea extensie. Lista se obține din toate fișierele (recursiv) din 
 directorul dat ca parametru. """


def path(my_path):
    if os.path.isfile(my_path):
        try:
            f = open(my_path, "r")
            f_content = f.read()
            return f_content[-20:]

        except:
            print("Unable to open file")
            return 0
    elif os.path.isdir(my_path):
        list = []
        d = dict()
        for (root,directories,files) in os.walk(my_path):
            for fileName in files:
                base_name = os.path.basename(fileName)
                dot_position = 0
                for i in range(len(base_name)):
                    if base_name[i] == '.':
                        dot_position = i
                        break
                ext_name = base_name[dot_position+1:]
                if ext_name in d:
                    d[ext_name] = d[ext_name] + 1
                else:
                    d[ext_name] = 1

        for element in d:
            list.append((element, d[element]))
        list.sort(key = lambda i: i[1], reverse = True)
        return list
    return "invalid path"
        


# print(path(r"C:\Users\Alex\Desktop\Python\laborator4\ex2.txt"))
# print(path(r"C:\Users\Alex\Desktop\Python"))


"""4)	Să se scrie o funcție ce returnează o listă cu extensiile unice a fișierelor din directorul dat ca argument la linia de comandă
(nerecursiv). Lista trebuie să fie sortată crescător."""


def extensions(dir):
    ext = set()
    for (root,directories,files) in os.walk(dir):
        for fileName in files:
            base_name = os.path.basename(fileName)
            dot_position = 0
            for i in range(len(base_name)):
                if base_name[i] == '.':
                    dot_position = i
                    break
            ext.add(base_name[dot_position+1:])
        break
    x = []
    x = list(ext)
    x.sort()
    return x

# print(extensions(sys.argv[1]))


"""5)	Să se scrie o funcție care primește ca argumente două șiruri de caractere, target și to_search șireturneaza o listă de fișiere
 care conțin to_search. Fișierele se vor căuta astfel: dacă target este un fișier, se caută doar in fișierul respectiv iar dacă este un
  director se va căuta recursiv in toate fișierele din acel director. Dacă target nu este nici fișier, nici director, se va arunca o 
  excepție de tipul ValueError cu un mesaj corespunzator."""


def search(target, to_search):
    list = []
    try:
        if os.path.isfile(target):
            print("file")
            f = open(target, "r")
            f_content = f.read()
            f.close()
            if to_search in f_content:
                list.append(target)
            

        elif os.path.isdir(target):
            for (root,directories,files) in os.walk(target):
                for fileName in files:
                    full_fileName = os.path.join(root,fileName)
                    f = open(full_fileName, "r")
                    f_content = f.read()
                    f.close()
                    if to_search in f_content:
                        list.append(full_fileName)

        else: 
            raise ValueError
    except ValueError:
        print("invalid path")
    return list


# print(search(r"C:\Users\Alex\Desktop\Python\laborator3\laborator3.py", "x"))
# print(search(r"C:\Users\Alex\Desktop\Python\laborator3", "x"))


"""6)	Să se scrie o funcție care are același comportament ca funcția de la exercițiul anterior, cu diferența că primește un parametru
 în plus: o funcție callback, care primește un parametru, iar pentru fiecare eroare apărută în procesarea fișierelor, se va apela funcția
  respectivă cu instanța excepției ca parametru"""

#TODO


"""7)	Să se scrie o funcție care primește ca parametru un șir de caractere care reprezintă calea către un fișer si returnează un dicționar
 cu următoarele cămpuri: full_path = calea absoluta catre fisier, file_size = dimensiunea fisierului in octeti, file_extension = extensia
  fisierului (daca are) sau "", can_read, can_write = True/False daca se poate citi din/scrie in fisier."""


def dictionary(path):
    d = dict()
    d["full_path"]=path
    d["file_size"]=os.path.getsize(path)
    d["file_extension"]=os.path.splitext(path)[1][1:]
    if os.access(path, os.R_OK):
        d["can_read"] = True
    else:
        d["can_read"] = False
    if os.access(path, os.W_OK):
        d["can_write"] = True
    else:
        d["can_write"] = False
    return d


# print(dictionary(r"C:\Users\Alex\Desktop\Python\laborator3\laborator3.py"))


"""8)	Să se scrie o funcție ce primește un parametru cu numele dir_path. Acest parametru reprezintă calea către un director aflat pe disc.
 Funcția va returna o listă cu toate căile absolute ale fișierelor aflate în rădăcina directorului dir_path."""


def directories(dir_path):
    list = []
    try:
        if not os.path.isdir(dir_path):
            raise Exception
        for (root,directories,files) in os.walk(dir_path):
            for fileName in files:
                full_fileName = os.path.join(root,fileName)
                list.append(full_fileName)
    except Exception:
        print("not a directory")
    finally:
        return list


print(directories(r"C:\Users\Alex\Desktop\Python"))