import streamlit as st
import numpy as np
import plotly.express as px

st.title("リアルタイムサイン波グラフ")

factor = st.slider("係数", 0.1, 5.0, 1.0)
x = np.linspace(0, 10, 100)
y = np.sin(factor * x)

fig = px.line(x=x, y=y, labels={"x": "X軸", "y": "Y軸"}, title="y = sin(factor * x)")
st.plotly_chart(fig)
