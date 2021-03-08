## Project 1

### **Housing Data Scraped from Zillow**


The first step I took for this exercise is to initially create 
a database by running code to scrape n=400 houses directly from Zillow's website. I initially
completed this step in class using the first iteration of the zillow_scrape.py code, and this is the 
database which I used in this project. After successfully scraping the data following our instruction
in class, I attempted to create another database from housing data in Miami, FL. However, by this time
the ingenious data scientists at Zillow had made an alteration to their website code that rendered 
my zillow_scrape.py functionally useless.  

Given this alteration, I reverted back to my original dataset of Austin, TX. [insert dataset link]
A quick check of the data showed that there were about eight seemingly random errors in transcribing house prices 
from Zillow. I manually searched for these houses and found the Zestimate for each. After trying to run the code 
in Pycharm, I repeatedly received an error on the initial scaling of the data:

```
homes[['prices_scale']] = homes[['prices']]/100000 
homes[['sqft_scale']] = homes[['sqft']]/1000 
```

I concluded that the error was due to missing values in the square foot column for houses that did not report 
square footage anywhere on zillow. This caused these values to spit back more html code. In order to avoid skewing the
data, I replaced these 10 homes with other randomly chosen houses in Austin that had values for each metric we are measuring. 

Ultimately, I continued with 400 data points in my homes csv. 



### **Model Architecture**

The model architecture itself consists of a neural network with one dense layer 

```
model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')
history = model.fit(x_1, y, epochs=500)
```

### **Project File**

<a id="raw-url" href="https://raw.githubusercontent.com/antoniomarra8/DATA310/main/project1.py">project1.py</a>

