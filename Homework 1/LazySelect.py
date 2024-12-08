"""
Code inspired by the pseudo-code in the chapter 3 of the texbook
 "Randomized Algorithms" by Rajeev Motwani and Prabhakar Raghavan

Author : Romain Markowitch
Matricule : 000540172
Date : 24/10/2024
Course : INFO-F-413 Randomized algorithms
Project : Comparison between QuickSelect and LazySelect
"""
import random
import math

""" LazySelect class that implements the lazySelect algorithm and its comparisons"""
class LazySelect:
    def __init__(self):
        self.comparisons = 0

    def rank_ab(self, S, a, b):
        """ Return the ranks of 'a' and 'b' in one pass with fewer comparisons 
        and the different version of the list p """
        self.comparisons += len(S)
        rS_a = 0
        rS_b = 0
        greater_a = [] # all elements greater or equal to a
        between_ab = [] # all elements between a and b (inclusive)
        lesser_b = [] # all elements lesser or equal to b
        for elem in S:
            # Compare elem with 'a' and 'b', while avoiding duplicate comparisons
            if elem < a:
                rS_a += 1
                rS_b += 1  # Since elem < a, it is also <= b
                lesser_b.append(elem)
            elif elem <= b:
                rS_b += 1
                lesser_b.append(elem)
                greater_a.append(elem)
                between_ab.append(elem)
            else: # elem > b
                greater_a.append(elem)
        return rS_a, rS_b, lesser_b, greater_a, between_ab
    
    
    def lazySelect(self, S, k)-> int:
        """ Return the k-th smallest element in S """
        n = len(S)
        if k < 1 or k > n:
            raise ValueError("k is out of bounds")
        while True:
            # Step 1: Pick n^(3/4) random elements from S with replacement
            R_size = int(n ** (3 / 4))
            R = [random.choice(S) for _ in range(R_size)]

            # Step 2: Sort R
            R.sort()
            self.comparisons += R_size * math.log2(R_size)

            # Step 3: Variables
            x = k * (n ** (-1 / 4))
            l = max(math.floor(x - (n ** 0.5)), 1)
            h = min(math.ceil(x + (n ** 0.5)), R_size)
            a = R[l-1]
            b = R[h-1]
            
            # Find the ranks of a and b
            rS_a, rS_b, lesser_b, greater_a, between_ab = self.rank_ab(S, a, b)

            # Step 4: Define P based on k
            if k < n ** (1 / 4):
                p = lesser_b
            elif k > n - n ** (1 / 4):
                p = greater_a
            else:
                p = between_ab
            
            # Check if the size of P is manageable
            if len(p) <= 4 * R_size + 2 and  len(p)> k-rS_a > 0: #S[k] in p:  ##### this cond is false (first pary ...)   
                
                # Step 5: Sort P and find the (k - rS(a) + 1)-th element in P
                p.sort()
                self.comparisons += len(p) * math.log2(len(p))
                if k < n ** (1 / 4):
                    return p[k]
                return p[k - rS_a -1]  # Return the k-th smallest element
  