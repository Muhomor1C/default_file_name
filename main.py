import re
listofstrings = ['name', 'file', 'Denis', 'name(1)', 'Copy(1)name', 'name(1l', 'name(23)']


def find_index(pattern):
    list_ = []
    index = 0
    for name in listofstrings:
        result = re.match(pattern, name)
        if not result is None:
            list_.append(int(result.group(2)))
    if len(list_) > 0:
        index = sorted(list_)[-1]
    return index


def up_version(desiredname, operation):
    replasename = desiredname.replace('(', '\\(').replace(')', '\\)')
    if operation == "1":  # Make
        suffix = r"\()([0-9]+)(\))"
        pattern = f"({replasename}{suffix}"
        version = find_index(pattern)
        return desiredname + '(' + str(version + 1) + ')'
    if operation == "2":  # Copy
        preffix = r"(Copy\()([0-9]+)(\)"
        pattern = f'{preffix}{replasename})'
        version = find_index(pattern)
        return 'Copy(' + str(version + 1) + ')' + desiredname


def add_file(desiredname, operation):
    if desiredname not in listofstrings:
        filename = desiredname
    else:
        filename = up_version(desiredname, operation)
    listofstrings.append(filename)
    print_filenames_list()


def print_filenames_list():
    listofstrings.sort()
    for n in range(len(listofstrings)):
        print(str(n) + "  " + str(listofstrings[n]))
    print()


def main():
    desiredname = "My book"
    operattion = input("1 - содать файл, 2 - копировать, 222 - выход  -> ")
    if operattion == "2":
        print_filenames_list()
        desiredname = listofstrings[int(input("Выбери файл (0, 1, 2... -> "))]
        if desiredname == '':
            desiredname = "My book"
    elif operattion == "1":
        print_filenames_list()
        desiredname = input("Введи имя нового файла. По умолчанию - My book  ->")
        if desiredname == '':
            desiredname = "My book"
    elif operattion == "222":
        return
    else:
        print("Нет такой комманды")
        main()
    add_file(desiredname, operattion)
    main()


if __name__ == '__main__':
    main()
