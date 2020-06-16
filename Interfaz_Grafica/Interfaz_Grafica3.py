from tkinter import *

root=Tk()
miFrame=Frame(root)
miFrame.pack()

miContraseña=StringVar()

cuadroContrasena=Entry(miFrame, textvariable=miContraseña)
cuadroContrasena.grid(row=1, column=1, padx=10, pady=10)
cuadroContrasena.config(show="*", justify="left")
contrasenaLabel=Label(miFrame, text="Contraseña:")
contrasenaLabel.grid(row=1, column=0, sticky="w", padx=10, pady=10)

textComentarios=Text(miFrame, width=15, height=5)
textComentarios.grid(row=2, column=1, padx=10, pady=10)
comentariosLablel=Label(miFrame, text="Comentarios:")
comentariosLablel.grid(row=2, column=0, sticky="w", padx=10, pady=10)
scrollVert=Scrollbar(miFrame, command=textComentarios.yview)
scrollVert.grid(row=2, column=2, sticky="nsew")
textComentarios.config(yscrollcommand=scrollVert.set)

def codigoBoton():
	miContraseña.set("Constraseña ultrasecreta")

botonEnvio=Button(root, text="Enviar", command=codigoBoton)
botonEnvio.pack()

root.mainloop()