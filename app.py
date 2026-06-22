import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="Birthday Surprise 🎉", page_icon="🐣", layout="centered")

PASSWORD = "happybirthday"

# ---------- CSS ----------
st.markdown("""
<style>
/* الخلفية العامة */
.stApp {
    background: linear-gradient(135deg, #ffe4e1, #fffacd);
}

/* ستايل الكارت */
.card-outer {
    background: white;
    padding: 40px;
    border-radius: 20px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    text-align: center;
    border: 2px solid #ffcad4;
}

/* تنسيق الخط والرسالة */
.message-body {
    text-align: left; 
    line-height: 1.8; 
    font-size: 22px; 
    color: #333;
    font-family: 'Arial', sans-serif;
}

/* حركة الكتاكيت والقلوب */
.float-element {
    position: fixed;
    font-size: 24px;
    opacity: 0.6;
    animation: float 15s infinite linear;
    z-index: 0;
}

@keyframes float {
    0% {transform: translateY(100vh) rotate(0deg);}
    100% {transform: translateY(-10vh) rotate(360deg);}
}
</style>
""", unsafe_allow_html=True)

# ---------- ديكورات الخلفية ----------
st.markdown("""
<div class="float-element" style="left:10%; animation-delay:0s;">🐣</div>
<div class="float-element" style="left:20%; animation-delay:3s;">❤️</div>
<div class="float-element" style="left:40%; animation-delay:6s;">🐣</div>
<div class="float-element" style="left:60%; animation-delay:1s;">❤️</div>
<div class="float-element" style="left:80%; animation-delay:4s;">🐣</div>
<div class="float-element" style="left:90%; animation-delay:8s;">❤️</div>
""", unsafe_allow_html=True)

# ---------- منطق الجلسة ----------
if "open" not in st.session_state:
    st.session_state.open = False

# ---------- شكل الكارت من بره (Login) ----------
if not st.session_state.open:
    st.markdown("""
    <div class="card-outer">
        <h1>🎂 Happy Birthday! 🎂</h1>
        <p>ده كارت صغير ليكي يا جنجون..</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("---")
    password = st.text_input("اكتبي الباسورد عشان تفتحي الكارت:", type="password")
    if st.button("افتحي الهدية 🎁"):
        if password == PASSWORD:
            st.session_state.open = True
            st.rerun()
        else:
            st.error("الباسورد غلط يا كتكوتة.. حاولي تاني! 😂")

# ---------- شكل الكارت من جوه (الرسالة) ----------
else:
    st.balloons() 
    st.markdown("""
    <div class="card-outer">
        <h1>🎉 HAPPY BIRTHDAY 🎉</h1>
        <h3>أهلاً بالكتكوتة اللي كبرت سنة ❤️✨</h3>
        <br>
        <div class="message-body">
        النهاردة إنتي كبرتي سنة، بس كل سنة بتمر بتزودك جمال في عيني وقرب في قلبي أكتر من اللي قبلها.<br><br>
        
        كل سنة وإنتي طيبة ❤️<br>
        وجودك مش بس حلى أيامي، ده خلاني أعرف يعني إيه أحب بجد وأحس إن قلبي مبسوط ومكتفي بيكي، وإن يومي بيكمل بيكي. معاكي ببقى على طبيعتي من غير أي حسابات، وبفك من أي ضغط لمجرد إني بكلمك أو أسمع صوتك.<br><br>
        
        فيكي تفاصيل بتخطف القلب.. ضحكتك، طريقتك في الكلام، وبساطتك اللي بتخلي أي حاجة حواليكي أهدى وأحلى. بصة واحدة في عينيكي كفاية تخليني أنسى الدنيا كلها.<br><br>
        
        وعارفة يا جنجون، أكتر حاجة بحبها فيكي إنك طبيعية جدًا، مفيكيش أي تصنع، وكل حاجة فيكي حقيقية وده اللي مخليكي مميزة بجد في عيني.<br><br>
        
        ولما بفضل أهزر وأناكف فيكي، فده عشان بحب أشوف رياكشناتك وبحب أطلع الطفلة اللي جواكي. وعلفكرة إنتي عارفة إن دمي خفيف جدًا، بس كبريائك وغرورك هما اللي مانعينك تعترفي.. بطلي مقاوحة بقى 😂<br><br>
        
        وجودك في حياتي فرق كبير، مش بس في يومي، ده حسسني إني أخدت نصيبي الحلو من الدنيا فيكي.<br><br>
        
        بدعي ربنا دايمًا إن السنة الجاية تكون أحلى، وإن قلبك يفضل مبسوط، وضحكتك تفضل منورة وشك، ومفيش حاجة في الدنيا تقدر تعكّر عليك.<br><br>
        
        كل سنة وإنتي منورة حياتي، وكل سنة وإنتي القريبة لقلبي ❤️<br>
        عقبال عمر بحاله نعيشه سوا، ونحتفل بيكي دايماً وإيدي مابتسيبش إيدك ✨
        </div>
    </div>
    """, unsafe_allow_html=True)
