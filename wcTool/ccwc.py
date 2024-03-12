import os.path
import sys


def get_system_arguments():
    return sys.argv[1], sys.argv[2]


def is_valid_file(path):
    return os.path.isfile(path)

def count_bytes(file_path):
    count = 0

    with open(file_path, "rb") as f:
        byte = f.read(1)
        while byte:
            byte = f.read(1)
            count += 1
    return count

option, file_path = get_system_arguments()
print(str(count_bytes(file_path)) + " " + file_path)
