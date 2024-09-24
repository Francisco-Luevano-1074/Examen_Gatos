class Gatos1074():
    
    idgato=0
    nombre=""
    edad=0
    color=""
    raza=""
    precio=0
    caract=""
    

    def lista_gatos(self):
        listanomgatos=["Miauricio","Megatron","Patrick","Bosnio","Garfield"]
        for x in listanomgatos:
            print(x)
                
    def tupla_gatos(self):
        tuplagatos=(2,3,1,5,4)
        for x in tuplagatos:
            print(x)
    
    def dic_gatos(self):
        dic_cat={
            "Miauricio": "café",
            "Megatron": "bicolor",
            "Patrick": "gris",
            "Bosnio": "negro",
            "Garfield": "naranja"
        }
        for x,y in dic_cat.items():
            print(x,y)
        
    def altas(self):
        print("La operación se realizo correctamente para los datos del gato")
    def bajas(self):
        print("La operación no se realizó correctamente para los datos del gato")
        
mostrar_datos=Gatos1074()
miauricio=Gatos1074()
print("---Resultados para Miauricio---")
miauricio.idgato=1
miauricio.nombre="Miauricio"
miauricio.edad=2
miauricio.color="Café"
miauricio.raza="Persa"
miauricio.precio=30
miauricio.caract="Travieso"
print(f"ID: {miauricio.idgato}")
print(f"Nombre: {miauricio.nombre}")
print(f"Edad: {miauricio.edad}")
print(f"Color: {miauricio.color}")
print(f"Raza: {miauricio.raza}")
print(f"Precio: {miauricio.precio}")
print(f"Caract: {miauricio.caract}")
                
megatron=Gatos1074()
print("---Resultados para Megatron---")
megatron.idgato=2
megatron.nombre="Megatron"
megatron.edad=3
megatron.color="bicolor"
megatron.raza="Azul ruso"
megatron.precio=20
megatron.caract="Curioso"
print(f"ID: {megatron.idgato}")
print(f"Nombre: {megatron.nombre}")
print(f"Edad: {megatron.edad}")
print(f"Color: {megatron.color}")
print(f"Raza: {megatron.raza}")
print(f"Precio: {megatron.precio}")
print(f"Caract: {megatron.caract}")
        
patrick=Gatos1074()
print("---Resultados para Patrick---")
patrick.idgato=3
patrick.nombre="Patrick"
patrick.edad=1
patrick.color="Gris"
patrick.raza="Bengalí"
patrick.precio=15
patrick.caract="Conflictivo"
print(f"ID: {patrick.idgato}")
print(f"Nombre: {patrick.nombre}")
print(f"Edad: {patrick.edad}")
print(f"Color: {patrick.color}")
print(f"Raza: {patrick.raza}")
print(f"Precio: {patrick.precio}")
print(f"Caract: {patrick.caract}")
        
bosnio=Gatos1074()
print("---Resultados para Bosnio---")
bosnio.idgato=4
bosnio.nombre="Bosnio"
bosnio.edad=5
bosnio.color="negro"
bosnio.raza="Callejero"
bosnio.precio=10
bosnio.caract="Pacífico"
print(f"ID: {bosnio.idgato}")
print(f"Nombre: {bosnio.nombre}")
print(f"Edad: {bosnio.edad}")
print(f"Color: {bosnio.color}")
print(f"Raza: {bosnio.raza}")
print(f"Precio: {bosnio.precio}")
print(f"Caract: {bosnio.caract}")
        
garfield=Gatos1074()
print("---Resultados para Garfield---")
garfield.idgato=5
garfield.nombre="Garfield"
garfield.edad=4
garfield.color="Naranja"
garfield.raza="Escocés"
garfield.precio=21
garfield.caract="Comelón"
print(f"ID: {garfield.idgato}")
print(f"Nombre: {garfield.nombre}")
print(f"Edad: {garfield.edad}")
print(f"Color: {garfield.color}")
print(f"Raza: {garfield.raza}")
print(f"Precio: {garfield.precio}")
print(f"Caract: {garfield.caract}")
        
mostrar_datos.lista_gatos()
mostrar_datos.tupla_gatos()
mostrar_datos.dic_gatos()