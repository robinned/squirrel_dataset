import os

flist = os.listdir('./')

pre_list = '6789abcdef'

orig_path = 'C:/Users/highf/Documents/GitHub/squirrel_dataset/unlabeled/'

for char in pre_list:
    new_path = orig_path + char + '/'
    for fname in flist:
        if (fname[0] == char) and not (len(fname) == 1):
            print("renaming", orig_path + fname, 'to', new_path + fname)
            os.rename(orig_path + fname, new_path + fname)