import streamlit as st
import math

st.title("Menghitung Volume Tabung", icon=":material/dashboard:")
r = st.number_input("Masukkan jari-jari (cm)")
t = st.number_input("Masukkan tinggi tabung (cm)")

if st.button("hasil volume tabung", type="float"):
  v = math.pi*(r**2*t)
  st.success(f"volume tabung adalah {v}cm")
  
  
