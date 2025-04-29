# Projeto de Simulação de Monitoramento Agrícola

Este projeto visa criar uma aplicação web para simulação de monitoramento de temperatura e irrigação em ambientes agrícolas. Através do uso do Flask, o sistema permite ao usuário escolher entre dois ambientes (estufa ou campo) e visualizar as leituras do sensor de temperatura e o status do módulo de irrigação correspondente.

## Estrutura dos Arquivos

Abaixo está a estrutura de arquivos do projeto:

📂 Estrutura dos Arquivos
projeto_flask/
│
├── app.py `# Arquivo principal que configura a aplicação Flask.`
├── fabrica/  `# Contém os módulos relacionados à fábrica de criação dos sensores e módulos.`
│   ├── interfaces.py  `# Define as interfaces para sensores e módulos de irrigação.`
│   ├── estufa.py `# Implementação específica para a criação de objetos para a estufa.` 
│   ├── campo.py `# Implementação específica para a criação de objetos para o campo.`
│   └── fabrica.py `# Fábrica que cria os objetos conforme o ambiente selecionado.` 
├── singleton/ `# Implementação do padrão Singleton para a leitura do XML.`
│   └── conexao_xml.py `# Responsável por carregar e fornecer os dados do XML.` 
├── dados/  `# Contém o arquivo XML com os dados da estufa e do campo.`
│   └── banco.xml `# Arquivo XML com dados simulados de sensores e módulos.`
├── static/ `# Contém os arquivos estáticos (CSS).`
│   └── style.css `# Arquivo de estilo para a aplicação.`
├── templates/ `# Contém os templates HTML renderizados pelo Flask.`
│   ├── index.html `# Página inicial com o formulário para seleção do ambiente.`
│   └── resultado.html `# Página que exibe os resultados da simulação.`
└── README.md `# Este arquivo, que descreve o projeto.`


## Como Executar o Projeto

### Requisitos

Certifique-se de ter o Python 3.x instalado em sua máquina. Além disso, instale as dependências necessárias executando o seguinte comando:

`pip install flask`

### Passos para rodar

1. Clone o repositório para o seu ambiente local.
2. Navegue até o diretório do projeto.
3. Execute o arquivo `app.py` para iniciar a aplicação Flask:

python `app.py`


4. Abra o navegador e acesse `http://127.0.0.1:5000/` para interagir com a aplicação.

### Descrição dos Arquivos

- **app.py**: Configura o servidor Flask e define as rotas da aplicação. A rota principal renderiza o formulário para escolher o ambiente, enquanto a rota `/resultado` exibe os resultados da simulação de monitoramento com base na seleção do usuário.

- **fabrica/estufa.py e fabrica/campo.py**: Contêm as implementações específicas dos sensores de temperatura e módulos de irrigação para os ambientes de estufa e campo, respectivamente. Implementam as interfaces `SensorTemperatura` e `ModuloIrrigacao` que são consumidas pelo código principal.

- **fabrica/fabrica.py**: Implementa o padrão Factory que cria as instâncias corretas das fábricas de sensores e módulos de acordo com o ambiente selecionado pelo usuário (estufa ou campo).

- **singleton/conexao_xml.py**: Implementa o padrão Singleton para garantir que a leitura do arquivo XML ocorra uma única vez durante o ciclo de vida da aplicação, oferecendo os dados necessários para as simulações.

- **dados/banco.xml**: Arquivo XML que contém os dados simulados de sensores de temperatura e módulos de irrigação para os ambientes de estufa e campo.

- **static/style.css**: Arquivo CSS que define o estilo visual da aplicação, com temas e responsividade para diferentes dispositivos.

- **templates/index.html**: Página inicial com o formulário de seleção do ambiente.

- **templates/resultado.html**: Página que exibe os resultados da simulação, mostrando a leitura do sensor de temperatura e o status da irrigação.

