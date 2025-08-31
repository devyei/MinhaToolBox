# MinhaToolBox

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)

MinhaToolBox é uma coleção de ferramentas de utilidade desenvolvida em Python, projetada para simplificar tarefas como download de arquivos e otimizações de sistema. A interação é feita através de uma interface de console simples e direta.

## 🚀 Funcionalidades Planejadas

O projeto está estruturado para incluir as seguintes funcionalidades:

* **Interface de Console:** Um sistema de menus para navegar entre as ferramentas disponíveis no terminal.
* **Downloader de Arquivos:** Um módulo dedicado para realizar downloads a partir de links.
* **Otimizações de Sistema (`System Tweaks`):** Ferramentas para aplicar ajustes e melhorias no sistema operacional.

## 📂 Estrutura do Projeto

O código está organizado da seguinte forma para facilitar a manutenção e o desenvolvimento:

```
MinhaToolBox/
├── .vscode/
│   └── launch.json        # Configurações do VS Code
├── core/
│   ├── __init__.py
│   ├── downloader.py      # Lógica para download de arquivos
│   └── system_tweaks.py   # Lógica para otimizações do sistema
├── ui/
│   ├── __init__.py
│   ├── console.py         # Elementos visuais do console
│   └── menus.py           # Gerenciamento dos menus da aplicação
├── main.py                # Ponto de entrada da aplicação
└── requirements.txt       # Lista de dependências
````

* A pasta `core` contém a lógica principal e as funcionalidades centrais da aplicação.
* A pasta `ui` é responsável por toda a interação com o usuário no console.
* O arquivo `main.py` inicializa e executa o programa.

## 🛠️ Tecnologias Utilizadas

* **Python**
* **requests**: Biblioteca para realizar requisições HTTP (utilizada no downloader).
* **tqdm**: Biblioteca para criar barras de progresso elegantes no console.

## 📝 A Fazer (To-Do)

-   [ ] Desenvolver a lógica completa do módulo `system_tweaks`.
-   [ ] Implementar a interface de menus no `ui/menus.py`.
-   [ ] Conectar a interface do usuário com as funções do `core`.
-   [ ] Adicionar tratamento de erros e exceções.
-   [ ] Escrever a documentação das funções.
