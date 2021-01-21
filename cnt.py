import os
import sys

"""
excpects:
cnt.py all.txt folder_photos
"""
print(len(os.listdir(sys.argv[1])))