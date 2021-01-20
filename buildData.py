import os
import random
import sys

"""
excpects:
buildData.py all.txt folder_photos class_number folder_photos class_number folder_photos class_number ...
"""
def main():
	data = sys.argv[1:]
	all_file = data[0]
	data = data[1:]
	i = 1
	folder_val = {}
	while i < len(data):
		folder_val[data[i-1]] = data[i]
		i+=2
	data = []
	for key in mask:
		images = os.listdir(key)
		for img in images:
			data.append(key+img+' '+mask[key])
	random.shuffle(data)
	with open(all_file, 'a+') as f:
		f.write('\n'.join(data))

if __name__ == '__main__':
    main()