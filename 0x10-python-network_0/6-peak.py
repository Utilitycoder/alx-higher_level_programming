#!/usr/bin/python3
#!/usr/bin/python3
""" let's find peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """ find peak in a list of unsorted integers """
    if list_of_integers is None or len(list_of_integers) == 0:
        return None
    return find_peak_rec(list_of_integers, 0, len(list_of_integers) - 1)


def find_peak_rec(list_of_integers, low, high):
    """ find peak recursively """
    if low == high:
        return list_of_integers[low]
    mid = (low + high) // 2
    if list_of_integers[mid] > list_of_integers[mid + 1]:
        return find_peak_rec(list_of_integers, low, mid)
    return find_peak_rec(list_of_integers, mid + 1, high)

