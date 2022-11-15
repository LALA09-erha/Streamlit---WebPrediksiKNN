# import libary 
import streamlit as st
import knn
import time

# pige title
st.set_page_config(
    page_title="Klasifikasi Penyakit Jantung",
    page_icon="https://e7.pngegg.com/pngimages/594/747/png-clipart-heart-heart-cartoon-heart.png",
)

    # 0 = tidak ada penyakit jantung
    # 1 = ada penyakit jantung

# hide menu
hide_streamlit_style = """



<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 






# insialisasi web
kolom = st.columns((2, 0.48, 2.7))
home = kolom[1].button('Home')
about = kolom[2].button('About')

# home page
if home==False and about==False or home==True and about==False:
    st.markdown("<h1 style='text-align: center; color: white; margin:0 ; padding:0;'>Klasifikasi Penyakit Jantung</h1>", unsafe_allow_html=True)
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
                st.success("Hasil Klasifikasi : "+nama+" Tidak Ada Penyakit Jantung")
            else:
                time.sleep(1)
                st.warning("Hasil Klasifikasi : "+nama+" Ada Penyakit Jantung")

# about page
if about==True and home==False:
    st.markdown("<h1 style='text-align: center; color: white; margin:0 ; padding:0;'>Tentang Sistem ini</h1>", unsafe_allow_html=True)
    st.write('Sistem Klasifikasi Penyakit Jantung adalah sebuah sistem yang bertujuan untuk mengklasifikasikan penyakit jantung dini. Sistem ini dibuat menggunakan bahasa pemrograman python dan library streamlit.')
    st.markdown("<p  color: white;'>Pada sistem ini menggunakan model KNN ( <i>K-nearest neighbors algorithm</i> ) dengan parameter <b>K = 11</b> . Dataset yang digunakan memiliki <b>5 fitur</b> termasuk kelas.</p>", unsafe_allow_html=True)
    st.write('Alasan menggunakan model KNN dengan parameter k = 11 adalah karena memiliki akurasi yang terbesar dari model lainnya pada dataset ini, sehingga diputuskan untuk menggunakan model tersebut. Sebelumnya sudah dilakukan dua analisa dan percobaan untuk model lainnya, lebih lengkapnya pada link dibawah.')
    st.markdown("<p> <a class='text-warning' target='_blank' href='https://lala09-erha.github.io/datamining/notebooks8.html'>Percobaan model pertama</a> | <a target='_blank' class='text-warning' href='https://lala09-erha.github.io/datamining/notebooks10.html'>Percobaan model kedua</a></p>", unsafe_allow_html=True)
    

        

            





