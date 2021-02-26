# DATA 310 - Antonio Marra

  * **Informal Response 2/8**  


  * **Q: In the video, First steps in computer vision, Laurence Maroney introduces us to the Fashion 
   MNIST data set and using it to train a neural network in order to teach a computer “how to see.” 
   One of the first steps towards this goal is splitting the data into two groups, a set of training 
   images and training labels and then also a set of test images and test labels. Why is this done? 
   What is the purpose of splitting the data into a training set and a test set?**
   
   Splitting images into training and testing sets allows us to gauge the performance of the 
   neural network to predict images that it has never seen before. Testing the neural network on images
   that it has already been trained with is useless.
    
  * **Q: The fashion MNIST example has increased the number of layers in our neural network from 1 in the 
   past example, now to 3. The last two are .Dense layers that have activation arguments using the relu 
   and softmax functions. What is the purpose of each of these functions. Also, why are there 10 neurons 
   in the third and last layer in the neural network. .relu function basically removes the negative values 
   from the data to avoid a negative skew.**
   
   This prevents against the cancellation of positive values in the data from an individual or 
   small group of skewed points. .softmax function attempts to categorize each image into a category
   by finding the most likely candidate, setting this equal to 1, and all else to 0. It uses 10 neurons 
   for the 10 categories of shoe that this particular neuron measures.
   
  * **Q: In the past example we used the optimizer and loss function, while in this one we are using the 
   function adam in the optimizer argument and sparse_categorical- crossentropy for the loss argument. How 
   do the optimizer and loss functions operate to produce model parameters (estimates) within the model.compile()
   function?**
   
   After we specify the specific optimizer and loss function in the compile() function, 
   they work together to guess the category of an image based on analysis of every pixel, and
   the loss funtion calculates the validity of this guess. The optimizer then revises this 
   guess accordingly, and the cycle repeats with this informed guess.
   
  * **Q: What is the shape of the images training set (how many and the dimension of each)?**
   
   There are 60,000 images and the size for each is 28 by 28 pixels.
   
  * **Q: What is the length of the labels training set?**
   
   60,000 images
   
  * **Q: What is the shape of the images test set?**
   
   10,000 images, each 28 by 28 pixels.
   
   
   
