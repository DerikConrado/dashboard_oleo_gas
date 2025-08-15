# Dashboard Interativo da Produção de Petróleo no Rio de Janeiro

![Dashboard Screenshot](dashboard.png)

## 📖 Visão Geral do Projeto

Este repositório contém um projeto de portfólio que consiste em um dashboard interativo para a **Análise da Produção de Petróleo no Estado do Rio de Janeiro**, de 1997 a 2025. Dada a importância da indústria de Óleo & Gás para a economia do estado, especialmente para cidades como Macaé, este projeto busca fornecer uma visão clara e exploratória sobre os dados históricos de produção.

O projeto foi desenvolvido de ponta a ponta em Python, utilizando um pipeline de dados que envolve o processamento de um arquivo CSV bruto e a apresentação dos resultados em uma aplicação web construída com Streamlit.

## 🛠️ Tecnologias Utilizadas

- **Python:** Linguagem de programação principal.
- **Pandas:** Para limpeza, transformação e manipulação dos dados.
- **Streamlit:** Para a construção da aplicação web e do dashboard interativo.
- **Plotly Express:** Para a criação de gráficos dinâmicos e visualmente atraentes.
- **PyArrow:** Para leitura/escrita eficiente de arquivos no formato Parquet.

## 📊 Funcionalidades do Dashboard

- **KPIs Dinâmicos:** Métricas chave como Produção Total, Média Mensal e Pico de Produção, que se atualizam de acordo com os filtros.
- **Filtros Interativos:** Permite a filtragem dos dados por Ano e por Localização da produção (Mar ou Terra).
- **Visualizações Detalhadas:**
  - **Gráfico de Linha:** Evolução da produção mensal ao longo do tempo.
  - **Gráfico de Barras:** Produção total acumulada por ano.
  - **Gráfico de Pizza:** Distribuição percentual da produção entre Mar e Terra.
- **Tabela de Dados:** Apresentação dos dados detalhados que correspondem à seleção dos filtros.

## 🚀 Como Executar o Projeto

Siga os passos abaixo para executar o projeto em sua máquina local.

1. **Clone o repositório:**

    ```bash
    git clone [https://github.com/](https://github.com/)[SEU_USUARIO]/[SEU_REPOSITORIO].git
    cd [SEU_REPOSITORIO]
    ```

2. **Instale as dependências:**
    (Recomendado criar um ambiente virtual primeiro)

    ```bash
    pip install -r requirements.txt
    ```

    *(Para criar o arquivo `requirements.txt`, use o comando `pip freeze > requirements.txt`)*

3. **Verifique o arquivo de dados:**
    Certifique-se de que o arquivo `producao-petroleo-m3-1997-2025.csv` está dentro da pasta `data`.

4. **Execute o script de processamento:**
    Este script irá ler o CSV, limpá-lo e criar o arquivo `.parquet` otimizado.

    ```bash
    python data_processing.py
    ```

5. **Execute o dashboard:**

    ```bash
    streamlit run app.py
    ```

    Uma nova aba será aberta no seu navegador com a aplicação.

## 🌐 Fonte dos Dados

Os dados foram obtidos a partir de um arquivo CSV (`producao-petroleo-m3-1997-2025.csv`) contendo dados públicos de produção de petróleo, originalmente compilados pela Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP).

## 👨‍💻 Autor

- **Derik Conrado**
- **LinkedIn:** [https://www.linkedin.com/in/derik-conrado/]
- **E-mail:** [derikconrado@gmail.com]
