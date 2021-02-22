### Response 3 ###

![Original Image](/DATA310/myplotOG.png)

**Pictured above is the first iteration, unedited, of a home built in a modern style.**

![Filter 1](/DATA310/myplot1.png)

**Here is the same picture but with a filter that accentuates the vertical lines on the image.**

![Filter 2](/DATA310/myplot2.png)

**And finally, a filter that accentuates the horizontal lines in the image rather than vertical.**

Essentially, changing the filter on each image establishes different weigths for the filtration of the color values for each pixel. 
Convolution itself is a helpful tool for allowing a computer to identify the correct filters to apply to an image. The "correct"
filter can be chosen and refined through a loss function and optimizer.  

***2x2 Filter***

Using a 2x2 filter on this image works as a compressor for the image itself. This would compress all of the pixel values proportionally 
and create an image that may be slightly less focused than its 3x3 counterpart, but it uses less memory.
