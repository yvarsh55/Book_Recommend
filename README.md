# Book Recommendation System 
https://book-recommend.streamlit.app/

## Introduction
The Book Recommendation System aims to provide personalized book recommendations to the user based on their preferences and behaviours. This document outlines the detailed design and implementation of the system’s components.

## System Architecture
The architecture consists of several key modules, including User Profile Management, Data Processing, Collaborative Filtering, Content-Based Filtering, Recommendation Generation, and User Feedback.

![Capture](https://github.com/yvarsh55/Book_Recommend/assets/104003929/8883cf9b-d758-43b2-a338-d63531f8f95e)

## Exploring Architecture
### Data Pre-processing Module:
Data processing includes cleaning, transforming, and organizing raw data collected from users and books. It prepares the data for further analysis.
### Feature Extraction:
Transforming raw data into numerical features that can be processed while preserving the information in the original data set.
### Collaborative Filtering:
This module implements collaborative filtering algorithms for user-based and item-based recommendations. It calculates similarities between users/books and generates candidate recommendations.
### User Input:
This module takes inputs to a machine learning model, we have to create a NumPy array, where the user has to input the values of the required attributes which are used to train the machine learning model.
### Cosine Similarity:
Cosine similarity is a mathematical measure that calculates the cosine of the angle between two non-zero vectors in a multi-dimensional space. It's commonly used to quantify the similarity between two vectors, regardless of their magnitudes. In machine learning, cosine similarity is often employed to measure the similarity or dissimilarity between documents, texts, or other data represented as vectors
### Book Recommendation:
After calling model Books/Output will be recommended, this output will be saved in Database and it will be used to show the same Output if other users provide the same data.

## Web app
we will be using Streamlit to build the web app of the recommendation model. 
