#!/usr/bin/python3
"""
    1-my_list: class MyList
"""


class MyList(list):
    """
        MyList inherits from List
        Method:
            print_sorted: print the list in sorted manner
    """
    def print_sorted(self):
        """
            Prints a sorted format of the list.
        """
        new_list = self[:]
        done = False
        while not done:
            done = True
            for loop in range(len(new_list) - 1):
                a = new_list[loop]
                if new_list[loop] > new_list[loop + 1]:
                    new_list[loop] = new_list[loop + 1]
                    new_list[loop + 1] = a
                    done = False
        print(new_list)
