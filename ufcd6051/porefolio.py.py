import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Portefólio - Bruno Lopes")
app.geometry("800x600")

# Frame principal
frame = ctk.CTkFrame(app, corner_radius=15)
frame.pack(padx=20, pady=20, fill="both", expand=True)

# Foto (substitui 'foto.jpg' pela tua imagem)
try:
    imagem = ctk.CTkImage(light_image=Image.open("foto.jpg"), size=(140, 140))
    foto_label = ctk.CTkLabel(frame, image=imagem, text="")
    foto_label.pack(pady=10)
except:
    erro = ctk.CTkLabel(frame, text="Adicionar foto: foto.jpg", font=("Arial", 14))
    erro.pack(pady=10)

# Nome
nome = ctk.CTkLabel(frame, text="Bruno Lopes", font=("Arial", 28, "bold"))
nome.pack(pady=5)

# Informação
info = """
Profissão: Operário de Calçado
Objetivo: Curso Técnico de Eletricista
Escolaridade: 12.º Ano
Email: brunoirvilha@hotmail.com

Competências:
• Trabalho em equipa
• Organização
• Responsabilidade
• Aprendizagem rápida
"""

texto = ctk.CTkLabel(frame, text=info, font=("Arial", 16), justify="left")
texto.pack(pady=10)

# Botão contacto
botao = ctk.CTkButton(frame, text="Contactar", command=lambda: print("Email: brunoirvilha@hotmail.com"))
botao.pack(pady=20)

app.mainloop()
