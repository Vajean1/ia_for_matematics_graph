# 🤖 IA para Gráficos de Funções Matemáticas

 Modelo de linguagem local (Microsoft Phi-3 via Ollama) para gerar e visualizar gráficos de funções matemáticas a partir de comandos em linguagem natural.

## ✨ Funcionalidades Principais

- **Geração por Texto**: Cria gráficos complexos a partir de frases simples.
- **Suporte Amplo**: Gera gráficos para funções lineares, constantes, quadráticas, cúbicas, trigonométricas, modulares, exponenciais e logarítmicas e quais mais você desejar.
- **Execução 100% Local**: Toda a operação é feita na máquina localmente. Garantindo total privacidade e zero custos de API.
- **Código Limpo e Modular**: A estrutura orientada a objetos facilita a manutenção e a adição de novas funcionalidades.
- **"Cérebro" Customizável**: O conhecimento da IA é definido em um arquivo `prompt_template.json`, permitindo que qualquer um "treine" com novos exemplos sem precisar alterar o código Python.

## Como funciona o "treinamento" dessa IA 🧠

O "treinamento" desta IA não é um processo de machine learning tradicional que exige dias de processamento. Em vez disso, utiliza-se uma técnica poderosa e imediata chamada **aprendizagem em contexto** (in-context learning ou few-shot learning).

A arquitetura é dividida em dois arquivos principais:

- **`prompt_template.json`**: Este arquivo é o verdadeiro "cérebro" da IA. Ele contém um longo prompt com:
  - **Instruções de Sistema**: Diz à IA qual é seu papel e como ela deve se comportar.
  - **Exemplos de Alta Qualidade**: Uma série de pares de "pergunta" e "resposta perfeita" (Perfect Match).
  É através destes exemplos que a IA aprende em tempo real o formato exato do código que deve gerar.

- **`matematics_ia_for_graphics.py`**: Este script contém a classe `IAGeradoraDeGraficos` que executa a lógica. Ela carrega o template do arquivo JSON, insere a pergunta do usuário e envia tudo para o modelo Phi-3.

Como deixar a IA ainda mais inteligente? É fácil! Abra o arquivo `prompt_template.json` e adicione um novo bloco de exemplo. Quanto mais exemplos de qualidade você fornecer, melhores e mais precisas serão as respostas da IA.

## Pré-requisitos 🛠️

Para executar, você precisará ter o seguinte instalado em sua máquina:

- Python 3.9 ou superior
- Git para clonar o repositório
- Uma instalação funcional do Ollama com o modelo phi3, ou qual você desejar, somente altera na classe.

## Instalação ⚙️

Siga estes passos para configurar o ambiente:

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/ia_for_matematics_graph.git
   cd ia_for_matematics_graph
   ```

2. **Baixe o modelo de IA (Phi-3)**:  
   No terminal, rode o seguinte comando. Isso precisa ser feito apenas uma vez e pode levar alguns minutos.
   ```bash
   ollama run phi3:mini
   ```

3. **Instale as dependências do Python**:  
   ```bash
   pip install requests matplotlib numpy
   ```

## Como usar ▶️

Com tudo instalado, usar a aplicação é muito simples:

1. Garanta que o Ollama esteja rodando em segundo plano.
2. No terminal ou VSCODE, navegue até a pasta do projeto.
3. Execute o script Python:
   ```bash
   python matematics_ia_for_graphics.py
   ```
4. Observe o terminal!
