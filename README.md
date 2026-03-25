# Klasifikasi Gambar Hewan (Kucing, Anjing, Ular) 🐾

Proyek ini adalah aplikasi web sederhana yang dibuat menggunakan **Streamlit** untuk mengklasifikasikan gambar hewan menjadi tiga kategori:
- Kucing
- Anjing
- Ular

Aplikasi ini menggunakan model **Deep Learning** berbasis TensorFlow Lite (TFLite) untuk melakukan inferensi gambar secara langsung dengan cepat dan efisien.

## 🚀 Fitur
- Upload gambar (mendukung format `jpg`, `jpeg`, `png`).
- Prediksi instan kelas hewan dari gambar yang dimasukkan.
- Tampilan tingkat kepercayaan (Confidence Score / Probability) dari hasil prediksi model.

## 📂 Struktur Folder Utama
- `app.py`: Script utama aplikasi antarmuka Streamlit.
- `requirements.txt`: Daftar pustaka Python yang dibutuhkan untuk menjalankan aplikasi.
- `tflite/animal_model.tflite`: Model TFLite yang sudah dilatih (pretrained).
- `tflite/label.txt`: Daftar label dari kelas model.
- `Proyek_Klasifikasi_Gambar_Dasar_Deep_Learning_Muhammad_Varel_Arifianta.ipynb`: Notebook Jupyter berisi proses pembuatan model dari awal (Data Preparation, Training, Evaluasi).

## 🛠️ Persyaratan
Pastikan kamu telah menginstal Python. Library yang digunakan dapat dilihat pada `requirements.txt`.

## 💻 Menjalankan Aplikasi Secara Lokal
1. Buka terminal atau command prompt.
2. Navigasi ke dalam folder proyek ini.
3. Install file `requirements.txt`:
```bash
pip install -r requirements.txt
```
4. Jalankan aplikasi Streamlit:
```bash
streamlit run app.py
```
5. Buka tautan lokal yang muncul (biasanya `http://localhost:8501`) pada browser web kamu.

## 🌐 Deploy ke Streamlit Community Cloud
Proyek ini sudah dioptimasi untuk dapat di-deploy secara mulus di [Streamlit Community Cloud](https://share.streamlit.io/). 
1. Push/upload repository ini ke GitHub.
2. Hubungkan akun GitHub dengan Streamlit Cloud.
3. Buat "New App", pilih repository, branch, dan Set Main File Path ke `app.py`.
4. Klik **Deploy**!
