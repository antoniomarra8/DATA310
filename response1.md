# DATA310 - Antonio Marra

 * **Informal Response 1**
  
 **Q: In Laurence Maroney’s video, What is ML, he compares traditional programming with
 machine learning and argues that the main difference between the two is a reorientation
 of the rules, data and answers. According to Maroney, what is the difference between 
 traditional programming and machine learning?**
  
  Maroney argues that traditional programming identifies the rules and data,
    and then answers are produced using these two inputs. Machine Learning
    uses answers and data as its inputs, and infers the rules from these
    pieces.
    
  **Q: With the first basic script that Maroney used to predict a value output from the model 
  he estimated (he initially started with 10 that predicted ~31. Modify the predict function
  to produce the output for the value 7. Do this twice and provide both answers. Are they the 
  same? Are they different? Why is this so?**

   First output: 22.0032871
   
   Second output: 21.997840
   
   An input of 7 yields ~22, depending on the MSE that the optimizer ends
     up with. Answers will vary more due to the machine being trained on 6 
     outputs rather than a larger data pool from which it can refine its guess.
     
    
  **Q: Using the script you produced to predict housing price, take the provided six houses from 
  Mathews, Virginia and train a neural net model that estimates the relationship between them. 
  Based on this model, which of the six homes present a good deal? Which one is the worst deal? 
  Justify your answer.**
  
  **Best Deal -** 160 Holly Point Road had the largest difference between the expected price for a house with 
  three bedrooms and its listed price.
  
   **Worst Deal -** 984 Fitchett's Wharf Road was the most overvalued, with a listed price of   
    Based on the price per square foot, I have chosen these two houses as the 
     best and worst of our group of houses.
     
     
   **UPDATE: Using the modified code, the new house with the worst value is 228 Church St,
   as it is overvalued by almost $100,000 based on our new model.**
