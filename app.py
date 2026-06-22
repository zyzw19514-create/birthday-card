import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="For Jannah ❤️", page_icon="🐣", layout="centered")

PASSWORD = "love" # الباسورد

# ---------- CSS للتصميم ----------
st.markdown("""
<style>
.stApp { background-color: #fcf4f2; }

/* تصميم الظرف */
.envelope-box {
    background: white;
    width: 320px;
    height: 220px;
    margin: 20px auto;
    border-radius: 15px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    border: 2px solid #f8e1e7;
}
.seal {
    width: 60px;
    height: 60px;
    background: #ff4d6d;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-size: 30px;
    margin-bottom: 10px;
}
.text-style {
    font-size: 22px !important;
    line-height: 1.8 !important;
    color: #444;
    font-family: sans-serif;
    text-align: center;
    padding: 20px;
}
</style>
""", unsafe_allow_html=True)

# ---------- المنطق ----------
if "open" not in st.session_state:
    st.session_state.open = False

if not st.session_state.open:
    # واجهة الظرف
    st.markdown('<div style="text-align:center"><h1>LOVE</h1><p>my everything ❤️</p></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="envelope-box">
        <div class="seal">💌</div>
        <p>ENTER THE SECRET WORD</p>
    </div>
    """, unsafe_allow_html=True)
    
    password = st.text_input("", type="password")
    if st.button("Unlock 🔓"):
        if password == PASSWORD:
            st.session_state.open = True
            st.rerun()
        else:
            st.error("Wrong word!")

else:
    # محتوى الهدية بعد الفتح
    st.balloons()
    
    # حط هنا صورك (تأكد إن الصور مرفوعة على GitHub في نفس الفولدر)
    # st.image("pic1.jpg", use_column_width=True) 
    
    st.markdown('<div class="text-style">', unsafe_allow_html=True)
    
    st.write("النهاردة إنتي كبرتي سنة، بس كل سنة بتمر بتزودك جمال في عيني وقرب في قلبي أكتر من اللي قبلها.")
    st.write("كل سنة وإنتي طيبة ❤️")
    st.write("وجودك مش بس حلى أيامي، ده خلاني أعرف يعني إيه أحب بجد وأحس إن قلبي مبسوط ومكتفي بيكي.")
    st.write("معاكي ببقى على طبيعتي من غير أي حسابات.. وعقبال عمر بحاله نعيشه سوا وإيدي في إيدك ✨")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # st.image("pic2.jpg", use_column_width=True)
