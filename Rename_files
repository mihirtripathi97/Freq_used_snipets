import os
import glob

    
old_file_array = glob.glob('*.profile.txt')
print(old_file_array)
new_file_array = []

for file in old_file_array:
    x = file.replace('.profile', '_ds_profile')
    os.rename(file,x)
    new_file_array.append(x)
    
print(new_file_array)    
