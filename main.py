import os
import sys
import subprocess
import ctypes

project_root = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, project_root)

import ui.menus as menus
from ui.console import set_color, clear_screen, show_placeholder_message, COLOR_RED, COLOR_GREEN, COLOR_WHITE

def check_and_install_packages():
    """Verifica se os pacotes necessários estão instalados e, se não, os instala."""
    try:
        import requests
        from tqdm import tqdm
    except ImportError:
        print("Pacotes necessários não encontrados. Tentando instalar...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "requests", "tqdm"])
            print("\nPacotes instalados com sucesso! Por favor, execute o script novamente.")
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("\nERRO: Falha ao instalar pacotes automaticamente.")
            print("Por favor, instale-os manualmente: pip install requests tqdm")
        
        input("\nPressione Enter para sair.")
        sys.exit(0)

def main_menu():
    """Exibe o menu principal e gerencia a navegação."""
    menu_actions = {
        "1": menus.menu_action_center,
        "2": menus.menu_event_viewer,
        "3": menus.menu_store_cache,
        "5": menus.menu_hibernation,
        "6": menus.menu_pagefile,
        "7": menus.menu_take_ownership,
        "9": menus.menu_compact_os,
        "11": menus.menu_store_uwp,
        "20": menus.menu_clipboard,
        "22": menus.navegadores,
        "24": menus.menu_personalizacao,
    }
    
    while True:
        clear_screen(); set_color(COLOR_GREEN)
        print("""
========================================================================================
                                ADMINISTRATOR: MinhaToolBox
========================================================================================

 TWEAK / FIXED / CLEANER                               OTHER / ETC
 =======================                               ===========
 [1] Action Center & Notificações                      [22] Navegadores
 [2] Limpar Logs de Eventos                            [24] Personalização do Windows
 [3] Limpar Cache de Updates                           [31] Recuperação do Windows (WinRE)
 [5] Hibernação / Fastboot                             [34] Alterar nome de Administrador
 [6] Arquivo de Paginação                              [35] Esquemas de Cores do CMD
 [7] Obter Controle (Take Ownership)                   [38] Windows Update Standalone
 [8] Parar Updates do Windows                          [39] Otimização para Jogos
 [9] Compactação do Sistema (LZX)                      [40] Clientes de Jogos

 UWP APPS / OUTROS
 =================
 [11] Microsoft Store & Xbox
 [19] Microsoft Xbox Game Bar
 [20] Clipboard e Teclado Virtual
 [23] Microsoft Xbox Game Pass
 [26] Microsoft Zune Music
 [28] Microsoft Seu Telefone
 [29] Microsoft .NET Framework
 [30] Microsoft OneDrive
 [43] Opções para Windows 11
 
 [Q] Sair do Programa
 
========================================================================================
        """)
        set_color(COLOR_WHITE)
        choice = input("Digite a opção: ").lower()

        if choice in menu_actions:
            menu_actions[choice]()
        elif choice in ['q', 'quit', 'exit']:
            print("Saindo..."); break
        else:
            show_placeholder_message(f"Opção [{choice}] (Ainda não implementada)")

if __name__ == "__main__":
    
    is_dev_mode = "--dev" in sys.argv

    check_and_install_packages()

    if not is_dev_mode:
        try:
            is_admin = (os.getuid() == 0)
        except AttributeError: 
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

        if not is_admin:
            set_color(COLOR_RED)
            print("Erro: Por favor, execute este script como Administrador.")
            print("Para testes de UI, use o modo de desenvolvimento: python main.py --dev")
            set_color(COLOR_WHITE)
            input("Pressione Enter para sair.")
            sys.exit(1)

    if os.name == 'nt':
        os.system("title MinhaToolBox")
    
    if is_dev_mode:
        print("--- EXECUTANDO EM MODO DE DESENVOLVIMENTO (ADMIN CHECK DESATIVADO) ---")

    main_menu()
    
    set_color(COLOR_WHITE)
