import heapq
import time 
import timeit

#start_time = timeit.default_timer()

test_size = 8
test_list = [3, 7, 4, 11, 8, 5, 24, 10]

test_size2 = 5
test_list2 = [21, 14, 7, 41, 33]

test_size3 = 7
test_list3 = [1, 100, 5, 200, 10, 300, 15]

k = 0
m = 0

def format(array):
	X.split(",")

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

def compute(m):
	if m % 2 == 0:
		return(2*m +1)
	else:
		return(3*m +1)

def game(size, X):
	while size > 1:
		m = alt_minimum(X,size)
		k = compute(m)

		X = [item - k for item in X if item >= 0] #I have found no way of compressing these two loops into one loop
		X = [item for item in X if item >= 0]

		#print('The value of k is:', k)
		#print('The current array is:', X)
		
		size = len(X)

	if size == 1:
		print('A')
	else:
		print('B')

game(test_size, test_list)
game(test_size2, test_list2)
game(test_size3, test_list3)

#elapsed = timeit.default_timer() - start_time
#rint('Runtime:', elapsed)
