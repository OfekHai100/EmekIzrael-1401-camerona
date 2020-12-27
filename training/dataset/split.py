import os

def main():
	path = "data\\"
	train_path = "train\\"
	test_path = "test\\"
	val_path = "validation\\"
	number_of_img = len(os.listdir(path))
	train = 0.75*number_of_img
	val = 0.8*number_of_img
	i = 1
	j = 1
	while i < train:
		input_path = os.path.join(path, str(i)+'.jpg')
		output_path = os.path.join(train_path, str(j)+'.jpg')
		os.rename(input_path, output_path)
		i+=1
		j+=1
	j = 1
	while i < val:
		input_path = os.path.join(path, str(i)+'.jpg')
		output_path = os.path.join(val_path, str(j)+'.jpg')
		os.rename(input_path, output_path)
		i+=1
		j+=1
	j = 1
	while i < number_of_img:
		input_path = os.path.join(path, str(i)+'.jpg')
		output_path = os.path.join(test_path, str(j)+'.jpg')
		os.rename(input_path, output_path)
		i+=1
		j+=1

if __name__ == '__main__':
    main()