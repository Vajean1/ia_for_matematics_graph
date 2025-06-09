import requests
import json
import os

#Classe principal da para gerar gráficos usando IA
class IAGeradoraDeGraficos:
    def __init__(self, model: str = "phi3", 
                 api_url: str = "http://localhost:11434/api/generate",
                 prompt_file: str = "json/prompt_template.json"):
        self.model = model
        self.api_url = api_url
        # Carrega o prompt do arquivo JSON no construction
        self.prompt_template = self._carregar_prompt_de_arquivo(prompt_file)

    def _carregar_prompt_de_arquivo(self, arquivo_path: str) -> str:
        try:
            with open(arquivo_path, 'r', encoding='utf-8') as f:
                dados = json.load(f)
                return dados['prompt_template']
        except FileNotFoundError:
            print(f"Erro: O arquivo de prompt '{arquivo_path}' não foi encontrado.")
            print("Por favor, crie o arquivo ou verifique o caminho.")
            exit()
        except (json.JSONDecodeError, KeyError):
            print(f"Erro: O arquivo '{arquivo_path}' não é um JSON válido ou não contém a chave 'prompt_template'.")
            exit()

    def _gerar_codigo(self, pergunta: str) -> str | None:

        print(f"Enviando pergunta para a IA: '{pergunta}'")
        
        prompt_final = self.prompt_template.format(pergunta_do_usuario=pergunta)
        
        payload = {
            "model": self.model,
            "prompt": prompt_final,
            "stream": False,
            "options": {
                "temperature": 0.1,
                "stop": ["[FIM DO EXEMPLO]", "[SISTEMA]", "USUÁRIO:"]
            }
        }
        
        try:
            response = requests.post(self.api_url, json=payload)
            response.raise_for_status()
            
            response_json = response.json()
            codigo_gerado = response_json.get("response", "").strip()
            
            print("✅ IA gerou o código com sucesso!")
            return codigo_gerado
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Erro ao conectar com o Ollama: {e}")
            print("   Por favor, verifique se o Ollama está rodando.")
            return None
    
    @staticmethod
    def _salvar_codigo_em_json(self, pergunta: str, codigo: str, arquivo_json: str = "json/codes.json"):
        
        novo_registro = {
            "pergunta": pergunta,
            "codigo_gerado": codigo
        }
        
        try:
            if os.path.exists(arquivo_json) and os.path.getsize(arquivo_json) > 0:
                with open(arquivo_json, 'r', encoding='utf-8') as f:
                    dados = json.load(f)
            else:
                dados = []
            
            dados.append(novo_registro)
            
            with open(arquivo_json, 'w', encoding='utf-8') as f:
                json.dump(dados, f, ensure_ascii=False, indent=4)
                
            print(f"✅ Código salvo com sucesso em '{arquivo_json}'!")

        except (IOError, json.JSONDecodeError) as e:
            print(f"Erro ao salvar o arquivo JSON: {e}")
            return None
        
    @staticmethod
    def _executar_codigo(codigo: str):
        if codigo:
            print("\n--- Executando o Código Gerado ---")
            try:
                exec(codigo, {'plt': __import__('matplotlib.pyplot'), 'np': __import__('numpy')})
            except Exception as e:
                print(f"❌ Erro ao executar o código gerado: {e}")

    def plotar_funcao(self, pergunta: str):
        codigo_gerado = self._gerar_codigo(pergunta)

        if codigo_gerado:
            self._executar_codigo(codigo_gerado)
    

if __name__ == "__main__":

    gerador_de_graficos = IAGeradoraDeGraficos()

    perguntas = {
        "função_linear": "Gere o código para a função y = 2*x + 1 de -10 a 10",
        "função_constante": "Gere o código para a função y = 5 de -10 a 10",
        "função_quadrática": "Gere o código para a função f(x) = -2*x**2 + 3*x + 5",
        "função_cúbica": "Gere o código para a função y = x**3 - 3*x de -3 a 3",
        "função_trigonométrica": "Gere o código para a função y = cos(2*x) de -pi a pi",
        "função_modular": "Gere o código para a função y = |2x + 1| de -4 a 3",
        "função_exponencial": "Gere o código para a função y = 2**x de -5 a 5",
        "função_logarítmica": "Gere o código para a função y = log10(x) de 0.1 a 20"
    }


    print("--- GERANDO GRÁFICO ---")
    pergunta = "Gere o código para a função f(x) = -2*x**2 + 3*x + 5"
    gerador_de_graficos.plotar_funcao(pergunta)

