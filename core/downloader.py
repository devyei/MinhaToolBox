import os
import requests
from tqdm import tqdm

from ui.console import clear_screen, set_color, show_placeholder_message
from ui.console import COLOR_GREEN, COLOR_WHITE, COLOR_RED, COLOR_CYAN

def download_with_progress(url, friendly_name):
    """Baixa um arquivo de uma URL e exibe uma barra de progresso."""
    clear_screen()
    set_color(COLOR_CYAN)
    print("="*70)
    print(f"  Iniciando o download do {friendly_name}")
    print("="*70)
    set_color(COLOR_WHITE)

    try:
        response = requests.get(url, stream=True, allow_redirects=True, timeout=30)
        response.raise_for_status()

        filename = f"{friendly_name}_Setup.exe"
        total_size = int(response.headers.get('content-length', 0))
        print(f"\nBaixando: {filename} ({total_size / 1024 / 1024:.2f} MB)")

        progress_bar = tqdm(
            total=total_size,
            unit='iB',
            unit_scale=True,
            desc="Progresso",
            bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}]'
        )

        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    progress_bar.update(len(chunk))
                    f.write(chunk)
        progress_bar.close()

        set_color(COLOR_GREEN)
        print(f"\nDownload de '{filename}' concluído com sucesso!")
        print(f"O arquivo foi salvo em: {os.getcwd()}")
        set_color(COLOR_WHITE)

    except requests.exceptions.RequestException as e:
        set_color(COLOR_RED)
        print(f"\nOcorreu um erro de rede ao tentar baixar o arquivo: {e}")
        set_color(COLOR_WHITE)

    input("\nPressione Enter para voltar ao menu.")

def get_browser_url(browser_name):
    """Retorna a URL de download para o navegador solicitado."""
    browser_name = browser_name.lower()
    
    browser_links = {
        "brave": "https://laptop-updates.brave.com/latest/winx64",
        "firefox": "https://download.mozilla.org/?product=firefox-latest-ssl&os=win64&lang=pt-BR",
        "chrome": "https://dl.google.com/chrome/install/standalonedl/chrome_installer.exe",
        "operagx": "https://net.geo.opera.com/opera_gx/stable/windows",
        "duckduckgo": "https://static.duckduckgo.com/windows/DuckDuckGo.msix",
        "librewolf": "https://windows.librewolf.net/",
        "thorium": "https://github.com/Alex313031/thorium/releases/latest/download/Thorium_AVX2_mini_installer.exe"
    }
    return browser_links.get(browser_name, None)
