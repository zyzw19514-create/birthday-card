import streamlit as st

st.set_page_config(page_title="Birthday Surprise 🎁", page_icon="🎂", layout="centered")

PASSWORD = "happybirthday"

# ---------- CSS ----------
st.markdown("""
<style>

body {
    background: linear-gradient(135deg, #fff7d6, #ffe4f0);
    font-family: Arial;
}

/* envelope */
.envelope {
    width: 280px;
    height: 180px;
    margin: auto;
    background: #ff4d88;
    border-radius: 12px;
    position: relative;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    cursor: pointer;
    animation: pop 1s ease-in-out;
}

.envelope:before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 0;
    height: 0;
    border-left: 140px solid transparent;
    border-right: 140px solid transparent;
    border-top: 90px solid #ff6fa5;
}

/* animation */
@keyframes pop {
    from {transform: scale(0.7); opacity: 0;}
    to {transform: scale(1); opacity: 1;}
}

/* card */
.card {
    background: white;
    padding: 35px;
    border-radius: 20px;
    box-shadow: 0px 10px 30px rgba(0,0,0,0.15);
    text-align: center;
    animation: fade 1.2s ease-in-out;
}

@keyframes fade {
    from {opacity: 0; transform: translateY(20px);}
    to {opacity: 1; transform: translateY(0);}
}

h1 {
    color: #ff4d88;
}

p {
    font-size: 18px;
    line-height: 2;
    color: #222;
}

</style>
""", unsafe_allow_html=True)

# ---------- SESSION ----------
if "open" not in st.session_state:
    st.session_state.open = False

# ---------- PASSWORD ----------
if not st.session_state.open:
    st.title("🔒 Enter Password")

    password = st.text_input("Password", type="password")

    if st.button("Open Your Gift 🎁"):
        if password == PASSWORD:
            st.session_state.open = True
            st.rerun()
        else:
            st.error("Wrong password 😢")

# ---------- VIEW MODE ----------
else:

    st.markdown("""
    <div class="envelope"></div>
    """, unsafe_allow_html=True)

    st.markdown("## 💌 Opening your gift... 🎁")
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
