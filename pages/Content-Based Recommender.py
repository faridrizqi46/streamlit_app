import streamlit as st
import pandas as pd
import re
import joblib
import random

tab1, tab2, tab3 = st.tabs(["Restaurant", "Anime", "K-Drama"])

with tab1:
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

with tab2:
    df2 = pd.read_csv('pages/model/anime_recommender/anime_df.csv')
    indices2 = pd.Series(df2.index, index=df2['title'])
    model_anime = joblib.load('pages/model/anime_recommender/model7.pkl')
    
    def get_recommendations(title, ind=indices2 ,cosine_sim=model_anime):
        idx = ind[title]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:11]
        anime_indices = [i[0] for i in sim_scores]
        return df2.iloc[anime_indices]
    
    anime_title = st.selectbox("Type Anime Title",df2['title'].tolist())
    
    if st.button('Generate Anime Recommendation'):
        anime_recommend = get_recommendations(anime_title)
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.text(anime_recommend['title'].values[0])
            st.image(anime_recommend['main_picture'].values[0], width=140)
        with col2:
            st.text(anime_recommend['title'].values[1])
            st.image(anime_recommend['main_picture'].values[1], width=140)

        with col3:
            st.text(anime_recommend['title'].values[2])
            st.image(anime_recommend['main_picture'].values[2], width=140)
        with col4:
            st.text(anime_recommend['title'].values[3])
            st.image(anime_recommend['main_picture'].values[3], width=140)
        with col5:
            st.text(anime_recommend['title'].values[4])
            st.image(anime_recommend['main_picture'].values[4], width=140)
            
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.text(anime_recommend['title'].values[5])
            st.image(anime_recommend['main_picture'].values[5], width=140)
        with col2:
            st.text(anime_recommend['title'].values[6])
            st.image(anime_recommend['main_picture'].values[6], width=140)

        with col3:
            st.text(anime_recommend['title'].values[7])
            st.image(anime_recommend['main_picture'].values[7], width=140)
        with col4:
            st.text(anime_recommend['title'].values[8])
            st.image(anime_recommend['main_picture'].values[8], width=140)
        with col5:
            st.text(anime_recommend['title'].values[9])
            st.image(anime_recommend['main_picture'].values[9], width=140)
    else:
        print('Error')
with tab3:
    df3 = pd.read_csv('pages/model/kdrama_recommender/df_drama2.csv')
    indices3 = pd.Series(df3.index, index=df3['name'])
    model_att = joblib.load('pages/model/kdrama_recommender/model_atributes.pkl')
    model_syn = joblib.load('pages/model/kdrama_recommender/model_synopsis.pkl')
    
    def get_recommendations(title, ind=indices3 ,cosine_sim=model_att):
        idx = ind[title]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:11]
        kdrama_indices = [i[0] for i in sim_scores]
        return df3.iloc[kdrama_indices]
    
    kdrama_title = st.selectbox("Type K-Drama Title",df3['name'].tolist())
    
    if st.button('Generate K-Drama Recommendation'):
        drama_recommendation = get_recommendations(kdrama_title, cosine_sim=model_syn)
        st.markdown('## Recommendation From Synopsis')
        col1, col2, col3 = st.columns([2,3,1])
        with col1:
            st.text("Drama Title")
        with col2:
            st.text("Where You Can Watch The Drama")
        with col3:
            st.markdown("URL")
        col1, col2, col3 = st.columns([2,3,1])
        with col1:
            st.text(drama_recommendation['name'].values[0])
            st.text(drama_recommendation['name'].values[1])
            st.text(drama_recommendation['name'].values[2])
            st.text(drama_recommendation['name'].values[3])
            st.text(drama_recommendation['name'].values[4])
        with col2:
            st.text(drama_recommendation['where_to_watch'].values[0])
            st.text(drama_recommendation['where_to_watch'].values[1])
            st.text(drama_recommendation['where_to_watch'].values[2])
            st.text(drama_recommendation['where_to_watch'].values[3])
            st.text(drama_recommendation['where_to_watch'].values[4])
        with col3:
            st.markdown(f"[Link]({drama_recommendation['url'].values[0]})")
            st.markdown(f"[Link]({drama_recommendation['url'].values[1]})")
            st.markdown(f"[Link]({drama_recommendation['url'].values[2]})")
            st.markdown(f"[Link]({drama_recommendation['url'].values[3]})")
            st.markdown(f"[Link]({drama_recommendation['url'].values[4]})")
        drama_recommendation2 = get_recommendations(kdrama_title, cosine_sim=model_att)
        st.write('-----')
        st.markdown('## Recommendation From Drama Attributes')
        col1, col2, col3 = st.columns([2,3,1])
        with col1:
            st.text("Drama Title")
        with col2:
            st.text("Where You Can Watch The Drama")
        with col3:
            st.markdown("URL")
        col1, col2, col3 = st.columns([2,3,1])
        with col1:
            st.text(drama_recommendation2['name'].values[0])
            st.text(drama_recommendation2['name'].values[1])
            st.text(drama_recommendation2['name'].values[2])
            st.text(drama_recommendation2['name'].values[3])
            st.text(drama_recommendation2['name'].values[4])
        with col2:
            st.text(drama_recommendation2['where_to_watch'].values[0])
            st.text(drama_recommendation2['where_to_watch'].values[1])
            st.text(drama_recommendation2['where_to_watch'].values[2])
            st.text(drama_recommendation2['where_to_watch'].values[3])
            st.text(drama_recommendation2['where_to_watch'].values[4])
        with col3:
            st.markdown(f"[Link]({drama_recommendation2['url'].values[0]})")
            st.markdown(f"[Link]({drama_recommendation2['url'].values[1]})")
            st.markdown(f"[Link]({drama_recommendation2['url'].values[2]})")
            st.markdown(f"[Link]({drama_recommendation2['url'].values[3]})")
            st.markdown(f"[Link]({drama_recommendation2['url'].values[4]})")
    else:
        print('error')