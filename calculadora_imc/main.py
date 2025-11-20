import customtkinter as ctk 

cor0 = "#2C3E50"  # Azul escuro
cor1 = "#FFFFFF"  # Branco puro para fundo
cor2 = "#3498DB"  # Azul do botão
cor3 = "#E5E8E8"  # Cinza claro para bordas
cor4 = "#16A085"  # Verde água para o título
cor5 = "#95A5A6"  # Cinza para textos secundários

# função para calcular o IMC
def calcular_imc():
    try:
        peso = float(e_peso.get())
        altura = float(e_altura.get())
        resultado = peso / (altura ** 2)

        l_resultado.configure(text=f"{resultado:.2f}")

        if resultado < 18.5:
            l_texto_resultado.configure(text="Seu IMC é: Abaixo do peso")
        elif 18.5 <= resultado < 24.9:
            l_texto_resultado.configure(text="Seu IMC é: Normal")
        elif 25 <= resultado < 29.9:
            l_texto_resultado.configure(text="Seu IMC é: Sobrepeso")
        else:
            l_texto_resultado.configure(text="Seu IMC é: Obesidade")

    except:
        l_resultado.configure(text="--")
        l_texto_resultado.configure(text="Erro! Digite valores válidos.")

# configuração da janela
ctk.set_appearance_mode('light')
janela = ctk.CTk()
janela.title("Calculadora de IMC")
janela.geometry('440x540')
janela.configure(fg_color=cor1)

# dividindo a janela
quadro_superior = ctk.CTkFrame(janela, width=400, height=90, corner_radius=15, fg_color=cor1)
quadro_superior.grid(row=0, column=0, sticky='nsew', padx=20, pady=20)

quadro_inferior = ctk.CTkFrame(janela, width=380, height=400, corner_radius=15, fg_color=cor1)
quadro_inferior.grid(row=1, column=0, sticky='nsew', padx=20, pady=20)

# título
nome_app = ctk.CTkLabel(
    quadro_superior, 
    text="Calculadora de IMC", 
    text_color=cor4, 
    anchor='center',
    font=('Helvetica', 30, 'bold'),
    bg_color=cor1
)
nome_app.place(x=0, y=25, relwidth=1)

# Peso
l_peso = ctk.CTkLabel(quadro_inferior, text="Digite seu peso (Kg)", text_color=cor0, font=('Helvetica', 14), bg_color=cor1)
l_peso.grid(row=0, column=0, sticky='nw', padx=15, pady=15)

e_peso = ctk.CTkEntry(quadro_inferior, width=180, font=('Helvetica', 16), justify='center', corner_radius=12)
e_peso.grid(row=0, column=1, sticky='nsew', padx=15, pady=15)

# Altura
l_altura = ctk.CTkLabel(quadro_inferior, text="Digite sua altura (m)", text_color=cor0, font=('Helvetica', 14), bg_color=cor1)
l_altura.grid(row=1, column=0, sticky='nw', padx=15, pady=15)

e_altura = ctk.CTkEntry(quadro_inferior, width=180, font=('Helvetica', 16), justify='center', corner_radius=12)
e_altura.grid(row=1, column=1, sticky='nsew', padx=15, pady=15)

# Resultado grande
l_resultado = ctk.CTkLabel(
    quadro_inferior, 
    text="----", 
    width=5, 
    height=1,
    text_color=cor0,
    font=('Helvetica', 32, 'bold'),
    anchor='center', 
    corner_radius=12,
    bg_color=cor1
)
l_resultado.grid(row=2, column=0, columnspan=2, padx=15, pady=30)

# Texto do IMC
l_texto_resultado = ctk.CTkLabel(
    quadro_inferior, 
    text="", 
    text_color=cor0, 
    font=('Helvetica', 16),
    anchor='center',
    bg_color=cor1
)
l_texto_resultado.grid(row=3, column=0, columnspan=2, padx=15, pady=15)

# Botão calcular
b_calcular = ctk.CTkButton(
    quadro_inferior, 
    text='Calcular',
    width=100, 
    height=50,
    font=('Helvetica', 16, 'bold'),
    fg_color=cor2,
    hover_color='#2980B9',
    corner_radius=12,
    command=calcular_imc
)
b_calcular.grid(row=4, column=0, columnspan=2, padx=15, pady=25)

janela.mainloop()
