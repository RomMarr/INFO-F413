import random
import time
import matplotlib.pyplot as plt
from LazySelect import LazySelect
from QuickSelect import QuickSelect

def collect_data(nb_tests, nb_values):
    nb_tests = nb_tests
    max_val = nb_values
    len_arr = nb_values
    k_values = list(range(1,nb_values-1,nb_values//100))
    
    qs_times = []
    ls_times = []
    qs_comparisons_list = []
    ls_comparisons_list = []
    
    for k in k_values:
        qs_comparisons = 0
        ls_comparisons = 0
        total_time_1 = 0
        total_time_2 = 0
        for i in range(nb_tests):
            A = [random.randint(1, max_val) for _ in range(len_arr)]
            
            # QuickSelect
            qs = QuickSelect()
            start = time.time()
            result = qs.quickSelect(A, 0, len(A)-1, k) 
            total_time_1 += time.time() - start
            qs_comparisons += qs.comparisons

            # LazySelect
            ls = LazySelect()
            start_2 = time.time()
            result_2 = ls.lazySelect(A, k)
            total_time_2 += time.time() - start_2
            ls_comparisons += ls.comparisons
        
        qs_times.append(total_time_1 / nb_tests)
        ls_times.append(total_time_2 / nb_tests)
        qs_comparisons_list.append(qs_comparisons / nb_tests)
        ls_comparisons_list.append(ls_comparisons / nb_tests)
        
    return k_values, qs_times, ls_times, qs_comparisons_list, ls_comparisons_list

def plot_time_comparisons(k_values, qs_times, ls_times, nb_test, nb_values):
    plt.figure(figsize=(10, 6))
    plt.plot(k_values, qs_times, label="QuickSelect Time", marker='o')
    plt.plot(k_values, ls_times, label="LazySelect Time", marker='o')
    plt.xlabel("k")
    plt.ylabel("Time (seconds)")
    title = "Average Time Comparison for "+ str(nb_test) + " tests on " + str(nb_values) +" elements" 
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_comparisons(k_values, qs_comparisons_list, ls_comparisons_list, nb_test, nb_values):
    plt.figure(figsize=(10, 6))
    plt.plot(k_values, qs_comparisons_list, label="QuickSelect Comparisons", marker='o')
    plt.plot(k_values, ls_comparisons_list, label="LazySelect Comparisons", marker='o')
    plt.xlabel("k")
    plt.ylabel("Number of Comparisons")
    title = "Average Number of Comparisons for "+ str(nb_test)+ " tests on " + str(nb_values) +" elements"
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    nb_tests = 10
    nb_values = 10000000
    k_values, qs_times, ls_times, qs_comparisons_list, ls_comparisons_list = collect_data(nb_tests, nb_values)
    
    plot_time_comparisons(k_values, qs_times, ls_times, nb_tests, nb_values)
    plot_comparisons(k_values, qs_comparisons_list, ls_comparisons_list, nb_tests, nb_values)

if __name__ == "__main__":
    main()
