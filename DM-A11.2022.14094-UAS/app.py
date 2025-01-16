import pickle
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

model = pickle.load(open('model_predict_CO(GT).sav', 'rb'))

df = pd.read_csv("cleaned_dataset.csv")
df['Datetime'] = pd.to_datetime(df['Datetime'], format='%Y-%m-%d%H%M%S')
df.set_index('Datetime', inplace=True)


# Membuat input untuk pengguna
st.title('Forecasting Kualitas Udara')

# Input data (misalnya untuk memprediksi beberapa langkah ke depan)
st.sidebar.header("Input Parameters")
forecast_steps = st.sidebar.slider('Jumlah jam ke depan untuk prediksi', 1, 30, 10)

# Menambahkan tombol "Predict"
predict_button = st.sidebar.button("Predict")

if predict_button:
    # Lakukan prediksi dengan model jika tombol ditekan
    forecast = model.forecast(steps=forecast_steps)
    
    forecast_table = {'CO(GT)': forecast}
    # Menampilkan hasil prediksi
    st.write(f"Prediksi untuk {forecast_steps} jam ke depan:")
    st.write(forecast_table)
else:
    st.write("Klik tombol 'Predict' untuk melakukan prediksi.")