def bubblesort(arr):
	for i in range(len(arr)):
		for k in range(len(arr) - 1, i, -1):
			if(arr[k] < arr[k - 1]):
				swap(arr, k , k - 1)

def swap(arr, pos, dest):
	temp = arr[pos]
	arr[pos] = arr[dest]
	arr[dest] = temp

if __name__ == "__main__":
	A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
	bubblesort(A)
	print A