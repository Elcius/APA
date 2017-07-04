def QuickSort(num_list, first,last):
	i = first
	j = last
	pivot = num_list[first]

	while i<j:
		while num_list[i] < pivot:
			i += 1

		while num_list[j] > pivot:
			j -= 1

		if i <= j:
			tmp = num_list[i]
			num_list[i] = num_list[j]
			num_list[j] = tmp
			i += 1
			j -= 1

	if j > first:
		QuickSort(num_list,first,j)

	if i < last:
		QuickSort(num_list,i,last)



def MergeSort(num_list):
	if len(num_list) > 1:
		mid = len(num_list)//2
		lefthalf = num_list[:mid]
		righthalf = num_list[mid:]

		MergeSort(lefthalf)
		MergeSort(righthalf)

		i = 0
		j = 0
		k = 0

		while i < len(lefthalf) and j < len(righthalf):
			if lefthalf[i] < righthalf[j]:
				num_list[k] = lefthalf[i]
				i += 1
			else:
				num_list[k] = righthalf[j]
				j += 1
			k += 1

		while i < len(lefthalf):
			num_list[k] = lefthalf[i]
			i += 1

		while j < len(righthalf):
			num_list[k] = righthalf[j]
			j += 1



def InsertionSort(list):
	for i in range(1, len(list)):
		current = list[i]
		previous_pos = i-1

		while previous_pos >= 0 and current < list[previous_pos]:
			list[previous_pos + 1] = list[previous_pos]
			previous_pos -= 1

		list[previous_pos+1] = current




def SelectionSort(list):
	for i in range(0, len(list)-1):
		min_index = i
		for j in range(i+1, len(list)):
			if list[j] < list[min_index]:
				min_index = j
		if i != min_index:
			list[i], list[min_index] = list[min_index], list[i]

def HeapSort(list, begin = None, end = None):
	if begin == None:
		for numb in range((len(list)-1)//2, -1, -1):
			HeapSort(list, numb, len(list) - 1)

		for numb in range(len(list)-1, 0, -1):
			list[0], list[numb] = list[numb], list[0]
			HeapSort(list, 0, numb-1)

	else:
		aux = list[begin]
		i = begin * 2 + 1

		while i <= end:
			if i < end and list[i] < list[i+1]:
				i = i + 1
			if aux < list[i]:
				list[begin] = list[i]
				begin = i
				i = 2 * begin + 1
			else:
				i= end + 1
		list[begin] = aux