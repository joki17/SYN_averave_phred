
import os
import csv

#1. read files phred scores
#2. get average
#3. list average of all phred scores

def avg(lst): 
    return sum(lst) / len(lst) 

avgPhred_list = []
nameList = []

with open('avg_phred.csv', mode='w') as avg_phred_file:
	csv_writer = csv.writer(avg_phred_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)

	for filename in os.listdir(os.getcwd()):
		if filename.endswith('phd.1'):
			print(filename)

			f = open(filename, "r")
			
			file_list = []

			copy = False
			for line in f:
				#get lines in phd.1 file from BEGIN_DNA to END_DNA
				if line.strip() == "BEGIN_DNA":
					copy = True
				elif line.strip() == "END_DNA":
					copy = False
				elif copy:

					start_phred = line.find(' ')
					end_phred = line.find(' ', 2)
					file_list.append(int(line[start_phred+1 : end_phred]))

			#print(file_list)
			average = avg(file_list)
			print('Average: ' + str(average))
			avgPhred_list.append(average) #add the average phred to list
			nameList.append(filename)



			csv_writer.writerow([filename,average])



