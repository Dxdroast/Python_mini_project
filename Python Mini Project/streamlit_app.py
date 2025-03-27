import streamlit as st
import subprocess
import time

# --- PAGE CONFIG ---
st.set_page_config(page_title="Tic-Tac-Toe", page_icon="🎮", layout="wide")

# --- CUSTOM CSS FOR AESTHETICS ---
st.markdown(
    """
    <style>
        body {
            background-color: #0d1117;
            color: white;
            font-family: 'Poppins', sans-serif;
        }

        .glass-box {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            padding: 30px;
            text-align: center;
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            max-width: 500px;
            margin: auto;
            box-shadow: 0px 10px 30px rgba(255, 255, 255, 0.1);
            transition: transform 0.3s ease-in-out;
        }

        .glass-box:hover {
            transform: scale(1.02);
        }

        h1 {
            font-size: 40px;
            font-weight: 700;
            text-align: center;
            background: linear-gradient(90deg, #ff416c, #ff4b2b);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .stButton>button {
            background: linear-gradient(90deg, #00c6ff, #0072ff);
            color: white;
            font-size: 20px;
            font-weight: bold;
            padding: 12px 30px;
            border-radius: 50px;
            border: none;
            outline: none;
            cursor: pointer;
            transition: all 0.3s ease-in-out;
            box-shadow: 0px 4px 15px rgba(0, 198, 255, 0.5);
            display: block;
            margin: auto;
        }

        .stButton>button:hover {
            background: linear-gradient(90deg, #0072ff, #00c6ff);
            transform: scale(1.05);
            box-shadow: 0px 6px 25px rgba(0, 198, 255, 0.8);
        }

        .credits-box {
            background: rgba(255, 255, 255, 0.2);
            border-radius: 10px;
            padding: 10px;
            text-align: center;
            color: white;
            font-size: 16px;
            font-weight: bold;
            max-width: 400px;
            margin: 20px auto;
            box-shadow: 0px 5px 15px rgba(255, 255, 255, 0.1);
        }

        .info-box {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            padding: 15px;
            text-align: center;
            font-size: 18px;
            font-weight: bold;
            max-width: 500px;
            margin: auto;
            box-shadow: 0px 5px 15px rgba(255, 255, 255, 0.2);
        }

    </style>
    """,
    unsafe_allow_html=True
)

# --- GAME INSTRUCTIONS (TOP BOX) ---
st.markdown('<div class="info-box">🎮 Welcome to Tic-Tac-Toe! Play against your friend or test your skills against AI.</div>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# --- MAIN GAME SECTION ---
st.markdown('<div class="glass-box">', unsafe_allow_html=True)
st.markdown("<h1>🎮 Tic-Tac-Toe</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Click below to launch the game.</p>", unsafe_allow_html=True)

# Centered Button
if st.button("🚀 Start Game"):
    st.session_state["status"] = "Game is starting..."
    with st.spinner("Launching game..."):
        time.sleep(2)
    subprocess.Popen(["python", "game.py"])
    st.session_state["status"] = "Game is running!"

st.markdown('</div>', unsafe_allow_html=True)

# --- GAME STATUS (BOTTOM BOX) ---
if "status" not in st.session_state:
    st.session_state["status"] = "Waiting for player to start..."

st.markdown(f'<div class="info-box">{st.session_state["status"]}</div>', unsafe_allow_html=True)

# --- CREDITS SECTION ---
st.markdown('<div class="credits-box">🎨 Made by: Samim, Rudra & Saswata</div>', unsafe_allow_html=True)
