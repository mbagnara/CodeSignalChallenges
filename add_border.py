'''
Given a rectangular matrix of characters, add a border of asterisks(*) to it.

For

picture = ["abc",
           "ded"]

the output should be

addBorder(picture) = ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]


'''


def listMatrix(m):
    for i in m:
        print(i)


def addBorder(picture):

    # first and last line
    new_list = []
    # print(picture[0])
    length = len(picture[0]) + 2
    new_line = "*" * length

    # print("len", len(picture[0]), new_line)

    new_list.append(new_line)

    for i in picture:
        new_list.append("*" + str(i) + "*")

    new_list.append(new_line)

    return new_list


picture = ["abc",
           "ded"]

listMatrix(addBorder(picture))
