import time, timeit, math, random

"""
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
"""

test_size0 = 8
test_list0 = [3, 7, 4, 11, 8, 5, 24, 10]
test_size1 = 5
test_list1 = [21, 14, 7, 41, 33]

test_size2 = 7
test_list2 = [1, 100, 5, 200, 10, 300, 15]

"""
user_size = 100000
user_array = [random.randint(0,1000000) for r in range(20000)]
"""
user_size = int(input())
user_array = input()
user_array = [int(e) for e in user_array.split()]


class Heap:
        #array, size
        def __init__(self, array, size):
                self.array = array
                self.size = size
                self.heapify()

        def heapify(self):
                start = math.floor(self.size/2)
                while start >= 0:
                        self.sift_down(start)
                        start -= 1

        def sift_down(self, start):
                root, local_min = start, start
                child = 2*root+1
                while child < self.size:
                        if self.array[local_min] > self.array[child]:
                                local_min = child
                        elif child + 1 < self.size and self.array[local_min] > self.array[child+1]:
                                local_min = child+1
                        elif local_min != root:
                                self.array[root], self.array[local_min] = self.array[local_min], self.array[root]
                                root = local_min
                        else:
                                return

        def get_min(self):
                return self.array[0]

        def reduce(self, k):
                self.array = [(a-k) for a in self.array if a-k >= 0]
                self.size  = len(self.array)
                self.heapify()

        def get_size(self):
                return self.size

def game(X, size):
        a = Heap(X, size)
        while a.get_size() > 1:
                m = a.get_min()
                k = (2 + (m % 2)) * m + 1
                # k will be odd when m is even, even m is odd
                a.reduce(k)
                results = ['B', 'A']
        return results[a.get_size()]


# print(game(test_list0, test_size0))
# print(game(test_list1, test_size1))
# print(game(test_list2, test_size2))

start_time0 = timeit.default_timer()
print(game(user_array, user_size))
elapsed0 = timeit.default_timer() - start_time0
print(elapsed0)
