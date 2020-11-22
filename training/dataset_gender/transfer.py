import os

def main():
	path = "validation\\temp\\"
	dst = "validation\\male\\"
	images = os.listdir(path)
	i = 1
	break_at = int(input("how much photos to transfer? "))
	for img_path in images:
		if i == break_at+1:
			break
		input_path = os.path.join(path, img_path)
		output_path = os.path.join(dst, str(i)+'.jpg')
		os.rename(input_path, output_path)
		i += 1

if __name__ == '__main__':
    main()