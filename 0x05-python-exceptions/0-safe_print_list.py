#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        elements_printed = 0
        for i in range(x):
            print(my_list[i], end="")
            elements_printed += 1
        print()
        return elements_printed
    except:
        print()
        return elements_printed
