import streamlit as st

st.set_page_config(page_title="For Jannah ❤️", layout="centered")

PASSWORD = "love"

if "open" not in st.session_state:
    st.session_state.open = False

# الخلفية العامة للـ app
st.markdown("""
<style>
    .stApp { background-color: #fcf4f2; }
</style>
""", unsafe_allow_html=True)

if not st.session_state.open:
    # واجهة الظرف بشكل بسيط ومضمون
    st.markdown("""
    <div style="background:white; padding:40px; border-radius:20px; text-align:center; box-shadow:0px 5px 15px rgba(0,0,0,0.1);">
        <h1 style="color:#ff4d6d;">LOVE</h1>
        <p>My everything ❤️</p>
        <div style="font-size:50px;">💌</div>
    </div>
    """, unsafe_allow_html=True)
    
    password = st.text_input("اكتبي الباسورد:", type="password")
    if st.button("Unlock 🔓"):
        if password == PASSWORD:
            st.session_state.open = True
            st.rerun()
        else:
            st.error("الباسورد غلط!")

else:
    st.balloons()
    # الرسالة بخط واضح جداً ومن غير تعقيد
    st.markdown("""
    <div style="background:white; padding:40px; border-radius:20px; font-size:20px; line-height:1.6; color:#333;">
        <h2 style="color:#ff4d6d;">🎉 Happy Birthday!</h2>
        <p>النهاردة إنتي كبرتي سنة، بس كل سنة بتمر بتزودك جمال في عيني وقرب في قلبي أكتر من اللي قبلها.</p>
        <p>كل سنة وإنتي طيبة ❤️</p>
        <p>وجودك مش بس حلى أيامي، ده خلاني أعرف يعني إيه أحب بجد وأحس إن قلبي مبسوط ومكتفي بيكي.</p>
        <p>معاكي ببقى على طبيعتي من غير أي حسابات.. وعقبال عمر بحاله نعيشه سوا وإيدي في إيدك ✨</p>
    </div>
    """, unsafe_allow_html=True)
