import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.io as pio
from datetime import datetime

# --- Configuración visual ---
pio.templates.default = "plotly_dark"
st.set_page_config(page_title="Dashboard Premium", layout="wide")

# --- Estilos CSS corregidos ---
st.markdown("""
    <style>
    .main {
        background: linear-gradient(to right, #003366 15%, #0e1117 70%, #003366 15%);
    }
    .block-container {
        max-width: 1200px;
        margin: auto;
        padding-top: 2rem;
    }
    .stMetric {
        background-color: #1c1f26;
        padding: 15px;
        border-radius: 10px;
    }
    h1 {
        color: #ff4b4b;
    }
    </style>
""", unsafe_allow_html=True)

# --- 1. Cargar datos ---
df = pd.read_excel("ventas2.xlsx")

# --- 2. Encabezado con logo, nombre y fecha ---
col_logo, col_title, col_fecha = st.columns([1, 4, 2])
with col_logo:
    st.image("automatizacion y api/logo.png", width=80)
with col_title:
    st.title("📊 Dashboard Premium de Ventas - Juan Ruiz")
with col_fecha:
    fecha_actual = datetime.now().strftime("%A, %d de %B de %Y")
    st.write(f"📅 {fecha_actual}")

st.markdown("---")

# --- 3. Filtros dinámicos ---
meses = st.multiselect("Selecciona meses:", df["Mes"].unique(), default=df["Mes"].unique())
categorias = st.multiselect("Selecciona categorías:", df["Categoria"].unique(), default=df["Categoria"].unique())
df_filtrado = df[(df["Mes"].isin(meses)) & (df["Categoria"].isin(categorias))]

# --- 4. KPIs en columnas ---
col1, col2, col3 = st.columns(3)
ventas_totales = df_filtrado["Ventas"].sum()
ventas_promedio = df_filtrado["Ventas"].mean()
num_categorias = df_filtrado["Categoria"].nunique()

col1.metric("💰 Ventas Totales", f"${ventas_totales:,.0f}")
col2.metric("📈 Promedio Ventas", f"${ventas_promedio:,.0f}")
col3.metric("🏷️ Categorías", num_categorias)

# --- 5. Gráfico de barras ---
fig_bar = px.bar(df_filtrado, x="Mes", y="Ventas", color="Categoria", barmode="group",
                title="📊 Ventas por Mes y Categoría",
                color_discrete_sequence=px.colors.qualitative.Vivid)
st.plotly_chart(fig_bar, width='stretch')

# --- 6. Gráfico de línea (tendencia) ---
fig_line = px.line(df_filtrado, x="Mes", y="Ventas", color="Categoria", markers=True,
                title="📈 Tendencia de Ventas",
                color_discrete_sequence=px.colors.qualitative.Bold)
st.plotly_chart(fig_line, width='stretch')

# --- 7. Gráfico de pastel (participación por categoría) ---
fig_pie = px.pie(df_filtrado, names="Categoria", values="Ventas",
                title="🥧 Participación de Ventas por Categoría",
                color_discrete_sequence=px.colors.qualitative.Set3)
st.plotly_chart(fig_pie, width='stretch')

# --- 8. Tabla interactiva ---
st.subheader("📋 Datos filtrados")
st.dataframe(df_filtrado.style.highlight_max(axis=0, color="lightgreen"))