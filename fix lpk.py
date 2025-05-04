import streamlit as st
import pandas as pd

# Tambahkan CSS untuk background pink dan teks gelap
st.markdown(
    """
    <style>
    /* Mengubah latar belakang aplikasi dan teks di seluruh aplikasi */
    .stApp {
        background-color: #ffc0cb !important;  /* Warna background pink */
        color: #222222 !important;             /* Warna teks utama */
    }
    
    /* Mengubah warna teks di judul-judul */
    h1, h2, h3, h4, h5, h6 {
        color: #ff8080 !important;  /* Warna merah muda untuk judul */
    }
    
    /* Mengubah warna background sidebar */
    .css-1d391kg, .css-1v3fvcr {
        background-color: #ffc0cb !important;
        color: #222222 !important;
    }

    /* Mengubah warna button dan teks pada button */
    .css-1y6vkvb, .stButton>button {
        background-color: #ff8080 !important;
        color: #ffffff !important;
    }

    /* Mengubah warna background kolom widget */
    .st-bd {
        background-color: #ffc0cb !important;
    }

    /* Styling untuk area "Selamat Datang" */
    .selamat-datang {
        background-color: #f8a5c2;
        padding: 20px;
        border-radius: 10px;
    }

    /* Styling untuk area kalkulator */
    .kalkulator-area {
        background-color: #ff8080;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# Slide pendahuluan dengan style custom
st.markdown(
    """
    <div class="selamat-datang">
        <h2 style='color: #ff8080; text-align:center;'>Selamat Datang di Aplikasi Menghitung Kadar Gula Dalam Jus Buah</h2>
        <p style='color: #333333; text-align:justify;'>Aplikasi ini dirancang untuk membantu Anda menghitung jumlah kadar gula dalam berbagai jenis buah sebanyak 250mL. 
        Pilih jus buah yang anda ingin ketahui kadar gulanya dan aplikasi kami akan memberikan informasi tentang jumlah kadar gulanya.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# Judul utama aplikasi
st.markdown("<h1 style='color:#ff8080;'>🍓kalkulator kadar gula dalam jus buah</h1>", unsafe_allow_html=True)

# Data dan sidebar
informasi_tambahan = {
    'apel': {'manfaat': "Apel mengandung serat...", 'cara_memilih': "Pilih apel yang..."},
    'pisang': {'manfaat': "Pisang kaya akan kalium...", 'cara_memilih': "Pilih pisang yang..."},
    'jeruk': {'manfaat': "Jeruk kaya vitamin C...", 'cara_memilih': "Pilih jeruk yang..."},
    'pir': {'manfaat': "Pir mengandung serat...", 'cara_memilih': "Pilih pir yang..."},
    'strawberry': {'manfaat': "Stroberi kaya vitamin C...", 'cara_memilih': "Pilih stroberi yang..."},
    'semangka': {'manfaat': "Semangka mengandung air...", 'cara_memilih': "Pilih semangka yang..."},
    'mangga': {'manfaat': "Mangga mengandung vitamin A dan C...", 'cara_memilih': "Pilih mangga yang..."},
    'alpukat': {'manfaat': "Alpukat kaya lemak sehat...", 'cara_memilih': "Pilih alpukat yang..."},
    'kiwi': {'manfaat': "Kiwi kaya vitamin C dan serat...", 'cara_memilih': "Pilih kiwi yang..."},
    'melon': {'manfaat': "Melon meningkatkan hidrasi...", 'cara_memilih': "Perhatikan aroma dan warna..."},
    'buah naga': {'manfaat': "Buah naga meningkatkan kekebalan...", 'cara_memilih': "Pilih yang warna cerah..."},
    'sirsak': {'manfaat': "Sirsak meredakan peradangan...", 'cara_memilih': "Pilih kulit agak lunak..."},
    'tomat': {'manfaat': "Tomat kaya akan nutrisi, mendukung kesehatan jantung, mendukung kesehatan mata", 'cara_memilih': "Pilih yang Berwarna Cerah, Periksa Kekerasan, Hindari Bercak atau Kerusakan"},
    'pepaya': {'manfaat': "Pepaya meningkatkan sistem kekebalan tubuh, mendukung kesehatan pencernaan", 'cara_memilih': "Periksa warna kulit, aroma, tekstur kulit"},
    'lemon': {'manfaat': "Lemon mengandung Vitamin C yang baik,membantu menjaga kesehatan kulit, mendukung penurunan berat badan", 'cara_memilih': "Periksa warna kulit, aroma, tekstur kulit"},
    'blueberry': {'manfaat': "Blueberry kaya antioksidan, baik untuk otak, mata, dan kesehatan jantung", 'cara_memilih': "Pilih blueberry yang berwarna biru gelap, terasa kenyal dan tidak terlalu lembek, noda putih pada blueberry adalah tanda bahwa buah tersebut sudah terlalu lama disimpan"},
    'nanas': {'manfaat': "Nanas melancarkan pencernaan, anti-inflamasi dan penyembuhan luka, meningkatkan kekebalan tubuh, menjaga kesehatan jantung, menjaga kesehatan kulit", 'cara_memilih': "pilih warna kulit kuning keemasan, Aroma Harum manis di bagian pangkal, Tekstur Kulit sedikit lunak saat ditekan lembut, Daun mahkota Hijau segar dan mudah dicabut jika buah sudah matang, Berat nanas matang terasa berat, menandakan banyak air dan daging buah"},
    'markisa': {'manfaat': "Markisa baik untuk relaksasi, pencernaan, dan kulit karena kaya antioksidan", 'cara_memilih': "Markisa yang matang memiliki kulit yang sedikit keriput. Buah yang terlalu halus atau mulus mungkin belum matang. Pilih markisa yang terasa berat untuk ukurannya, karena ini menunjukkan bahwa buah tersebut mengandung banyak air dan rasa yang lebih manis. Markisa matang akan mengeluarkan aroma harum yang kuat"},
    
    







}

st.sidebar.title('Informasi Tambahan')
buah_info = st.sidebar.selectbox('Pilih Jus Buah', list(informasi_tambahan.keys()), format_func=lambda x: x.capitalize())

if buah_info and st.sidebar.checkbox('Tampilkan Informasi Tambahan'):
    st.sidebar.subheader('Manfaat Kesehatan:')
    st.sidebar.write(informasi_tambahan[buah_info]['manfaat'])
    st.sidebar.subheader('Cara Memilih Buah:')
    st.sidebar.write(informasi_tambahan[buah_info]['cara_memilih'])

kadargula_buah = {
    'Jus apel': {'kadar gula': 24, 'vitamin': {'Vitamin A': '3%', 'Vitamin C': '14%'}},
    'Jus pisang': {'kadar gula': 24, 'vitamin': {'Vitamin B6': '20%', 'Vitamin C': '14%'}},
    'Jus jeruk': {'kadar gula': 21, 'vitamin': {'Vitamin C': '90%'}},
    'Jus pir': {'kadar gula': 12, 'vitamin': {'Vitamin C': '7%'}},
    'Jus strawberry': {'kadar gula': 13, 'vitamin': {'Vitamin C': '98%'}},
    'Jus semangka': {'kadar gula': 9, 'vitamin': {'Vitamin A': '11%', 'Vitamin C': '13%'}},
    'Jus mangga': {'kadar gula': 30, 'vitamin': {'Vitamin A': '25%', 'Vitamin C': '76%'}},
    'Jus alpukat': {'kadar gula': 2, 'vitamin': {'Vitamin K': '26%', 'Vitamin E': '14%'}},
    'Jus kiwi': {'kadar gula': 20, 'vitamin': {'Vitamin C': '112%', 'Vitamin K': '38%'}},
    'Jus melon': {'kadar gula': 12, 'vitamin': {'Vitamin A': '12%', 'Vitamin C': '61%'}},
    'Jus buah naga': {'kadar gula': 15, 'vitamin': {'Vitamin C': '9%', 'Vitamin B3': '8%'}},
    'Jus sirsak': {'kadar gula': 12, 'vitamin': {'Vitamin C': '24%', 'Vitamin B6': '5%'}},
    'Jus tomat': {'kadar gula': 7, 'vitamin': {'Vitamin C': '15%', 'Vitamin A': '28%'}},
    'Jus pepaya': {'kadar gula': 36, 'vitamin': {'Vitamin C': '67%', 'Vitamin A': '19%'}},
    'Jus lemon': {'kadar gula': 6, 'vitamin': {'Vitamin C': '59%'}},
    'Jus blueberry': {'kadar gula': 35, 'vitamin': {'Vitamin C': '11%', 'Vitamin A': '1%'}},
    'Jus nanas': {'kadar gula': 30, 'vitamin': {'Vitamin C': '80%', 'Vitamin B1': '7%'}},
    'Jus markisa': {'kadar gula': 30, 'vitamin': {'Vitamin C': '33%', 'Vitamin A': '7%'}},
}

# Mengubah urutan judul dan kalkulator
st.markdown("<div class='kalkulator-area'>", unsafe_allow_html=True)
st.markdown("<h2 style='color: white; text-align:center;'>🥭Menghitung Kadar Gula dalam Jus Buah</h2>", unsafe_allow_html=True)
st.write("Pilih buah favorit Anda untuk melihat kadar gula dalam 250mL jus.")
buah = st.selectbox('Pilih Buah', list(kadargula_buah.keys()), format_func=lambda x: x.capitalize())

if st.button('Hitung Kadar Gula'):
    kadargula_total = kadargula_buah[buah]['kadar gula']
    st.success(f"Jumlah kadar gula dalam 250mL {buah.lower()} adalah: {kadargula_total} gram")
    st.write("Kandungan Vitamin:")
    for vitamin, nilai in kadargula_buah[buah]['vitamin'].items():
        st.write(f"- {vitamin}: {nilai}")
st.markdown("</div>", unsafe_allow_html=True)
