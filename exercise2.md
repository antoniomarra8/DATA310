# DATA 310 - Antonio Marra

  * **Informal Response 2/8** 
   1. Splitting images into training and testing sets allows us to gauge the performance of the 
    neural network to predict images that it has never seen before. Testing the neural network on images
    that it has already been trained with is useless.
   2. .relu function basically removes the negative values from the data to avoid a negative skew. 
   This prevents against the cancellation of positive values in the data from an individual or 
   small group of skewed points. .softmax function attempts to categorize each image into a category
   by finding the most likely candidate, setting this equal to 1, and all else to 0. It uses 10 neurons 
   for the 10 categories of shoe that this particular neuron measures.
   3. After we specify the specific optimizer and loss function in the compile() function, 
   they work together to guess the category of an image based on analysis of every pixel, and
   the loss funtion calculates the validity of this guess. The optimizer then revises this 
   guess accordingly, and the cycle repeats with this informed guess.
