import all_sorts
import time

global time_exceeded
time_exceeded = False

global total_time_per_sort
total_time_per_sort = 0

def CallSort(vec,sort_op):

	if sort_op == 1:
		option = "QuickSort"
		path = "resultados/result_quicksort"
		start = time.time()		# Getting initial time
		all_sorts.QuickSort(vec,0,len(vec)-1)
		stop = time.time()		# Getting final time

	elif sort_op == 2:
		option = "MergeSort"
		path = "resultados/result_mergesort"
		start = time.time()	
		all_sorts.MergeSort(vec)
		stop = time.time()

	elif sort_op == 3:
		option = "HeapSort"
		path = "resultados/result_heapsort"
		start = time.time()	
		all_sorts.HeapSort(vec)
		stop = time.time()

	elif sort_op == 4:
		option = "InsertionSort"
		path = "resultados/result_insertionsort"
		start = time.time()	
		all_sorts.InsertionSort(vec)
		stop = time.time()

	elif sort_op == 5:
		option = "SelectionSort"
		path = "resultados/result_selectionsort"
		start = time.time()	
		all_sorts.SelectionSort(vec)
		stop = time.time()

	if (int((stop-start)*1000)/1000) > 300:		# Checking if the processing time is bigger than 5 min (300 sec).
		global time_exceeded
		time_exceeded = True
		return False			# Incomplete process of file

	global total_time_per_sort
	total_time_per_sort += (int((stop-start)*1000)/1000)	# Getting the total time function processing.
	
	output_file = open(path, 'a')
	for item in vec:
		output_file.write("%s\n" % item)	# Writing the sorted numbers in a output file.
	output_file.close()

	print ("File: "+ input_names[11:] + " " + option + ", input file process time: " + str((int((stop-start)*1000)/1000)) + "s.")


def Processing(input_names,sort_number,n):
	print ("Processing ...")

	if int(input_names[14]) == 1 and (len(input_names)-1) == 24:	# Selecting the x0.100000.x.in files. Ex: 10.100000.1.in
		with open(input_names) as file:
			numbs = file.readlines()	# Acessing the file and getting all numbers that will be sorted.
				
		vec = []
		for numb in numbs:
			vec.append(int(numb))		# Felling the vector with numbers.

		if sort_number == 1:		#QuickSort
			if (CallSort(vec,sort_number) == False):	# Checking if some file of the subset got more than 5 minuts.
				print ("File: "+ input_names[11:] + " QuickSort TIMEOUT!")

		elif sort_number == 2:		#MergeSort
			if (CallSort(vec,sort_number) == False):
				print ("File: "+ input_names[11:] + " MergeSort TIMEOUT!")

		elif sort_number == 3:		#HeapSort
			if (CallSort(vec,sort_number) == False):
				print ("File: "+ input_names[11:] + " HeapSort TIMEOUT!")

		elif sort_number == 4:		#InsertionSort
			if (CallSort(vec,sort_number) == False):
				print ("File: "+ input_names[11:] + " InsertionSort TIMEOUT!")

		elif sort_number == 5:		#SelectionSort
			if (CallSort(vec,sort_number) == False):
				print ("File: "+ input_names[11:] + " SelectionSort TIMEOUT!")

	if int(input_names[14]) == 5:			# Selecting the 'x0.500000.x.in' files. Ex: '10.500000.1.in'
		with open(input_names) as file:
			numbs = file.readlines()
				
		vec = []
		for numb in numbs:
			vec.append(int(numb))
		
		if sort_number == 1:
			if (CallSort(vec,1) == False):
				print ("File: "+ input_names[11:] + " QuickSort TIMEOUT!")

		elif sort_number == 2:		#Merge
			if (CallSort(vec,sort_number) == False):
				print ("File: "+ input_names[11:] + " MergeSort TIMEOUT!")

		elif sort_number == 3:		#Heap
			if (CallSort(vec,sort_number) == False):
				print ("File: "+ input_names[11:] + " HeapSort TIMEOUT!")

		elif sort_number == 4:		#Insertion
			if (CallSort(vec,sort_number) == False):
				print ("File: "+ input_names[11:] + " InsertionSort TIMEOUT!")

		elif sort_number == 5:		#Selection
			if (CallSort(vec,sort_number) == False):
				print ("File: "+ input_names[11:] + " SelectionSort TIMEOUT!")

	if int(input_names[14]) == 1 and (len(input_names)-1) == 25:		# Selecting the 'x0.1000000.x.in' files. Ex: '10.1000000.1.in'
		with open(input_names) as file:
			numbs = file.readlines()
				
		vec = []
		for numb in numbs:
			vec.append(int(numb))
		
		if sort_number == 1:		#Quick
			if (CallSort(vec,1) == False):
				print ("File: "+ input_names[11:] + " QuickSort TIMEOUT!")

		elif sort_number == 2:		#Merge
			if (CallSort(vec,sort_number) == False):
				print ("File: "+ input_names[11:] + " MergeSort TIMEOUT!")

		elif sort_number == 3:		#Heap
			if (CallSort(vec,sort_number) == False):
				print ("File: "+ input_names[11:] + " HeapSort TIMEOUT!")

		elif sort_number == 4:		#Insertion
			if (CallSort(vec,sort_number) == False):
				print ("File: "+ input_names[11:] + " InsertionSort TIMEOUT!")

		elif sort_number == 5:		#Selection
			if (CallSort(vec,sort_number) == False):
				print ("File: "+ input_names[11:] + " SelectionSort TIMEOUT!")


with open("files_input.txt") as file:	# files_input.txt has all the names of input (.in) files.
	lines_input = file.readlines()

print ("\n------------------------ Program initiated ------------------------")

count = 0			# Controls the process order based in the sequence of the names in 'files_input.txt'. First files with 10% of entropy then 50% and at the end 90%
sort_function = 1	# Controls the sort function that is running. 1 to QuickSort, 2 to MergeSort, 3 to HeapSort, 4 to InsertionSort and 5 to SelectionSort.
while sort_function < 6:	# The code bellow will be executed by each sort function.
	print ("\n-------------------------------------------------------------------\n\n")

	for line in lines_input:	# Getting names of input files one by one and acessing them at directory 'instancias'.
		input_names = "instancias/" + str(line)
		input_names = input_names[0:len(input_names)-1]
		if input_names[len(input_names)-1] != 'n':
			input_names = input_names + 'n'

		if int(input_names[11]) == 9:	# Processing files with 10% of entropy.
			if time_exceeded == False: 	# Check if the sort function needed more then 5 minutes to process the first file.
				Processing(input_names,sort_function,90)

			count += 1

			if count == 15:
				time_exceeded = False	#reseting

		if int(input_names[11]) == 5 and count >= 15 and count <=30:	# Processing files with 50% of entropy.

			if time_exceeded == False: 
				Processing(input_names,sort_function,50)

			count += 1

			if count == 30:		
				time_exceeded = False	#reseting
				

		if int(input_names[11]) == 1 and count >= 30:  # Processing files with 90% of entropy.

			if time_exceeded == False: 
				Processing(input_names,sort_function,10)

			count += 1

			if count == 45:
				time_exceeded = False	#reseting
				count = 0

	sort_function += 1		# Select the next sort function.
	print ("Sort function total process time: " + str(total_time_per_sort) + "s.")
