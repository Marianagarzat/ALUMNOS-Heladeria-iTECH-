// Este archivo ya esta listo. ¡Los alumnos NO necesitan tocarlo!
const boton = document.getElementById("actualizar");
const estado = document.getElementById("estado");

function escribir(id, valor) {
  document.getElementById(id).textContent = valor;
}

function dinero(numero) {
  return "$" + Number(numero).toLocaleString("es-MX", { maximumFractionDigits: 2 });
}

async function actualizar() {
  estado.textContent = "Actualizando...";
  boton.disabled = true;
  try {
    const respuesta = await fetch("/api/heladeria", { cache: "no-store" });
    if (!respuesta.ok) throw new Error("No se pudo conectar a Python");
    const resultado = await respuesta.json();
    if (!resultado.ok) throw new Error(resultado.error);
    const datos = resultado.datos;
    for (const nombre of ["nombre", "mensaje", "sabor1", "sabor2", "sabor3", "especial"]) {
      escribir(nombre, datos[nombre]);
    }
    // El color de Python controla el tema de la página.
    document.documentElement.style.setProperty("--blue", datos.color);
    escribir("precio", dinero(datos.precio));
    escribir("precio_final", dinero(datos.precio_final) + " MXN");
    escribir("descuento", dinero(datos.descuento));
    estado.textContent = "Cambios guardados. Variables completas: " + datos.completos + "/" + datos.total;
  } catch (error) {
    estado.textContent = "⚠ " + error.message;
  } finally {
    boton.disabled = false;
  }
}

boton.addEventListener("click", actualizar);
actualizar();
