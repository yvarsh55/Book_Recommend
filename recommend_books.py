
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pickle

def recommend_books(book_title, model, books_df):
    idx = books_df[books_df['Title'] == book_title].index[0]
    sim_scores = list(enumerate(model[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]  # Top 5 similar books
    book_indices = [i[0] for i in sim_scores]
    return books_df['Title'].iloc[book_indices]

def main():
    st.title("Book Recommender")

    st.text('Welcome to the site, Hope you find what you are looking for')

    st.sidebar.title('INFO')
    st.sidebar.text('This project is done by \nYashu Varshney and Manik Gupta \nas part of virtual internship \nprogram offered by iNeuron.ai') 
    

    # Load the cosine similarity model
    model = pickle.load(open("cosine_similarity_model.pkl", "rb"))

    # Load the books dataset
    books_df = pd.read_csv("books.csv")

    # Create book selection dropdown
    book_title = st.selectbox("Select a book you like:", books_df['Title'].values)

    if st.button("Recommend Books"):
        recommended_books = recommend_books(book_title, model, books_df)
        st.markdown("## Recommended Books")
        for book in recommended_books:
            st.write(book)

if __name__ == '__main__':
    main()
