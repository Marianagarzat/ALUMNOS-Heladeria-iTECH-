# Guía de instalación para alumnos — Windows y Mac

## Antes de llegar
Necesitas una laptop, su cargador, Python 3 y VS Code. **Recomendado:** instala también la extensión **Python** de Microsoft en VS Code. No necesitas instalar librerías con `pip`.

Enlaces oficiales:
- Python: https://www.python.org/downloads/
- Visual Studio Code: https://code.visualstudio.com/download
- Extensión de Python: https://marketplace.visualstudio.com/items?itemName=ms-python.python
- Tutorial oficial: https://code.visualstudio.com/docs/python/python-tutorial

## Windows
1. Instala Python desde `python.org` y termina el asistente de instalación. Si tu instalador ofrece **Add Python to PATH**, actívalo.
2. Instala VS Code y ábrelo.
3. Abre el proyecto usando **File / Archivo → Open Folder / Abrir carpeta**.
4. En VS Code elige **Terminal → New Terminal**.
5. Escribe `py -3 --version` y presiona Enter. Debe mostrar una versión de Python 3.
6. Escribe `py practica.py` para hacer los ejercicios.
7. Para la heladería escribe `py app.py` (puedes abrir otra terminal con el botón `+`).
8. Visita `http://localhost:8000` si la página no aparece sola.

Si Windows no reconoce `py`, prueba `python --version` y luego `python app.py`. Si aparece un mensaje de la Microsoft Store, pide apoyo al instructor: suele indicar que falta instalar o seleccionar Python.

## Mac
1. Instala Python 3 desde `python.org` (o mediante un método compatible con macOS).
2. Instala y abre VS Code, después **File → Open Folder**.
3. Abre **Terminal → New Terminal**.
4. Comprueba `python3 --version`.
5. Escribe `python3 practica.py` para el primer ejercicio.
6. Después escribe `python3 app.py`.
7. Visita `http://localhost:8000` si no se abre sola.

En Mac el botón Guardar suele ser **Cmd + S**; en Windows es **Ctrl + S**.

## Personaliza tu heladería
1. Abre **`heladeria.py`** en VS Code.
2. Cambia `nombre = "Nube de Helado"` por el nombre que tú quieras, dejando las comillas.
3. Guarda.
4. En la página haz clic en **↻ Actualizar heladería**. ¡Verás el nombre nuevo!
5. Prueba también `color = "#FF8800"`, cambia un sabor o el número de `precio`.

**Colores:** escribe cualquier código hexadecimal de 6 dígitos, como `"#0F5EA8"` (azul), `"#FF8800"` (naranja), `"#8A2BE2"` (morado) o `"#22A06B"` (verde). Conserva las comillas y el símbolo `#`.

## Si ves un error
- `SyntaxError`: revisa que hayas dejado **ambas comillas** y que el texto esté dentro.
- `NameError`: puede faltar una palabra, por ejemplo `precio`.
- `TypeError` o error de precio: los números van sin comillas (`precio = 55`).
- El botón no cambia nada: guarda `heladeria.py`, deja abierta la terminal de `app.py` y vuelve a presionar.
- El navegador dice que no puede conectarse: asegúrate de que la terminal esté ejecutando `app.py`.
- `Address already in use` / puerto ocupado: cierra la otra terminal que está ejecutando el mismo proyecto.

## ¡Sin internet!
Después de descargar el ZIP y tener Python instalado, puedes completar la actividad sin Wi-Fi. Abre `app.py`: la página se muestra desde tu propia laptop.

### Referencia visual
La captura de **la heladería funcionando visualmente** está en `capturas/heladeria_vista_previa.png`. Para las pantallas reales de instalación, las capturas deberán realizarse en una computadora Windows/Mac del taller, porque las ventanas varían según versión y equipo.

Otra ayuda visual de pasos está en `capturas/guia_visual_instalacion.png`. Es un **esquema ilustrativo**, no una captura real del instalador.
