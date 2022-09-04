import os
import shutil

paths = {
    'label_val' : 'C:/Users/highf/Documents/GitHub/squirrel_dataset/dataset_two/Labels/val/',
    'label_train' : 'C:/Users/highf/Documents/GitHub/squirrel_dataset/dataset_two/Labels/train/',
    'img_val' : 'C:/Users/highf/Documents/GitHub/squirrel_dataset/dataset_two/Images/val/',
    'img_train' : 'C:/Users/highf/Documents/GitHub/squirrel_dataset/dataset_two/Images/train/',
    'img' : 'C:/Users/highf/Documents/GitHub/squirrel_dataset/dataset_one/Images/', #all annotated images
    'label' : 'C:/Users/highf/Documents/GitHub/squirrel_dataset/dataset_one/Labels/' #all labels
    }


def main():
    shutil.rmtree(paths['label_val'])
    shutil.rmtree(paths['label_train'])
    shutil.rmtree(paths['img_val'])
    shutil.rmtree(paths['img_train'])
    
    os.mkdir(paths['label_val'])
    os.mkdir(paths['label_train'])
    os.mkdir(paths['img_val'])
    os.mkdir(paths['img_train'])
    
    
    num_img = len(os.listdir(paths['img'])) #number of annotated images
    num_val = int((num_img * 0.1) // 1) #get number of val images to be made
    
    img_names = os.listdir(paths['img'])
    
    val_img_names = img_names[:num_val]
    train_img_names = img_names[num_val:]
    
    for name in train_img_names:
        shutil.copy(paths['img'] + name, paths['img_train'] + name)
        try:
            shutil.copy(paths['label'] + name[:len(name)-3] + 'txt', paths['label_train'] + name[:len(name)-3] + 'txt') 
        except FileNotFoundError:
            print('label not found, asuming background image')
        
    for name in val_img_names:
        shutil.copy(paths['img'] + name, paths['img_val'] + name)
        try:
            shutil.copy(paths['label'] + name[:len(name)-3] + 'txt', paths['label_val'] + name[:len(name)-3] + 'txt') 
        except FileNotFoundError:
            print('label not found, asuming background image')

if __name__ == '__main__':
    main()