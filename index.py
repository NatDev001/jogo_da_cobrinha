import FreeSimpleGUI as sg
import jogo
import config

def tela_menu():
    LARGURA, ALTURA = 400, 400

    layout = [
        [sg.Graph(
            canvas_size=(LARGURA, ALTURA),
            graph_bottom_left=(0, 0),
            graph_top_right=(LARGURA, ALTURA),
            key="-GRAPH-",
            enable_events=True,
            pad=(0,0) # remove padding
        )]
    ]

    window = sg.Window("Python Game - Menu", layout, finalize=True, margins=(0,0), element_padding=(0,0))
    
    graph = window["-GRAPH-"]
    
    # background
    graph.draw_image(filename="pg_fundo.png", location=(0, ALTURA))

    # botão Iniciar
    graph.draw_rectangle((100, 205), (300, 155), fill_color='#37504B', line_color='white')
    graph.draw_text("INICIAR", (200, 180), color='white', font=("Helvetica", 14, "bold"))

    # botão Configurações
    graph.draw_rectangle((100, 145), (300, 95), fill_color='#37504B', line_color='white')
    graph.draw_text("CONFIGURAÇÕES", (200, 120), color='white', font=("Helvetica", 12, "bold"))

    # botão Sair
    graph.draw_rectangle((100, 85), (300, 35), fill_color='#37504B', line_color='white')
    graph.draw_text("SAIR", (200, 60), color='white', font=("Helvetica", 14, "bold"))

    return window

# Loop do Menu com 'clic'
window = tela_menu()

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, "Sair"):
        break

    if event == "-GRAPH-":
        x, y = values["-GRAPH-"]
        
        if 100 <= x <= 300 and 155 <= y <= 205:
            window.hide()
            jogo.rodar_jogo()
            window.un_hide()
            
        elif 100 <= x <= 300 and 95 <= y <= 145:
            window.hide()
            config.tela_configuracoes() # tela de escolha de cores
            window.un_hide()

        elif 100 <= x <= 300 and 60 <= y <= 86:
            break

window.close()