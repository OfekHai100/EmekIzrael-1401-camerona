import os

def main():
	path = "mid\\"
	dst = "val\\"
	i = len(os.listdir(dst)) + 1
	images = os.listdir(path)
	print(len(images))
	for image in images:
		input_path = os.path.join(path, image)
		output_path = os.path.join(dst, str(i)+'.jpg')
		os.rename(input_path, output_path)
		i += 1

if __name__ == '__main__':
    main()