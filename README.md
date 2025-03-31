Planificador Terapéutico con IA - Proyecto con Streamlit y OpenAI

Descripción del Proyecto  
Este proyecto es una aplicación web desarrollada con Streamlit e integrada con la API de OpenAI. Está diseñada para asistir a terapeutas en la generación de planes de actividades personalizados para niños con TEA, TGD u otras dificultades comunicacionales, a partir de la descripción del perfil del paciente ingresada por el usuario.

Requisitos  
- Python 3.12 o superior  
- Streamlit: Framework para aplicaciones web en Python  
- OpenAI: Acceso a modelos de lenguaje para generar el contenido  
- FPDF: Para exportar el plan generado en formato PDF  
- python-dotenv: Para gestionar variables de entorno

Instalación y Configuración Desde Cero

Clonar el Proyecto  
Ubicarse en la carpeta donde se desea clonar el repositorio y ejecutar el siguiente comando:

git clone https://github.com/tuusuario/planificador-terapia.git

Ingresar a la carpeta del proyecto:

cd planificador-terapia

Crear un entorno virtual  
python -m venv venv  
source venv/Scripts/activate

Instalar dependencias  
pip install -r requirements.txt

Configurar la clave de OpenAI  
Crear una carpeta llamada `.streamlit` y dentro de ella un archivo `secrets.toml` con el siguiente contenido:

OPENAI_API_KEY = "sk-..."

Uso del Proyecto

Ejecutar la aplicación localmente  
Para iniciar la aplicación web en el navegador:

streamlit run app.py

Esto abrirá automáticamente la aplicación en la URL:

http://localhost:8501

Funcionamiento de la App  
El usuario debe ingresar una descripción breve del paciente. Luego, al hacer clic en el botón de generar plan, se contacta a la API de OpenAI con un prompt especializado. El sistema devuelve un plan terapéutico dividido en:

- Objetivos de la sesión  
- Actividades recomendadas  
- Materiales necesarios  
- Consejos para el terapeuta

Una vez generado, se puede descargar el plan en formato .txt o .pdf.

Consideraciones Finales  
Este proyecto demuestra cómo integrar una interfaz simple desarrollada con Streamlit con modelos de lenguaje de OpenAI para automatizar tareas clínicas. Ofrece una base sólida para construir herramientas de asistencia terapéutica basadas en IA, priorizando la accesibilidad y personalización de las intervenciones.

Contacto  
Autor: Maximiliano Sastre Bocalon
