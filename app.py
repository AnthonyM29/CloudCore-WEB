from controllers.srv_controller import SrvController
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='views')

controlador = SrvController()

@app.route('/')
def index():
    # datos = controlador.obtener_inventario_completo()
    
    paquete_datos = controlador.obtener_datos_dashboard()
    return render_template('index.html', servidores=paquete_datos['servidores'], monitoreo=paquete_datos['monitoreo'])

@app.route('/registro')
def vista_registro():
    return render_template('registro.html')
    
    
@app.route('/guardar_servidor', methods=['POST'])
def guardar_servidor():
    datos = {
        "hostname": request.form('hostname'),
        "ip": request.form('ip'),
        "sistema_operativo": request.form('sistema_operativo')
    }
    
    if controlador.registarrar_servidor(datos):
        return redirect('/')
    else:
        return "Error al registrar el servidor", 500

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