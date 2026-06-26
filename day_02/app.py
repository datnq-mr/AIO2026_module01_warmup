import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import io
from PIL import Image

# hàm tính trung bình
def calculate_average(scrores):
    return sum(scrores) / len(scrores)

# hàm phân loại điểm số
def percentage_distribution(scores):
    bins = {
        '90 - 100': 0,
        '80 - 89': 0,
        '70 - 79': 0,
        '60 - 69': 0,
        '< 60': 0
    }
    for score in scores:
        if score >= 90:
            bins['90 - 100'] +=1
        elif score >= 80:
            bins['80 - 89'] += 1
        elif score >= 70:
            bins['70 - 79'] += 1
        elif score >= 60:
            bins['60 - 69'] += 1
        else:
            bins['< 60'] += 1
    return bins

if __name__ == '__main__':
    # tiêu đề
    st.title("Phân tích dữ liệu điểm số học sinh")

    # Upload file
    # Nếu không có cột điểm số hoặc tên cột sai (phân biệt chữ hoa thường) sẽ bị lỗi
    uploaded_file = st.file_uploader("Chọn file excel (có cột 'Điểm số')", type=['xlsx'])

    # khi có file
    if uploaded_file:

        # Đọc file Excel thành DataFrame để Python có thể xử lý dữ liệu dạng bảng.
        df = pd.read_excel(uploaded_file)

        # 1. Chọn cột điểm số
        # 2. Loại bỏ các dòng có dữ liệu bị khuyết, bị trống hoặc mang giá trị NaN(not a number)
        # 3. chuyển dữ liệu sang kiểu float
        # 4. Chuyển đổi cấu trúc dữ liệu từ dạng Series của Pandas về dạng danh sách list
        scores = df['Điểm số'].dropna().astype(float).tolist()

        # phân tích điểm số
        if scores:
            # đếm tổng số học sinh và điểm trung bình dựa trên hàm tính trung bình đã được thiết lập ở trên
            st.write("Tổng số học sinh: ", len(scores), "Điểm trung bình:", round(calculate_average(scores), 2))

            # phân loại điểm
            # tạo một dictionary bằng hàm percentage_distribution đã code ở trên
            dist = percentage_distribution(scores)

            # tạo danh sách nhãn và giá trị để vẽ biểu đồ
            labels = list(dist.keys())
            values = list(dist.values())

            # vẽ hình
            # chuẩn bị một frame có kích thước (1x1 inch) để vẽ biểu đồ
            # fig: lớp nền bao quanh biểu đồ
            # ax: hệ trục tọa độ
            fig, ax = plt.subplots(figsize=(1,1))
            '''
            Matplotlib sẽ tự động cộng tổng tất cả các giá trị value trong dict phân loại điểm, 
            sau đó tính toán xem mỗi giá trị chiếm bao nhiêu phần trăm tổng thể để chia góc cho từng "miếng bánh" tương ứng
            '''
            ax.pie(
                values,             # số lượng điểm số của từng khoảng, lấy từ danh sách value của dict phân loại điểm
                labels=labels,      # nhãn dán lấy từ danh sách key của dict phân loại điểm
                autopct='%1.1f%%',  # %1.1f: Hiển thị số thực với 1 chữ số thập phân sau dấu phẩy, %% in ra dấu phần trăm (%)
                textprops={'fontsize': 3.5},    # cấu hình font chữ cho các văn bản hiển thị trên biểu đồ
            )
            ax.axis('equal')        # cố định tỷ lệ thiết lập của hai trục tọa độ ($x$ và $y$) bằng nhau
            plt.tight_layout(pad=0.1)


            # Lưu biểu đồ trực tiếp vào bộ nhớ RAM dưới dạng dữ liệu nhị phân (Binary Data) chứ không ghi thành một file cứng trên ổ đĩa
            buf = io.BytesIO()
            #Xuất và lưu hình ảnh của biểu đồ (fig) vào "file ảo" buf vừa tạo
            fig.savefig(buf, format='png', dpi=300)
            # Đặt lại con trỏ đọc/ghi (file pointer) về vị trí xuất phát đầu tiên (vị trí số 0) của file ảo, vì sau khi ghi xong, con trỏ nằm ở cuối file
            buf.seek(0)
            # st.markdown("Biểu đồ phân bố điểm số")
            img = Image.open(buf)

            # tạo ba cột với tỷ lệ [1, 2, 1], trong đó cột giữa có độ rộng lớn hơn để chứa biểu đồ
            col1, col2, col3 = st.columns([1,2,1])

            # sử dụng with col2: để đặt biểu đồ vào cột giữa, đảm bảo nội dung được căn giữa giao diện
            with col2:
                st.image(img, width=300)
                st.markdown("Biểu đồ phân bố điểm số.")