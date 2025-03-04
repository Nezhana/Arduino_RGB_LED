import streamlit as st
import websocket
import json

# Налаштування WebSocket
ARDUINO_IP = "ws://YOUR_ARDUINO_IP:81"

# Функція для відправки команд на Arduino
def send_command(command):
    ws = websocket.create_connection(ARDUINO_IP)
    ws.send(json.dumps(command))
    ws.close()

# Інтерфейс Streamlit
st.title("Керування RGB-світлодіодом")
st.write("Оберіть режим або налаштуйте власний колір:")

# Кнопки для режимів
if st.button("Кіно"):
    send_command({"mode": "movie"})
if st.button("Робота"):
    send_command({"mode": "work"})
if st.button("Відпочинок"):
    send_command({"mode": "relax"})

st.write("---")

# Слайдери для ручного налаштування кольору
st.write("Кастомний режим:")
r = st.slider("Червоний", 0, 255, 0)
g = st.slider("Зелений", 0, 255, 0)
b = st.slider("Синій", 0, 255, 0)

# Відправка кастомного кольору
if st.button("Застосувати колір"):
    send_command({"mode": "custom", "r": r, "g": g, "b": b})

# Вимкнення світлодіода
if st.button("Вимкнути"):
    send_command({"mode": "off"})
