import sys

def pmi_pump(monthly_gain_dict, pmi_dict):
	average_monthly_pump_pmi_45to50 = 0
	count1 = 0
	sum1 = 0
	average_monthly_pump_pmi_50to55 = 0
	count2 = 0
	sum2 = 0
	average_monthly_pump_pmi_55to60 = 0
	count3 = 0
	sum3 = 0
	average_monthly_pump_pmi_60to65 = 0
	count4 = 0
	sum4 = 0

	for key in monthly_gain_dict:
		if key not in pmi_dict:
			continue
		pmi = float(pmi_dict[key])
		if pmi > 45 and pmi < 50:
			count1 += 1
			sum1 += float(monthly_gain_dict[key])
		elif pmi > 50 and pmi < 55:
			count2 += 1
			sum2 += float(monthly_gain_dict[key])
		elif pmi > 55 and pmi < 60:
			count3 += 1
			sum3 += float(monthly_gain_dict[key])
		elif pmi > 60 and pmi < 65:
			count4 += 1
			sum4 += float(monthly_gain_dict[key])

	average_monthly_pump_pmi_45to50 = sum1 / count1
	average_monthly_pump_pmi_50to55 = sum2 / count2
	average_monthly_pump_pmi_55to60 = sum3 / count3
	average_monthly_pump_pmi_60to65 = sum4 / count4

	print("average monthly pump after pmi is 45-50: ", average_monthly_pump_pmi_45to50)
	print("average monthly pump after pmi is 50-55: ", average_monthly_pump_pmi_50to55)
	print("average monthly pump after pmi is 55-60: ", average_monthly_pump_pmi_55to60)
	print("average monthly pump after pmi is 60-65: ", average_monthly_pump_pmi_60to65)

	'''
	average monthly pump after pmi is 45-50:  4.085
	average monthly pump after pmi is 50-55:  6.912345679012344
	average monthly pump after pmi is 55-60:  15.936111111111112
	average monthly pump after pmi is 60-65:  11.244444444444445
	'''

def return_pmi_dict():
	with open('pmi_data.txt', 'r') as fp1:
		pmi = fp1.readlines()
	fp1.close()
	dict1 = {}
	for i in pmi:
		str1 = ''
		content = i.split('\t')
		date = content[0].split('-')
		str1 = str1 + date[0] + '-' + date[1]
		dict1[str1] = round(float(content[1][:-1]), 1)
	return dict1


def monthly_return():
	with open('spx_price.txt', 'r') as fp:
		spx = fp.readlines()
	fp.close()
	dict1 = {}
	len1 = len(spx)
	idx = 0
	flag = 0
	first_monthly_data = 0
	key = ''
	while idx < len1:
		str1 = ''
		content = spx[idx].split(' ')
		date = content[0].split('-')
		str1 = str1 + date[0] + '-' + date[1]
		if str1 not in dict1:
			if flag == 1:
				last_monthly_data = spx[idx - 1].split(' ')
				gain_loss = float(last_monthly_data[1]) - float(first_monthly_data[1])
				dict1[key] = round(gain_loss, 1)
				flag = 0
			else:
				first_monthly_data = content
				key = str1
				dict1[key] = 0
				flag = 1
		idx += 1
	return dict1

def main():
	monthly_gain_dict = monthly_return()
	pmi_dict = return_pmi_dict()
	pmi_pump(monthly_gain_dict, pmi_dict)

if __name__ == "__main__":
	main()



