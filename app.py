import streamlit as st
from PIL import Image

st.title("きーちゃんのプロフィール")

# 横並びにする: 左に説明、右に写真
col1, col2 = st.columns([2, 1])
with col1:
    with st.container(border=True):
        st.write("名前: きーちゃん")
        st.write("性別: オス")
        st.write("犬種: キャバリア・キング・チャールズ・スパニエル")
        st.write("誕生日: 2014年2月8日")
        st.write("年齢: 11歳")
        st.write("体重: 7.5kg")
        st.write("好きな食べ物: 肉")
        st.write("好きな遊び: 骨のおもちゃで遊ぶこと")
        st.write("性格: 食べることと寝ることが大好き")
        st.write("一言: キャバリアが集まる保護犬団体から来ました。今は家族の一員として幸せに暮らしています。")
        

with col2:
    images = [
        ("imgs/osuwari.jpg", "おすわり中のきーちゃん", -90),
        ("imgs/getting_clothing.jpg", "ソファで寝ているきーちゃん", 0),
        ("imgs/sleeping.jpg", "寝ているきーちゃん", -90),
        ("imgs/smiling.jpg", "笑っているきーちゃん", 0),
        ("imgs/standing.jpg", "立っているきーちゃん", -90),
    ]

    if "img_idx" not in st.session_state:
        st.session_state.img_idx = 0
    n = len(images)
    
    idx = st.session_state.img_idx
    img_path, caption, rotate = images[idx]
    img = Image.open(img_path)
    if rotate:
        img = img.rotate(rotate, expand=True)
    st.image(img, caption=f"{caption} ({idx+1}/{n})", use_container_width=True)

    prev_col, next_col = st.columns(2)
    with prev_col:
        if st.button("◀ 前へ", use_container_width=True):
            st.session_state.img_idx = (st.session_state.img_idx - 1) % n
            st.rerun()
    with next_col:
        if st.button("次へ ▶", use_container_width=True):
            st.session_state.img_idx = (st.session_state.img_idx + 1) % n
            st.rerun()

    