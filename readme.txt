📁 Nama Proyek:
Video Transcription and Voice Synthesis for Indonesian Language Sign Translation
---------------------------------------------------------------------------------------------------------
📖 Deskripsi Singkat:
Program ini adalah sistem penerjemah bahasa isyarat Indonesia (SIBI) 
berbasis video real-time, yang mampu mendeteksi gesture tangan dan mengubahnya
 menjadi teks serta suara. Sistem ini dibangun menggunakan Python, OpenCV, Teachable Machine, dan gTTS.
---------------------------------------------------------------------------------------------------------
-jika error no cv module 
perbarui: 
opencv-python
opencv-contrib-python  #pip install opencv-contrib-python

labels = ["aku", "sedang", "makan"] HARUS BERURUTAN DENGANN FILE DI MODEL DATA DAN DATASET HARUS SESUAI BERURUTAN

AttributeError: 'NoneType' object has no attribute 'copy' 
bermasalah bagian webcam (cabut pasang ulang)
PENCAHAYAAN SANGAT MEMPENGARUHI USAHAKAN BERADA DI TEMPAT YANG TIDAK TERLALU GELAP DAN TIDAK TERLALU TERANG SAAT MENCOBA PROGRAM.
---------------------------------------------------------------------------------------------------------
🚀 Fitur Utama:
Deteksi gesture tangan secara real-time
Konversi gesture ke teks
Konversi teks ke suara (Text-to-Speech)
Akurasi gesture dan suara > 95%
Mendukung kosa kata dasar seperti: "aku", "bagus", "bangku", "besar","dia","jalan","kita","lihat","panas","pegang",
"pelan","pelangi","pohon","tiang","tunjuk"
---------------------------------------------------------------------------------------------------------
🚀 Fitur Utama:
Deteksi gesture tangan secara real-time
Konversi gesture ke teks
Konversi teks ke suara (Text-to-Speech)
Akurasi gesture dan suara > 87%
--------------------------------------------------------------------------
🛠️ Tools dan Library:
Python 3.x
OpenCV
TensorFlow / Keras (model Teachable Machine)
gTTS
Pygame
CVZone
VS Code
--------------------------------------------------------------------------
🖥️ Cara Menjalankan:
Buka terminal / VSCode

Jalankan perintah:
.venv\Scripts\activate [pada terminal]
kemudian
python deaf_program.py
deactivate [jika program sudah tak di pakai]

Arahkan gesture tangan ke kamera
Sistem akan menampilkan teks & mengeluarkan suara
--------------------------------------------------------------------------
📂 Struktur Folder:
_pycache_
.venv
Data/→ foto dataset yang belum di olah 
dataset/ → berisi dataset yang sudah di olah
model/ → berisi model keras (.h5) dan json [ telah di latih di Teachable machine]
dokumentasi
deaf_program.py → program utama

utils.py → fungsi bantu
README.md → dokumentasi proyek

--------------------------------------------------------------------------
-jika error no cv module 
perbarui: 
opencv-python
opencv-contrib-python  #pip install opencv-contrib-python

labels = ["aku", "sedang", "makan"] HARUS BERURUTAN DENGANN FILE DI MODEL DATA DAN DATASET HARUS SESUAI BERURUTAN

AttributeError: 'NoneType' object has no attribute 'copy' 
bermasalah bagian webcam (cabut pasang ulang)
PENCAHAYAAN SANGAT MEMPENGARUHI USAHAKAN BERADA DI TEMPAT YANG TIDAK TERLALU GELAP DAN TIDAK TERLALU TERANG SAAT MENCOBA PROGRAM.

--------------------------------------------------------------------------
🎯 Target User:
Penyandang tunarungu, pendidik, dan peneliti teknologi inklusif.

💡 Catatan Khusus:
Sistem paling akurat digunakan dengan pencahayaan yang cukup.
Jangan menutupi gesture dengan benda lain.
Proyek ini dibuat sebagai bagian dari Tugas Akhir (Skripsi) di Universitas Malikussaleh.

👩‍💻 Pengembang:
Nazwa Aulia
S1 Teknik Informatika
Universitas Malikussaleh