# import libary 
import streamlit as st
import knn
import time
import webbrowser
# pige title
st.set_page_config(
    page_title="Prediksi Penyakit Jantung",
    page_icon="https://e7.pngegg.com/pngimages/594/747/png-clipart-heart-heart-cartoon-heart.png",
)

    # 0 = tidak ada penyakit jantung
    # 1 = ada penyakit jantung

# hide menu
hide_streamlit_style = """



<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>

"""
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.4.0/css/font-awesome.min.css">', unsafe_allow_html=True)
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
st.markdown(' <div style="position: fixed; top: 0; left: 0; z-index: 9999; width: 100%; background: rgb(14, 17, 23); ; text-align: center;"><a href="https://github.com/LALA09-erha/Streamlit---WebPrediksiKNN" target="_blank"><button style="border-radius: 12px;position: relative; top:50%; margin:10px;"><i class="fa fa-github"></i> Source Code</button></a><a href="https://lala09-erha.github.io/datamining/intro.html" target="_blank"><button  style="border-radius: 12px;position: relative; top:50%;"><i style="color: orange" class="fa fa-book"></i> Jupyter Book</button></a></div>', unsafe_allow_html=True)





# insialisasi web
st.markdown("<p style='text-align: center; color: white; margin:0 ; padding:0;'>MENU</p>", unsafe_allow_html=True)
kolom = st.columns((2.2, 0.48, 2.7))
home = kolom[1].button('🏠')
about = kolom[2].button('📰')

# home page
if home==False and about==False or home==True and about==False:
    st.markdown("<h1 style='text-align: center; color: white; margin:0 ; padding:0;'>Prediksi Penyakit Jantung</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: white;'>Harap Diisi Semua Kolom</p>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        nama = st.text_input("Masukkan Nama",placeholder='Nama')
    with col2:
        umur = st.number_input("Masukkan Umur",max_value=100)
    jk = st.selectbox("Jenis Kelamin",('Laki-laki','Perempuan'))
    col3,col4 = st.columns(2)
    with col3:
        bp = st.number_input("Tekanan Darah",min_value=0,max_value=1000)
    with col4:
        chol = st.number_input("Kadar Kolesterol",min_value=0,max_value=1000)
    #    Centering Butoon 
    columns = st.columns((2, 0.6, 2))
    sumbit = columns[1].button("Submit")
    if sumbit and nama != '' and jk != '' and bp != 0 and chol != 0 and umur != 0:
        # cek jenis kelamin
        #0 = laki-laki
        #1 = perempuan
        if jk == 'Laki-laki':
            jk = 0
        else:
            jk = 1
        # normalisasi data
        data = knn.normalisasi([umur,jk,bp,chol])
        # prediksi data
        prediksi = knn.knn(data)
        # cek prediksi
        with st.spinner("Tunggu Sebentar Masih Proses..."):
            if prediksi[-1] == 0:
                time.sleep(1)
                st.success("Hasil Prediksi : "+nama+" Tidak Ada Penyakit Jantung")
            else:
                time.sleep(1)
                st.warning("Hasil Prediksi : "+nama+" Ada Penyakit Jantung")

# about page
if about==True and home==False:
    url = 'https://www.kaggle.com/datasets/shrutipandit707/heartdisease'
    n8 = 'https://lala09-erha.github.io/datamining/notebooks8.html'
    n9 = 'https://lala09-erha.github.io/datamining/notebooks9.html'
    st.markdown("<h2 style='text-align: center; color: white; margin:0 ; padding:0;'>Tentang Sistem ini</h2>", unsafe_allow_html=True)
    st.write('Sistem Prediksi Penyakit Jantung adalah sebuah sistem yang bertujuan untuk memprediksi penyakit jantung dini. Sistem ini dibuat menggunakan bahasa pemrograman python dan library streamlit.')
    st.markdown("<p  color: white;'>Dataset yang digunakan pada sistem ini memiliki <b>5 fitur</b> termasuk kelas, Dataset yang digunakan dalam sistem ini menggunakan data yang didapatkan melalui repository dataset yang berada pada website Kaggle.com . Dataset yang berjudul <i>Heart Disease</i>, dataset untuk mendeteksi apakah seseorang mengidap Penyakit Jantung atau tidak berdasarkan berbagai faktor seperti <i>cholestrol</i>,<i>blood pressure</i>,<i>sex</i>,<i>age</i>. Lebih lengkapnya pada link dibawah.</p>", unsafe_allow_html=True)
    st.info("Dataset : [link](%s)" % url,icon="ℹ️")
    st.markdown("<p  color: white;'>Pada sistem ini menggunakan model KNN ( <i>K-nearest neighbors algorithm</i> ) dengan parameter <b>K = 11</b> .</p>", unsafe_allow_html=True)
    st.write('Alasan menggunakan model KNN dengan parameter k = 11 adalah karena memiliki akurasi yang terbesar dari model lainnya pada dataset ini, sehingga diputuskan untuk menggunakan model tersebut. Sebelumnya sudah dilakukan dua analisa dan percobaan untuk model lainnya, lebih lengkapnya pada link dibawah.')
    st.info("[Percobaan model pertama](%s) | [Percobaan model Kedua](%s)" % (n8,n9),icon="ℹ️")        