import os
import random

def main():
	path = "data\\"
	mask = {"with_mask\\" : '1', "without_mask\\": '0'}
	dst = "data\\all.txt"
	f = open(dst, 'a+')
	for key in mask:
		images = os.listdir(path+key)
		for img in images:
			f.write(key+img+' '+mask[key]+'\n')
	f = open(dst, 'r')
	data = f.read().split('\n')
	random.shuffle(data)
	f.close()
	f = open(dst, 'w')
	for d in data:
		f.write(d+'\n')
	f.close()

if __name__ == '__main__':
    main()