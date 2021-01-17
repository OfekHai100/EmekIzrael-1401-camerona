import os
import random

def main():
	path = "all.txt"
	train_path = "train.txt"
	test_path = "test.txt"
	val_path = "val.txt"

	f = open(path, 'r')
	data = f.read().split('\n')
	f.close()
	random.shuffle(data)
	random.shuffle(data)

	amount = len(data)
	train = 0.75*amount
	val = 0.8*amount

	f = open(train_path, 'w+')
	f.write('\n'.join(data[:int(train)]))
	f.close()

	f = open(val_path, 'w+')
	f.write('\n'.join(data[int(train):int(val)]))
	f.close()

	f = open(test_path, 'w+')
	f.write('\n'.join(data[int(val):]))
	f.close()

if __name__ == '__main__':
    main()