# teste_leitura.py

import pandas as pd
import os

print("--- INICIANDO TESTE DE LEITURA ---")
print("Este script vai tentar ler apenas as 10 primeiras linhas do seu CSV.")

# Define o caminho do arquivo
caminho_do_arquivo = os.path.join("data", "producao-petroleo-m3-1997-2025.csv")
print(f"Caminho do arquivo: {caminho_do_arquivo}")

# Verifica se o arquivo existe no caminho especificado
if not os.path.exists(caminho_do_arquivo):
    print("\n--- ERRO: Arquivo não encontrado! ---")
    print("Verifique se o nome do arquivo e da pasta 'data' estão corretos.")
else:
    try:
        print("\nTENTANDO LER o arquivo agora... Por favor, aguarde.")
        
        # Tentamos ler apenas as 10 primeiras linhas para ser mais rápido e seguro
        df_teste = pd.read_csv(
            caminho_do_arquivo, 
            sep=';', 
            encoding='latin-1',
            nrows=10  # <<<--- ESTE É O PARÂMETRO MAIS IMPORTANTE DO TESTE
        )
        
        print("\n--- SUCESSO! A leitura funcionou! ---")
        print("As 10 primeiras linhas do arquivo foram lidas com sucesso.")
        print("Abaixo estão as colunas encontradas:")
        print(df_teste.columns.tolist())
        
    except Exception as e:
        print(f"\n--- ERRO DURANTE A LEITURA! ---")
        print(f"Ocorreu um erro inesperado: {e}")

print("\n--- FIM DO TESTE DE LEITURA ---")