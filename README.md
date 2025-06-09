# 🤖 IA para Gráficos de Funções Matemáticas
Um projeto que utiliza um modelo de linguagem local (Microsoft Phi-3 via Ollama) para gerar e visualizar gráficos de funções matemáticas a partir de comandos em linguagem natural.

🎬 Demonstração
(Aqui você pode adicionar um GIF ou vídeo mostrando o script em ação! Grave sua tela executando o programa para um efeito visual incrível.)

Exemplo de como uma demonstração poderia se parecer.

📖 Sobre o Projeto
Este projeto nasceu da ideia de simplificar a visualização de funções matemáticas. Em vez de escrever código Matplotlib manualmente para cada novo gráfico, esta aplicação permite que você simplesmente peça à IA para gerar o gráfico de uma função específica.

A aplicação é construída em Python com uma estrutura orientada a objetos, garantindo que o código seja limpo, modular e fácil de estender. A "inteligência" do assistente é moldada por um prompt externo em formato JSON, permitindo fácil customização e melhoria contínua.

🚀 Tecnologias Utilizadas
Python: Linguagem principal do projeto.
Ollama: Ferramenta para rodar modelos de linguagem localmente.
Microsoft Phi-3: O modelo de linguagem que gera o código.
Matplotlib & NumPy: As bibliotecas que o código gerado utiliza para criar e exibir os gráficos.
Requests: Para comunicação com a API local do Ollama.
✨ Funcionalidades
Geração por Texto: Crie gráficos complexos a partir de frases simples.
Suporte Amplo: Gera gráficos para funções lineares, constantes, quadráticas, cúbicas, trigonométricas, modulares, exponenciais e logarítmicas.
Execução Local: Toda a operação é feita na sua máquina. Seus dados e pedidos nunca saem do seu computador, garantindo 100% de privacidade e zero custos de API.
Código Limpo: Estrutura orientada a objetos que facilita a manutenção e a adição de novas funcionalidades.
Prompt Customizável: O "cérebro" da IA está em um arquivo prompt_template.json separado, permitindo que qualquer um possa "treinar" a IA com novos exemplos sem tocar em uma linha de código Python.
🏁 Começando
Siga estes passos para ter o projeto rodando na sua máquina.

Pré-requisitos
Python 3.9 ou superior.
Git para clonar o repositório.
Uma instalação funcional do Ollama.
Instalação
Clone o repositório:

Bash

git clone https://github.com/seu-usuario/ia_for_matematics_graph.git
cd ia_for_matematics_graph
(Substitua seu-usuario pelo seu nome de usuário no GitHub)

Instale o Ollama:

Se ainda não o tiver, baixe e instale o Ollama do site oficial.
Baixe o modelo Phi-3:

No seu terminal, rode o seguinte comando. Isso precisa ser feito apenas uma vez.
<!-- end list -->

Bash

ollama run phi3
Instale as dependências do Python:

O script foi projetado para instalar as dependências automaticamente na primeira execução. Alternativamente, você pode instalá-las manualmente:
<!-- end list -->

Bash

pip install requests matplotlib numpy
kullanım
Com tudo instalado, usar a aplicação é muito simples.

Garanta que o Ollama esteja rodando em segundo plano.
No seu terminal, na pasta do projeto, execute o script Python:
Bash

python matematics_ia_for_graphics.py
Observe o terminal! Ele mostrará as perguntas sendo enviadas para a IA e, em seguida, uma janela do Matplotlib aparecerá com cada gráfico gerado.
🛠️ Como Funciona
A arquitetura do projeto é dividida em dois arquivos principais:

prompt_template.json: Este arquivo é o "cérebro" da IA. Ele contém um longo prompt com instruções detalhadas ([SISTEMA]) e uma série de exemplos de alta qualidade ([EXEMPLO]). É através destes exemplos que a IA aprende o formato exato do código que deve gerar (técnica conhecida como few-shot learning).

matematics_ia_for_graphics.py: Este script contém a classe IAGeradoraDeGraficos.

Ao ser inicializada, ela carrega o template do prompt_template.json.
O método plotar_funcao recebe uma pergunta em linguagem natural.
Ele insere a pergunta no template e envia tudo para a API local do Ollama.
Recebe o código Python gerado pelo modelo Phi-3.
Executa este código em tempo real para exibir o gráfico.
🔧 Customização e Melhorias
Quer deixar a IA ainda mais inteligente? É fácil!

Abra o arquivo prompt_template.json e adicione um novo bloco [EXEMPLO]...[FIM DO EXEMPLO] com uma nova função ou um caso mais complexo. Quanto mais exemplos de qualidade você fornecer, melhores e mais precisas serão as respostas da IA. Você pode fazer tudo isso sem alterar o código Python.

📄 Licença
Distribuído sob a Licença MIT. Veja o arquivo LICENSE para mais informações.

Feito com ❤️ e muito código.