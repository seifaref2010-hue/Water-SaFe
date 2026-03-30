# water_dashboard_streamlit.py
import streamlit as st
import matplotlib.pyplot as plt

# === دوال التحليل ===
def calculate_pollution(data):
    score = 0
    if data.get('color') in ['بنية','رمادية','صفراء','Brown','Gray','Yellow']:
        score += 20
    if data.get('impurities') in ['رمل','جزيئات صغيرة','شوائب واضحة','Sand','Small particles','Visible impurities']:
        score += 30
    if data.get('pipe_age') in ['5–10 سنوات','أكثر من 10 سنوات','5–10 years','More than 10 years']:
        score += 15
    return score

def water_quality(pollution):
    return 100 - pollution

def water_status(quality, lang):
    if quality >= 80:
        return '🟢 Safe to drink' if lang=='EN' else '🟢 صالحة للشرب'
    elif quality >= 50:
        return '🟡 Only for use' if lang=='EN' else '🟡 صالحة للاستخدام فقط'
    else:
        return '🔴 Unsafe' if lang=='EN' else '🔴 غير صالحة'

def suggested_solution(data, lang):
    solutions = []
    if data.get('impurities') in ['رمل','جزيئات صغيرة','شوائب واضحة','Sand','Small particles','Visible impurities']:
        solutions.append('Sediment filter' if lang=='EN' else 'فلتر رواسب')
    if data.get('smell') in ['كلور','Chlorine']:
        solutions.append('Carbon filter' if lang=='EN' else 'فلتر كربون')
    if data.get('taste') in ['مر','Bitter','ملح','Salty']:
        solutions.append('3-stage filter' if lang=='EN' else 'فلتر 3 مراحل')
    return ', '.join(solutions) if solutions else ('No filter needed' if lang=='EN' else 'لا حاجة لفلتر')

# === واجهة Streamlit ===
def main():
    st.set_page_config(page_title="Water Quality Dashboard", layout="centered")
    
    # اختيار اللغة
    lang = st.radio("Choose Language / اختر اللغة", ['English','العربية'])
    lang_code = 'EN' if lang=='English' else 'AR'

    st.markdown("<h1 style='text-align:center;'>Water Quality Dashboard / لوحة تحكم جودة المياه</h1>", unsafe_allow_html=True)

    # الأسئلة
    data = {}
    
    # تعريف الأسئلة والخيارات
    questions = [
        ("color", "Water Color / لون المياه", ['Clear (شفافة)','Yellow (صفراء)','Brown (بنية)','Gray (رمادية)','Unclear (غير واضح)']),
        ("smell", "Water Smell / رائحة المياه", ['None (لا توجد)','Chlorine (كلور)','Rust (صدأ)','Sulfur (كبريت)','Strange (غريبة)']),
        ("taste", "Water Taste / طعم المياه", ['Normal (طبيعي)','Mineral (معدني)','Salty (ملح)','Bitter (مر)','Unknown (غير معروف)']),
        ("impurities", "Impurities / شوائب", ['None (لا يوجد)','Sand (رمل)','Small particles (جزيئات صغيرة)','Visible impurities (شوائب واضحة)']),
        ("pipe_age", "Pipe Age / عمر المواسير", ['<5 years (أقل من 5 سنوات)','5–10 years (5–10 سنوات)','>10 years (أكثر من 10 سنوات)','Unknown (غير معروف)']),
    ]
    
    st.header("Please answer the following questions:" if lang_code=='EN' else "أجب على الأسئلة التالية:")

    for key, q_text, options in questions:
        data[key] = st.selectbox(q_text, options).split('(')[0].strip()
    
    if st.button("Submit / إرسال"):
        pollution = calculate_pollution(data)
        quality = water_quality(pollution)
        status = water_status(quality, lang_code)
        solution = suggested_solution(data, lang_code)
        
        st.subheader("Results / النتائج")
        st.markdown(f"*Water Quality / درجة جودة المياه:* {quality}")
        st.markdown(f"*Pollution Level / نسبة التلوث:* {pollution}%")
        st.markdown(f"*Status / الحالة:* {status}")
        st.markdown(f"*Suggested Solution / الحل المقترح:* {solution}")
        
        # رسم بياني
        fig, ax = plt.subplots()
        categories = ['Quality', 'Pollution']
        values = [quality, pollution]
        colors = ['#2ca02c', '#ff7f0e']
        ax.bar(categories, values, color=colors)
        ax.set_ylim(0,100)
        for i, v in enumerate(values):
            ax.text(i, v+2, str(v), ha='center', fontweight='bold')
        st.pyplot(fig)

if _name_ == "_main_":
    main()