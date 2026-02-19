import FreeSimpleGUI as sg

def salvar_cor(cor, progressivo):
    with open("preferencias.txt", "w") as f:
        f.write(f"{cor}\n{progressivo}")

def carregar_cor():
    try:
        with open("preferencias.txt", "r") as f:
            linhas = f.readlines()
            cor = linhas[0].strip()
            # converte a string 'True' ou 'False' de volta para booleano
            progressivo = linhas[1].strip() == "True"
            return cor, progressivo
    except:
        return "green", True # cor padrão

def tela_configuracoes():
    cor, modo_prog = carregar_cor()
    
    layout = [
        [sg.Text("Escolha a cor da Cobra:", font=("Helvetica", 15))],
        # cores para clicar
        [sg.Button("Verde", button_color="green", size=(10, 2)),
         sg.Button("Azul", button_color="blue", size=(10, 2)),
         sg.Button("Amarelo", button_color="yellow", size=(10, 2))],
        [sg.Button("Vermelho", button_color="red", size=(10, 2)),
         sg.Button("Roxo", button_color="purple", size=(10, 2)),
         sg.Button("Branco", button_color="white", size=(10, 2))],
        [sg.HorizontalSeparator()],

        [sg.Text("Dificuldade Progressiva:", font=("Helvetica", 12))],
        # botão de liga/desliga
        [sg.Button("LIGADO" if modo_prog else "DESLIGADO", 
            key="-PROG-", 
            button_color=("white", "green" if modo_prog else "red"),
            size=(15, 1), pad=(0, 10))],
        [sg.HorizontalSeparator()],

        [sg.Button("Voltar", size=(15, 1), pad=(0, 20))]
    ]
    
    window = sg.Window("Configurações", layout, element_justification="c", finalize=True)
    
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Voltar"):
            break
        
        # salvar e avisar
        if event in ["Verde", "Azul", "Amarelo", "Vermelho", "Roxo", "Branco"]:
            cores_map = {
                "Verde": "green", "Azul": "blue", "Amarelo": "yellow",
                "Vermelho": "red", "Roxo": "purple", "Branco": "white"
            }
            salvar_cor(cores_map[event])
            sg.popup(f"Cor alterada para {event}!")

        if event == "-PROG-":
            modo_prog = not modo_prog # Inverte o valor (True vira False e vice-versa)
            texto = "LIGADO" if modo_prog else "DESLIGADO"
            cor_btn = "green" if modo_prog else "red"
            window["-PROG-"].update(texto, button_color=("white", cor_btn))
            salvar_cor(cor, modo_prog)
            
    window.close()

#tela_configuracoes() #testar