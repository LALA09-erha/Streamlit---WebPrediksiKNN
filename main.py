# import libary 
import streamlit as st
import metode
import time


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
about = kolom[2].button('About')

# home page
if home==False and about==False or home==True and about==False:
    st.markdown("<h1 style='text-align: center; color: white; margin:0 ; padding:0;'>Prediksi Penyakit Jantung</h1>", unsafe_allow_html=True)
    # setting kolom
    with st.expander("Setting"):

        preprosesing = st.radio('Preprocessing Data', options=['Normalization (Min-Max)', 'Normal'], index=0, horizontal=True)
        st.markdown("""---""")
        st.write("""Metode Klasfikasi""")

        model_1 = st.checkbox('K-Nearest Neighbors (K=11) ', value=True)
        model_2 = st.checkbox('Bagging Clasifier (Gaussian) ')
        model_3 = st.checkbox('Random Forest')

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
    if sumbit == True:

        if  nama != '' and jk != '' and bp != 0 and chol != 0 and umur != 0:
            if model_1 or model_2 or model_3:
                if preprosesing == 'Normalization (Min-Max)':
                    # cek jenis kelamin
                    #1 = laki-laki
                    #0 = perempuan
                    if jk == 'Laki-laki':
                        jk = 0
                    else:
                        jk = 1
                    # normalisasi data
                    data = metode.normalisasi([umur,jk,bp,chol])
                    # prediksi data
                    if model_1:
                        prediksi = metode.knn(data)
                        # cek prediksi
                        with st.spinner("Tunggu Sebentar Masih Proses..."):
                            if prediksi[-1] == 0:
                                time.sleep(1)
                                st.success("Hasil Prediksi Metode KNN: "+nama+" Tidak Ada Penyakit Jantung")
                            else:
                                time.sleep(1)
                                st.warning("Hasil Prediksi Metode KNN: "+nama+" Ada Penyakit Jantung")
                    if model_2:
                        prediksi = metode.bagging(data)
                        # cek prediksi
                        with st.spinner("Tunggu Sebentar Masih Proses..."):
                            if prediksi[-1] == 0:
                                time.sleep(1)
                                st.success("Hasil Prediksi Metode Bagging: "+nama+" Tidak Ada Penyakit Jantung")
                            else:
                                time.sleep(1)
                                st.warning("Hasil Prediksi Metode Bagging: "+nama+" Ada Penyakit Jantung")
                    if model_3:
                        prediksi = metode.randomforest(data)
                        # cek prediksi
                        with st.spinner("Tunggu Sebentar Masih Proses..."):
                            if prediksi[-1] == 0:
                                time.sleep(1)
                                st.success("Hasil Prediksi Metode Random Forest: "+nama+" Tidak Ada Penyakit Jantung")
                            else:
                                time.sleep(1)
                                st.warning("Hasil Prediksi Metode Random Forest: "+nama+" Ada Penyakit Jantung")
                else:
                    # cek jenis kelamin
                    #1 = laki-laki
                    #0 = perempuan
                    if jk == 'Laki-laki':
                        jk = 1
                    else:
                        jk = 0
                    # normalisasi data
                    data = metode.normal([umur,jk,bp,chol])
                    # prediksi data
                    if model_1:
                        prediksi = metode.knn_no_norm(data)
                        # cek prediksi
                        with st.spinner("Tunggu Sebentar Masih Proses..."):
                            if prediksi[-1] == 0:
                                time.sleep(1)
                                st.success("Hasil Prediksi Metode KNN: "+nama+" Tidak Ada Penyakit Jantung")
                            else:
                                time.sleep(1)
                                st.warning("Hasil Prediksi Metode KNN: "+nama+" Ada Penyakit Jantung")
                    if model_2:
                        prediksi = metode.bagging_no_norm(data)
                        # cek prediksi
                        with st.spinner("Tunggu Sebentar Masih Proses..."):
                            if prediksi[-1] == 0:
                                time.sleep(1)
                                st.success("Hasil Prediksi Metode Bagging: "+nama+" Tidak Ada Penyakit Jantung")
                            else:
                                time.sleep(1)
                                st.warning("Hasil Prediksi Metode Bagging: "+nama+" Ada Penyakit Jantung")
                    if model_3:
                        prediksi = metode.randomforest_no_norm(data)
                        # cek prediksi
                        with st.spinner("Tunggu Sebentar Masih Proses..."):
                            if prediksi[-1] == 0:
                                time.sleep(1)
                                st.success("Hasil Prediksi Metode Random Forest: "+nama+" Tidak Ada Penyakit Jantung")
                            else:
                                time.sleep(1)
                                st.warning("Hasil Prediksi Metode Random Forest: "+nama+" Ada Penyakit Jantung")
            else:
                st.error("Pilih Salah Satu Metode")
        else:
            st.error("Harap Diisi Semua Kolom")

# about page
if about==True and home==False:
    url = 'https://www.kaggle.com/datasets/shrutipandit707/heartdisease'
    n8 = 'https://lala09-erha.github.io/datamining/notebooks8.html'
    n9 = 'https://lala09-erha.github.io/datamining/notebooks10.html'
    s8 = 'https://lala09-erha.github.io/datamining/Salinan8.html'
    s10 = 'https://lala09-erha.github.io/datamining/Salinan10.html'
    st.markdown("<h2 style='text-align: center; color: white; margin:0 ; padding:0;'>Tentang Sistem ini</h2>", unsafe_allow_html=True)
    st.write('Sistem Prediksi Penyakit Jantung adalah sebuah sistem yang bertujuan untuk memprediksi penyakit jantung dini. Sistem ini dibuat menggunakan bahasa pemrograman python dan library streamlit.')
    st.markdown("<h4 style='text-align: center; color: white; margin:0 ; padding:0;'>Dataset</h4>", unsafe_allow_html=True)
    st.markdown("<p  color: white;'>Dataset yang digunakan pada sistem ini memiliki <b>5 fitur</b> termasuk kelas, Dataset yang digunakan dalam sistem ini menggunakan data yang didapatkan melalui repository dataset yang berada pada website Kaggle.com . Dataset yang berjudul <i>Heart Disease</i>, dataset untuk mendeteksi apakah seseorang mengidap Penyakit Jantung atau tidak berdasarkan berbagai faktor seperti <i>cholestrol</i> (mg/dL),<i>blood pressure</i> (mm Hg),<i>sex</i> (female/male),<i>age</i>,class (0/1), semua fitur yang disebutkan bertipe numerik.</p>", unsafe_allow_html=True)
    st.write('Untuk Fitur kolestrol bisa didapatkan dengan cara mengecek ke dokter atau dengan cara mengukur sendiri dengan menggunakan alat yang disediakan oleh dokter. Untuk fitur blood pressure bisa didapatkan dengan cara mengecek ke dokter atau dengan cara mengukur sendiri dengan menggunakan alat yang disediakan oleh dokter.')
    st.info("Dataset : [link](%s)" % url,icon="ℹ️")
    st.markdown("<h4 style='text-align: center; color: white; margin:0 ; padding:0;'>Tahap preprosessing</h4>", unsafe_allow_html=True)
    st.write('Sistem ini menggunakan preprosessing data yaitu dengan normalisasi data. Metode normalisasi yang digunakan adalah MinMaxScaler.')
    st.markdown("<h4 style='text-align: center; color: white; margin:0 ; padding:0;'>Metode yang digunakan</h4>", unsafe_allow_html=True)
    st.markdown("<p  color: white;'>Pada sistem ini menggunakan model KNN ( <i>K-nearest neighbors algorithm</i> ) dengan parameter <b>K = 11</b> dengan akurasi 75% jika sebelumnya data dinormalisasi terlebih dahulu, namun jika tanpa normalisasi akurasi yang didapat sebesar 70% .</p>", unsafe_allow_html=True)
    st.write('Selanjutnya memakai model Bagging Clasfifier dengan base_estimator = gaussianNB dan n_estimators = 6 dengan akurasi sebesar 77% jika sebelumnya data dinormalisasi terlebih dahulu, namun jika tanpa tanpa normalisasi data menggunakan n_estimators = 2 dengan akurasi sebesar 77%.')
    st.write('Terakhir memakai model Random Forest dengan n_estimators = 13 dengan akurasi sebesar 72% jika sebelumnya data dinormalisasi terlebih dahulu, namun jika tanpa tanpa normalisasi data menggunakan n_estimators = 14 dengan akurasi sebesar 72% juga.')
    st.markdown("<h4 style='text-align: center; color: white; margin:0 ; padding:0;'>Penjelasan Singkat</h4>", unsafe_allow_html=True)
    st.write('Ketiga metode tersebut ialah metode klasifikasi,alasan menggunakan ketiga model tersebut adalah karena memiliki akurasi yang terbesar dari model lainnya pada dataset ini, sehingga diputuskan untuk menggunakan model tersebut. Sebelumnya sudah dilakukan empat analisa dan percobaan untuk model lainnya dengan kondisi data yang tanpa menggunakan maupun menggunakan normalisasi sebelumnya, lebih lengkapnya pada link dibawah.')
    st.info("[Percobaan model pertama](%s) | [Percobaan model Kedua](%s) | [Percobaan model Ketiga](%s) | [Percobaan model Keempat](%s)" % (n8,n9,s8,s10),icon="ℹ️")        