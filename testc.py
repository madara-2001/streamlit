import streamlit as st
import random
from PIL import Image
import base64

with st.sidebar:
    st.text("请选择房间类型\n")
    type=st.selectbox(
        "none",
        ('普通房间','机房'),
        label_visibility="collapsed"
    )
    st.text("请输入房间尺寸\n")
    if st.button("随机生成房间尺寸"):
        length=random.uniform(5,20)
        width=length*random.uniform(0.7,1)
        height=random.uniform(2.5,5)
    else:
        length=st.slider("长",5.0,20.0)
        width=st.slider("长宽比",1.0,1.4)*length
        height=st.slider("高",2.5,5.0)

st.markdown("![Alt Text](https://i.postimg.cc/NfDC63Vq/test.gif)")
            
# file_ = open("C:/Users/terry/Downloads/f631910e7bec54e7fc8d5ddcfc389b504ec26a9a.gif", "rb")
# contents = file_.read()
# data_url = base64.b64encode(contents).decode("utf-8")
# file_.close()

# st.markdown(
#     f'<img src="data:image/gif;base64,{data_url}" alt="gif">',
#     unsafe_allow_html=True,
# )

