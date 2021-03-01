### DATA 310 - Antonio Marra Informal Response 2/26 ###

   **Q: Convolve the two 3x3 matrices that were assigned to you with your 9x9 
   matrix and calculate the resulting two matrices**
   
   ![Matrices](/DATA310/matrices.jpg)
   
   **Q: What is the purpose of using a 3x3 filter to convolve across a 2D image matrix?**
   
   Using a 3x3 filter can create a more usable image for processing in ML models and otherwise, as it 
   can retain certain desired features. Convolving across a 2D image matrix can compress a larger image 
   into a smaller variant without altering the fundamental features of the image to a large degree.
   
   **Q: Why would we include more than one filter? How many filters did you assign as 
   part of your architecture when training a model to learn images of numbers from the 
   mnist dataset?** 
   
   Using multiple filters allows the user to highlight distinct features within the photo, for example,
   emphasizing vertical lines over horizontal, or vice versa. In my mnist model I used three separate filters, 
   one for horizontal emphasis, one for vertical, and the final 2x2 filter.
   
   
