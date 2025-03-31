# formulario con un campo para la descripcion del paciente y un boton para generar el plan, luego un espacio
# donde ira el resultado del plan usando streamlit

import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os
from fpdf import FPDF

# clave api desde .env
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Título de la app

st.title("Planificador de Actividades Terapéuticas con IA")

# Descripción

st.markdown("""
            Esta aplicación está diseñada para ayudar a terapeutas a generar planes de actividades personalizadas
para niños con TEA, TGD u otras dificultades comunicacionales usando inteligencia artificial.
""")

# Input: perfil del paciente

profile = st.text_area("Describí brevemente al paciente:",
                    placeholder="Ej: Niño de 7 años con TEA, interés por animales, dificultades en comunicación verbal")

# Botón para generar el plan
if st.button("Generar plan terapéutico"):
    if profile.strip() == "":
        st.warning("Por favor, ingresá una descripción del paciente.")
    else:
        with st.spinner("Generando plan terapéutico con IA..."):
            try:
                # Prompt personalizado con el perfil ingresado
                prompt = f"""Actuá como un planificador terapéutico experto en niños con TEA, TGD y dificultades comunicacionales.
Dado el siguiente perfil de paciente, generá un plan con estos ítems:
1. Objetivos de la sesión
2. Actividades recomendadas
3. Materiales necesarios
4. Consejos para el terapeuta

Perfil del paciente: {profile}
"""
        
                # Llamada a la API de OpenAI
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "Sos un asistente especializado en terapia infantil."},
                        {"role": "user", "content": prompt}
                    ],

                temperature=0.2,
                max_tokens=800
                
                )

                # Mostrar el resultado en pantalla
                plan = response.choices[0].message.content
                st.success("Plan terapéutico generado con éxito:")
                st.write(plan)

                # Botón para descargar como TXT
                st.download_button(
                    label="Descargar plan en TXT",
                    data=plan,
                    file_name="plan_terapeutico.txt",
                    mime="text/plain"
                )

                # Crear PDF
                pdf = FPDF()
                pdf.add_page()
                pdf.set_auto_page_break(auto=True, margin=15)
                pdf.set_font("Arial", size=12)
                for line in plan.split('\n'):
                    pdf.multi_cell(0, 10, line)

                # Guardar PDF en memoria
                pdf_output = bytes(pdf.output(dest='S').encode('latin-1'))

                # Botón para descargar como PDF
                st.download_button(
                    label="Descargar plan en PDF",
                    data=pdf_output,
                    file_name="plan_terapeutico.pdf",
                    mime="application/pdf"
                )

            except Exception as e:
                st.error(f"Ocurrió un error al generar el plan: {e}")
