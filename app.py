import streamlit as st
import numpy as np
import plotly.express as px

st.title("ボタンで再描画：サイン波グラフ")

# スライダーで係数を選ぶ
factor = st.slider("係数", 0.1, 5.0, 1.0)

# ボタンが押されたときだけグラフを描画
if st.button("グラフを描画する"):
    x = np.linspace(0, 10, 100)
    y = np.sin(factor * x)

    fig = px.line(x=x, y=y, labels={"x": "X軸", "y": "Y軸"}, title=f"y = sin({factor} * x)")
    st.plotly_chart(fig)
else:
    st.write("ボタンを押すとグラフが表示されます。")
