import random
import pandas as pd
from datetime import datetime
from extracao import extrair_origens

def transformar_dados(lista_cidades):
    print(f"Iniciando transformação de {len(lista_cidades)} registros...")
    
    dados_logisticos = []
    
    for cidade in lista_cidades:
        # Gerando dados fictícios
        peso = round(random.uniform(1.0, 500.0), 2)  # Peso entre 1kg e 500kg
        volume = round(peso * 0.005, 3)              # Volume proporcional ao peso
        codigo_carga = f"BR-{random.randint(1000, 9999)}-{cidade[:3].upper()}"
        
        registro = {
            'codigo_carga': codigo_carga,
            'origem_cidade': cidade,
            'volume_m3': volume,
            'peso_kg': peso,
            'data_registro': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'status_entrega': random.choice(['Em Trânsito', 'Processando', 'Despachado'])
        }
        dados_logisticos.append(registro)
    
    # Convertendo para DataFrame para manipulação avançada
    df = pd.DataFrame(dados_logisticos)
    return df

if __name__ == "__main__":
    # Testando o fluxo
    cidades = extrair_origens()
    if cidades:
        df_final = transformar_dados(cidades)
        print("\n--- Amostra dos Dados Transformados ---")
        print(df_final.head())
    else:
        print("Erro: Nenhuma cidade encontrada para transformar.")	

from database_setup import engine

if __name__ == "__main__":
    cidades = extrair_origens()
    if cidades:
        df_final = transformar_dados(cidades)
        
        print("\nEnviando dados para o banco de dados...")
        
        # if_exists='append' garante que ele adicione novos dados sem apagar os antigos
        df_final.to_sql('volumes', con=engine, if_exists='append', index=False)
        
        print("✅ Sucesso! Dados carregados na tabela 'volumes'.")
    else:
        print("Erro: Nenhuma cidade encontrada.")
