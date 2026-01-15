# 🚲 Bike Sharing Analysis Dashboard

Dashboard ini dibuat menggunakan **Streamlit** untuk menganalisis pola peminjaman sepeda berdasarkan waktu, cuaca, musim, dan jenis hari (hari kerja vs hari libur).

---

## 📦 Setup Environment

### 🔹 Opsi 1: Menggunakan Anaconda (Direkomendasikan)

```bash
conda create --name main-ds python=3.10 -y
conda activate main-ds
pip install -r requirements.txt
```

### 🔹 Opsi 2: Menggunakan Shell / Terminal (Pipenv)

```bash
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Menjalankan Aplikasi Streamlit
```bash
streamlit run dashboard/dashboard.py
```