# Usa la imagen oficial de Cassandra
FROM cassandra:latest

# Establece el directorio de trabajo
WORKDIR /app

# Instala Python, pip y otros paquetes necesarios
RUN apt-get update && apt-get install -y \
    python3 python3-pip curl git && \
    apt-get clean

# Copia los archivos del proyecto al contenedor
COPY . .

# Instala dependencias desde requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Expone los puertos de Cassandra y Jupyter
EXPOSE 8888 9042

# Comando de inicio: arranca Cassandra, Jupyter y ejecuta app.py
CMD ["/bin/bash", "-c", "cassandra -R & jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root & python3 app.py"]