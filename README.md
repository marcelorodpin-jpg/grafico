# 📊 Analisador de Planilhas com Gráfico Automático

Este é um programa automatizado que **abre e lê uma planilha do Excel, analisa os dados inseridos e gera um gráfico de colunas** de forma totalmente automática. Ideal para otimizar relatórios e visualizar dados com apenas um clique.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**: Linguagem base do projeto.
- **Pandas**: Para a leitura, manipulação e análise eficiente dos dados da planilha.
- **Matplotlib / Seaborn**: Para a renderização e estilização do gráfico de colunas.
- **Openpyxl**: Engine necessária para a integração e leitura de arquivos `.xlsx`.

---

## 🚀 Como Funciona?

1. **Leitura:** O script busca e abre o arquivo Excel configurado (ex: `dados.xlsx`).
2. **Processamento:** O Pandas limpa, filtra ou agrupa as informações necessárias para a análise.
3. **Visualização:** O programa gera um gráfico de colunas e o exibe na tela (ou salva automaticamente como uma imagem `.png`/`.jpg`).

---

## 📦 Como Instalar e Executar

### Pré-requisitos
Certifique-se de ter o **Python** instalado na sua máquina.

### 1. Clonar o repositório
```bash
git clone https://github.com
cd nome-do-repositorio
```

### 2. Instalar as dependências
Instale as bibliotecas necessárias utilizando o gerenciador de pacotes `pip`:
```bash
pip install pandas matplotlib openpyxl
```

### 3. Executar o programa
Coloque sua planilha na pasta raiz do projeto com o nome correto e execute:
```bash
python main.py
```

---

## 📊 Exemplo de Resultado

O programa lerá dados estruturados (como vendas por mês, produtos mais vendidos, etc.) e gerará um gráfico parecido com este:

