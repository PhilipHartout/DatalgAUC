"""
Jesse Hoogland and Philip Hartout - Programming Assignment 1

So we thought, oh this assignment looks pretty simple we just
need to implement a heap and that'll do that.

Little did we know that it's much easier to implement a heap than
one that manages routine <2 second runtime for very long inputs

Approaches we tried:
1) check out of it would make sense to actually sort the list in full
this way we wouldn't have to reheapify everytime we remove k from the elements
however, even using python's default sorted, likely the fastest sorting alg
available in python, the resulting program routinely underperformed our original
heap. Implementing our own full sort would not have proved much more successful.


2) change the get_min function
Instead of reheapifying, we considered simply changing the get min function to a
divide and conquer approach that would take log(n) time, we wouldn't have to
restructure the entire heap every time. in order to deal with this we would also
have to include a second "full_size" that keeps track of the total number of
elements where "size" kept track of only positive elements
However this was also slower.
The implementation of this new get_min is below

def get_min(self, loc=0):
        if self.array[loc] > 0:
                return self.array[loc]
        # Divide and conquer
        first, second = None, None
        if 2 * loc + 1 < self.full_size:
                first = self.get_min(2*loc+1)
        if 2 * loc + 2 < self.full_size:
                second = self.get_min(2*loc+2)

        if first:
                if second:
                        return min(first, second)
                return first

3) we considered a more elegant reheapifying upon removing negative elements
As the resulting structure would be still consist of disjoint heaps, we thought
we might simply swap the top negative elements of the subheaps with their right
most element, sift-down again and repeat less times than the standard heapify
However, upon doing this, the program again performed slower than our standard.
                # while start >= 0:
                #         if self.array[start] < 0:
                #                 self.array[start] = self.array.pop()
                #                 self.size -= 1
                #                 self.sift_down(start)
                #        start -= 1

4) Got rid of class, used global variables instead, hard-wire everything
This made the whole thing a bit uglier, and we started getting namespace errors.
Didn't get it to work successfully

5) WE FIGURED IT OUT:
We realized that the time intensive step was removing k from every element,
and reheapifying. While before we were focusing on the latter of those two
steps (reheapifying), now instead we looked at the k. we realized we could just
keep increasing k instead of having to subtract this from everything. Then
we could iterate over the sorted list and it would be done in no time
This is the final implementation we stuck to, so all the extra heap code
is excess

"""
import time, timeit, math, random

user_size = int(input())
user_array = input()
user_array = [int(e) for e in user_array.split()]


class Heap:
        #Array, size
        def __init__(self, array, size):
                self.array = array
                self.size = size
                self.heapify()
                self.heap_sort()

        #Assumes self.array is already a heap
        def heap_sort(self):
                sorted_array = []
                for i in range(len(self.array)):
                        sorted_array.append(self.heap_pop())
                self.array = sorted_array

        #Assumes unordered array
        def heapify(self):
                start = math.floor(self.size/2)
                while start >= 0:
                        self.sift_down(start)
                        start -= 1

        def sift_down(self, start):
                root, local_min = start, start
                while (2*root+1) < self.size:
                        child = 2*root+1
                        if self.array[local_min] > self.array[child]:
                                local_min = child
                        elif child + 1 < self.size and self.array[local_min] > self.array[child+1]:
                                local_min = child+1
                        elif local_min != root:
                                self.array[root], self.array[local_min] = self.array[local_min], self.array[root]
                                root = local_min
                        else:
                                return

        def heap_pop(self):
                self.array[0], self.array[-1] = self.array[-1], self.array[0]
                m = self.array.pop()
                self.size -= 1
                self.sift_down(0)
                return m

        def get_min(self):
                return self.array[0]

#------------------------------------------------------------
# FUNCTIONWISE IMPLEMENTATION BELOW
#------------------------------------------------------------
def sift_down(a, a_size, start):
        root, local_min = start, start
        while (2*root+1) < a_size:
                child = 2*root+1
                if a[local_min] > a[child]:
                        local_min = child
                elif child + 1 < a_size and a[local_min] > a[child+1]:
                        local_min = child+1
                elif local_min != root:
                        a[root], a[local_min] = a[local_min], a[root]
                        root = local_min
                else:
                        return a

def heapify(a, a_size):
        start = math.floor(a_size/2)
        while start >= 0:
                a = sift_down(a, a_size, start)
                start -= 1
        return a

def heapsort(X, size):
        s, h  = size, heapify(X, size)
        def heap_pop(a, a_size):
                a[0], a[-1] = a[-1], a[0]
                m = a.pop()
                a_size -= 1
                a = sift_down(a, s, 0)
                return a, a_size, m

        #Sorting on heap
        sorted_array = []
        for i in range(len(h)):
                h, s, e = heap_pop(h, s)
                sorted_array.append(e)

        self.array = sorted_array

def game(X, size):
        a = Heap(X, size).array 
        k = 0
        for i in range(len(a)-1):
                e = a[i]
                if e > k:
                        m = e - k
                        k += (2 + (m % 2)) * m + 1
        if a[-1] > k:
                return "A"
        return "B"

print(game(user_array, user_size))
