import streamlit as st
import joblib
import pandas as pd

st.set_page_config(page_title="Predicción de Diabetes", page_icon="🩺")

st.title("🩺 Evaluador Clínico de Riesgo de Diabetes")
st.markdown("---")

# --- PUNTO 10: REQUISITO DE INFORMACIÓN OBLIGATORIA ---
st.sidebar.header("📋 Información del Alumno")
st.sidebar.write("**Estudiante:** Liz Kateryn Chancafe Pisfil")
st.sidebar.write("**Código ISIL:** 48116503")
# REEMPLAZA EL LINK DE ABAJO CON EL ENLACE REAL DE COMPARTIR DE TU CUADERNO DE COLAB
st.sidebar.write("[🔗 Ver Cuaderno Google Colab (Lector)](https://colab.research.google.com/drive/1wPpgiJNjGyzsmv91JjVahrjxVQALXrU_#scrollTo=9gIxk7_snJ9f)")

# Cargar el modelo .pkl guardado
try:
    model = joblib.load("modelos/modelo_diabetes.pkl")
    st.sidebar.success("✅ Conectado al Cerebro IA")
except:
    st.sidebar.error("❌ Archivo 'modelo_diabetes.pkl' no detectado")

st.subheader("📊 Ingrese las Métricas Clínicas del Paciente:")

# Organizado de forma elegante en 3 columnas
col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("Edad (Normalizada)", value=0.0, format="%.4f")
    bmi = st.number_input("Índice Masa Corporal (bmi)", value=0.0, format="%.4f")
    bp = st.number_input("Presión Arterial (bp)", value=0.0, format="%.4f")

with col2:
    s1 = st.number_input("Suero Sanguíneo s1", value=0.0, format="%.4f")
    s2 = st.number_input("Suero Sanguíneo s2", value=0.0, format="%.4f")
    s3 = st.number_input("Suero Sanguíneo s3", value=0.0, format="%.4f")

with col3:
    s4 = st.number_input("Suero Sanguíneo s4", value=0.0, format="%.4f")
    s5 = st.number_input("Suero Sanguíneo s5", value=0.0, format="%.4f")
    s6 = st.number_input("Suero Sanguíneo s6", value=0.0, format="%.4f")

st.markdown("---")

# Columnas idénticas a los datos cargados en el entrenamiento
columnas_diabetes = ['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6']

# Generamos el vector con un valor por defecto neutral para 'sex' para cumplir la estructura
datos_entrada = pd.DataFrame([[age, 0.0, bmi, bp, s1, s2, s3, s4, s5, s6]], columns=columnas_diabetes)

# Botón de acción para el despliegue
if st.button("🔮 Diagnosticar Nivel de Riesgo", use_container_width=True):
    try:
        prediccion = model.predict(datos_entrada)
        
        st.subheader("🎯 Resultado del Análisis:")
        if prediccion[0] == 1:
            st.warning("⚠️ **ALERTA:** Los indicadores químicos muestran un **RIESGO ALTO** de progresión de diabetes. Se recomienda evaluación médica urgente.")
        else:
            st.success("🎉 **ESTABLE:** Los indicadores clínicos muestran un **RIESGO BAJO O NORMAL** de progresión de diabetes.")
    except:
        st.error("No se pudo calcular la predicción. Asegúrate de haber subido el archivo .pkl en la carpeta correcta.")
