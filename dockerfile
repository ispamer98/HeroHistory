# Usar una imagen base oficial de Python
FROM python:3.11-slim

# Establecer el directorio de trabajo
WORKDIR /app_docker

# Copiar los archivos necesarios para la aplicación
COPY requirements.txt ./

# Establecer variables de entorno para el entorno virtual
ENV VIRTUAL_ENV=/app_docker/.venv_docker
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Crear el entorno virtual y actualizar pip
RUN python -m venv $VIRTUAL_ENV && \
    pip install --upgrade pip

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de los archivos de la aplicación
COPY . .

# Verificar si reflex está instalado
RUN $VIRTUAL_ENV/bin/pip show reflex || echo "Reflex no instalado en el entorno virtual"

# Exponer el puerto que usará la aplicación
EXPOSE 8000

# Establecer el comando de inicio para solo backend
CMD ["reflex", "run", "--env", "prod", "--backend-only"]
