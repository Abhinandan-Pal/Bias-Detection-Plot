# Bias Detection Plot
A plot using matplotlib that helps you detect if the dataset has too many data points in certain criteria.
It takes two fields ( x and y ) of the data as input and two intgers Kx and Ky. Kx represents the number of quantile x-axis is to be broken into and Ky epresents the number of quantile y-axis is to be broken into.
Each number in x and y are replace by a number between(1 ,Kx) and (1,Ky) respectively.A new data set is generated for each combination of these numbers in x and y. And then their number of occurance is calculated.
This dataset is now ploted using a 2-D hist plot. It there are two many data points at any part of the plot it shows that most of our data is way too biased on that side.Thus it is difficult to come over a generalized conclusion based on the data.
 
 
![Example plot](Bias_Detection_Plot_Price_year.png?raw=true "Bias_Detection_Plot_Price_year")

## Taking two fields from the cars dataset : Price and Year of registration as X and Y respectively.
![Dataset image](Images/x_y_intial.png?raw=true "x_y_intial")

## Calculate the quantile range
Here the Kx = 10 , Ky = 10 so the each feild is seperated into 10 groups by calculating the quantile values(0.1,0.2,...1) 

![Quatile_range image](Images/Quatile_range.png?raw=true "Quatile_range")

## Replace the Copy of data by new range number values
The data stored in X and Y are replaced according to the range number they belong based on the quantile values.

![x_y_final](Images/x_y_final.png?raw=true "x_y_final")


## Find occurace of each combination of range number values
The number of times a particular combination of range number values for x and y are found.And stored in a dataset which is then used to plot a 2D hist plot.

![Final_dataset](Images/Final_dataset.png?raw=true "Final_dataset")
