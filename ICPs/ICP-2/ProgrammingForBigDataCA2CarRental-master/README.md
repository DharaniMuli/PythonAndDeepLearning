# Team members
* Dharani, Muli: CLASS ID: 21
* Teja, Devarapalli: CLASS ID: 12
* Ugandhar Reddy, Singani: CLASS ID:31


# Introduction
This report is about python and machine learning basic concepts

# Objective
The main objective of this lab assignment is to get experienced with some of the concepts in python like lists, tuples, sets, dictionaries, performing various string operations and OOPS concepts. This lab work also contains the application of some of the machine learning algorithms like Navie Bayes, SVM, KNN, Multiple regression and K-Means clustering.


## Problem-1: 
Finding longest substring without repeating characters
### Approach
* Given an input string
* Initially I find the length of the given string which helps me to traverse through the string till its length reaches.
* I created a dictionary and by iterating, I am checking whether a particular character is in my dic or not. If not I am pushing it to the dictionary and assigned with value 1 and storing length temporarily. 
* If I find the character in my dic, then flushing out my dic and checking my temporary length is greater than max length. If temlenght>maxlength then I am replacing max length with temp length or else no change in the max length
* In this way I can find the longest substring without repeating characters
### Workflow
![](https://raw.githubusercontent.com/DharaniMuli/PythonAndDeepLearning/master/LabAssignments/Lab-1/PythonLab-1/Screenshots/Task_1/Code.PNG)
### Output

![](https://raw.githubusercontent.com/DharaniMuli/PythonAndDeepLearning/master/LabAssignments/Lab-1/PythonLab-1/Screenshots/Task_1/Output.PNG)

## Problem-2: 
Creating a dictionary with key as names and values as a list of (subjects, marks) in sorted order
### Approach
* The input is given in the program itself ( input --> list of tuples )
* Initializing a dictionary with list elements as values.
* Storing the values of the list into a dictionary with key as name and (subject, marks) tuple as the value in the list.
* Each value in dict_values is a list of tuples. Sorting the list based on the name field in the tuple and storing them in another dict (sorted_dict)
* Displaying the dictionary after sorting based on name and dumping the value in the JSON format with 4 as indentation.
### Workflow
![](https://raw.githubusercontent.com/DharaniMuli/PythonAndDeepLearning/master/LabAssignments/Lab-1/PythonLab-1/Screenshots/Task_2/Code.PNG)

### Output
![](https://raw.githubusercontent.com/DharaniMuli/PythonAndDeepLearning/master/LabAssignments/Lab-1/PythonLab-1/Screenshots/Task_2/output.PNG)

## Problem - 3: 
Library Management System using Python programming
### Approach
My Library system contains 3 below components:
1. List all the available books
2. Request for Book
3. Return Book

Basically I divided my system into 4 classed ManagerLibrary, Members, Student and Faculty.
* availableBooks method will check all the available books from my dic and prints
* checkOutBook method is for checking out books which the user requested. But I am doing user validation if user exists or not before issuing book. 
* If the book which user requested is not available then I am showing the message to the user that "Sorry we don't have the book you requested"
* returnBook method will help us to back store the book which the user gives and update the dictionary accordingly after user validation check.
* When the user is returning the wrong book then they receive the message "Sorry we haven't issued any book with this name".
* Student class and Faculty class which is inheriting properties from Members are validating the user.
* I have used cprint package in the python to print the messages with their appropriate colors like if is sucess message with green in color.
from termcolor import colored, cprint


### Workflow
![](https://raw.githubusercontent.com/DharaniMuli/PythonAndDeepLearning/master/LabAssignments/Lab-1/PythonLab-1/Screenshots/Task_3/Code1.PNG)

![](https://raw.githubusercontent.com/DharaniMuli/PythonAndDeepLearning/master/LabAssignments/Lab-1/PythonLab-1/Screenshots/Task_3/Code2.PNG)

![](https://raw.githubusercontent.com/DharaniMuli/PythonAndDeepLearning/master/LabAssignments/Lab-1/PythonLab-1/Screenshots/Task_3/Code3.PNG)


![](https://raw.githubusercontent.com/DharaniMuli/PythonAndDeepLearning/master/LabAssignments/Lab-1/PythonLab-1/Screenshots/Task_3/Code4.PNG)


![](https://raw.githubusercontent.com/DharaniMuli/PythonAndDeepLearning/master/LabAssignments/Lab-1/PythonLab-1/Screenshots/Task_3/Code5.PNG)


![](https://raw.githubusercontent.com/DharaniMuli/PythonAndDeepLearning/master/LabAssignments/Lab-1/PythonLab-1/Screenshots/Task_3/Code6.PNG)


![](https://raw.githubusercontent.com/DharaniMuli/PythonAndDeepLearning/master/LabAssignments/Lab-1/PythonLab-1/Screenshots/Task_3/Code7.PNG)

### Output
![](https://raw.githubusercontent.com/DharaniMuli/PythonAndDeepLearning/master/LabAssignments/Lab-1/PythonLab-1/Screenshots/Task_3/Output1.PNG)


![](https://raw.githubusercontent.com/DharaniMuli/PythonAndDeepLearning/master/LabAssignments/Lab-1/PythonLab-1/Screenshots/Task_3/Output2.PNG)


![](https://raw.githubusercontent.com/DharaniMuli/PythonAndDeepLearning/master/LabAssignments/Lab-1/PythonLab-1/Screenshots/Task_3/Output3.PNG)


![](https://raw.githubusercontent.com/DharaniMuli/PythonAndDeepLearning/master/LabAssignments/Lab-1/PythonLab-1/Screenshots/Task_3/Output4.PNG)


![](https://raw.githubusercontent.com/DharaniMuli/PythonAndDeepLearning/master/LabAssignments/Lab-1/PythonLab-1/Screenshots/Task_3/Output5.PNG)



![](https://raw.githubusercontent.com/DharaniMuli/PythonAndDeepLearning/master/LabAssignments/Lab-1/PythonLab-1/Screenshots/Task_3/Output6.PNG)



![](https://raw.githubusercontent.com/DharaniMuli/PythonAndDeepLearning/master/LabAssignments/Lab-1/PythonLab-1/Screenshots/Task_3/Output7.PNG)

## Problem - 4: 
Fetch comparison of the clustering algorithms in scikit-learn using beautiful soup
### Approach
1. Fetched all the data from the url using requests method.
1. Parsed into html format using beautiful soup
1. Retrieved table of a particular class name
1. Iterated through all the td elements and fetched all the text and stripped it using strip() method.
### Workflow

![](https://raw.githubusercontent.com/DharaniMuli/PythonAndDeepLearning/master/LabAssignments/Lab-1/PythonLab-1/Screenshots/Task_4/Code.PNG)

### Output
![](https://raw.githubusercontent.com/DharaniMuli/PythonAndDeepLearning/master/LabAssignments/Lab-1/PythonLab-1/Screenshots/Task_4/Output.PNG)


## Problem - 5: 
Comparing Different Classifications algorithms accuracy
### Approach
1. Importing all required libraries
1. Loading telecom customer details dataset using the pandas library
1. Replacing empty values in the Total Charges column with the NaN value and then dropping the fields with NaN value.
1. dropping the Customer ID column which is not necessary for classification as it a random number.
1. Finding the correlation of each feature with other all features and plotting the heat map graph which shows the correlation with different shades of colors
1. dropping all the columns which are having very less correlation
1. converting all object datatypes ( categorical) to the numerical data type.
1. Based on RFE feature selection ranking splitting the dataset into train and test dataset.
1. Applying 3 different models and training the models with X_train and Y-train datasets.
1. predicting the output y_predict for all 3 models.
1. Using the y_predict and y_test data -> calculating the accuracy score provided by the metric sklearn library.
1. After evaluating the scores -> kNN has 0.7 accuracy
1. SVM linear has 1 accuracy score.
1. where as naive bayes classification has 0.5 accuracy score.
### Workflow
![](https://raw.githubusercontent.com/DharaniMuli/PythonAndDeepLearning/master/LabAssignments/Lab-1/PythonLab-1/Screenshots/Task_5/Code1.PNG)

![](https://raw.githubusercontent.com/DharaniMuli/PythonAndDeepLearning/master/LabAssignments/Lab-1/PythonLab-1/Screenshots/Task_5/Code2.PNG)


![](https://raw.githubusercontent.com/DharaniMuli/PythonAndDeepLearning/master/LabAssignments/Lab-1/PythonLab-1/Screenshots/Task_5/code3.PNG)
### Output

### Data
![](https://raw.githubusercontent.com/DharaniMuli/PythonAndDeepLearning/master/LabAssignments/Lab-1/PythonLab-1/Screenshots/Task_5/Data.PNG)

### Before Replacing of String Values

![](https://raw.githubusercontent.com/DharaniMuli/PythonAndDeepLearning/master/LabAssignments/Lab-1/PythonLab-1/Screenshots/Task_5/Before_replaceOfStringValues.PNG)

### After Replacing of String Values

![](https://raw.githubusercontent.com/DharaniMuli/PythonAndDeepLearning/master/LabAssignments/Lab-1/PythonLab-1/Screenshots/Task_5/After_replaceOfStringValues.PNG)

### Correlation

![](https://raw.githubusercontent.com/DharaniMuli/PythonAndDeepLearning/master/LabAssignments/Lab-1/PythonLab-1/Screenshots/Task_5/CorrData.PNG)

![](https://raw.githubusercontent.com/DharaniMuli/PythonAndDeepLearning/master/LabAssignments/Lab-1/PythonLab-1/Screenshots/Task_5/CorrData1.PNG)

### Exploratory Data Analysis

![](https://raw.githubusercontent.com/DharaniMuli/PythonAndDeepLearning/master/LabAssignments/Lab-1/PythonLab-1/Screenshots/Task_5/exploratory_data_analysis.PNG)

### Null Check

![](https://raw.githubusercontent.com/DharaniMuli/PythonAndDeepLearning/master/LabAssignments/Lab-1/PythonLab-1/Screenshots/Task_5/NullCheck.PNG)

### Preprocessing

![](https://raw.githubusercontent.com/DharaniMuli/PythonAndDeepLearning/master/LabAssignments/Lab-1/PythonLab-1/Screenshots/Task_5/PreProcessing.PNG)

### Accuracy 

![](https://raw.githubusercontent.com/DharaniMuli/PythonAndDeepLearning/master/LabAssignments/Lab-1/PythonLab-1/Screenshots/Task_5/AccuracyReport.PNG)

## Problem - 6 : 
Comparing Different clustering alogirithms accuracy
### Approach
1. Importing all required libraries
1. Loading College details dataset using pandas library
1. Splitting the features/columns based on indexes
1. printing the null values in the dataset for any column
1. replacing the null values with the mean value
1. Splitting the dataset and Applying the K means clustering on the dataset.
1. predicting the test data using the build/trained model.
1. Using the predicted score finding the Silhoutte score where it was 0.38 score.
1. elbow method shows that k=4 value is the number of cluster from the elbow graph.

### Workflow

![](https://raw.githubusercontent.com/DharaniMuli/PythonAndDeepLearning/master/LabAssignments/Lab-1/PythonLab-1/Screenshots/Task_6/Code1.PNG)

![](https://raw.githubusercontent.com/DharaniMuli/PythonAndDeepLearning/master/LabAssignments/Lab-1/PythonLab-1/Screenshots/Task_6/Code2.PNG)

### Output

### Dataset

![](https://raw.githubusercontent.com/DharaniMuli/PythonAndDeepLearning/master/LabAssignments/Lab-1/PythonLab-1/Screenshots/Task_6/DataSet.PNG)

### Null Values

![](https://raw.githubusercontent.com/DharaniMuli/PythonAndDeepLearning/master/LabAssignments/Lab-1/PythonLab-1/Screenshots/Task_6/NullValues.PNG)

### Elbow

![](https://raw.githubusercontent.com/DharaniMuli/PythonAndDeepLearning/master/LabAssignments/Lab-1/PythonLab-1/Screenshots/Task_6/elbow.PNG)

### Clustering

![](https://raw.githubusercontent.com/DharaniMuli/PythonAndDeepLearning/master/LabAssignments/Lab-1/PythonLab-1/Screenshots/Task_6/Output1.PNG)

![](https://raw.githubusercontent.com/DharaniMuli/PythonAndDeepLearning/master/LabAssignments/Lab-1/PythonLab-1/Screenshots/Task_6/Output2.PNG)

### Score

![](https://raw.githubusercontent.com/DharaniMuli/PythonAndDeepLearning/master/LabAssignments/Lab-1/PythonLab-1/Screenshots/Task_6/Score.PNG)

## Problem-7:
Write a program in which take an Input file, use the simple approach below to summarize a text file:

Link to input file: https://umkc.box.com/s/7by0f4540cdbdp3pm60h5fxxffefsvrw
1. Read the data from a file
1. Tokenize the text into words and apply lemmatization technique on each word.
1. Find all the trigrams for the words.
1. Extract the top 10 of the most repeated trigrams based on their count.
1. Go through the text in the file. 
1. Find all the sentences with the most repeated tri-grams
1. Extract those sentences and concatenate. 
1. Print the concatenated result

### Approach

1.I initially tokenize the text into words and apply the lemmatization technique on each word using word_tokenize method under nltk package in python
2. And then performed trigram and extracted top 10 trigrams
3. Then tokenized into input data into the sentence using "sent_tokenize" method and found all the sentences with the most repeated tri-grams. For finding top 10 valued I used a python in build method called "nlargest".
4. After getting the required sentences I concatenated and printed.

### Workflow

![](https://raw.githubusercontent.com/DharaniMuli/PythonAndDeepLearning/master/LabAssignments/Lab-1/PythonLab-1/Screenshots/Task_7/Code1.PNG)

![](https://raw.githubusercontent.com/DharaniMuli/PythonAndDeepLearning/master/LabAssignments/Lab-1/PythonLab-1/Screenshots/Task_7/Code2.PNG)

![](https://raw.githubusercontent.com/DharaniMuli/PythonAndDeepLearning/master/LabAssignments/Lab-1/PythonLab-1/Screenshots/Task_7/Code3.PNG)

### Output

![](https://raw.githubusercontent.com/DharaniMuli/PythonAndDeepLearning/master/LabAssignments/Lab-1/PythonLab-1/Screenshots/Task_7/Task_b_Output.PNG)

![](https://raw.githubusercontent.com/DharaniMuli/PythonAndDeepLearning/master/LabAssignments/Lab-1/PythonLab-1/Screenshots/Task_7/Task_c_d_Output.PNG)

![](https://raw.githubusercontent.com/DharaniMuli/PythonAndDeepLearning/master/LabAssignments/Lab-1/PythonLab-1/Screenshots/Task_7/Task_e_f_g_h_Output.PNG)


## Problem - 8 : 
Create Multiple Regression and evaluate the model  using  RMSE  and  R2  and  observations  improvement before and after the EDA
### Approach
1. Boston dataset is chosen from pandas
1. Data is checked for the null values. If there are any null values then they will be replaced by mean. In this data set there are no null values.
1. Finding the correlation between the target class MEDV and features. Most correlated features are used and remaining all features are dropped.
1. Splitting the data into training and test data using train_test_split
1. Creating the regression model and training it by providing the train data
1. Predicting the target class. In multiple regression, model evaluation is performed by using Mean square error and r2_score
1. Calculating the Mean Square Error and R2 score
1. A multiple regression model is evaluated as good if its Mean Square Error is low and R2_score is high. What we observed from this program is before performing EDA Mean Square Error is high and R2 score is low. After performing EDA, Mean Square Error is low and R2_score is high.
### Workflow

![](https://raw.githubusercontent.com/DharaniMuli/PythonAndDeepLearning/master/LabAssignments/Lab-1/PythonLab-1/Screenshots/Task_8/Code1.PNG)

![](https://raw.githubusercontent.com/DharaniMuli/PythonAndDeepLearning/master/LabAssignments/Lab-1/PythonLab-1/Screenshots/Task_8/Code2.PNG)

![](https://raw.githubusercontent.com/DharaniMuli/PythonAndDeepLearning/master/LabAssignments/Lab-1/PythonLab-1/Screenshots/Task_8/Code3.PNG)
### Output
![](https://raw.githubusercontent.com/DharaniMuli/PythonAndDeepLearning/master/LabAssignments/Lab-1/PythonLab-1/Screenshots/Task_8/Score.PNG)


Conclusion:

This Lab exercise is really very exciting and interesting which gave us the opportunity to cover various topics like python dictionaries(default dictionary), Object-Oriented concepts, beautiful soup, machine learning algorithms such as classification, clustering, and regression. Moreover, it helps us to practice through all the topic in one shot
