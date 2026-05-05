import customtkinter as ctk
import webbrowser

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')

app = ctk.CTk()
app.title('Portefólio - Bruno Lopes')
app.geometry('900x600')

# Função para abrir GitHub

def abrir_github():
    webbrowser.open('https://github.com/')

# Título
titulo = ctk.CTkLabel(
    app,
    text='Bruno Lopes',
    font=('Arial', 32, 'bold')
)
titulo.pack(pady=20)

subtitulo = ctk.CTkLabel(
    app,
    text='Portefólio Profissional em CustomTkinter',
    font=('Arial', 20)
)
subtitulo.pack(pady=5)

# Frame principal
frame = ctk.CTkFrame(app, corner_radius=15)
frame.pack(padx=20, pady=20, fill='both', expand=True)

# Sobre mim
sobre = ctk.CTkLabel(
    frame,
    text='Operário de calçado, 40 anos, com curso de eletricidade e projetos desenvolvidos nas UFCD publicados no GitHub.',
    font=('Arial', 16),
    wraplength=700
)
sobre.pack(pady=20)

# Trabalhos / UFCDs
ufcd_label = ctk.CTkLabel(
    frame,
    text='UFCD Realizadas',
    font=('Arial', 22, 'bold')
)
ufcd_label.pack(pady=10)

lista_ufcd = ctk.CTkTextbox(frame, width=600, height=180)
lista_ufcd.pack(pady=10)
lista_ufcd.insert('0.0', '- UFCD 1: Programação Python\n- UFCD 2: Bases de Dados\n- UFCD 3: Desenvolvimento de Interfaces\n- UFCD 4: Projeto Final')
lista_ufcd.configure(state='disabled')

# Botão GitHub
botao = ctk.CTkButton(
    frame,
    text='Ver GitHub',
    command=abrir_github,
    width=200,
    height=40
)
botao.pack(pady=25)

app.mainloop()
