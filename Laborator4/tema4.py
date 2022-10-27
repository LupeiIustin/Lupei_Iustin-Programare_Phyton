import os
from pathlib import Path

def get_sorted_extensions(directory):
    result = []
    for root, dirs, files in os.walk(directory):
        for filename in files:
            print(os.path.join(root, filename))
            filename, file_extension = os.path.splitext(file)
            result.append(file_extension)

    result = result.sort()


if __name__ == "__main__":
    print(get_sorted_extensions("Tema4"))

    

