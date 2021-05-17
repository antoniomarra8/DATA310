## Project 4

### **ASL Image Segmentation for Use in Education**   

**Q: Problem Statement that introduces your selected topic, identifies significant goals 
associated with the implementation of your applied machine learning method, demonstrates
why your problem is important, and describes and analyzes the complex nature of your 
problem including any process oriented causes and effects. Conclude your problem statement 
with a stated central research question. You are welcome to articulate a central research 
question in broad and general terms, given the abbreviated time frame for this investigation.**

A: Literature in and around the education discipline in recent years has identified tangible discrepancies
in the availability of teachers qualified to educate deaf and disabled students. According to a 
2019 letter by the Council on Education of the Deaf (CED), there is a crisis in deaf education; a steady decline
in deaf education teacher training programs has left the population of teachers in dire straits. Graduates in
2020 numbered just 11% of the 1982 graduating class, and combined with a high retirement rate, there is
a serious need for educational assistance to avoid burnout and overworking of the existing population
of certified deaf teachers. As language is imperative for the healthy growth of any child, deaf or otherwise, 
lower quality education due to the overworking of teachers is unacceptable. 
Incorporating a machine learning model to conduct examinations and other assignments
can provide breathing room for teachers to better focus their energy on students who may require more assistance,
and simultaneously avoid burnout or early retirement as a result of chronic work-related stress.
Thus, my research question is this: can a ML model use image classification to adequately perform testing 
for elementary and middle school deaf students?

**Q: A description of the data that you are using as input for your applied machine learning methodology, 
including the source of the data, the different features (variables) and well as their data class (i.e. 
continuous or discrete). Be sure to include a description of your dataset size (number of rows / observations 
as well as number of columns / variables / features) and provide context on how the data was collected as well
as the source organization, as it is relevant to your investigation.**

A: I acquired a dataset from Kaggle that includes 1500 images of 37 unique alphabet characters, numeric characters, and 
one character that is used to delineate space between words or concepts. The data is split into two folders for two
different purposes. The first contains color images of hands forming each character, or the 'raw data' for the ML model. 
The second folder includes the same pictures, but after pre-processing, where each image is threshold binary converted images 
for easier implementation in a model. Particularly, this will be useful for a CNN. 

**Q: Provide the specification for your applied machine learning method that presented the most promise in 
providing a solution to your problem. Include the section from your python or R script that specifies your
model architecture, layers, functional arguments and specifications for compiling and fitting. Provide a brief 
description of how you implemented your code in practice.**

A: The specification that I believe to be the most applicable for this problem is using an image segmentation
model to identify the hand various hand signs within a given image. If applied to a zoom environment, it is very
unlikely that every camera will be oriented in the same way, so an agile image processing approach is needed. Getting
a more basic understanding of the image at the pixel level can allow for more accurate processing of varying types of images. 

First, I normalize the dataset and create a segmentation mask for the images. I will be using a pretrained weight named MobileNetV2 .
The model and layers are as follows:

```
base_model = tf.keras.applications.MobileNetV2(input_shape=[128, 128, 3], include_top=False)

layer_names = [
    'block_1_expand_relu',   # 64x64
    'block_3_expand_relu',   # 32x32
    'block_6_expand_relu',   # 16x16
    'block_13_expand_relu',  # 8x8
    'block_16_project',      # 4x4
]
base_model_outputs = [base_model.get_layer(name).output for name in layer_names]

down_stack = tf.keras.Model(inputs=base_model.input, outputs=base_model_outputs)

down_stack.trainable = False
```

```
def unet_model(output_channels):
  inputs = tf.keras.layers.Input(shape=[128, 128, 3])

  # Downsampling through the model
  skips = down_stack(inputs)
  x = skips[-1]
  skips = reversed(skips[:-1])

  # Upsampling and establishing the skip connections
  for up, skip in zip(up_stack, skips):
    x = up(x)
    concat = tf.keras.layers.Concatenate()
    x = concat([x, skip])

  # This is the last layer of the model
  last = tf.keras.layers.Conv2DTranspose(
      output_channels, 3, strides=2,
      padding='same')  #64x64 -> 128x128

  x = last(x)

  return tf.keras.Model(inputs=inputs, outputs=x)
```




**Q: Conclude with a section that preliminarily assesses model performance. If you have results from your implementation,
you are welcome to add those in this section. Compare your preliminary results with those from the literature on your 
topic for a comparative assessment. If you are not able to produce preliminary results, provide a cursory literature review
that includes 2 sources that present and describes their validation. With more time and project support, estimate what an 
ideal outcome looks like in terms of model validation.**

A: I believe that the model performance will turn out with a solid accuracy prediction between the hand signals in the 
dataset. The entire dataset is over 100,000 images, so the quantity of material for a well-trained model is, in my 
estimation, within reach.
