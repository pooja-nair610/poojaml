
import pandas as pd
import streamlit as st
import numpy as np
import seaborn as sns 

st.balloons()
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("WORLD HAPPINESS REPORT")
df = pd.read_csv('whr.csv')

st.subheader("PARAMETERS OF THE DATASET ")
for col in df.columns:
    st.text(col)
st.subheader("TOP 20 ")    
report = df.head(20)
st.table(report)
st.subheader("BARPLOT")

sns.barplot(x='Score',y='Country',data=report,orient="h")
st.pyplot()
st.subheader("PAIRPLOT")
sns.pairplot(report,palette='rainbow')
st.pyplot()
st.subheader("HEATMAP")
sns.heatmap(report.corr(),annot=True)
st.pyplot()