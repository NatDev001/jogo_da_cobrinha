import FreeSimpleGUI as sg
import random
import config

def rodar_jogo():

    # configurações
    cor_cobra = config.carregar_cor()
    TAMANHO_CELULA = 20
    LARGURA_CAMPO = 400
    ALTURA_CAMPO = 400
    VELOCIDADE = 0.15 

    cores_corpo = {
        "green": "darkgreen",
        "blue": "darkblue",
        "yellow": "#B8860B",
        "red": "darkred",
        "purple": "#4B0082", 
        "white": "#A9A9A9"  
    }

    cor_corpo = cores_corpo.get(cor_cobra, cor_cobra)

    def gerar_comida():
        return (random.randint(0, (LARGURA_CAMPO // TAMANHO_CELULA) - 1) * TAMANHO_CELULA,
                random.randint(0, (ALTURA_CAMPO // TAMANHO_CELULA) - 1) * TAMANHO_CELULA)

    layout = [
        [sg.Text("Pontuação: 0", key="-PONTOS-", font=("Helvetica", 14))],
        [sg.Graph(
            canvas_size=(LARGURA_CAMPO, ALTURA_CAMPO),
            graph_bottom_left=(0, 0),
            graph_top_right=(LARGURA_CAMPO, ALTURA_CAMPO),
            background_color="black",
            key="-GRAPH-",
            change_submits=True
        )],
        [sg.Button("Sair", button_color="red")]
    ]

    window = sg.Window("Python Game - Start", layout, return_keyboard_events=True, finalize=True)

    # inicialização do Jogo
    cobra = [(100, 100), (80, 100), (60, 100)]
    direcao = "Right"
    comida = gerar_comida()
    pontos = 0

    while True:
        # fps
        event, values = window.read(timeout=VELOCIDADE * 1000)

        if event in (sg.WIN_CLOSED, "Sair"):
            break

        # direção (lembrar d evitar q a cobra volte sobre si)
        if event in ("Left:37", "a", "Left", "4") and direcao != "Right":
            direcao = "Left"
        elif event in ("Right:39", "d", "Right", "6") and direcao != "Left":
            direcao = "Right"
        elif event in ("Up:38", "w", "Up", "8") and direcao != "Down":
            direcao = "Up"
        elif event in ("Down:40", "s", "Down", "2") and direcao != "Up":
            direcao = "Down"

        # logica d movimento
        cabeca_x, cabeca_y = cobra[0]
        if direcao == "Left": cabeca_x -= TAMANHO_CELULA
        elif direcao == "Right": cabeca_x += TAMANHO_CELULA
        elif direcao == "Up": cabeca_y += TAMANHO_CELULA
        elif direcao == "Down": cabeca_y -= TAMANHO_CELULA

        nova_cabeca = (cabeca_x, cabeca_y)

        # se bater na parede ou se morder
        if (cabeca_x < 0 or cabeca_x >= LARGURA_CAMPO or 
            cabeca_y < 0 or cabeca_y >= ALTURA_CAMPO or 
            nova_cabeca in cobra):
            sg.popup(f"Fim de Jogo! Pontuação Final: {pontos}")
            break

        cobra.insert(0, nova_cabeca)

        # se comer a fruta
        if nova_cabeca == comida:
            pontos += 10
            window["-PONTOS-"].update(f"Pontuação: {pontos}")
            comida = gerar_comida()
        else:
            cobra.pop() # remove a cauda se não comeu

        # desenhar na tela
        graph = window["-GRAPH-"]
        graph.erase()
        
        # desenhar Comida
        graph.draw_rectangle((comida[0], comida[1]), (comida[0] + TAMANHO_CELULA, comida[1] + TAMANHO_CELULA), fill_color="red")
        
        # desenhar Cobra
        for i, segmento in enumerate(cobra):
            cor_final = cor_cobra if i == 0 else cor_corpo
        
            graph.draw_rectangle(
                (segmento[0], segmento[1]), 
                (segmento[0] + 20, segmento[1] + 20), 
                fill_color=cor_final,
                line_color="black" # contorno pra ficar bonito
            )

    window.close()

#rodar_jogo() #testar