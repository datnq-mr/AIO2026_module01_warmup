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

#Streamlit có thể hỗ trợ markdown và latex
st.markdown('**Hello** *World*. This is the markdown')
st.markdown('-----')
st.caption('Hi I am Caption')
#Hiển thị dạng ma trận 2x2
st.latex(r'\begin{pmatrix}a&b\\c&d\end{pmatrix}')

#Hiển thị code ở trong 1 khung
code = '''
print('Hello World')
def funt():
    return 0
'''
st.code(code, language='python')
#--------------------------------------------------------------------------------------
st.write("## this is write function")
st.metric(label='Wind speed', value='120ms', delta='1.4ms')
#-------------------------------------------------------------------------------------------------------
#Hiển thị dạng table nhưng bằng 2 cách khác nhau
st.write('Khác nhau giữa table và dataframe là dataframe có thể sắp xếp')
table = pd.DataFrame({"Column 1": [1, 2, 3, 4, 5, 6, 7], "Column 2:": [11, 12, 13, 14, 15, 16, 17]})
st.table(table)
st.dataframe(table)

# Có thể dùng thể hiển thị các media: ảnh, video, audio
st.image("chim.webp", caption="This is my Image", width=680)