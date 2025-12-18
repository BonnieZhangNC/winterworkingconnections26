Chris Santo 12/18/2025 5:35 PM • import streamlit as st
import numpy as np

with st.chat_message("assistant"):
  st.write("Hello human")
  st.bar_chart(np.random.randn(30, 3))
