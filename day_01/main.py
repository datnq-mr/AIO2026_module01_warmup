#Link đã triển khai: https://aio2026module01warmup-datnq.streamlit.app/
import streamlit as st
import pandas as pd

'''[Streamlit](https://streamlit.io/) là một framework mã nguồn mở dành cho Python, 
cho phép bạn xây dựng các ứng dụng web tương tác mà 
không cần phải tìm hiểu sâu về HTML, CSS hay JavaScript.
'''
# Các câu lệnh để hiển thị
st.title("I am title! ")
st.header("I am Header")
st.subheader("I'm sub header. It's so hot outside")
st.text('Hi I am text function and programers uses me inplace of paragraph tag')

# Nhập vào số mũ
so_mu = st.number_input("Nhập vào số mũ: ")

if st.button("Tính"):
    ket_qua = co_so ** so_mu
    st.success(f"Kết quả: {co_so} ^ {so_mu} = {ket_qua}")