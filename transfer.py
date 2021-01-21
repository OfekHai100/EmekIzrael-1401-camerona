import os
import sys

"""
excpects:
transfer.py input_folder output_folder
"""
def main():
	data = sys.argv[1:]
	print(data)
	input_path = data[0]
	dst_path = data[1]
	i = len(os.listdir(dst_path)) + 1
	images = os.listdir(input_path)
	print(len(images))
	for image in images:
		full_input_path = os.path.join(input_path, image)
		output_path = os.path.join(dst_path, str(i)+'.jpg')
		os.rename(full_input_path, output_path)
		i += 1

if __name__ == '__main__':
    main()