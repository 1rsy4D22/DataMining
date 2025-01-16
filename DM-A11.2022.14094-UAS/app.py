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

    # Menampilkan keterangan kualitas udara
    st.write("""
    ### Keterangan Kualitas Udara:
    
    1. **Baik**  
       - **CO(GT) <= 4.4**  
       Kualitas udara sangat baik dan aman untuk semua orang. Tidak ada dampak negatif bagi kesehatan.

    2. **Sedang**  
       - **4.5 <= CO(GT) <= 9.4**  
       Kualitas udara berada dalam kategori sedang. Untuk kebanyakan orang, tidak ada dampak signifikan pada kesehatan. Namun, individu dengan kondisi pernapasan atau jantung mungkin mengalami ketidaknyamanan.

    3. **Tidak Sehat untuk Kelompok Sensitif**  
       - **9.5 <= CO(GT) <= 12.4**  
       Kualitas udara tidak sehat untuk kelompok sensitif seperti anak-anak, lansia, dan orang dengan masalah pernapasan atau penyakit jantung. Paparan dalam waktu lama dapat mempengaruhi kesehatan.

    4. **Tidak Sehat**  
       - **12.5 <= CO(GT) <= 15.4**  
       Kualitas udara dianggap tidak sehat. Semua orang dapat merasakan efek negatif pada kesehatan jika terpapar dalam waktu lama. Sebaiknya, batasi aktivitas di luar ruangan.

    5. **Sangat Tidak Sehat**  
       - **15.5 <= CO(GT) <= 30.4**  
       Kualitas udara sangat buruk dan dapat menyebabkan gangguan kesehatan serius bagi sebagian besar orang. Disarankan untuk menghindari kegiatan di luar ruangan.

    6. **Berbahaya**  
       - **CO(GT) > 30.4**  
       Kualitas udara sangat berbahaya. Paparan udara luar bisa menyebabkan keracunan karbon monoksida dan gangguan pernapasan yang serius. Semua orang harus menghindari aktivitas luar ruangan sampai kondisi membaik.
    """)
    
else:
    st.write("Klik tombol 'Predict' untuk melakukan prediksi.")

    