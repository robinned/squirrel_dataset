import os

image_dir = 'C:/Users/highf/Documents/GitHub/squirrel_dataset/dataset_one/Images'
label_dir = 'C:/Users/highf/Documents/GitHub/squirrel_dataset/dataset_one/Labels'

image_names = os.listdir(image_dir)
label_names = os.listdir(label_dir)

for i in range(len(image_names)):
    name = image_names[i]
    image_names[i] = name[:len(name)-3]

for i in range(len(label_names)):
    name = label_names[i]
    label_names[i] = name[:len(name)-3]
    
image_names.sort()
label_names.sort()

images_without_labels = []
for name in image_names:
    count = 0
    for label in label_names:
        if(name == label):
            count = count + 1
    if count == 0:
        images_without_labels.append(name)
        #print('image', name, "has no label")
       
labels_without_images = []       
for label in label_names:
    count = 0
    for image in image_names:
        if(label == image):
            count = count + 1
    if count == 0:
        labels_without_images.append(label)
        #print('label', label, "has no image")

print('percentage of background images:', (len(images_without_labels)/len(image_names)) * 100, '%')