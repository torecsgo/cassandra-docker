from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import json

from dotenv import load_dotenv
import os

# Configuración de conexión con Cassandra
cloud_config = {
    'secure_connect_bundle': 'data/secure-connect-test-cassandra.zip'
}

# Cargar variables del archivo .env
load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
TOKEN = os.getenv("TOKEN")

auth_provider = PlainTextAuthProvider(CLIENT_ID, CLIENT_SECRET)
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

# Verificar conexión
row = session.execute("SELECT release_version FROM system.local").one()
if row:
    print(f"Cassandra Release Version: {row[0]}")
else:
    print("An error occurred.")

# Establecer el keyspace
session.set_keyspace('test')  # Reemplaza con tu keyspace

def consultar_clientes(session):
    rows = session.execute("SELECT * FROM cliente")
    print("Clientes:")
    for row in rows:
        print(f"ID: {row.cliente_id}, Nombre: {row.nombre}, Dirección: {row.direccion}, Teléfono: {row.telefono}")

def consultar_pedidos(session):
    rows = session.execute("SELECT * FROM pedido")
    print("\nPedidos:")
    for row in rows:
        print(f"Cliente ID: {row.cliente_id}, Pedido ID: {row.pedido_id}, Fecha: {row.fecha}, Estado: {row.estado}")

def consultar_productos(session):
    rows = session.execute("SELECT * FROM producto")
    print("\nProductos:")
    for row in rows:
        print(f"Pedido ID: {row.pedido_id}, Producto ID: {row.producto_id}, Nombre: {row.nombre}, Cantidad: {row.cantidad}, Precio: {row.precio}")

if __name__ == "__main__":
    consultar_clientes(session)
    consultar_pedidos(session)
    consultar_productos(session)