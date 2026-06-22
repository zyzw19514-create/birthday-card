import streamlit as st

st.set_page_config(page_title="Birthday Card 🎁", page_icon="🎂", layout="centered")

PASSWORD = "happybirthday"

# ---------- CSS ----------
st.markdown("""
<style>

body {
    background: linear-gradient(135deg, #fff7d6, #ffe4f0);
    font-family: Arial;
}

/* card before unlock */
.locked-card {
    background: white;
    padding: 40px;
    border-radius: 20px;
    box-shadow: 0px 10px 30px rgba(0,0,0,0.15);
    text-align: center;
    opacity: 0.7;
}

/* unlocked card */
.card {
    background: white;
    padding: 40px;
    border-radius: 20px;
    box-shadow: 0px 10px 30px rgba(0,0,0,0.15);
    text-align: center;
    animation: fade 1s ease-in-out;
}

@keyframes fade {
    from {opacity: 0; transform: scale(0.95);}
    to {opacity: 1; transform: scale(1);}
}

h1 { color: #ff4d88; }

p {
    font-size: 18px;
    line-height: 2;
    color: #222;
}

</style>
""", unsafe_allow_html=True)

# ---------- STATE ----------
if "unlocked" not in st.session_state:
    st.session_state.unlocked = False

# ---------- CARD ALWAYS SHOWN ----------
if not st.session_state.unlocked:

    st.markdown("""
    <div class="locked-card">
        <h1>🎁 Birthday Card</h1>
        <p>🔒 Enter password to open your gift</p>
    </div>
    """, unsafe_allow_html=True)

    password = st.text_input("Password", type="password")

    if st.button("Open 🎉"):
        if password == PASSWORD:
            st.session_state.unlocked = True
            st.rerun()
        else:
            st.error("Wrong password 😢")

# ---------- UNLOCKED VIEW ----------
else:
    st.balloons()

    st.markdown("""
    <div class="card">

    <h1>🎉 HAPPY BIRTHDAY 🎉</h1>

    <h3>أهلاً بالكتكوتة اللي كبرت سنة ❤️✨</h3>

    <p>

    أهلاً بالكتكوتة اللي كبرت سنة ❤️✨<br><br>

    النهاردة إنتي كبرتي سنة، بس كل سنة بتمر بتزودك جمال في عيني وقرب في قلبي أكتر من اللي قبلها.<br><br>

    كل سنة وإنتي طيبة ❤️<br><br>

    وجودك مش بس حلى أيامي، ده خلاني أعرف يعني إيه أحب بجد وأحس إن قلبي مبسوط ومكتفي بيكي، وإن يومي بيكمل بيكي.<br><br>

    معاكي ببقى على طبيعتي من غير أي حسابات، وبفك من أي ضغط لمجرد إني بكلمك أو أسمع صوتك.<br><br>

    فيكي تفاصيل بتخطف القلب.. ضحكتك، طريقتك في الكلام، وبساطتك اللي بتخلي أي حاجة حواليكي أهدى وأحلى.<br><br>

    وعارفة يا جنجون، أكتر حاجة بحبها فيكي إنك طبيعية جدًا، مفيكيش أي تصنع، وكل حاجة فيكي حقيقية وده اللي مخليكي مميزة بجد في عيني.<br><br>

    ولما بفضل أهزر وأناكف فيكي 😂 فده عشان بحب أشوف رياكشناتك وبحب أطلع الطفلة اللي جواكي.<br><br>

    وجودك في حياتي فرق كبير، حسسني إني أخدت نصيبي الحلو من الدنيا فيكي.<br><br>

    بدعي ربنا دايمًا إن السنة الجاية تكون أحلى ❤️<br><br>

    كل سنة وإنتي منورة حياتي ✨<br><br>

    عقبال عمر بحاله نعيشه سوا ❤️

    </p>

    </div>
    """, unsafe_allow_html=True)
