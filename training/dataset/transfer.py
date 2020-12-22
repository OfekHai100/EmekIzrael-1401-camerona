import os

def main():
    path = "all_data\\"
    dst = "dest\\"
    folders = os.listdir(path)
    i = 1
    for folder in folders:
    	print(folder)
    	new_pth = os.path.join(path, folder)
    	images = os.listdir(new_pth)
    	for image in images:
    		input_path = os.path.join(new_pth, image)
    		output_path = os.path.join(dst, str(i)+'.jpg')
    		os.rename(input_path, output_path)
    		i += 1

    """
    i = len(os.listdir(dst)) + 1
    break_at = int(input("how much photos to transfer? "))
    for image_path in images:
        if i == break_at:
            break
        input_path = os.path.join(path, image_path)
        output_path = os.path.join(dst, str(i)+'.jpg')
        os.rename(input_path, output_path)
        i += 1"""

if __name__ == '__main__':
    main()