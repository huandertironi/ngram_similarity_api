# ngram_similarity_api

API leve em Flask que calcula a similaridade entre palavras utilizando a técnica de **n-gramas (bigramas)**. Ideal para sugestões de ortografia, busca por palavras similares e aplicativos de NLP básicos.

---

## Funcionalidades

- Carrega um vocabulário do arquivo `pt‑BR.txt` contendo palavras do português brasileiro.
- Calcula a similaridade entre a palavra digitada e cada termo do vocabulário usando a fórmula do coeficiente de Sørensen–Dice:

  ![Fórmula da Similaridade](https://latex.codecogs.com/png.image?\dpi{120}&space;S=\frac{2C}{A+B})

  onde:
  - \( A \) e \( B \): tamanho do conjunto de n‑gramas de cada palavra;
  - \( C \): número de n‑gramas em comum.
- Exibe as palavras mais similares, ordenadas por similaridade.

---

## Tecnologias

- **Python 3.11+**
- **Flask** (microframework web)
- **Docker** (para conteinerização opcional)

---

## Como executar

### Sem Docker

1. Clone o repositório:
   ```bash
   git clone https://github.com/huandertironi/ngram_similarity_api.git
   cd ngram_similarity_api
   ```
2. Crie um ambiente virtual e instale dependências:

   ```bash
   python -m venv venv
   source venv/bin/activate  # no Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

4. Execute a API:

   `python app.py`

6. Acesse no navegador ou via curl:

   `http://127.0.0.1:5000/similar?word=abacate&n=2`

### Com Docker (opcional)

1. Construa a imagem:

   `docker build -t ngram-similarity-api .`

2. Execute o container:

   `docker run -p 5000:5000 ngram-similarity-api`

4. Acesse:

    `http://localhost:5000/similar?word=abacaxi&n=2`


## Exemplo de resposta JSON

   ```bash
   [
     {"word": "abacate", "similarity": 1.0},
     {"word": "abacaxi", "similarity": 0.75},
     {"word": "abacá", "similarity": 0.5},
     {"word": "abacás", "similarity": 0.5},
     {"word": "abade", "similarity": 0.33}
   ]
   ```

##  Sugestões de uso

🔤 Corretores ortográficos com sugestões dinâmicas.

🤖 Integração com chatbots (Telegram, Discord, etc.).

📚 Aplicações de NLP para educação ou jogos linguísticos.

🧪 Ferramentas para pesquisa linguística e lexicografia.

   
