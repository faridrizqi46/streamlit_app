import streamlit as st
import pandas as pd
import joblib

model = joblib.load('pages/model/anime_collab_filter/model_first.pkl')
df_anime = pd.read_csv('pages/model/anime_collab_filter/df_anime.csv')
df_rating = pd.read_csv('pages/model/anime_collab_filter/df_rating.csv')

user_id = st.selectbox("Select User ID",df_rating['user_id'].unique().tolist())


def recommend(user_id=user_id):
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
    df_pred = recommend()
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