#!/bin/bash

# Cambiar al directorio del proyecto
cd herohistory

# Crear y activar el entorno virtual
python -m venv .venv
source .venv/bin/activate

# Actualizar pip e instalar las dependencias
pip install --upgrade pip
pip install -r requirements.txt

# Eliminar cualquier carpeta de frontend existente
rm -rf frontend

# Inicializar reflex (esto solo es necesario si es un proyecto nuevo)
reflex init

# Establecer la URL de la API y exportar solo el frontend
API_URL=https://herohistory-back.onrender.com reflex export --frontend-only

# Descomprimir el archivo frontend.zip en la carpeta public
unzip frontend.zip -d public

# Eliminar el archivo frontend.zip después de descomprimir
rm -f frontend.zip

# Desactivar el entorno virtual
deactivate
