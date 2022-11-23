def main(img_folder):
    import keras
    #from keras.layers import Input, Lambda, Dense, Flatten
    from keras.models import Model

    import tensorflow as tf
    from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
    from tensorflow.keras.preprocessing import image
    import numpy as np
    import matplotlib.pyplot as plt

    import cv2 as cv
    import numpy as np

    loc = "./model_1"
    
    recon = keras.models.load_model(loc)
    recon.summary()

    from keras.preprocessing.image import ImageDataGenerator

    import os
    num_images = len(os.listdir(img_folder+"/" + os.listdir(img_folder)[1]))-1
    #print(num_images)

    datagen = ImageDataGenerator(rescale = 1./255,
                                      shear_range = 0.2,
                                      zoom_range = 0.2)

    data = datagen.flow_from_directory(img_folder,
                                            shuffle = False,
                                            target_size = (30, 30),
                                            batch_size = num_images,
                                            class_mode = 'binary')

    (image_batch, label_batch) = next(iter(data))

    prediction = recon.predict(image_batch)

    num_classes = 3
    identified = list("")

    for i in prediction:
        prob_class = 0
        prob_value = 0
        j = 0
        while(j<num_classes):
            if(i[j]>prob_value):
                prob_class = j
                prob_value = i[j]
            j+=1
        if(prob_class == 0):
            identified.append("bookmark")
        if(prob_class == 1):
            identified.append("calendar")
        if(prob_class == 2):
            identified.append("search")
        identified.append(prob_value)

    n=0
    for i in image_batch:
      print(identified[n])
      print(identified[n+1])
      n+=2
      #plt.imshow(i)
      #plt.show()

    return(identified)
















