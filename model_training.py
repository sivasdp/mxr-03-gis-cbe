import tensorflow
from tensorflow import keras
from keras.preprocessing.image import ImageDataGenerator 

dataset_path='dataset/' #make label to solve this error

train_gen=ImageDataGenerator(rescale=1./255,
                             shear_range=0.2,
                             zoom_range=0.2,
                             horizontal_flip=True)

train_data=train_gen.flow_from_directory(dataset_path,target_size=(224,224),batch_size=32)

if train_data:
    print("Data Created Sucessfully")
else:
    print("Some error occured")