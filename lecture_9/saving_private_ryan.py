# This save the words 'private ryan' to the hard disk.
def save_private_ryan(path):
    f = open(path, 'w')

    lines = []
    for i in range(5):
        lines.append('This is line {}\n'.format(i + 1))
    f.writelines(lines)
    f.close()


def read_private_ryan(path):
    f = open('private.txt', 'r')
    print(type(f))
    data = f.read()
    f.close()
    return data


def read_with_cool_syntax(path):
    with open(path, 'r') as file_stream:
        for line in file_stream:
            print(line)
        # option 2
        lines = file_stream.readlines()
        for line in lines:
            print(line)


def bad_duplicate(path):
    path2 = 'private1.txt'
    f1 = open(path, 'r')
    f2 = open(path2, 'w')
    f2.write(f1.read())
    f1.close()
    f2.close()


# # First option
# f = open(path, 'w')
# f.write('hello')
# f.close()
#
# # second option
# with open(path, 'w') as f:
#     f.write('hello')
print('This is after the file is closed.')

path = r'C:\Users\Borat\PycharmProjects\python_basic_course\python_september\lecture_9\private.txt'
read_with_cool_syntax(path)
# bad_duplicate(path)
# print(read_private_ryan(path))
