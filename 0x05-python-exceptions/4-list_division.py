#!/usr/bin/python3
def list_division(my_list1, my_list2, list_length):
    listt = []
    for z in range(0, list_length):
        try:
            division = my_list1[z] / my_list2[z]
        except TypeError:
            print("wrong type")
            division = 0
        except ZeroDivisionError:
            print("division by 0")
            division = 0
        except IndexError:
            print("out of range")
            division = 0
        finally:
            listt.append(division)
    return (listt)
