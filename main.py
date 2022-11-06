# import libary 
import streamlit as st
import knn
import time

# pige title
st.set_page_config(
   page_title="Prediksi Penyakit Jantung",
    page_icon=":dolphin:",
)


# hide menu
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 


# insialisasi web
st.markdown("<h1 style='text-align: center; color: white; margin:0 ; padding:0;'>Prediksi Penyakit Jantung</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: white;'>Harap Diisi Semua Kolom</p>", unsafe_allow_html=True)


 # 0 = tidak ada penyakit jantung
 # 1 = ada penyakit jantung
if __name__ == "__main__":

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
                    st.success("Hasil Prediksi : Tidak Ada Penyakit Jantung")
                else:
                    time.sleep(1)
                    st.warning("Hasil Prediksi : Ada Penyakit Jantung")
        

            





