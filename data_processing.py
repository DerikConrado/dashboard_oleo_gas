# data_processing.py (VERSÃO FINAL E CORRIGIDA)

import pandas as pd
import os

print("--- INICIANDO SCRIPT DE PROCESSAMENTO ---")

INPUT_CSV_PATH = os.path.join("data", "producao-petroleo-m3-1997-2025.csv")
OUTPUT_PARQUET_PATH = os.path.join("data", "producao_rio_de_janeiro.parquet")

def processar_dados_locais():
    try:
        print(f"Lendo arquivo: {INPUT_CSV_PATH}")
        
        # --- CORREÇÃO DE ENCODING ---
        # Usando 'utf-8-sig' para lidar com o BOM (ï»¿) e os acentos corretamente
        df = pd.read_csv(INPUT_CSV_PATH, sep=';', encoding='utf-8-sig')
        
        print("Arquivo CSV lido com sucesso!")

        # Forçando a renomeação de todas as colunas pela sua ordem
        nomes_colunas = [
            'ano', 'mes', 'grande_regiao', 'uf', 'produto', 
            'localizacao', 'producao_m3'
        ]
        df.columns = nomes_colunas
        print("Colunas renomeadas com sucesso.")

        # Converte as colunas de texto para MAIÚSCULAS e remove espaços
        df['uf'] = df['uf'].str.upper().str.strip()
        df['produto'] = df['produto'].str.upper().str.strip()
        
        # Filtrar apenas dados de Petróleo e do Rio de Janeiro
        df_rj = df[(df['uf'] == 'RIO DE JANEIRO') & (df['produto'] == 'PETRÓLEO')].copy()
        print(f"Dados filtrados para Rio de Janeiro e Petróleo. Total de {len(df_rj)} registros encontrados.")
        
        if not df_rj.empty:
            mes_map = {
                'JAN': 1, 'FEV': 2, 'MAR': 3, 'ABR': 4, 'MAI': 5, 'JUN': 6,
                'JUL': 7, 'AGO': 8, 'SET': 9, 'OUT': 10, 'NOV': 11, 'DEZ': 12
            }
            df_rj['mes_num'] = df_rj['mes'].map(mes_map)
            df_rj['data'] = pd.to_datetime(df_rj['ano'].astype(str) + '-' + df_rj['mes_num'].astype(str) + '-01')
            df_rj['producao_m3'] = df_rj['producao_m3'].str.replace(',', '.').astype(float)
            df_rj = df_rj[df_rj['producao_m3'] > 0]
        
        df_final = df_rj[['data', 'ano', 'mes', 'uf', 'localizacao', 'producao_m3']] if not df_rj.empty else pd.DataFrame(columns=['data', 'ano', 'mes', 'uf', 'localizacao', 'producao_m3'])

        os.makedirs("data", exist_ok=True)
        df_final.to_parquet(OUTPUT_PARQUET_PATH, index=False)
        
        print("\n--- SUCESSO! Processamento concluído! ---")
        print(f"Arquivo '{os.path.basename(OUTPUT_PARQUET_PATH)}' foi criado/atualizado na pasta 'data'.")

    except Exception as e:
        print(f"\n--- ERRO CRÍTICO INESPERADO: {e} ---")

if __name__ == "__main__":
    processar_dados_locais()