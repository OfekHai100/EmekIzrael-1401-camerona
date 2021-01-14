import os


f = open('all.txt', 'r')
data = f.read().split('\n')
f.close()

data1 = []
for img in data:
	data1.append(img.split(' ')[0])

images = os.listdir('images/')

f = open('all.txt', 'a')
for img in images:
	if img not in data1:
		f.write(img+'\n')
f.close()