import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# Konfigurasi halaman
st.set_page_config(page_title="Klasifikasi Hewan", page_icon="🐾")

st.title("🐾 Klasifikasi Hewan (Kucing, Anjing, Ular)")
st.write("Silakan unggah gambar hewan untuk dianalisis oleh model Deep Learning (TFLite).")

@st.cache_resource
def load_model():
    # Load model TFLite
    interpreter = tf.lite.Interpreter(model_path="tflite/animal_model.tflite")
    interpreter.allocate_tensors()
    return interpreter

@st.cache_data
def load_labels():
    with open("tflite/label.txt", "r") as f:
        return [line.strip() for line in f.readlines()]

interpreter = load_model()
labels = load_labels()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Mendapatkan ukuran input dari model
input_shape = input_details[0]['shape']
height = input_shape[1]
width = input_shape[2]

uploaded_file = st.file_uploader("Pilih gambar...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption='Gambar yang diunggah.', use_container_width=True)
    st.write("⏳ Mendeteksi...")

    # Preprocessing
    image_resized = image.resize((width, height))
    input_data = np.expand_dims(image_resized, axis=0)
    
    if input_details[0]['dtype'] == np.float32:
        input_data = np.float32(input_data) / 255.0  # Normalisasi ke [0, 1]

    # Inference
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()
    
    output_data = interpreter.get_tensor(output_details[0]['index'])
    predictions = output_data[0]
    
    # Hasil
    predicted_index = np.argmax(predictions)
    score = predictions[predicted_index]
    
    st.success(f"✨ Prediksi: **{labels[predicted_index].capitalize()}**")
    st.info(f"Tingkat Kepercayaan: {score:.2%}")
