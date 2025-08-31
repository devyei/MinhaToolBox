from ui.console import clear_screen, set_color, show_placeholder_message
from ui.console import COLOR_GREEN, COLOR_WHITE
from core.downloader import download_with_progress, get_browser_url

def menu_action_center():
    while True:
        clear_screen(); set_color(COLOR_GREEN)
        print("""
========================================================================
 Action Center, Cortana e Impressão
========================================================================
 [1] Ativar  | Action Center e Notificações
 [2] Desativar | Action Center e Notificações
------------------------------------------------------------------------
 [3] Ativar  | Cortana
 [4] Desativar | Cortana
------------------------------------------------------------------------
 [5] Ativar  | Spooler de Impressão (Automático)
 [6] Desativar | Spooler de Impressão (Manual)
------------------------------------------------------------------------
 [0] Voltar ao Menu Principal
========================================================================
        """)
        set_color(COLOR_WHITE)
        choice = input("Digite a opção: ")
        if choice == '1': show_placeholder_message("Ativar Action Center")
        elif choice == '2': show_placeholder_message("Desativar Action Center")
        elif choice == '3': show_placeholder_message("Ativar Cortana")
        elif choice == '4': show_placeholder_message("Desativar Cortana")
        elif choice == '0': break
        else: input("Opção inválida. Pressione Enter para tentar novamente.")

def menu_event_viewer():
    while True:
        clear_screen(); set_color(COLOR_GREEN)
        print("""
========================================================================
 Logs de Eventos do Windows
========================================================================
 [1] Limpar todos os logs agora
 [2] Desativar alguns logs de eventos
------------------------------------------------------------------------
 [0] Voltar ao Menu Principal
========================================================================
        """)
        set_color(COLOR_WHITE)
        choice = input("Digite a opção: ")
        if choice == '1': show_placeholder_message("Limpar Logs de Eventos")
        elif choice == '2': show_placeholder_message("Desativar Logs de Eventos")
        elif choice == '0': break
        else: input("Opção inválida. Pressione Enter para tentar novamente.")

def menu_store_cache():
    while True:
        clear_screen(); set_color(COLOR_GREEN)
        print("""
========================================================================
 Limpeza de Cache da Windows Store
========================================================================
 [1] Limpar cache da Store e Otimização de Entrega
------------------------------------------------------------------------
 [0] Voltar ao Menu Principal
========================================================================
        """)
        set_color(COLOR_WHITE)
        choice = input("Digite a opção: ")
        if choice == '1': show_placeholder_message("Limpar Cache da Windows Store")
        elif choice == '0': break
        else: input("Opção inválida. Pressione Enter para tentar novamente.")

def menu_hibernation():
    while True:
        clear_screen(); set_color(COLOR_GREEN)
        print("""
========================================================================
 Hibernação / Fastboot / Sysmain
========================================================================
 [1] Desativar : hiberfil.sys
 [2] Ativar  : hiberfil.sys
------------------------------------------------------------------------
 [3] Desativar : Sysmain / Superfetch
 [4] Ativar  : Sysmain / Superfetch
------------------------------------------------------------------------
 [0] Voltar ao Menu Principal
========================================================================
        """)
        set_color(COLOR_WHITE)
        choice = input("Digite a opção: ")
        if choice == '1': show_placeholder_message("Desativar Hibernação")
        elif choice == '2': show_placeholder_message("Ativar Hibernação")
        elif choice == '3': show_placeholder_message("Desativar Sysmain")
        elif choice == '4': show_placeholder_message("Ativar Sysmain")
        elif choice == '0': break
        else: input("Opção inválida. Pressione Enter para tentar novamente.")

def menu_pagefile():
    while True:
        clear_screen(); set_color(COLOR_GREEN)
        print("""
========================================================================
 Arquivo de Paginação (Memória Virtual)
========================================================================
 [1] Desativar   : Pagefile.sys
 [2] Ativar    : Pagefile.sys [256MB]
 [3] Ativar    : Pagefile.sys [3.0GB]
 [4] Ativar    : Pagefile.sys [4.0GB]
 [5] Ativar    : Pagefile.sys [8.0GB]
 [6] Ativar    : Pagefile.sys [16.0GB]
 [7] Ativar    : Pagefile.sys [Gerenciado pelo Sistema]
------------------------------------------------------------------------
 [0] Voltar ao Menu Principal
========================================================================
        """)
        set_color(COLOR_WHITE)
        choice = input("Digite a opção: ")
        if choice == '1': show_placeholder_message("Desativar Pagefile")
        elif choice == '7': show_placeholder_message("Definir Pagefile como Gerenciado pelo Sistema")
        elif choice == '0': break
        else: input("Opção inválida. Pressione Enter para tentar novamente.")

def menu_take_ownership():
    while True:
        clear_screen(); set_color(COLOR_GREEN)
        print("""
========================================================================
 Menu de Contexto 'Take Ownership' (Obter Controle)
========================================================================
 [1] Adicionar ao menu de contexto do clique direito
 [2] Remover do menu de contexto
------------------------------------------------------------------------
 [0] Voltar ao Menu Principal
========================================================================
        """)
        set_color(COLOR_WHITE)
        choice = input("Digite a opção: ")
        if choice == '1': show_placeholder_message("Adicionar 'Take Ownership'")
        elif choice == '2': show_placeholder_message("Remover 'Take Ownership'")
        elif choice == '0': break
        else: input("Opção inválida. Pressione Enter para tentar novamente.")
        
def menu_compact_os():
    while True:
        clear_screen(); set_color(COLOR_GREEN)
        print("""
========================================================================
 Compactação do Sistema Operacional (LZX)
========================================================================
 [1] Compactar OS LZX (Recomendado para SSD/NVMe)
 [2] Usar compactação normal (Reverter)
------------------------------------------------------------------------
 [0] Voltar ao Menu Principal
========================================================================
        """)
        set_color(COLOR_WHITE)
        choice = input("Digite a opção: ")
        if choice == '1': show_placeholder_message("Compactar OS com LZX")
        elif choice == '2': show_placeholder_message("Reverter para compactação normal")
        elif choice == '0': break
        else: input("Opção inválida. Pressione Enter para tentar novamente.")

def menu_store_uwp():
    while True:
        clear_screen(); set_color(COLOR_GREEN)
        print("""
========================================================================
 Microsoft Store e Apps UWP
========================================================================
 [1] Instalar Microsoft Store & Xbox Companion (UWP)
 [2] Remover Microsoft Store & Xbox Companion (UWP)
------------------------------------------------------------------------
 [0] Voltar ao Menu Principal
========================================================================
        """)
        set_color(COLOR_WHITE)
        choice = input("Digite a opção: ")
        if choice == '1': show_placeholder_message("Instalar Microsoft Store")
        elif choice == '2': show_placeholder_message("Remover Microsoft Store")
        elif choice == '0': break
        else: input("Opção inválida. Pressione Enter para tentar novamente.")

def menu_clipboard():
    while True:
        clear_screen(); set_color(COLOR_GREEN)
        print("""
========================================================================
 Clipboard (Área de Transferência) e Teclado Virtual
========================================================================
 [1] Ativar  | Histórico da Área de Transferência
 [2] Desativar | Histórico da Área de Transferência
------------------------------------------------------------------------
 [3] Ativar  | Teclado Virtual / Touch Keyboard
------------------------------------------------------------------------
 [0] Voltar ao Menu Principal
========================================================================
        """)
        set_color(COLOR_WHITE)
        choice = input("Digite a opção: ")
        if choice == '1': show_placeholder_message("Ativar Histórico do Clipboard")
        elif choice == '2': show_placeholder_message("Desativar Histórico do Clipboard")
        elif choice == '3': show_placeholder_message("Ativar Teclado Virtual")
        elif choice == '0': break
        else: input("Opção inválida. Pressione Enter para tentar novamente.")

def menu_personalizacao():
    while True:
        clear_screen(); set_color(COLOR_GREEN)
        print("""
========================================================================
 Personalização do Windows
========================================================================
 [1] Download de Wallpapers Sugeridos
------------------------------------------------------------------------
 [2] Cores - Tema Roxo Escuro
 [8] Cores - Tema Padrão Branco do Windows
 [9] Cores - Tema Padrão Escuro do Windows
------------------------------------------------------------------------
 [10] Ativar  : Explorer UI Ribbon
 [11] Desativar : Explorer UI Ribbon
------------------------------------------------------------------------
 [12] Ativar  : Barra de Tarefas Transparente
 [13] Desativar : Barra de Tarefas Transparente
------------------------------------------------------------------------
 [0] Voltar ao Menu Principal
========================================================================
        """)
        set_color(COLOR_WHITE)
        choice = input("Digite a opção: ")
        if choice == '1': show_placeholder_message("Download de Wallpapers")
        elif choice == '10': show_placeholder_message("Ativar Explorer UI Ribbon")
        elif choice == '0': break
        else: input("Opção inválida. Pressione Enter para tentar novamente.")

def navegadores():
    browser_map = {
        '1': 'brave', '2': 'firefox', '3': 'chrome', '4': 'duckduckgo',
        '5': 'librewolf', '6': 'operagx', '7': 'thorium',
    }
    
    while True:
        clear_screen(); set_color(COLOR_GREEN)
        print("""
========================================================================
  Navegadores
========================================================================
  [1] Brave
  [2] FireFox
  [3] Chrome
  [4] DuckDuck GO
  [5] LibraWolf
  [6] Opera GX
  [7] Thorium
  [8] Tor

  [0] Voltar ao Menu Principal
========================================================================
        """)
        set_color(COLOR_WHITE)
        choice = input("Digite a opção: ")
        
        if choice in browser_map:
            browser_key = browser_map[choice]
            url = get_browser_url(browser_key)
            if url:
                download_with_progress(url, browser_key.capitalize())
            else:
                show_placeholder_message(f"Link de download não encontrado para {browser_key.capitalize()}.")
        elif choice == '8': 
            show_placeholder_message("Download de Tor (não implementado)")
        elif choice == '0': 
            break
        else: 
            input("Opção inválida. Pressione Enter para tentar novamente.")
