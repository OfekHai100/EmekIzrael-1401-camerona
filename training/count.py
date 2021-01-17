import os

count_at = ["female\\", "male\\", "validation\\female\\", "validation\\male\\",
			"test\\female\\" , "test\\male\\"]

for path in count_at:
	print(path, len(os.listdir(path)))


#train:
#with: 1505
#out: 1885

#test
#with: 0
#out: 0

#validation
#with: 0
#out: 0