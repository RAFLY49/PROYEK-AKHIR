# Import Library
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def load_data():
    hour_csv_path = "dataset/Bike-sharing-dataset/hour.csv"
    day_csv_path = "dataset/Bike-sharing-dataset/day.csv"
    
    data_hour = pd.read_csv(hour_csv_path)
    data_day = pd.read_csv(day_csv_path)
    
    return data_hour, data_day


# Panggil fungsi load_data
data_hour, data_day = load_data()

# Fungsi untuk membuat visualisasi dan grafik
def plot_hourly_interaction():
    # Scatter plot 3D untuk interaksi musiman, kondisi cuaca, hari dalam seminggu, dan jumlah peminjaman sepeda
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')  # Specify 3D projection

    scatter = ax.scatter(data_hour['season'], data_hour['weathersit'], data_hour['weekday'],
                         c=data_hour['cnt'], cmap='viridis', s=50)

    ax.set_xlabel('Musim')
    ax.set_ylabel('Kondisi Cuaca')
    ax.set_zlabel('Hari dalam Seminggu')
    ax.set_title('Interaksi Musiman, Kondisi Cuaca, dan Hari dengan Jumlah Peminjaman Sepeda')

    # Menambahkan colorbar dengan menggunakan objek scatter sebagai mappable
    cbar = fig.colorbar(scatter)
    cbar.set_label('Jumlah Peminjaman Sepeda', rotation=270, labelpad=20)

    st.pyplot(fig)


def plot_holiday_trends():
    # Line plot untuk tren peminjaman sepeda selama liburan
    fig, ax = plt.subplots(figsize=(10, 5))
    data_day['dteday'] = pd.to_datetime(data_day['dteday'])
    sns.lineplot(x='dteday', y='cnt', data=data_day, hue='holiday', palette='Set1', ax=ax)
    ax.set_title('Tren Peminjaman Sepeda Selama Liburan')
    ax.set_xlabel('Tanggal')
    ax.set_ylabel('Jumlah Peminjaman Sepeda')
    ax.legend(title='Liburan', loc='upper right')
    ax.xaxis.set_major_locator(plt.MaxNLocator(7))
    plt.xticks(rotation=45)
    
    st.pyplot(fig)

# Judul halaman
st.title("Bike Sharing Analysis Dashboard")

# Sidebar
st.sidebar.title("Information:")
st.sidebar.markdown("**• Nama: Rafly Ramadan**")
st.sidebar.markdown(
    "**• Email: [raframadan1@gmail.com](raframadan1@gmail.com)**")
st.sidebar.markdown(
    "**• Instagram: [rafly_rmdnn1](https://www.instagram.com/rafly_rmdnn1?igsh=NXE1Nm1maHR1OXBt)**")

# Sidebar untuk memilih visualisasi
selected_chart = st.sidebar.radio("Pilih Visualisasi:", ["Interaksi Musiman", "Tren Liburan"])

# Tampilkan visualisasi berdasarkan pilihan
if selected_chart == "Interaksi Musiman":
    st.header("Interaksi Musiman, Kondisi Cuaca, dan Hari dalam Seminggu")
    plot_hourly_interaction()
elif selected_chart == "Tren Liburan":
    st.header("Tren Peminjaman Sepeda Selama Liburan")
    plot_holiday_trends()

# Tampilkan informasi tambahan atau analisis lainnya
st.markdown("### Analisis Tambahan:")
st.write("Dalam analisis ini, kita melihat bagaimana faktor musiman, kondisi cuaca, dan hari dalam seminggu "
         "memengaruhi pola peminjaman sepeda, terutama pada pengguna kasual dan terdaftar.")
st.write("Selain itu, kita mengeksplorasi tren khusus dalam peminjaman sepeda selama liburan atau peristiwa khusus, "
         "dan bagaimana tren ini berubah dari tahun ke tahun.")
