# ETL Logístico: Pipeline de Volumes e Cargas

Este projeto simula um ambiente real de Engenharia de Dados voltado para o ramo logístico. O pipeline extrai dados geográficos reais, aplica transformações de negocios e automatiza a carga em um Banco de dados (SQL).

# Ferramentas utilizadas na elaboração do projeto

 - Linguagem de Programação: Python3.X
 - Extração: BeautifulSoup4 (Web Scraping de Portos Brasileiros)
 - Tranformação: Pandas (Calculo de volume m³ e peso kg)
 - Banco de Dados: SQLite e SQLAlchemy
 - Sistema operacional utilizado: Linux (WSL)
 - Automatização: Shell Script (.sh) e Crontab (Agendamento)

# Estrutura do projeto

 1. Módulo 1: Setup do Banco de Dados e persistência.
 2. Módulo 2: Scraping de origens reais para dar veracidade aos dados coletados.
 3. Módulo 3: Scraping de origens reais para dar veracidade aos dados.
 4. Módulo 4: Automação do processo de execução diária.

# Como rodar

 1. Ativar o ambiente virtual: 'source venv/bin/activate'
 2. Instale as dependências: 'pip install -r requirements.txt'
 3. Execute o pipeline: 'bash run_pipeline.sh'

