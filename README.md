# Painel_Tempo_Real
 Tratamento de dados para dados em streming para o PowerBI


# 📊 Monitoramento de Leituras em Tempo Real

Este projeto Python automatiza o processo de monitoramento das leituras de medidores em tempo real, com capacidade de filtrar, calcular percentuais, e gerar relatórios detalhados para diferentes gerências. Os dados são enviados para APIs para posterior processamento ou visualização.

## 🚀 Funcionalidades

- **Filtragem e Cálculo**: Filtra dados de leituras realizadas e programadas por gerência, calcula percentuais de conclusão, impedimentos, e médias de leituras.
- **Identificação de Ocorrências**: Identifica as principais ocorrências registradas por leituristas.
- **Envio de Dados**: Envia os dados processados para URLs específicas para integração com outros sistemas.
- **Relatórios**: Gera relatórios detalhados com informações sobre leituras e ocorrências por gerência e leiturista.

## 🛠️ Requisitos

Antes de começar, certifique-se de ter os seguintes requisitos:

- **Python 3.x**
- **Bibliotecas Python**: `pandas`, `requests`, `json`

## 🚀 Como Usar

1. **Clone o repositório**:
    ```bash
    git clone https://github.com/ericfp87/Painel_Tempo_Real.git
    ```

2. **Instale as dependências**:
    ```bash
    pip install pandas requests
    ```

3. **Prepare seu arquivo CSV de entrada**:
   - O arquivo CSV deve conter as colunas `MatriculaClienteImovel`, `Dia`, `VolumeMedido`, `Gerencia`, `Ocorrencia01`, `Ocorrencia02`, e `NomeFuncionario`.

4. **Execute o script**:
    - Certifique-se de que o caminho do arquivo CSV de entrada esteja correto no script.
    - Atualize os URLs das APIs para onde os dados serão enviados.
    - Execute o script:
    ```bash
    python monitoramento_leituras.py
    ```

5. **Verifique os relatórios e o envio de dados**:
   - O script imprime relatórios detalhados no console e envia os dados para os URLs especificados.

## 📂 Estrutura do Projeto

```plaintext
├── monitoramento_leituras.py            # Script principal
├── data/                                # Pasta para armazenar os arquivos CSV de entrada
│   └── LeiturasTempoRealUNMT.csv        # Arquivo CSV contendo os dados das leituras
└── OUTPUT/                              # Pasta para armazenar os resultados processados
```

## 🔍 Dicas e Sugestões

- **Performance**: O script inclui tempos de espera (`time.sleep`) para evitar sobrecarga das APIs ao enviar dados em lotes. Ajuste conforme necessário para seu ambiente.
- **Personalização**: Você pode adicionar ou modificar as gerências e ocorrências de acordo com as necessidades específicas do seu projeto.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir um *pull request* ou relatar problemas na aba de *Issues*.

## 📄 Licença

Este projeto está sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.