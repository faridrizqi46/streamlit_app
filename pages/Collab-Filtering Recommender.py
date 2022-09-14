import streamlit as st
import pandas as pd
import joblib
from surprise import Reader, Dataset, NormalPredictor

tab1, tab2 = st.tabs(["By User_ID", "Custom"])

df_anime = pd.read_csv('pages/model/anime_collab_filter/df_anime.csv')

def recommend(user_id, model):
    all_anime = df_rating.anime_id.unique()
    watched = df_rating[df_rating.user_id==user_id].anime_id
    not_watched = [anime for anime in all_anime if anime not in watched]
    
    #predict
    score = [model.predict(user_id, anime_id) for anime_id in not_watched]
    anime_id = []
    pred_score = []
    for i in range(0, len(score)):
        anime_id.append(score[i].iid)
        pred_score.append(score[i].est)
    df_pred = pd.DataFrame({'anime_id':anime_id, 'pred_score':pred_score})
    df_pred_real = df_pred.sort_values('pred_score', ascending=False).head(10)
    df_pred_real = df_pred_real.merge(df_anime, how='left', on='anime_id')
    return df_pred_real

with tab1:
    model1 = joblib.load('pages/model/anime_collab_filter/model_5.pkl')
    df_rating = pd.read_csv('pages/model/anime_collab_filter/df_rating.csv')

    user_id = st.selectbox("Select User ID",df_rating['user_id'].unique().tolist())

    if st.button('Generate Anime Recommendation'):
        st.write("## Top Anime From This User")
        df_user = df_rating[df_rating['user_id']==user_id].sort_values('rating', ascending=False)
        df_user = df_user.merge(df_anime, how='left', on='anime_id')
        col1, col2, col3 = st.columns(3)
        with col1:
            st.text(df_user['title'].values[0])
            st.image(df_user['img_url'].values[0], width=140)
        try:
            with col2:
                st.text(df_user['title'].values[1])
                st.image(df_user['img_url'].values[1], width=140)
        except:
            pass
        try:
            with col3:
                st.text(df_user['title'].values[2])
                st.image(df_user['img_url'].values[2], width=140)
        except:
            pass
        
        st.write("## Anime Recommendation For This User")
        df_pred = recommend(user_id, model1)
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.text(df_pred['title'].values[0])
            st.image(df_pred['img_url'].values[0], width=140)
        with col2:
            st.text(df_pred['title'].values[1])
            st.image(df_pred['img_url'].values[1], width=140)
        with col3:
            st.text(df_pred['title'].values[2])
            st.image(df_pred['img_url'].values[2], width=140)
        with col4:
            st.text(df_pred['title'].values[3])
            st.image(df_pred['img_url'].values[3], width=140)
        with col5:
            st.text(df_pred['title'].values[4])
            st.image(df_pred['img_url'].values[4], width=140)

with tab2:
    df_rating2 = pd.read_csv('pages/model/anime_collab_filter/df_rating2.csv')
    df_rating3 = pd.read_csv('pages/model/anime_collab_filter/df_rating3.csv')
    df_rating3['combine'] = df_rating3['title'] + ' |' + df_rating3['anime_id'].astype('str')
    
    col1, col2 = st.columns([4,1])
    with col1:
        anime_1 = st.selectbox("Select Anime 1",df_rating3['combine'].unique().tolist())
        anime_2 = st.selectbox("Select Anime 2",df_rating3['combine'].unique().tolist())
        anime_3 = st.selectbox("Select Anime 3",df_rating3['combine'].unique().tolist())
    with col2:
        rating_1 = st.selectbox("Rating 1", [i for i in range(1,11)])
        rating_2 = st.selectbox("Rating 2", [i for i in range(1,11)])
        rating_3 = st.selectbox("Rating 3", [i for i in range(1,11)])
    
    if st.button('Generate Anime Recommendations'):
        your_list = [[99999, int(anime_1.split('|')[-1]), int(rating_1)], [99999, int(anime_2.split('|')[-1]), int(rating_2)], [99999, int(anime_3.split('|')[-1]), int(rating_3)]]
        df_test = pd.DataFrame(your_list, columns=['user_id', 'anime_id', 'rating'])
        df_rating2 = pd.concat([df_rating2, df_test])
        
        st.write("## Top Anime From This User")
        df_user1 = df_test.merge(df_anime, how='left', on='anime_id')
        col1, col2, col3 = st.columns(3)
        with col1:
            st.text(df_user1['title'].values[0])
            st.image(df_user1['img_url'].values[0], width=140)
        with col2:
            st.text(df_user1['title'].values[1])
            st.image(df_user1['img_url'].values[1], width=140)
        with col3:
            st.text(df_user1['title'].values[2])
            st.image(df_user1['img_url'].values[2], width=140)
        st.write("## Anime Recommendation For This User")
        # Train
        data = Dataset.load_from_df(df_rating2, Reader(rating_scale=(1,10)))
        trainset = data.build_full_trainset()
        model2 = NormalPredictor()
        model2.fit(trainset)
        
        # Prepare Dataset
        all_anime = df_rating2.anime_id.unique()
        watched = df_rating2[df_rating2.user_id==user_id].anime_id
        not_watched = [anime for anime in all_anime if anime not in watched]
        
        # Predict
        user_id2 = 99999
        df_pred2 = recommend(user_id2, model2)
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.text(df_pred2['title'].values[0])
            st.image(df_pred2['img_url'].values[0], width=140)
        with col2:
            st.text(df_pred2['title'].values[1])
            st.image(df_pred2['img_url'].values[1], width=140)
        with col3:
            st.text(df_pred2['title'].values[2])
            st.image(df_pred2['img_url'].values[2], width=140)
        with col4:
            st.text(df_pred2['title'].values[3])
            st.image(df_pred2['img_url'].values[3], width=140)
        with col5:
            st.text(df_pred2['title'].values[4])
            st.image(df_pred2['img_url'].values[4], width=140)