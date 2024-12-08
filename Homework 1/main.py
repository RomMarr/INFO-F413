import time
from LazySelect import LazySelect
from QuickSelect import QuickSelect
import random


def main():
    print("\\begin{center}")
    print("\\begin{tabular}{c c c c c}")

    nb_tests = 1000
    max_val = 10000
    len_arr = 10000
    total_time_1 = 0
    total_time_2 = 0
    print("k & QS time & LS time & Tests passed on 1000 QuickSelect & Tests passed on LazySelect \\\\")
    for k in range(10, 50):
        count_1 = 0
        count_2 = 0
        qs_comparisons = 0
        ls_comparisons = 0
        for i in range(nb_tests):
            #A = random.sample(range(1, max_val + 1), len_arr)
            A = [random.randint(1, max_val) for _ in range(len_arr)]
            qs = QuickSelect()
            start = time.time()
            result = qs.quickSelect(A,0, len(A)-1, k) 
            qs_comparisons += qs.comparisons
            total_time_1 += time.time() - start
            if result == sorted(A)[k]:
                count_1 += 1


            ls = LazySelect()
            start_2 = time.time()
            result_2 = ls.lazySelect(A, k)
            ls_comparisons += ls.comparisons
            total_time_2 += time.time() - start_2
            if result_2 == sorted(A)[k-1]:
                count_2 += 1

        print(k, "&", round(total_time_1 / nb_tests, 7), "&", round(total_time_2 /
            nb_tests, 7), "&", count_1, "&", count_2, "&",round(qs_comparisons/nb_tests,3),"&", round(ls_comparisons/nb_tests,3),"\\\\")

    print("\\end{tabular}")
    print("\\end{center}")





if __name__ == "__main__":
    main()