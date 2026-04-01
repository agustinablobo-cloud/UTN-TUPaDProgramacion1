# Ejercicio 1:
'''
while True:
    nombre = input("Ingrese nombre del cliente: ")
    if nombre != "" and nombre.isalpha():
        break
    else:
        print("Error. Ingrese solo letras y no deje vacío.")


while True:
    cantidad = input("Ingrese cantidad de productos: ")
    if cantidad.isdigit() and int(cantidad) > 0:
        cantidad = int(cantidad)
        break
    else:
        print("Error. Ingrese un número entero mayor a 0.")

total_sin_descuento = 0
total_con_descuento = 0


for i in range(1, cantidad + 1):
    
    
    while True:
        precio = input(f"Producto {i} - Precio: ")
        if precio.isdigit():
            precio = int(precio)
            break
        else:
            print("Error. Ingrese un número válido.")

    
    while True:
        descuento = input("Descuento (S/N): ").lower()
        if descuento == "s" or descuento == "n":
            break
        else:
            print("Error. Ingrese S o N.")

    total_sin_descuento += precio

    if descuento == "s":
        precio_desc = precio * 0.9
    else:
        precio_desc = precio

    total_con_descuento += precio_desc


ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad

print("\n--- RESUMEN ---")
print(f"Cliente: {nombre}")
print(f"Total sin descuentos: ${total_sin_descuento}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")
'''