from models.database import Database
from models.hardware import HardwareMonitor

class SrvController:
    def __init__(self):
        self.db = Database()
        self.hw = HardwareMonitor()

    def obtener_inventario_completo(self):
        """Obtiene todos los servidores de la base de datos."""
        self.db.connect()
        if not self.db.connection:
            return []

        cursor = None
        try:
            cursor = self.db.connection.cursor(dictionary=True)
            query ="""
                  SELECT
                    s.hostname,
                    s.direccion_ip,
                    c.tipo,
                    c.especificacion,
                    c.capacidad_gb AS cantidad_gb
                FROM sevidores s
                INNER JOIN componentes c ON s.id_servidor = c.id_servidor;"""
            cursor.execute(query)
            resultados = cursor.fetchall()
        finally:
            if cursor:
                cursor.close()
            if self.db.connection:
                self.db.connection.close()
        return resultados
    
    def obtener_datos_dashboard(self):
        return {
            'servidores': self.obtener_inventario_completo(),
            'monitoreo': self.hw.obtener_metricas()
        }
        
    def registrar_auditoria(self, accion, descripcion):
        """Registra una acción en la tabla de auditoría."""
        self.db.connect()
        if not self.db.connection:
            return False
        
        cursor = None
        try:
            cursor = self.db.connection.cursor()
            query = "INSERT INTO auditoria (Tabla_afectada, accion, descripcion) VALUES (%s, %s, %s)"
            valores = ('infraestructura', accion, descripcion)
            self.ejecutar_query(query, valores)
            return True
        except Exception as e:
            print(f"Error registrando auditoría: {e}")
            self.db.connection.rollback()
            return False
        finally:
            if cursor:
                cursor.close()
            if self.db.connection:
                self.db.connection.close()
                
    def registarrar_servidor(self, datos):
        """Registra un nuevo servidor en la base de datos."""
        query = "INSERT INTO sevidores (hostname, direccion_ip, sistema_operativo) VALUES (%s, %s, %s)"
        valores =(datos["hostname"], datos["ip"], datos["sistema_op"])
        
        if self.db.ejecutar_query(query, valores):
            self.registrar_auditoria("INSERT", f"Servidor {datos['hostname']} registrado.")
            return True