import streamlit as st
import pandas as pd
import numpy as np
import joblib
import random

def run():
    st.set_page_config(
        page_title="Fraud Detection"
        # page_icon="👋",
    )

st.title('Fraud Detection')
st.write('This page is using a model to detect credit card fraud, insert a value in the text box and the model will detect if it is a Fraud or Not')
st.write('Example Data')
columns = ['Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10',
       'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20',
       'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'Amount', 'Class']
values = [146718.0, -1.23764919546118,1.25255541561598,-0.511406359762841,0.441192017313928,1.91670458909893,
  1.23562062567237,1.3810001853597,-0.131646797384371,-0.170695227954108,1.21325929635598,0.883422149035452,
  0.679174304416117,0.0757077608912783,0.108374079137947,-0.165050128476753,-1.82616404677335,0.266133455859126,
  -1.06098775032359,0.310410104985635,-0.0061449501392005,0.0545727916384982, 1.08316534080046,-0.149417502435938,
  -1.60713801034613,-0.0950790561150539,-0.38270084720437,-0.516437451087927,-0.420305484015155,23.93, 0]

std_amount = joblib.load('pages\\model\\card_fraud\\amount_scale.save')
std_time = joblib.load('pages\\model\\card_fraud\\time_scale.save')
model = joblib.load('pages\\model\\card_fraud\\model.pkl')

df_example = pd.DataFrame(data = [values], columns = columns)
df = pd.read_csv('pages\\model\\card_fraud\\balance_df1.csv')

st.dataframe(df_example)

st.write('If you are too lazy to input the value one by one, just click this button')
if st.button('Generate & Predict'):
    df_random = df.sample(1)
    col1, col2 = st.columns(2)
    with col1:
        time = st.text_input('Time', value=df_random['Time'].values[0])
        v1 = st.text_input('V1', value=df_random['V1'].values[0])
        v2 = st.text_input('V2', value=df_random['V2'].values[0])
        v3 = st.text_input('V3', value=df_random['V3'].values[0])
        v4 = st.text_input('V4', value=df_random['V4'].values[0])
        v5 = st.text_input('V5', value=df_random['V5'].values[0])
        v6 = st.text_input('V6', value=df_random['V6'].values[0])
        v7 = st.text_input('V7', value=df_random['V7'].values[0])
        v8 = st.text_input('V8', value=df_random['V8'].values[0])
        v9 = st.text_input('V9', value=df_random['V9'].values[0])
        v10 = st.text_input('V10', value=df_random['V10'].values[0])
        v11 = st.text_input('V11', value=df_random['V11'].values[0])
        v12 = st.text_input('V12', value=df_random['V12'].values[0])
        v13 = st.text_input('V13', value=df_random['V13'].values[0])
        v14 = st.text_input('V14', value=df_random['V14'].values[0])

    with col2:
        v15 = st.text_input('V15', value=df_random['V15'].values[0])
        v16 = st.text_input('V16', value=df_random['V16'].values[0])
        v17 = st.text_input('V17', value=df_random['V17'].values[0])
        v18 = st.text_input('V18', value=df_random['V18'].values[0])
        v19 = st.text_input('V19', value=df_random['V19'].values[0])
        v20 = st.text_input('V20', value=df_random['V20'].values[0])
        v21 = st.text_input('V21', value=df_random['V21'].values[0])
        v22 = st.text_input('V22', value=df_random['V22'].values[0])
        v23 = st.text_input('V23', value=df_random['V23'].values[0])
        v24 = st.text_input('V24', value=df_random['V24'].values[0])
        v25 = st.text_input('V25', value=df_random['V25'].values[0])
        v26 = st.text_input('V26', value=df_random['V26'].values[0])
        v27 = st.text_input('V27', value=df_random['V27'].values[0])
        v28 = st.text_input('V28', value=df_random['V28'].values[0])
        amount = st.text_input('Amount', value=df_random['Amount'].values[0])
        
    scaled_amount = std_amount.transform([[float(amount)]])[0][0]
    scaled_time = std_time.transform([[float(time)]])[0][0]
    
    df_predict = pd.DataFrame([[amount, time, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, 
                                v16, v17, v18, v19, v20, v21, v22, v23, v24, v25, v26, v27, v28]])
    df_predict = df_predict.astype(float)
    result = model.predict(df_predict)[0]
    if result == 0:
        st.markdown('## Non Fraud')
    else:
        st.markdown('## Fraud')
else:
    col1, col2 = st.columns(2)
    with col1:
        time = st.text_input('Time')
        v1 = st.text_input('V1')
        v2 = st.text_input('V2')
        v3 = st.text_input('V3')
        v4 = st.text_input('V4')
        v5 = st.text_input('V5')
        v6 = st.text_input('V6')
        v7 = st.text_input('V7')
        v8 = st.text_input('V8')
        v9 = st.text_input('V9')
        v10 = st.text_input('V10')
        v11 = st.text_input('V11')
        v12 = st.text_input('V12')
        v13 = st.text_input('V13')
        v14 = st.text_input('V14')

    with col2:
        v15 = st.text_input('V15')
        v16 = st.text_input('V16')
        v17 = st.text_input('V17')
        v18 = st.text_input('V18')
        v19 = st.text_input('V19')
        v20 = st.text_input('V20')
        v21 = st.text_input('V21')
        v22 = st.text_input('V22')
        v23 = st.text_input('V23')
        v24 = st.text_input('V24')
        v25 = st.text_input('V25')
        v26 = st.text_input('V26')
        v27 = st.text_input('V27')
        v28 = st.text_input('V28')
        amount = st.text_input('Amount')

    if st.button('Predict'):
        scaled_amount = std_amount.transform([[float(amount)]])[0][0]
        scaled_time = std_time.transform([[float(time)]])[0][0]
        
        df_predict = pd.DataFrame([[amount, time, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, 
                                    v16, v17, v18, v19, v20, v21, v22, v23, v24, v25, v26, v27, v28]])
        result = model.predict(df_predict)[0]
        if result == 0:
            st.write('Non Fraud')
        else:
            st.write('Fraud')
    else:
        st.write('Click Predict')

col1a, col2a, col3a = st.columns(3)
with col2a:
    if st.button('Reset'):
        pass
    else:
        pass
