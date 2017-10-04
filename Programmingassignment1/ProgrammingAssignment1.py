import time, timeit, math, random
"""
test_size = 8
test_list = [3, 7, 4, 11, 8, 5, 24, 10]

test_size2 = 5
test_list2 = [21, 14, 7, 41, 33]

test_size3 = 7
test_list3 = [1, 100, 5, 200, 10, 300, 15]
"""
test_size4 = 100000
test_list4 = [random.randint(0,1000000) for r in range(20000)]
"""

user_array = input('array: ')
user_array = [int(e) for e in user_array.split()]
user_size = int(input('size: '))
"""
class Heap:
        #array, size
        def __init__(self, array, size):
                self.array = array
                self.size = size

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

        def get_min(self):
                return self.array[0]

        def reduce(self, k):
                self.array = [(a-k) for a in self.array if a-k >= 0]
                self.size = len(self.array)
                self.heapify() # DON'T REBUILD THE HEAP EVERY TIME THAT'S WASTEFUL AF

        def get_size(self):
                return self.size

"""
def minimum(X): #This implementation is faster, but I guess it's called cheating?
        heapq.heapify(X)
        return X[0]

def alt_minimum(X, size): #This needs some finetuning.
        for h in range((size//2)-1,-1,-1):
		val_h = X[h]
		j = 2*h+1
		while(j<size):
			if j<size-1 and X[j]>X[j+1]:
				j+=1
			if val_h<=X[j]:
				break
			X[(j-1)//2]=X[j]
			j=2*j+1
			X[(j-1)//2]=val_h
	return X[0]
"""
def game(X, size):

        #user_input = input('Array:')
        a = Heap(X, size)
        while a.get_size() > 1:
                m = a.get_min()
                k = (2+(m %2))*m+1

                a.reduce(k)
        results = ['B', 'A']
        return results[a.get_size()]

def faster_game(X):
        a = sorted(X)
        while len(a) > 1:
                m = a[0]
                k = (2+(m %2))*m+1
                a = [e-k for e in a if e-k >=0]
        results = ['B', 'A']
        return results[len(a)]
#print(game(test_list, test_size))
#print(game(test_list2, test_size2))
#print(game(test_list3, test_size3))
#print(game(user_array, user_size))

start_time0 = timeit.default_timer()
print(game(test_list4, test_size4))
elapsed0 = timeit.default_timer() - start_time0

start_time1 = timeit.default_timer()
print(faster_game(test_list4))
elapsed1 = timeit.default_timer() - start_time1

print('Runtime 0: ', elapsed0, '\nRuntme 1: ', elapsed1)
