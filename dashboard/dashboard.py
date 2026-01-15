import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
sns.set_style("whitegrid")

st.set_page_config(
    page_title="Bike Sharing Dashboard",
    layout="wide"
)
@st.cache_data
def load_data():
    base_dir = os.path.dirname(__file__)
    data_path = os.path.join(base_dir, "main_data.csv")
    df = pd.read_csv(data_path)
    
    df = df.rename(columns={
        'dteday': 'date',
        'yr': 'year',
        'mnth': 'month',
        'weathersit': 'weather_condition',
        'hum': 'humidity',
        'windspeed': 'wind_speed',
        'atemp': 'feels_like_temp',
        'cnt': 'total_rentals',
        'casual': 'casual_users',
        'registered': 'registered_users'
    })

    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['year'].map({0: 2011, 1: 2012})

    df['temp_celsius'] = df['temp'] * 41

    season_map = {1:'Spring', 2:'Summer', 3:'Fall', 4:'Winter'}
    df['season_label'] = df['season'].map(season_map)

    weather_map = {
        1:'Clear',
        2:'Mist/Cloudy',
        3:'Light Rain/Snow',
        4:'Heavy Rain/Snow'
    }
    df['weather_label'] = df['weather_condition'].map(weather_map)

    df['workingday_label'] = df['workingday'].map({
        0:'Non-working day',
        1:'Working day'
    })

    return df

day_df = load_data()


st.title("🚲 Bike Sharing Analysis Dashboard")
st.markdown(
    "Dashboard ini menampilkan analisis pola peminjaman sepeda berdasarkan waktu, cuaca, musim, dan jenis hari."
)


st.sidebar.header("Filter Data")

year_options = ['All'] + sorted(day_df['year'].unique().tolist())

selected_year = st.sidebar.selectbox(
    "Pilih Tahun",
    options=year_options
)

if selected_year == 'All':
    filtered_df = day_df.copy()
else:
    filtered_df = day_df[day_df['year'] == selected_year]



st.subheader("📈 Tren Peminjaman Sepeda Harian")

fig, ax = plt.subplots(figsize=(10,4))
ax.plot(filtered_df['date'], filtered_df['total_rentals'])
ax.set_xlabel("Date")
ax.set_ylabel("Total Rentals")

st.pyplot(fig)


st.subheader("🌦️ Pengaruh Cuaca dan Musim")

col1, col2 = st.columns(2)

with col1:
    fig1, ax1 = plt.subplots()
    sns.barplot(
        data=filtered_df,
        x='weather_label',
        y='total_rentals',
        ax=ax1
    )
    ax1.set_title("Berdasarkan Kondisi Cuaca")
    st.pyplot(fig1)

with col2:
    fig2, ax2 = plt.subplots()
    sns.barplot(
        data=filtered_df,
        x='season_label',
        y='total_rentals',
        ax=ax2
    )
    ax2.set_title("Berdasarkan Musim")
    st.pyplot(fig2)

st.subheader("📅 Hari Kerja vs Hari Libur")

fig, ax = plt.subplots(figsize=(6,4))
sns.barplot(
    data=filtered_df,
    x='workingday_label',
    y='total_rentals',
    ax=ax
)
ax.set_xlabel("")
ax.set_ylabel("Total Rentals")
plt.tight_layout()
st.pyplot(fig)


st.subheader("🌡️ Suhu vs Jumlah Peminjaman")

fig, ax = plt.subplots(figsize=(6,4))
sns.scatterplot(
    data=filtered_df,
    x='temp_celsius',
    y='total_rentals',
    ax=ax
)
ax.set_xlabel("Temperature (°C)")
ax.set_ylabel("Total Rentals")
plt.tight_layout()
st.pyplot(fig)


st.subheader("📊 Kategori Permintaan Sepeda")

bins = [0, 3000, 6000, filtered_df['total_rentals'].max()]
labels = ['Low Demand', 'Medium Demand', 'High Demand']
filtered_df['demand_category'] = pd.cut(
    filtered_df['total_rentals'],
    bins=bins,
    labels=labels
)

fig, ax = plt.subplots(figsize=(6,4))
sns.countplot(
    data=filtered_df,
    x='demand_category',
    ax=ax
)
ax.set_xlabel("")
ax.set_ylabel("Number of Days")
plt.tight_layout()
st.pyplot(fig)

