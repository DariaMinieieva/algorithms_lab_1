'''
This module contains experiments for sorting algorithms
'''

from random import randint, shuffle
from time import time
from sort_algorithms import selection_sort, shell_sort, insertion_sort, merge_sort


def random_lst(n: int) -> list:
    '''
    Generate list of random numbers with length 2**n
    '''
    lst = []

    for _ in range(2**n):
        lst.append(randint(0, 2**n))

    return lst


def reduced_random_lst(n: int) -> list:
    '''
    Generate list of random numbers from {1, 2, 3}
    with length 2**n
    '''
    lst = []

    for _ in range(2**n):
        lst.append(randint(1, 3))

    return lst


def test_random_list():
    '''
    Test algorithms on randomly generated data
    '''
    for i in range(7, 16):
        algorithms = {
            selection_sort: [0, 0],
            insertion_sort: [0, 0],
            merge_sort: [0, 0],
            shell_sort: [0, 0]
        }

        for _ in range(5):
            lst = random_lst(i)

            for algorithm, values in algorithms.items():
                lst_test = lst.copy()
                now = time()
                values[1] += algorithm(lst_test)
                values[0] += time() - now

        with open("res_1.csv", "a", encoding="utf-8") as output_file:
            output_file.write("Algorithm,Time,Num of Comparisons\n")
            output_file.write("Selection sort," + str(
                algorithms[selection_sort][0]/5) + "," + str(algorithms[selection_sort][1]/5) + "\n")

            output_file.write("Insertion sort," + str(
                algorithms[insertion_sort][0]/5) + "," + str(algorithms[insertion_sort][1]/5) + "\n")

            output_file.write("Merge sort," + str(
                algorithms[merge_sort][0]/5) + "," + str(algorithms[merge_sort][1]/5) + "\n")

            output_file.write("Shell sort," + str(
                algorithms[shell_sort][0]/5) + "," + str(algorithms[shell_sort][1]/5) + "\n\n")


def test_sorted_list():
    '''
    Test algorithms on sorted data
    '''
    algorithms = (selection_sort, insertion_sort, merge_sort, shell_sort)
    for i in range(7, 16):
        with open("res_2.csv", "a", encoding="utf-8") as output_file:
            output_file.write("Algorithm,Time,Num of Comparisons\n")
            for algorithm in algorithms:
                lst = list(range(2**i))
                now = time()
                comparison = algorithm(lst)
                time_comp = time() - now

                output_file.write(
                    f"{algorithm.__name__},{time_comp},{comparison}\n")

            output_file.write("\n")


def test_reversed_list():
    '''
    Test algorithms on data sorted in reversed order
    '''
    algorithms = (selection_sort, insertion_sort, merge_sort, shell_sort)
    for i in range(7, 16):
        with open("res_3.csv", "a", encoding="utf-8") as output_file:
            output_file.write("Algorithm,Time,Num of Comparisons\n")
            for algorithm in algorithms:
                lst = list(range(2**i, -1, -1))
                now = time()
                comparison = algorithm(lst)
                time_comp = time() - now

                output_file.write(
                    f"{algorithm.__name__},{time_comp},{comparison}\n")

            output_file.write("\n")


def test_reduced_random_list():
    '''
    Test algorithms on arrays that consist with elements from {1, 2, 3}
    '''
    for i in range(7, 16):
        algorithms = {
            selection_sort: [0, 0],
            insertion_sort: [0, 0],
            merge_sort: [0, 0],
            shell_sort: [0, 0]
        }

        lst = reduced_random_lst(i)
        for _ in range(3):
            shuffle(lst)

            for algorithm, values in algorithms.items():
                lst_test = lst.copy()
                now = time()
                values[1] += algorithm(lst_test)
                values[0] += time() - now

        with open("res_4.csv", "a", encoding="utf-8") as output_file:
            output_file.write("Algorithm,Time,Num of Comparisons\n")
            output_file.write("Selection sort," + str(
                algorithms[selection_sort][0]/3) + "," + str(algorithms[selection_sort][1]/3) + "\n")

            output_file.write("Insertion sort," + str(
                algorithms[insertion_sort][0]/3) + "," + str(algorithms[insertion_sort][1]/3) + "\n")

            output_file.write("Merge sort," + str(
                algorithms[merge_sort][0]/3) + "," + str(algorithms[merge_sort][1]/3) + "\n")

            output_file.write("Shell sort," + str(
                algorithms[shell_sort][0]/3) + "," + str(algorithms[shell_sort][1]/3) + "\n\n")


if __name__ == "__main__":
    test_random_list()
    test_sorted_list()
    test_reversed_list()
    test_reduced_random_list()
