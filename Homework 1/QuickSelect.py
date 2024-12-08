"""
Code inspired from wikipedia : Quickselect -> https://en.wikipedia.org/wiki/Quickselect

Author : Romain Markowitch
Matricule : 000540172
Date : 24/10/2024
Course : INFO-F-413 Randomized algorithms
Project : Comparison between QuickSelect and LazySelect
"""
import random

""" QuickSelect class that implements the quickSelect algorithm and its comparisons"""
class QuickSelect:
    def __init__(self):
        self.comparisons = 0

    def partition(self,list, left, right, pivot_index):
        """ Partition the list for left and right parts around the pivotIndex """
        pivot_value = list[pivot_index]
        list[pivot_index], list[right] = list[right], list[pivot_index]  # Move pivot to end
        store_index = left
        for i in range(left, right):
            self.comparisons += 1
            if list[i] < pivot_value:
                list[store_index], list[i] = list[i], list[store_index]
                store_index += 1
        list[right], list[store_index] = list[store_index], list[right]  # Move pivot to its final place
        return store_index

    def quickSelect(self,list, left, right, k):
        """ Return the k-th smallest element in the list given"""
        if left == right:  # If the list contains only one element,
            self.comparisons += 1
            return list[left]  
        pivot_index = random.randint(left, right)  # select a pivotIndex between left and right,
        # e.g., left + floor(rand() % (right − left + 1))
        pivot_index = self.partition(list, left, right, pivot_index)
        # The pivot is in its final sorted position
        self.comparisons += 1
        if k == pivot_index:
            return list[k]
        elif k < pivot_index:
            return self.quickSelect(list, left, pivot_index - 1, k)
        else:
            return self.quickSelect(list, pivot_index + 1, right, k)