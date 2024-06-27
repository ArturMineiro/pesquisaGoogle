import webbrowser
import time
import pyautogui
import pyperclip

# Função para abrir o navegador e o Google
def open_google():
    webbrowser.open("https://www.google.com")

# Simula cliques e entradas de teclado
def simulate_clicks():
    time.sleep(5)  # Aguarda o navegador abrir

    # Coordenadas da barra de pesquisa no Google (ajuste conforme necessário)
    search_box_coords = (2138, 85)

    # Clique na barra de pesquisa
    pyautogui.click(*search_box_coords)
    time.sleep(2)
    
    # Digitar a consulta de pesquisa usando pyperclip
    query = 'jogo da seleção'
    pyperclip.copy(query)
    pyautogui.hotkey('ctrl', 'v')
    
    time.sleep(1)
    # Pressionar Enter
    pyautogui.press('enter')

if __name__ == "__main__":
    open_google()
    simulate_clicks()
