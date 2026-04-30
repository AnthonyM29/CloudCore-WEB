from models.database import Database

class SrvController:
    def __init__(self):
        self.db = Database()

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