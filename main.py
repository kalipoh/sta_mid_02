import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# Menampilkan soal
st.subheader("Soal")
st.markdown("""
Sebuah **agensi penelitian pasar** melakukan survei terhadap **200 pelanggan** yang membeli berbagai produk elektronik di wilayah Jakarta. 
Setiap pelanggan diminta memberikan **rating kepuasan** terhadap produk yang mereka beli, menggunakan skala **1 hingga 5**, di mana:

- **1** berarti "Sangat Tidak Puas"
- **2** berarti "Tidak Puas"
- **3** berarti "Netral"
- **4** berarti "Puas"
- **5** berarti "Sangat Puas"

Hasil survei dirangkum dalam tabel berikut:
""")

# Data survei kepuasan pelanggan
ratings = [1, 2, 3, 4, 5]
frequencies = [30, 45, 50, 40, 35]

data = pd.DataFrame({"Rating (x)": ratings, "Frekuensi (f)": frequencies})

# Menampilkan tabel data
st.table(data.set_index("Rating (x)"))

st.markdown("""
**Tugas:**
1. **Buat distribusi probabilitas** untuk variabel acak x.
2. **Gambarkan histogram** berdasarkan distribusi probabilitas tersebut.
3. **Hitung mean dan variansi** dari distribusi probabilitas tersebut.

JAWABAN
""")
st.header("NOMOR 1")
st.write("Data Survei Pelanggan")

data = {
    1: 30,
    2: 45,
    3: 50,
    4: 40,
    5: 35
}

df_data = pd.DataFrame(list(data.items()), columns=['Rating (x)', 'Frekuensi (f)'])
st.table(df_data.set_index('Rating (x)')) # Menghapus indeks awal

total_responden = sum(data.values())
st.write(f"**Total Responden (N):** {total_responden}")



st.write("Menghitung Probabilitas untuk Setiap Rating")

probabilitas = {}
for rating, frekuensi in data.items():
    p = frekuensi / total_responden
    probabilitas[rating] = p
    st.write(f"P({rating}) = {frekuensi} / {total_responden} = {p:.3f}")


# Membuat DataFrame probabilitas dengan kolom 'Rating (x)'
prob_data = {'Rating (x)': list(probabilitas.keys()), 'Probabilitas P(x)': list(probabilitas.values())}
df_probabilitas = pd.DataFrame(prob_data)

df_distribusi = pd.merge(df_data, df_probabilitas, on='Rating (x)')
st.table(df_distribusi.set_index('Rating (x)')) # Menghapus indeks awal

st.write("""
**Jadi, distribusi probabilitas menggunakan rumus:**
P(x) = f / N
""")

st.write("""
**Penjelasan Rumus:**
P(x) = f / N
 - P(x): Probabilitas dari setiap nilai rating x
 - f: Frekuensi dari rating x (jumlah kejadian untuk rating tertentu)
 - N: Total seluruh frekuensi (jumlah total responden)
""")


st.header("NOMOR 2")
st.write("Histogram")
image = Image.open("histo.png")
st.image(image, caption='Histogram Distribusi Probabilitas',  use_container_width=True)

image = Image.open("histog.png")
st.image(image, caption='Histogram Distribusi Probabilitas',  use_container_width=True)

image = Image.open("grafik.png")
st.image(image, caption='Histogram Distribusi Probabilitas',  use_container_width=True)

image = Image.open("bunder.png")
st.image(image, caption='Histogram Distribusi Probabilitas',  use_container_width=True)

image = Image.open("grfk.png")
st.image(image, caption='Histogram Distribusi Probabilitas',  use_container_width=True)


st.header("NOMOR 3")
st.write("Mean")

def hitung_mean_distribusi_probabilitas(data):
    """Menghitung mean (nilai rata-rata) dari distribusi probabilitas."""
    df = pd.DataFrame(data)
    df['x * P(x)'] = df['Rating (x)'] * df['Probabilitas P(x)']
    mean = df['x * P(x)'].sum()
    return mean, df  # Mengembalikan mean dan DataFrame

def tampilkan_hasil(data, mean):
    """Menampilkan tabel data survei dan hasil perhitungan mean."""
    df = pd.DataFrame(data)
    st.write("Data Survei:")
    st.table(df.set_index('Rating (x)'))
    st.write(f"Mean (μ): {mean}")

def tampilkan_langkah_perhitungan(df, mean):  # Menerima DataFrame df
    """Menampilkan langkah-langkah perhitungan mean."""
    perkalian = [f"{x} * {px}" for x, px in zip(df['Rating (x)'], df['Probabilitas P(x)'])]
    hasil_perkalian = df['x * P(x)'].tolist()

    st.write("Langkah Perhitungan Mean (μ):")
    st.write(f"μ = ({' + '.join(perkalian)})")
    st.write(f"μ = {hasil_perkalian}")
    st.write(f"μ = {mean}")

# Data survei
data_survei = {
    'Rating (x)': [1, 2, 3, 4, 5],
    'Frekuensi (f)': [30, 45, 50, 40, 35],
    'Probabilitas P(x)': [0.150, 0.225, 0.250, 0.200, 0.175]
}

# Menghitung mean dan mendapatkan DataFrame
mean_hasil, df_hasil = hitung_mean_distribusi_probabilitas(data_survei)

# Menampilkan hasil
tampilkan_hasil(data_survei, mean_hasil)
tampilkan_langkah_perhitungan(df_hasil, mean_hasil)  # Menggunakan DataFrame yang dikembalikan


def hitung_variansi_distribusi_probabilitas(data, mean):
    """Menghitung variansi dari distribusi probabilitas."""
    df = pd.DataFrame(data)
    df['(x - μ)^2'] = (df['Rating (x)'] - mean) ** 2
    df['P(x) * (x - μ)^2'] = df['Probabilitas P(x)'] * df['(x - μ)^2']
    variansi = df['P(x) * (x - μ)^2'].sum()
    return variansi, df  # Mengembalikan variansi dan DataFrame

def tampilkan_hasil_variansi(data, mean, variansi):
    """Menampilkan hasil perhitungan variansi."""
    df = pd.DataFrame(data)
    st.write("Cara Menghitung Variansi (σ^2):")
    st.table(df)
    st.write(f"Variansi (σ^2): {variansi}")

def tampilkan_langkah_perhitungan_variansi(df, mean, variansi):
    """Menampilkan langkah-langkah perhitungan variansi."""
    langkah_1 = [f"({px} * ({x} - {mean})^2)" for x, px in zip(df['Rating (x)'], df['Probabilitas P(x)'])]
    langkah_2 = [(px * (x - mean) ** 2) for x, px in zip(df['Rating (x)'], df['Probabilitas P(x)'])]
    langkah_3 = [f"{v:.3f}" for v in langkah_2]

    st.write("Langkah Perhitungan Variansi (σ^2):")
    st.write(f"σ^2 = ({' + '.join(langkah_1)})")
    st.write(f"σ^2 = ({' + '.join(map(str, langkah_2))})")
    st.write(f"σ^2 = {' + '.join(langkah_3)}")
    st.write(f"σ^2 = {variansi}")

# Data survei
data_survei = {
    'Rating (x)': [1, 2, 3, 4, 5],
    'Probabilitas P(x)': [0.150, 0.225, 0.250, 0.200, 0.175]
}

# Mean yang telah dihitung sebelumnya
mean_hasil = 3.025


# Menghitung variansi dan mendapatkan DataFrame
variansi_hasil, df_hasil = hitung_variansi_distribusi_probabilitas(data_survei, mean_hasil)

# Menampilkan hasil
tampilkan_hasil_variansi(data_survei, mean_hasil, variansi_hasil)
tampilkan_langkah_perhitungan_variansi(df_hasil, mean_hasil, variansi_hasil)