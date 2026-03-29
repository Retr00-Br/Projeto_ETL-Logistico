#!/bin/bash

# Navega até a pasta do projeto
cd ~/projeto_logistica_etl

# Ativa o ambiente virtual
source venv/bin/activate

# Executa o pipeline e salva um log com a data
echo "--- Iniciando ETL Logístico em $(date) ---" >> log_execucao.txt
python3 transformacao.py >> log_execucao.txt 2>&1
echo "--- Finalizado com sucesso ---" >> log_execucao.txt
