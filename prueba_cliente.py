from mi_paquete.Datoscliente import Cliente

cliente1 = Cliente("martin", "garcia", "martingarcia@gmail.com", "4535-1334")
cliente2 = Cliente("ana", "garcia", "anagarcia@gmail.com", "4535-2278")

print(cliente1) 
cliente1.imprimir_datos() 
cliente2.actualizar_email("anagarcia@hotmail.com") 
cliente2.imprimir_datos() 
