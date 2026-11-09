# MOTOR DE LA PAGINA. NO NECESITAS EDITAR ESTE ARCHIVO.
# Solo funciona en esta computadora y no necesita internet.

from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import json
import os
import runpy
import re
import webbrowser

carpeta = Path(__file__).resolve().parent
pagina = carpeta / "web"


# Values shown until students create their own variables.
# The completed variables replace each example one by one.
def leer_heladeria():
    try:
        datos = runpy.run_path(str(carpeta / "heladeria.py"))
        textos = {
            "nombre": "Tu heladeria",
            "mensaje": "Escribe un mensaje para tus clientes",
            "sabor1": "Tu primer sabor",
            "sabor2": "Tu segundo sabor",
            "sabor3": "Tu tercer sabor",
            "especial": "Tu promocion especial",
        }
        resultado = {}
        completos = []

        for clave, ejemplo in textos.items():
            valor = datos.get(clave)
            if valor is None:
                resultado[clave] = ejemplo
            elif isinstance(valor, str):
                resultado[clave] = valor
                completos.append(clave)
            else:
                raise ValueError("'" + clave + "' debe ser texto entre comillas")

        color = datos.get("color")
        if color is None:
            resultado["color"] = "#0F5EA8"
        elif isinstance(color, str) and re.fullmatch(r"#[0-9a-fA-F]{6}", color):
            resultado["color"] = color
            completos.append("color")
        else:
            raise ValueError('El color debe ser como "#0F5EA8"')

        for clave, ejemplo in [("precio", 55), ("descuento", 10)]:
            valor = datos.get(clave)
            if valor is None:
                resultado[clave] = ejemplo
            elif type(valor) in [int, float] and valor >= 0:
                resultado[clave] = valor
                completos.append(clave)
            else:
                raise ValueError("'" + clave + "' debe ser un numero positivo")

        total = datos.get("precio_final")
        if total is None:
            # Show an example until students write their calculation.
            resultado["precio_final"] = 45
        elif type(total) in [int, float] and total >= 0:
            resultado["precio_final"] = total
            completos.append("precio_final")
        else:
            raise ValueError("'precio_final' debe ser un numero positivo")

        resultado["completos"] = len(completos)
        resultado["total"] = 10
        return {"ok": True, "datos": resultado}
    except SyntaxError as error:
        return {"ok": False, "error": "Revisa heladeria.py, linea " + str(error.lineno) + ". " + error.msg}
    except NameError as error:
        return {"ok": False, "error": "Revisa el nombre de tus variables: " + str(error)}
    except Exception as error:
        return {"ok": False, "error": str(error)}


class Servidor(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(pagina), **kwargs)

    def do_GET(self):
        if self.path.split("?", 1)[0] == "/api/heladeria":
            respuesta = json.dumps(leer_heladeria(), ensure_ascii=False).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Cache-Control", "no-store")
            self.send_header("Content-Length", str(len(respuesta)))
            self.end_headers()
            self.wfile.write(respuesta)
            return
        super().do_GET()


if __name__ == "__main__":
    try:
        with ThreadingHTTPServer(("127.0.0.1", 8000), Servidor) as servidor:
            print("¡Tu heladería esta lista!")
            print("Abre http://localhost:8000 en tu navegador")
            print("Deja esta terminal abierta. Para detener: Ctrl + C")
            if os.environ.get("NO_BROWSER") != "1":
                webbrowser.open("http://localhost:8000")
            servidor.serve_forever()
    except OSError:
        print("No se pudo usar el puerto 8000. Cierra otra heladería abierta y vuelve a intentarlo.")
    except KeyboardInterrupt:
        print("\n¡Hasta luego!")
