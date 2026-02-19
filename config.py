import FreeSimpleGUI as sg

def salvar_cor(cor):
    with open("preferencias.txt", "w") as f:
        f.write(cor)

def carregar_cor():
    try:
        with open("preferencias.txt", "r") as f:
            return f.read().strip()
    except:
        return "green" # cor padrão

def tela_configuracoes():
    layout = [
        [sg.Text("Escolha a cor da Cobra:", font=("Helvetica", 15))],
        # cores para o usuário clicar
        [sg.Button("Verde", button_color="green", size=(10, 2)),
         sg.Button("Azul", button_color="blue", size=(10, 2)),
         sg.Button("Amarelo", button_color="yellow", size=(10, 2))],
        [sg.Button("Vermelho", button_color="red", size=(10, 2)),
         sg.Button("Roxo", button_color="purple", size=(10, 2)),
         sg.Button("Branco", button_color="white", size=(10, 2))],
        [sg.HorizontalSeparator()],
        [sg.Button("Voltar", size=(21, 1))]
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
            
    window.close()

#tela_configuracoes() #testar