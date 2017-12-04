def calculate(arr,n,m,k):
	inx = m
	while len(arr) > k:
		#Here we treat the array as a stack and pop the elements as dictated by the step 'm' and calaculate the new index
		arr.pop(inx) 
		inx = (inx+m) % len(arr)
	
	print "The last "+str(k)+" numbers remaining are:" 
	print arr

def main():
	# Here we define and take the input from the user
	arr = []
	n = int(raw_input())
	m = int(raw_input())
	k = int(raw_input())

	#in the net part we populate the array based on the require length
	for i in range(0,n):
		arr.append(i)

	#calling the method that will give us the survivors based on k
	calculate(arr,n,m,k)
	
if __name__ == '__main__':
	main()
