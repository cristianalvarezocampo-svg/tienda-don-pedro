from pathlib import Path


carpeta_proyecto = Path(__file__).parent.parent
archivo = carpeta_proyecto / "datos" / "productos.txt"

lineas = archivo.read_text(encoding="utf-8").splitlines()
productos = lineas[2:]
total = 0

print("=== Inventario Tienda Don Pedro ===")
for linea in productos:
    print("-", linea)
    precio = int(linea.split("$")[-1].replace(".", ""))
    total += precio

print("Total de productos:", len(productos))
print("Valor del inventario: $" + str(total))