import streamlit as st
import pandas as pd
import re
import joblib
import random

df = pd.read_csv('pages/model/restaurant_recommender/new_df1.csv')
indices = pd.Series(df.index, index=df['name_address'])
cosine_sim = joblib.load('pages/model/restaurant_recommender/cosine_sim.pkl')

def get_recommendations(title, cosine_sim, ind=indices):
    idx = ind[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[0:11]
    prod_indices = [i[0] for i in sim_scores]
    return df.iloc[prod_indices]

list_image = ['pages/model/restaurant_recommender/rest1.jpg', 'pages/model/restaurant_recommender/rest2.jpg',
                'pages/model/restaurant_recommender/rest3.jpg', 'pages/model/restaurant_recommender/rest4.jpg',
                'pages/model/restaurant_recommender/rest5.jpg']
def make_clickable(val):
    return st.markdown(f"[Here]({val})")

def show_image(val):
    return '<a><img src="{}" width=50></img></a>'.format(val)

# test = df['name_address'].sample(1).values[0]
col1, col2 = st.columns(2)
with col1:
    rest_name = st.selectbox("Type Restaurant Name",df['name'].tolist())
with col2:
    rest_loc = st.selectbox("Select Restaurant Location", df[df['name']==rest_name]['address'].tolist())
rest_combine = rest_name + ',' + rest_loc


if st.button('Generate Restaurant Recommendation'):
    new_df = get_recommendations(rest_combine, cosine_sim)
    st.markdown('## Restaurant You Choose')
    col1, col2 = st.columns([1,3])
    with col1:
        st.image(random.choice(list_image))
    with col2:
        st.write(f"Name    : {new_df['name'].values[0]}")
        st.write(f"Address : {new_df['address'].values[0]}")
        st.write(f"Type    : {new_df['rest_type'].values[0]}")
        st.write(f"Cuisines: {new_df['cuisines'].values[0]}")
        st.write(f"Rate    : {new_df['rate'].values[0]} from {new_df['votes'].values[0]} votes")
        st.write(f"Link    : [{new_df['name'].values[0]}]({new_df['url'].values[0]})")
    st.markdown('## Top 5 Recommendations')
    col1, col2 = st.columns([1,3])
    with col1:
        st.image(random.choice(list_image))
    with col2:
        st.write(f"Name    : {new_df['name'].values[1]}")
        st.write(f"Address : {new_df['address'].values[1]}")
        st.write(f"Type    : {new_df['rest_type'].values[1]}")
        st.write(f"Cuisines: {new_df['cuisines'].values[1]}")
        st.write(f"Rate    : {new_df['rate'].values[1]} from {new_df['votes'].values[1]} votes")
        st.write(f"Link    : [{new_df['name'].values[1]}]({new_df['url'].values[1]})")
    st.write('-----')
    col1, col2 = st.columns([1,3])
    with col1:
        st.image(random.choice(list_image))
    with col2:
        st.write(f"Name    : {new_df['name'].values[2]}")
        st.write(f"Address : {new_df['address'].values[2]}")
        st.write(f"Type    : {new_df['rest_type'].values[2]}")
        st.write(f"Cuisines: {new_df['cuisines'].values[2]}")
        st.write(f"Rate    : {new_df['rate'].values[2]} from {new_df['votes'].values[2]} votes")
        st.write(f"Link    : [{new_df['name'].values[2]}]({new_df['url'].values[2]})")
    st.write('-----')
    col1, col2 = st.columns([1,3])
    with col1:
        st.image(random.choice(list_image))
    with col2:
        st.write(f"Name    : {new_df['name'].values[3]}")
        st.write(f"Address : {new_df['address'].values[3]}")
        st.write(f"Type    : {new_df['rest_type'].values[3]}")
        st.write(f"Cuisines: {new_df['cuisines'].values[3]}")
        st.write(f"Rate    : {new_df['rate'].values[3]} from {new_df['votes'].values[3]} votes")
        st.write(f"Link    : [{new_df['name'].values[3]}]({new_df['url'].values[3]})")
    st.write('-----')
    col1, col2 = st.columns([1,3])
    with col1:
        st.image(random.choice(list_image))
    with col2:
        st.write(f"Name    : {new_df['name'].values[4]}")
        st.write(f"Address : {new_df['address'].values[4]}")
        st.write(f"Type    : {new_df['rest_type'].values[4]}")
        st.write(f"Cuisines: {new_df['cuisines'].values[4]}")
        st.write(f"Rate    : {new_df['rate'].values[4]} from {new_df['votes'].values[4]} votes")
        st.write(f"Link    : [{new_df['name'].values[4]}]({new_df['url'].values[4]})")
    st.write('-----')
    col1, col2 = st.columns([1,3])
    with col1:
        st.image(random.choice(list_image))
    with col2:
        st.write(f"Name    : {new_df['name'].values[5]}")
        st.write(f"Address : {new_df['address'].values[5]}")
        st.write(f"Type    : {new_df['rest_type'].values[5]}")
        st.write(f"Cuisines: {new_df['cuisines'].values[5]}")
        st.write(f"Rate    : {new_df['rate'].values[5]} from {new_df['votes'].values[5]} votes")
        st.write(f"Link    : [{new_df['name'].values[5]}]({new_df['url'].values[5]})")
    st.write('-----')
    st.write("restaurant image is only an example")
    # print(new_df['image'].values[0])
    
    
    # print(ahay)
    # print(indices[test])
else:
    print('Error')