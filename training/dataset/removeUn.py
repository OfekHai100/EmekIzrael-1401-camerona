
def main():
	path = "val.txt"
	f = open(path, 'r')
	data = f.read()
	f.close()
	data = data.split('\n')
	data2 = []
	for d in data:
		data2.append(d[:-1])
	data = '\n'.join(data2)
	f = open(path, 'w+')
	f.write(data)

if __name__ == '__main__':
    main()