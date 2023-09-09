
import streamlit as st
import pandas as pd
import numpy as np
import pickle

def recommend_books(book_title, model, books_df):
    idx = books_df[books_df['Title'] == book_title].index[0]
    sim_scores = list(enumerate(model[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]  # Top 5 similar books
    book_indices = [i[0] for i in sim_scores]
    return books_df['Title'].iloc[book_indices]

def main():
    st.title("Book Recommendation System")
    #pic='pic2.jpg'
    #st.image(pic)

    st.info('Welcome to the site, Hope you find what you are looking for')
    st.markdown('#') #to create empty space

    st.sidebar.title('INFO')
    #pic2='capture.jpg'
    #st.sidebar.image(pic2)
    st.sidebar.text_area('This project is done by \nManik gupta and Yashu Varshney \nas part of virtual internship \nprogram offered by iNeuron.ai') 
    st.sidebar.button('Submit')

    # Load the cosine similarity model
    model = pickle.load(open("cosine_similarity_model.pkl", "rb"))

    # Load the books dataset
    books_df = pd.read_csv("books.csv")

    # Create book selection dropdown
    #book_title=st.text_input('Enter Name of Book')
    book_title = st.selectbox("Select a book you like:",books_df['Title'].values)

    if st.button("Recommend Books"):
        recommended_books = recommend_books(book_title, model, books_df)
        st.markdown("## Recommended Books")
        for book in recommended_books:
            st.write(book)
    st.markdown('##')
    st.select_slider("Rate",['Bad','Average','Good'])

if __name__ == '__main__':
    main()
