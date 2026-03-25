# Klasifikasi Gambar Hewan (Kucing, Anjing, Ular) 🐾

**🚀 Live Demo: [Coba Aplikasi di Sini!](https://klasifikasi-hewan-pekg8aqpttd7ep7grbfwxe.streamlit.app/)**

Proyek ini bertujuan untuk membangun sebuah model klasifikasi gambar menggunakan algoritma **Deep Learning (Machine Learning)** berbasis gambar. Model ini dirancang khusus untuk mengenali dan membedakan tiga ciri fisik jenis hewan: **Kucing, Anjing, dan Ular**. Setelah model kecerdasan buatan selesai dilatih, sebuah antarmuka web interaktif dibangun menggunakan **Streamlit** agar siapapun dapat mencoba mengunggah gambar dan melihat prediksi model secara *real-time*.

Aplikasi ini menggunakan model versi kompresi berskala **TensorFlow Lite (TFLite)** yang sangat teringankan sehingga prediksi (inferensi) tidak rakus sumber daya komputer dan dapat berjalan sangat cepat.

## 📈 Tahapan Pengembangan Proyek
Proyek ini dikembangkan melalui beberapa fase (alur kerja lengkapnya bisa dilihat di file Notebook):

1. **Pengumpulan & Persiapan Data (Data Preparation)**
   - Menyiapkan himpunan data (dataset) berisi sekumpulan gambar kucing, anjing, dan ular.
   - Melakukan prapemrosesan visual (*image preprocessing*) seperti mengubah resolusi, menormalisasi warna piksel, dan memanipulasi rentang gaya gambar (*data augmentation*) untuk memperbanyak sampel pelatihan secara artifisial.

2. **Pembuatan & Pelatihan Model (Modeling)**
   - Merancang arsitektur model *Convolutional Neural Network* (CNN) menggunakan TensorFlow / Keras untuk mengekstraksi dan mempelajari pola bentuk visual unik dari setiap jenis hewan.
   - Melatih model secara berulang-ulang (*epochs*) hingga bobot perhitungannya mantap.

3. **Evaluasi & Optimalisasi (Model Optimization)**
   - Memastikan rasio metrik prediksi dan akurasi telah tercapai pada data pengujian.
   - Mewujudkan deployment yang lebih cepat dan efisien dengan cara mengonversi model berukuran jumbo menjadi format **.tflite**.

4. **Pembuatan Antarmuka Web & Pemasaran (Web & Deployment)**
   - Menyuntikkan model *TFLite* ke dalam jembatan (*wrapper*) sederhana berbentuk halaman interaktif buatan **Streamlit** (tersimpan dalam script `app.py`).
   - Menerapkan (*deploy*) aplikasi beserta syarat kebutuhannya (`requirements.txt`) ke dalam layanan server **Streamlit Community Cloud** sehingga bisa langsung diakses oleh publik (Live Link).

## 🚀 Fitur Aplikasi
- Form unggah gambar pintar (mendukung ekstensi `.jpg`, `.jpeg`, `.png`).
- Prediksi kalkulasi kilat (hanya dalam hitungan kurang dari 1 detik) menggunakan pemrosesan TFLite-Interpreter CPU.
- Fitur penampil Probabilitas / Akurasi Prediksi (*Confidence Score*), mengemukakan persentase keyakinan model terhadap gambar tersebut.

## 📂 Struktur Repositori Utama
- `app.py`: Script pembangun UI utama yang menjembatani web dan model.
- `requirements.txt`: Daftar paket Python seperlunya yang dikhususkan agar Cloud mampu menjalankan aplikasi.
- `tflite/animal_model.tflite`: Komponen nyawa utama; Model siap-pakai.
- `tflite/label.txt`: Urutan dan nama target hasil keluaran model.
- `Proyek_Klasifikasi...ipynb`: Buku catatan jupyter yang berisikan urutan kode eksperimen kasar / mentah tempat data awal dilatih dari nol menjadi sebuah Model TFLite.
