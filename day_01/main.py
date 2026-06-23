import streamlit as st

# Tiêu đề của trang
st.title("Tính lũy thừa")

# Nhập vào cơ số
co_so = st.number_input("Nhập vào cơ số: ")

# Nhập vào số mũ
so_mu = st.number_input("Nhập vào số mũ: ")

if st.button("Tính"):
    ket_qua = co_so ** so_mu
    st.success(f"Kết quả: {co_so} ^ {so_mu} = {ket_qua}")