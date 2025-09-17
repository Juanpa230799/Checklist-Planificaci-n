import streamlit as st
from datetime import date

# --- Título ---
st.set_page_config(page_title="Checklist Área de Planificación", page_icon="✅")
st.title("Checklist Área de Planificación ✅")

# --- Información del checklist ---
col1, col2, col3 = st.columns(3)

# Fecha
fecha_checklist = col1.date_input("📅 Fecha del checklist", value=date.today())

# Encargado
encargados = ["Brany Gómez", "Gerardo Muñoz", "Juan Pablo"]  # aquí pones tu lista de encargados
encargado = col2.selectbox("👤 Encargado", encargados)

# Tienda
tiendas = ["Plaza Oeste", "Plaza Sur", "Plaza Norte"]  # aquí pones tu lista de tiendas
tienda = col3.selectbox("🏪 Tienda", tiendas)

st.markdown("---")  # separador

# --- Lista de tareas ---
tareas = [
    "Cubicación",
    "Reposición (Curva, RAMI)",
    "Despachos",
    "Club Pillin",
    "Mix colección",
    "Visual merchandising",
    "Competencia",
    "Experiencia del cliente (CX)",
    "Dotación y gestión equipo de venta",
    "Posibles áreas de mejora"
]

# --- Estado de tareas ---
estado = []
for tarea in tareas:
    checked = st.checkbox(tarea)
    estado.append(checked)

# --- Progreso ---
completadas = sum(estado)
total = len(tareas)
progreso = completadas / total if total > 0 else 0

st.progress(progreso)
st.write(f"Has completado **{completadas} de {total} tareas**.")

# --- Mensaje motivador ---
if completadas == total:
    st.success("🎉 ¡Excelente! Completaste todo el checklist.")
elif completadas > 0:
    st.info("💪 Vas avanzando, sigue así.")
else:
    st.warning("🙌 Aún no comienzas, ¡manos a la obra!")


