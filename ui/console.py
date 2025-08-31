import os
import ctypes

COLOR_GREEN = 10
COLOR_WHITE = 15
COLOR_RED = 12
COLOR_CYAN = 11

def set_color(color_code):
    """Muda a cor do texto no console do Windows."""
    if os.name == 'nt':
        kernel32 = ctypes.windll.kernel32
        handle = kernel32.GetStdHandle(-11)
        kernel32.SetConsoleTextAttribute(handle, color_code)

def clear_screen():
    """Limpa a tela do console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_placeholder_message(action_description):
    """Exibe uma mensagem padronizada para funções ainda não implementadas."""
    clear_screen()
    set_color(COLOR_WHITE)
    print("="*60)
    print(f"  Ação selecionada: {action_description}")
    print("="*60)
    print("\n[AVISO] Esta é uma função de exemplo (placeholder).")
    print("O comando real para executar esta ação precisa ser adicionado ao código.")
    set_color(COLOR_RED)
    print("\n--> Nenhuma alteração foi feita no sistema. <--")
    set_color(COLOR_WHITE)
    input("\nPressione qualquer tecla para voltar ao menu anterior...")
