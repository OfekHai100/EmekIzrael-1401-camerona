import os
import sys

def write(path, data):
	f = open(path, "w+")
	data = '\n'.join(data)
	f.write(data)
	f.close()

"""
excpects:
split.py all_data.txt train.txt percentage_in_float test.txt percentage_in_float val.txt
"""
def main():
	data = sys.argv[1:]
	data_file = data[0]
	train = data[1]
	train_am = float(data[2])
	test = data[3]
	test_am = float(data[4])
	val = data[5]
	f = open(data_file, 'r')
	data = f.read().split('\n')
	f.close()
	l = len(data)
	test_data = data[:int(l*test_am)]
	train_data = data[int(l*test_am):int(l*(test_am+train_am))]
	val_data = data[int(l*(test_am+train_am)):]
	write(val, val_data)
	write(test, test_data)
	write(train, train_data)

if __name__ == '__main__':
    main()