import psutil

class HardwareMonitor:
    @staticmethod
    def obtener_metricas():
        try:
            cpu_uso = psutil.cpu_percent(interval=0.5)
            ram_uso = psutil.virtual_memory().percent
            ram_total = round(psutil.virtual_memory().total / (1024 ** 3), 2)
            disco_uso = psutil.disk_usage('/').percent

            return {
                "cpu_uso": cpu_uso,
                "ram_uso": ram_uso,
                "ram_total": ram_total,
                "disco_uso": disco_uso,
            }
        except Exception as e:
            print(f"Error al obtener métricas de hardware: {e}")
            return None

