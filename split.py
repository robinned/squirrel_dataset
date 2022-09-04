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