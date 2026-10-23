# Conversor de Bases Numéricas

Uma aplicação web desenvolvida em **Python** com **Flask** para realizar conversões matemáticas entre diferentes sistemas de numeração: Binário, Decimal, Octal e Hexadecimal. 

A interface é amigável e responsiva, utilizando **Bootstrap 5**, com os resultados das conversões sendo exibidos de forma elegante através de janelas modais.

## 🚀 Funcionalidades

- **Conversor Binário:** Converte números de base 2 para Decimal, Octal e Hexadecimal.
- **Conversor Decimal:** Converte números de base 10 para Binário, Octal e Hexadecimal.
- **Conversor Octal:** Converte números de base 8 para Binário, Decimal e Hexadecimal.
- **Conversor Hexadecimal:** Converte números de base 16 para Binário, Decimal e Octal.
- **Validação de Entrada:** Tratamento de erros para garantir que o usuário digite apenas caracteres válidos para a base selecionada (ex: apenas 0 e 1 para binário).

## 🛠️ Tecnologias Utilizadas

- **Backend:** Python 3, Flask (Microframework)
- **Frontend:** HTML5, Jinja2 (Template Engine), Bootstrap 5 (CSS/JS via CDN)


## 📁 Estrutura do Projeto

Abaixo está a organização dos diretórios e arquivos do projeto:

```text
/
├── templates/                  # Arquivos de interface (HTML + Jinja2)
│   ├── binario.html            # Página do conversor binário
│   ├── decimal.html            # Página do conversor decimal
│   ├── equipe.html             # Página com informações da equipe
│   ├── hexadecimal.html        # Página do conversor hexadecimal
│   ├── index.html              # Página inicial (Home)
│   └── octal.html              # Página do conversor octal
├── venv/                       # Ambiente virtual Python (ignorado no git)
├── .gitignore                  # Arquivos ignorados pelo Git (ex: venv, __pycache__)
├── app.py                      # Arquivo principal que gerencia as rotas do Flask
├── conversor_binario.py        # Lógica matemática de conversão (Binário)
├── conversor_decimal.py        # Lógica matemática de conversão (Decimal)
├── conversor_hexadecimal.py    # Lógica matemática de conversão (Hexadecimal)
├── conversor_octal.py          # Lógica matemática de conversão (Octal)
└── requirements.txt            # Lista de dependências do projeto (Flask, etc.)
```

## ⚙️ Como executar o projeto localmente

Siga os passos abaixo para rodar a aplicação na sua máquina:

1. **Clone o repositório ou extraia os arquivos** em uma pasta local.
2. **Abra o terminal** na raiz do projeto.
3. **Crie e ative o ambiente virtual:**
   - python -m venv venv
   - No Windows: `.\venv\Scripts\activate`
   - No Linux/Mac: `source venv/bin/activate`
   
4. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```
5. **Execute a aplicação Flask:**
   ```bash
   python app.py
   ```
6. **Acesse no navegador:**
   Abra o seu navegador e acesse o endereço `http://127.0.0.1:5000` (ou `http://localhost:5000`).

## 👥 Equipe
*Projeto desenvolvido por [Agabo/Gustavo/José/Tiago]. Acesse a aba "Equipe" na aplicação para mais detalhes.*