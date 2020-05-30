import sys

def sort_data(contents):
	try:
		output = open("spx_price.txt", 'w')
	except IOError:
		output = open("spx_price.txt", 'w')

	for i in contents:
		str1 = ''
		lst = i.split('\t')
		str1 = str1 + lst[0] + ' ' + lst[len(lst) - 1] 
		print(str1)
		output.write(str1)
	output.close()

def flip_data(file_content): #this makes 1,2,3,... to ...,3,2,1
	output = open("spx_price.txt", "w")
	last_idx1 = len(file_content) - 1
	while last_idx1 > -1:
		str1 = ''
		lst = file_content[last_idx1].split(' ')
		str1 = str1 + lst[0] + ' ' + lst[len(lst) - 1]
		output.write(str1)
		last_idx1 -= 1
	output.close()

def fix_date_order(file_content):
	output = open("spx_price.txt", "w")
	for i in file_content:
		str1 = ''
		lst = i.split(' ')
		lst2 = lst[0].split('-')
		if int(lst2[2]) >= 2003:
			str1 = str1 + lst2[2] + '-' + change_month_to_num(lst2[1]) + '-' + lst2[0] + ' ' + lst[len(lst) - 1] 
			output.write(str1)
	output.close()

def change_month_to_num(string):
	if string == 'Jan':
		return '01'
	elif string == 'Feb':
		return '02'
	elif string == 'Mar':
		return '03'
	elif string == 'Apr':
		return '04'
	elif string == 'May':
		return '05'
	elif string == 'Jun':
		return '06'
	elif string == 'Jul':
		return '07'
	elif string == 'Aug':
		return '08'
	elif string == 'Sep':
		return '09'
	elif string == 'Oct':
		return '10'
	elif string == 'Nov':
		return '11'
	else:
		return '12'

'''def main(): #formatting spx data
	with open(sys.argv[1], 'r') as fp:
		contents = fp.readlines()
	sort_data(contents)
	with open("spx_price.txt", 'r') as fp1:
		file_content = fp1.readlines()
	fp1.close()
	flip_data(file_content)
	with open("spx_price.txt", 'r') as fp2:
		file_content = fp2.readlines()
	fp2.close()
	fix_date_order(file_content)'''

def invert_data(file_content1, file_content2):
	output1 = open("spx_price.txt", "w")
	output2 = open("pmi_data.txt", "w")

	last_idx1 = len(file_content1) - 1
	while last_idx1 > -1:
		str1 = ''
		lst = file_content1[last_idx1].split(' ')
		str1 = str1 + lst[0] + ' ' + lst[len(lst) - 1]
		output1.write(str1)
		last_idx1 -= 1
	output1.close()

	last_idx2 = len(file_content2) - 1
	while last_idx2 > -1:
		str2 = ''
		lst = file_content2[last_idx2].split(' ')
		str2 = str2 + lst[0] + ' ' + lst[len(lst) - 1]
		output2.write(str2)
		last_idx2 -= 1
	output2.close()




def main(): #formatting spx data and pmi data
	with open('spx_price.txt', 'r') as fp:
		file_content1 = fp.readlines()
	with open("pmi_data.txt", 'r') as fp1:
		file_content2 = fp1.readlines()
	fp.close()
	fp1.close()
	invert_data(file_content1, file_content2)


if __name__ == "__main__":
	main()





