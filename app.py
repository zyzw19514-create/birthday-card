import streamlit as st

st.set_page_config(page_title="Birthday Surprise 🎉", page_icon="🐣", layout="centered")

PASSWORD = "happybirthday"

# ---------- CSS ----------
st.markdown("""
<style>

body {
    background: linear-gradient(135deg, #fff7d6, #ffe4f0);
}

/* floating emojis */
.emoji {
    position: fixed;
    font-size: 28px;
    opacity: 0.5;
    animation: float 10s infinite linear;
}

@keyframes float {
    0% {transform: translateY(100vh);}
    100% {transform: translateY(-10vh);}
}

/* card */
.card {
    background: white;
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0px 10px 30px rgba(0,0,0,0.1);
    text-align: center;
    color: #222;
}

/* مهم جدًا عشان النص يظهر */
p {
    color: #222 !important;
    font-size: 16px;
    line-height: 1.8;
}

h1, h2, h3 {
    color: #ff4d88 !important;
}

button {
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)

# ---------- floating chicks ----------
st.markdown("""
<div class="emoji" style="left:10%">🐣</div>
<div class="emoji" style="left:25%; animation-delay:2s;">🐤</div>
<div class="emoji" style="left:40%; animation-delay:4s;">🐣</div>
<div class="emoji" style="left:60%; animation-delay:1s;">🐤</div>
<div class="emoji" style="left:80%; animation-delay:3s;">🐣</div>
""", unsafe_allow_html=True)

# ---------- session ----------
if "open" not in st.session_state:
    st.session_state.open = False

# ---------- LOGIN ----------
if not st.session_state.open:
    st.title("🔒 Enter Password")

    password = st.text_input("Password", type="password")

    if st.button("Open Your Gift 🎁"):
        if password == PASSWORD:
            st.session_state.open = True
            st.rerun()
        else:
            st.error("Wrong password 😢")

# ---------- CARD ----------
else:
    st.balloons()

    st.markdown("""
    <div class="card">

    <h1>🎉 HAPPY BIRTHDAY 🎉</h1>

    <h3>أهلاً بالكتكوتة اللي كبرت سنة ❤️🐣</h3>

    <br>

    <p>
    كل سنة وإنتي طيبة ❤️<br><br>

    النهاردة يوم مميز عشان إنتي فيه، واللي زيك صعب يتكرر أو يتنسى.<br><br>

    وجودك بيخلي أي يوم عادي يبقى أحلى من غير مجهود.<br>
    ضحكتك وكلامك وبساطتك بيخلو أي لحظة معاكي مختلفة 💖<br><br>

    وبحب هزارنا سوا 😂 وبحب إنك دايمًا خفيفة ولطيفة.<br><br>

    فيكي حاجة مميزة جدًا… إنك طبيعية جدًا، وده أكتر حاجة مخليكي مختلفة في عيني.<br><br>

    بدعي ربنا يفرح قلبك دايمًا ويحققلك كل اللي نفسك فيه ❤️<br><br>

    كل سنة وإنتي منورة حياتي ❤️✨
    </p>

    </div>
    """, unsafe_allow_html=True)
