import requests
import json
import os

# O endereço do servidor local do Ollama
OLLAMA_API_URL = "http://localhost:11434/api/generate"

# --- O CORAÇÃO DO PROJETO: O PROMPT MESTRE (VERSÃO CORRIGIDA E CLARA) ---
# Este é o nosso "treinamento em contexto". 
PROMPT_MESTRE_TEMPLATE = """[SISTEMA]
Você é um assistente de IA especialista em Python e na biblioteca Matplotlib. Sua única função é gerar o código Python completo e pronto para ser executado para plotar o gráfico de uma função matemática que o usuário pedir. O código deve ser limpo, comentado e sempre incluir `plt.show()`. O código não deve ser cercado por ```python e ```.

[EXEMPLO 1]
USUÁRIO: "Gere o código para a função linear y = 2x + 1, no intervalo de x de -10 a 10."

SUA RESPOSTA:
import matplotlib.pyplot as plt
import numpy as np

# 1. Definir o intervalo de x
x = np.linspace(-10, 10, 400)

# 2. Definir a função linear
y = 2 * x + 1

# 3. Configurar e plotar o gráfico
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='y = 2x + 1')
plt.title('Gráfico da Função Linear')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()

# 4. Exibir o gráfico
plt.show()
[FIM DO EXEMPLO]

---

[PERGUNTA ATUAL]
USUÁRIO: "{pergunta_do_usuario}"

SUA RESPOSTA:
""" # A IA começará a gerar sua resposta a partir deste ponto.

def gerar_codigo_com_phi3(pergunta: str):
    """
    Envia uma pergunta para o Phi-3 usando o prompt mestre e retorna o código gerado.
    """
    print(f"🤖 Enviando pergunta para a IA: '{pergunta}'")
    
    # Preenche o template com a pergunta atual do usuário
    prompt_final = PROMPT_MESTRE_TEMPLATE.format(pergunta_do_usuario=pergunta)
    
    # Prepara os dados para enviar à API do Ollama
    payload = {
        "model": "phi3",
        "prompt": prompt_final,
        "stream": False,  # Queremos a resposta completa de uma vez
        "options": {
            "temperature": 0.1, # Deixa a resposta mais determinística e focada
            "stop": ["[FIM DO EXEMPLO]", "[SISTEMA]", "USUÁRIO:"] # Tokens que param a geração
        }
    }
    
    try:
        # Envia a requisição para o servidor local
        response = requests.post(OLLAMA_API_URL, json=payload)
        response.raise_for_status()  # Lança um erro se a requisição falhar
        
        # Extrai a resposta em texto do JSON retornado pelo Ollama
        response_json = response.json()
        codigo_gerado = response_json.get("response", "").strip()
        
        print("✅ IA gerou o código com sucesso!")
        return codigo_gerado
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao conectar com o Ollama: {e}")
        print("   Por favor, verifique se o Ollama está rodando.")
        return None

def executar_codigo(codigo: str):
    """
    Executa o código gerado pela IA.
    CUIDADO: `exec` é poderoso e pode ser perigoso se o código não for confiável.
    Neste caso, confiamos na nossa IA "treinada" pelo prompt.
    """
    if codigo:
        print("\n--- Executando o Código Gerado ---")
        try:
            # Garante que as bibliotecas necessárias estão disponíveis para o `exec`
            exec(codigo, {'plt': __import__('matplotlib.pyplot'), 'np': __import__('numpy')})
        except Exception as e:
            print(f"❌ Erro ao executar o código gerado: {e}")

# --- PONTO DE PARTIDA DO SCRIPT ---
if __name__ == "__main__":
    # Garante que as dependências estão instaladas antes de rodar
    try:
        import requests
        import matplotlib
        import numpy
    except ImportError:
        print("Instalando dependências (requests, matplotlib, numpy)...")
        os.system('pip install requests matplotlib numpy')
        print("Dependências instaladas. Por favor, rode o script novamente.")
        exit()

    # Exemplo de uso: Peça à IA para gerar o gráfico de qualquer função!
    
    # Pergunta 1: Função Cúbica
    pergunta_usuario = "Gere o código para a função cúbica f(x) = x**3 - x - 2, com x de -3 a 3."
    codigo_cubico = gerar_codigo_com_phi3(pergunta_usuario)
    executar_codigo(codigo_cubico)
    
    print("\n" + "="*50 + "\n")
    
    # Pergunta 2: Função Exponencial
    pergunta_usuario_2 = "Gere o código para a função exponencial y = 2**(-x), com x de -5 a 5."
    codigo_exponencial = gerar_codigo_com_phi3(pergunta_usuario_2)
    executar_codigo(codigo_exponencial)

    
