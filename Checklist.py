import streamlit as st

# --- Título ---
st.set_page_config(page_title="Checklist Área de Planificación", page_icon="✅")
st.title("Checklist Área de Planificación ✅")

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

