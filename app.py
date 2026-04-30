from controllers.srv_controller import SrvController
from flask import Flask, render_template

app = Flask(__name__, template_folder='views')

controlador = SrvController()

@app.route('/')
def index():
    datos = controlador.obtener_inventario_completo()
    return render_template('index.html', servidores=datos)

"""def ejecutar_sistema():
    print("====== CLOUDCORE-WEB: Modelo de ingeneria (semana 2) ======")
    controller = SrvController()
    
    datos = controller.obtener_inventario_completo()
    if not datos:
        print("No se encontraron datos en la base de datos.")
    else:
        print("Inventario Completo de Servidores:")
        for item in datos:
            print(f"Hostname: {item['hostname']}, IP: {item['direccion_ip']}, Tipo: {item['tipo']}, Especificaciones: {item['especificacion']}, Capacidad (GB): {item['capacidad_gb']}")
            print(f"Componente: {item['tipo']}, Especificaciones: {item['especificacion']}, Capacidad (GB): {item['capacidad_gb']}")
            print("-" * 50)"""
            
if __name__ == "__main__":
    print("Iniciando servidor web en http://127.0.0.1:5000")
    app.run(debug=True, port=5000)