# 余振中 (Yu Chen Chung)
# app_streamlit.py
import streamlit as st
import requests
from PIL import Image
import io

## API_URL = "http://localhost:5000/process-image"
# 5/18新增
import os

# 從環境變數 API_ENDPOINT 讀，若沒設就回落到本機開發時的 localhost
API_URL = os.getenv("API_ENDPOINT", "http://localhost:5000/process-image")
# 5/18新增


st.title("圖像處理 API Demo")

uploaded = st.file_uploader("上傳圖片", type=["jpg","jpeg","png","gif"])
mode = st.selectbox("處理模式", [
    "grayscale", "resize", "edge",
    "blur", "sharpen", "rotate",
    "flip_horizontal", "flip_vertical", "invert_colors"
])
if st.button("開始處理"):
    if not uploaded:
        st.warning("請先上傳圖片")
    else:
        files = {"file": (uploaded.name, uploaded.getvalue())}
        data = {"mode": mode}
        try:
            resp = requests.post(API_URL, files=files, data=data)
            resp.raise_for_status()
            img = Image.open(io.BytesIO(resp.content))
            col1, col2 = st.columns(2)
            col1.image(uploaded, caption="原圖", use_container_width=True)
            col2.image(img, caption=f"處理：{mode}", use_container_width=True)

            # 提供下載
            buf = io.BytesIO()
            img_format = img.format or 'PNG'
            img.save(buf, format=img_format)
            st.download_button(
                label="下載處理後圖片",
                data=buf.getvalue(),
                file_name=f"result.{img_format.lower()}"
            )
        except Exception as e:
            st.error(f"處理失敗：{e}")