# Regression on Buldozers 

Welcome to the first weekly challenge, a summary mini-projects that comes to cement the info you drank from this weeks information fire hose.  
You are in a group of 3 and your challenge is to predict the sale price of a particular piece of heavy equiment at auction, based on it's usage, equipment type, and configuaration.  The data is sourced from auction result postings and includes information on usage and equipment configurations. 

### The key fields are in train.csv are:

* SalesID: the uniue identifier of the sale
* MachineID: the unique identifier of a machine.  A machine can be sold multiple times
* saleprice: what the machine sold for at auction (only provided in train.csv)
* saledate: the date of the sale

There are several fields towards the end of the file on the different options a machine can have.  The descriptions all start with "machine configuration" in the data dictionary.  Some product types do not have a particular option, so all the records for that option variable will be null for that product type.  Also, some sources do not provide good option and/or hours data.

<u> Bonus points: </u>
The machine_appendix.csv file contains the correct year manufactured for a given machine along with the make, model, and product class details. There is one machine id for every machine in all the competition datasets (training, evaluation, etc.).

### Evaluation

We are holding 10% of the data. The winning team be able to predict the lowest difference between at least 50% of the test data. The evaluation metric for this challenge is the RMSLE (root mean squared log error) between the actual and predicted auction prices. You will present your approach and results today at 6pm as a 5 min talk. Prepare slides.

## Tools: 

Before you dive into regression, algorithms and testing talk to your team mates and devise a strategy for analysing the data. Work effectively so that you can communicate your findings in a presentation. Use any of the tools we learnt this week (here are some suggestions...):

<u> Use EDA techniques: </u>

* Visualize the data set and understand your variables. 
* Look for the categorical and continuous regressors. 
* Use faceting or stratification to identify colinearity.

<u> Use the big guns:</u> 

* Linear regression
* Ridge regression
* Lasso regression 
* Gradient descent
* Logistic and Logit regression 

<u>Remove biases in data using:</u>

* Detecting and reducing Multicolinearity 
* Heteroscedasticity
* Influence and leverage points, and outliers.

<u> Test your predictions: </u>

* Use cross validation and k-fold means to test for overfitting


Good Luck!
 
