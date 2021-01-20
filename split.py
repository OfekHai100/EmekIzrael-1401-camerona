import os

def write(path, data):
	f = open(path, "w+")
	data = '\n'.join(data)
	f.write(data)
	f.close()

def main():
	data_file = "data\\all.txt"
	val = "data\\val.txt"
	test = "data\\test.txt"
	train = "data\\train.txt"
	f = open(data_file, 'r')
	data = f.read().split('\n')
	f.close()
	l = len(data)
	val1, test1, train1 = data[:int(l*0.1)], data[int(l*0.1):int(l*0.25)], data[int(l*0.25):]
	write(val, val1)
	write(test, test1)
	write(train, train1)

if __name__ == '__main__':
    main()