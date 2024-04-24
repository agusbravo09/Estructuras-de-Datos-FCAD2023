#Integrantes: Aquino Benjamin, Bravo Agustin, Cafre Marko

from calzado import Calzado
from calzado_tipo import CalzadoTipo
from calzado_talle import CalzadoTalle
from calzado_color import CalzadoColor
from calzado_admin import CalzadoAdmin

calzado_1 = Calzado(1, "Zapatillas 1", "Descripción de las zapatillas 1",
                    CalzadoTipo("Deportivas"), CalzadoTalle("41", 41),
                    CalzadoColor("Blanco"), 10, 99.99)
calzado_2 = Calzado(2, "Zapatillas 2", "Descripción de las zapatillas 2",
                    CalzadoTipo("Casuales"), CalzadoTalle("39", 39),
                    CalzadoColor("Negro"), 15, 89.99)
calzado_3 = Calzado(3, "Zapatillas 3", "Descripción de las zapatillas 3",
                    CalzadoTipo("Deportivas"), CalzadoTalle("40", 40),
                    CalzadoColor("Azul"), 20, 109.99)
calzado_4 = Calzado(4, "Zapatillas 4", "Descripción de las zapatillas 4",
                    CalzadoTipo("Casuales"), CalzadoTalle("38", 38),
                    CalzadoColor("Gris"), 12, 79.99)
calzado_5 = Calzado(5, "Zapatillas 5", "Descripción de las zapatillas 5",
                    CalzadoTipo("Deportivas"), CalzadoTalle("42", 42),
                    CalzadoColor("Rojo"), 8, 119.99)
calzado_6 = Calzado(6, "Zapatillas 6", "Descripción de las zapatillas 6",
                    CalzadoTipo("Casuales"), CalzadoTalle("37", 37),
                    CalzadoColor("Blanco"), 14, 69.99)
calzado_7 = Calzado(7, "Zapatillas 7", "Descripción de las zapatillas 7",
                    CalzadoTipo("Deportivas"), CalzadoTalle("43", 43),
                    CalzadoColor("Negro"), 16, 129.99)
calzado_8 = Calzado(8, "Zapatillas 8", "Descripción de las zapatillas 8",
                    CalzadoTipo("Casuales"), CalzadoTalle("39", 39),
                    CalzadoColor("Azul"), 11, 79.99)
calzado_9 = Calzado(9, "Zapatillas 9", "Descripción de las zapatillas 9",
                    CalzadoTipo("Deportivas"), CalzadoTalle("41", 41),
                    CalzadoColor("Gris"), 9, 109.99)
calzado_10 = Calzado(10, "Zapatillas 10", "Descripción de las zapatillas 10",
                     CalzadoTipo("Casuales"), CalzadoTalle("38", 38),
                     CalzadoColor("Rojo"), 13, 89.99)
calzado_11 = Calzado(11, "Zapatillas 11", "Descripcion de las zapatillas 11",
                     CalzadoTipo("Deportivas"), CalzadoTalle("38", 38),
                     CalzadoColor("Rojo", "Azul"), 20, 39.99) #<- ValueError: SKU iguales

#calzado_11.cantidad = -2 #<- ValueError cantidad
#calzado_11.precio = -23.4  #<- ValueError precio
#calzado_11.sku = -2 #<- ValueError SKU

admin = CalzadoAdmin()
admin.agregar(calzado_1)
admin.agregar(calzado_2)
admin.agregar(calzado_3)
admin.agregar(calzado_4)
admin.agregar(calzado_5)
admin.agregar(calzado_6)
admin.agregar(calzado_7)
admin.agregar(calzado_8)
admin.agregar(calzado_9)
admin.agregar(calzado_10)
admin.agregar(calzado_11)

print("************************")
print("* Todas las Zapatillas ")
print("************************")
print(admin)

print("************************")
print("* Zapatillas Deportivas")
print("************************")
print("admin.filtrar_por_tipo(CalzadoTipo('Deportivas'))",
      admin.filtrar_por_tipo(CalzadoTipo("Deportivas")))

print("************************")
print("* Precio entre 1")
print("************************")
print("admin.filtrar_precio_entre(70.00, 100.00):",
      admin.filtrar_precio_entre(70.00, 100.00))

print("************************")
print("* Precio entre 2")
print("************************")
print("admin.filtrar_precio_entre(hasta = 70.00)",
      admin.filtrar_precio_entre(hasta=70.00))

print("************************")
print("* Cantidad y Total")
print("************************")

print("Cantidad: ", admin.cantidad_productos())
print("Total: ", admin.total_productos())
