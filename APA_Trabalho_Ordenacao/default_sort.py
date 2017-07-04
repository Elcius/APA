import all_sorts
import time

global time_exceeded
time_exceeded = False

global total_time_per_sort
total_time_per_sort = 0

def CallSort(vec):

	option = "DefautSort"
	path = "resultados/result_defaultsort"
	start = time.time()	
	sorted(vec)
	stop = time.time()

	if (int((stop-start)*1000)/1000) > 300:		# 5 min -> 300 seg
		global time_exceeded
		time_exceeded = True
		return False			#Incomplete process

	global total_time_per_sort
	total_time_per_sort += (int((stop-start)*1000)/1000)
	#print(total_time_per_sort)

	output_file = open(path, 'a')
	for item in vec:
		output_file.write("%s\n" % item)
	output_file.close()

	#output_time_file.write("File: "+ input_names[11:] + " " + option + ", input file process time: " + str((int((stop-start)*1000)/1000)) + "s.")
	print ("File: "+ input_names[11:] + " " + option + ", input file process time: " + str((int((stop-start)*1000)/1000)) + "s.")


def Call(input_names,n):
	print ("Processing ...")

	if int(input_names[14]) == 1 and (len(input_names)-1) == 24:			
		with open(input_names) as file:
			numbs = file.readlines()
				
		vec = []
		for numb in numbs:
			vec.append(int(numb))

		#if (ISCall(vec,n,100000) == False):
		if (CallSort(vec) == False):
			print ("File: "+ input_names[11:] + " DefaultSort TIMEOUT!")

	if int(input_names[14]) == 5:			
		with open(input_names) as file:
			numbs = file.readlines()
				
		vec = []
		for numb in numbs:
			vec.append(int(numb))
		
		if (CallSort(vec) == False):
			print ("File: "+ input_names[11:] + " DefaultSort TIMEOUT!")

	if int(input_names[14]) == 1 and (len(input_names)-1) == 25:		
		with open(input_names) as file:
			numbs = file.readlines()
				
		vec = []
		for numb in numbs:
			vec.append(int(numb))
		
		if (CallSort(vec) == False):
			print ("File: "+ input_names[11:] + " DefaultSort TIMEOUT!")

with open("files_input.txt") as file:
	lines_input = file.readlines()

print ("\n------------------------ Program initiated ------------------------")

count = 0

print ("\n-------------------------------------------------------------------\n\n")

for line in lines_input:
	input_names = "instancias/" + str(line)
	input_names = input_names[0:len(input_names)-1]
	if input_names[len(input_names)-1] != 'n':
		input_names = input_names + 'n'

	if int(input_names[11]) == 9:
		#print (time_exceeded)
		if time_exceeded == False: 
			Call(input_names,90)

		count += 1

		#print(count)
		if count == 15:
			#print ("PROXIMO 2")
			time_exceeded = False	#reseting

	if int(input_names[11]) == 5 and count >= 15 and count <=30:
			#print ("PROXIMO 2")

			#print (time_exceeded)
		if time_exceeded == False: 
			Call(input_names,50)

		count += 1

			#print(count)
		if count == 30:
			time_exceeded = False	#reseting
				

	if int(input_names[11]) == 1 and count >= 30:
			#print ("PROXIMO 3")

			#print (time_exceeded)
		if time_exceeded == False: 
			Call(input_names,10)

		count += 1

			#print(count)
		if count == 45:
			time_exceeded = False	#reseting
			count = 0
				#print ("END_SORT")

print ("Sort function total process time: " + str(total_time_per_sort) + "s.")
