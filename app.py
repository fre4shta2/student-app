import streamlit as st
import matplotlib.pyplot as plt

# سەردێڕی بەرنامەکە
st.title("📊 سیستەمی فێرکاریی شیکاری داتا و گراف")
st.write("نمرەی وانەکانت تۆمار بکە تا تێکڕای ئاماری و گرافەکەت بۆ بپێوێت!")

# وەرگرتنی نمرەکان لە قوتابی لە بەشی لای چپ
st.sidebar.header("تۆمارکردنی نمرەکان")
kurdish = st.sidebar.number_input("کوردی", min_value=0, max_value=100, value=85)
arabic = st.sidebar.number_input("عەرەبی", min_value=0, max_value=100, value=70)
english = st.sidebar.number_input("ئینگلیزی", min_value=0, max_value=100, value=92)
math = st.sidebar.number_input("بیرکاری", min_value=0, max_value=100, value=65)
science = st.sidebar.number_input("زانست", min_value=0, max_value=100, value=88)

# ڕێکخستنی داتاکان
subjects = ['کوردی', 'عەرەبی', 'ئینگلیزی', 'بیرکاری', 'زانست']
scores = [kurdish, arabic, english, math, science]

# حیساباتە ئامارییەکان
average = sum(scores) / len(scores)

# نیشاندانی ئەنجامە ئامارییەکان
col1, col2, col3 = st.columns(3)
col1.metric("تێکڕای نمرەکان (Mean)", f"{average:.1f}")
col2.metric("بەرزترین نمرە", max(scores))
col3.metric("نزمترین نمرە", min(scores))

# دروستکردنی گرافەکە
fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(subjects, scores, color='skyblue')
ax.axhline(average, color='red', linestyle='--', label=f'تێکڕا ({average:.1f})')
ax.set_ylim(0, 100)
ax.set_ylabel('نمرە')
ax.set_title('گرافی بەراوردکاری نمرەکان')
ax.legend()

# نیشاندانی گرافەکە
st.pyplot(fig)