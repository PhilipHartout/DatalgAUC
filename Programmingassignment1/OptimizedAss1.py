import time, timeit, math, random

"""
test_size = 8
test_list = [3, 7, 4, 11, 8, 5, 24, 10]

test_size2 = 5
test_list2 = [21, 14, 7, 41, 33]

test_size3 = 7
test_list3 = [1, 100, 5, 200, 10, 300, 15
"""
test_size = 10000
test_list = [random.randint(0,20000) for r in range(10000)]
"""
test_size = int(input())
test_list = input()
test_list = [int(e) for e in test_list.split()]
"""



array, size = test_list, test_size

# THE IMPORTANT FUNCTIONS
def heapify():
        start = int(math.floor(size/2))
        while start >= 0:
                sift_down(start)
                start -= 1

def sift_down(start):
        root, local_min = start, start
        while (2*root+1) < size:
                child = 2*root+1

                if array[local_min] > array[child]:
                        local_min = child
                elif child + 1 < size and array[local_min] > array[child+1]:
                        local_min = child+1
                elif local_min != root:
                        array[root], array[local_min] = array[local_min], array[root]
                        root = local_min
                else:
                        return
def reduce(array, k):
        array = [a-k for a in array if a-k >= 0]
        return array


# THE GAME

start_time0 = timeit.default_timer()
heapify()

while size > 1:
        m = array[0]
        k = (2 + (m % 2)) * m + 1
        array = reduce(array, k)
        size = len(array)
        heapify()

results = ['B', 'A']
print(results[size])
elapsed0 = timeit.default_timer() - start_time0
print('Runtime 0: ', elapsed0)
