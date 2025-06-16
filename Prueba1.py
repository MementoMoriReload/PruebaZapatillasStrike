opcion=0
reservas={}
frase="EstoyEnListaDeReserva"
limite=20
def main():
        print("TOTEM AUTOATENCIÓN RESERVA STRIKE")
        print("1.-Reservar zapatillas")
        print("2.-Buscar zapatillas resevadas")
        print("3.-Cancelar reserva de zapatillas")
        print("4.-Salir")
        opcion=int(input("Ingrese una opcion (1-4): "))
        return opcion

def comprar():
    print("--Reservar Zapatillas--")
    if len(reservas)<=20:
        nombre=str(input("Ingrese nombre del comprador: "))
        if nombre not in reservas:
            zapatillas=[]
            reservas[nombre]={"zapatillas":zapatillas}
            clave=str(input("Introduzca la frase secreta para hacer la reserva: "))
            if clave==frase:
                reservas[nombre] = {"vip": False}
            else:
                print("frase incorrecta, se cancela la reserva")
                del reservas[nombre]
                return
        else:
            print("Nombre ya existente, se cancela la reserva")
    else:
        print("Limite de reservas ya alcanzada")
       
def buscar():
    print("--Buscar Zapatillas Reservadas--")
    reserva = input("Ingrese nombre del reservador a buscar: ")
    if reserva in reservas:
        print(f"Nombre: {reserva}")
        
    else:
        print("No se encontró una reserva con ese nombre.")
    if not reservas[reserva]["vip"]:
            opcion = input("¿Desea pagar para convertir su reserva a VIP y reservar 2 pares? (s/n): ").lower()
            if opcion == 's':
                extra = input("Ingrese segunda zapatilla a reservar: ")
                reservas[reserva]["vip"] = True
                print(f"Ahora {reservas[reserva]} tiene 2 pares reservados.")
            else:
                print("Manteniendo reserva actual.")
    else:
        print("Esta reserva ya es VIP.")
def cancelar():
    eliminar = input("Nombre del comprador cuya reserva desea cancelar: ")
    if eliminar in reservas:
        del reservas[eliminar]
        print(f"La reserva de {eliminar} ha sido cancelada")
    else:
        print("No se encontró ninguna reserva con ese nombre")

while opcion!=4:
    opcion=main()

    if opcion==1:
        comprar()
       
    elif opcion==2:
        buscar()
       
    elif opcion==3:
        cancelar()
   
    elif opcion==4:
        print("Programa terminado...")
   
    else:
        print("Debe ingresar una opción válida!!")