import os

count_at = ["without_mask\\", "with_mask\\", "validation\\without_mask\\", "validation\\with_mask\\",
			"test\\without_mask\\" , "test\\with_mask\\"]

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