# Fake_news_detection
## Project Overview

#### This project implements a machine learning model to detect fake news. The model is trained on a dataset containing real and fake news articles and can classify a given news article as either real or fake.

## Dataset Description

### True.csv: Contains real news articles with an additional label 1.A

### Fake.csv: Contains fake news articles with an additional label 0.

## Data Preprocessing Steps

### Data Loading:

### Loaded the datasets using pandas.

### Labeling:

### Added a label column: 1 for real news and 0 for fake news.

### Concatenation:

### Merged the datasets into a single DataFrame.

### Feature Selection:

### Dropped irrelevant columns like title, subject, and date.

## Text Preprocessing:

### Applied a preprocess_text function using swifter for faster processing.

### Data Shuffling and Splitting

### Shuffled the data to remove any potential order bias.

### Split into training and testing sets (70% train, 30% test).

## Text Vectorization

### Used TfidfVectorizer from sklearn to convert text into numerical features.

## Model Training

### Logistic Regression: Implemented Logistic Regression for binary classification.

## Model Evaluation

### Evaluated the model's performance using the test set.

### Calculated the accuracy score using LR.score().

### Web Application with Django

### Built a Django web application to provide a user-friendly interface for predictions.

## Features:

### Input Box: Users can enter a news article.

### Check Button: Submits the article for prediction.

### Result Display: Shows if the news is real or fake.

### Graphical Representation: Displays relevant insights through graphs.

### Installation and Setup

# Clone the repository.

### Install dependencies using:

### pip install -r requirements.txt

### Run the Django application:

### python manage.py runserver

### Technologies Used

#### Python

#### Pandas, Numpy

#### Scikit-Learn

#### Swifter

#### Django

#### Future Improvements

#### Implement additional models for comparison.

#### Enhance the UI for better user experience.

#### Extend the analysis to multilingual datasets.

## Conclusion

#### The model successfully distinguishes between real and fake news with high accuracy. The Django-based web application provides an intuitive interface for practical use cases.

