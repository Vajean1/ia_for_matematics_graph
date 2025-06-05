import requests
import json

# Baixar o modelo antes.
# Endereço local do Ollama API - Utilizando o Phi-3 da microsoft open-source com 3 Bilhões de parâmetros.
OLLAMA_API_URL = "http://localhost:11434/api/generate"

# --- O CORAÇÃO DO PROJETO: O PROMPT MESTRE --- Usando few-shot prompting (Exemplo perfeito) learning (treinamento em contexto) e depois a pergunta do usuário.

PROMPT_MESTRE_TEMPLATE = """
[SISTEMA]
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
"""

def gerar_codigo_com_phi3(pergunta: str):
    """
    Envia uma pergunta para o Phi-3 usando o prompt mestre e retorna o código gerado.
    """
    print(f"Enviando pergunta para o modelo Phi-3: '{pergunta}'")
    
    prompt_final = PROMPT_MESTRE_TEMPLATE.format(pergunta_do_usuario=pergunta)
    
    # Payload de dados para enviar ao Ollama
    payload = {
        "model": "phi3", 
        "prompt": prompt_final,
        "stream": False
    }
    
    try:
        #Envia a requisição para o servidor local do ollama
        response = requests.post(OLLAMA_API_URL, json=payload)
        response.raise_for_status()
        
        # Extrai a resposta em texto do JSON retornado pelo Ollama
        response_json = response.json()
        codigo_gerado = response_json.get("response", "").strip()
        
        print("IA gerou o código com sucesso!")
        return codigo_gerado
        
    except requests.exceptions.RequestException as e:
        print(f"erro ao conectar com o Ollama: {e}")
        print("\nPor favor, verifique se o Ollama está rodando.")
        return None

def executar_codigo(codigo: str):
    if codigo:
        print("\n--- Executando o Código Gerado ---")
        try:
            exec(codigo)
        except Exception as e:
            print(f"Erro ao executar o código gerado: {e}")


if __name__ == "__main__":
    # Exemplo de uso: Peça à IA para gerar o gráfico de qualquer função!
    
    # Pergunta 1: Função Quadrática
    pergunta_usuario = "Gere o código para a função quadrática f(x) = x**2 - 2*x - 3, com x de -3 a 5."
    codigo_quadratico = gerar_codigo_com_phi3(pergunta_usuario)
    executar_codigo(codigo_quadratico)
    
    print("\n" + "="*50 + "\n")
    
    # Pergunta 2: Função Modular
    pergunta_usuario_2 = "Gere o código para a função modular y = |x - 2|, com x de -5 a 10."
    codigo_modular = gerar_codigo_com_phi3(pergunta_usuario_2)
    executar_codigo(codigo_modular)


