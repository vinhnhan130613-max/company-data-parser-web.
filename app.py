import streamlit as st
from main import process_data

st.title("Company Data Parser")

st.write("Nhập dữ liệu công ty để chuẩn hóa và dịch sang tiếng Anh:")

raw_name = st.text_input("Tên công ty (VD: Công Ty TNHH Xây Dựng Minh Khang)")
raw_address = st.text_input("Địa chỉ (VD: Đường Lê Lợi, Thôn Đông, Xã Đại Lãnh, Huyện Vạn Ninh, Tỉnh Khánh Hòa)")
phone = st.text_input("Số điện thoại (VD: 0905123456)")
director = st.text_input("Tên người đại diện (VD: Nguyễn Văn A)")

if st.button("Xử lý dữ liệu"):
    if raw_name and raw_address and phone and director:
        result = process_data(raw_name, raw_address, phone, director)
        st.subheader("Kết quả")
        for k, v in result.items():
            st.write(f"**{k}**: {v}")
    else:
        st.warning("Vui lòng nhập đầy đủ thông tin trước khi xử lý.")
