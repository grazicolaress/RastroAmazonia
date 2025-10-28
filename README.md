# Atividade Desenvolvimento Web III - Parte 1

## Parte 1: Consolidação e versionamento do código das aulas 1 a 7

### Commit Inicial
- **Descrição**: Configurado o repositório com os arquivos iniciais fornecidos, incluindo os códigos das aulas 1 a 7 ('aula01.py', 'aula02.py', etc.).
- **Objetivo**: Preparar a base para consolidar todas as versões em um único arquivo 'app.py'.

### Aula 01
- **Descrição**: Adicionado o código da aula 01 ao 'app.py', implementando a rota inicial ('/') que retorna "Olá, turma!".
- **Alterações**:
  - Criado o arquivo 'app.py' com a funcionalidade inicial do Flask.
  - Removido o arquivo 'aula01.py' para unificar o código.

### Aula 02
- **Descrição**: Adicionado o código da aula 02 ao 'app.py', incluindo rota adicional '/ola' e função de saudação personalizada.
- **Alterações**:
  - Adicionadas rotas '/' e '/ola' (ambas retornam "Olá, turma!").
  - Criada função 'saudacoes(nome)' para retornar saudação com nome.
  - Usado 'port=8880' e bloco 'if __ name __ == '__ main __':' para execução.
  - Removido o arquivo 'aula02_rota.py' para unificar o código.


### Aula 03
- **Descrição**: Adicionado o código da aula 03 ao 'app.py', incluindo a rota '/rota1' e a nova rota '/rota2' com resposta em HTML.
- **Alterações**:
  - Substituída a rota '/ola' por '/rota1', mantendo a resposta "Olá, turma!".
  - Adicionada a rota '/rota2' que retorna uma página HTML com título.
  - Removida a rota dinâmica '/ ola/< nome >' para saudações personalizadas, agora a função não pertence a nenhuma rota.
  - Removido o arquivo 'aula03_rotas.porta.def.py' para unificar o código.

### Aula 04
- **Descrição**: Adicionado o código da aula 04 ao 'app.py', implementando a renderização de páginas html estáticas para as rotas '/' e '/contato'.
- **Alterações**:
  - Importada a biblioteca 'render_template' para renderizar templates HTML.
  - Configurado o 'app_grazi' com 'template_folder='t_templates'' para definir a pasta dos templates HTML.
  - Adicionadas rotas '/' (renderiza 'homepage.html') e '/contato' (renderiza 'contato.html').
  - Removido o arquivo 'aula04_paginas.py' para unificar o código.

### Aula 05
- **Descrição**: Adicionado o código da aula 05 ao 'app.py', implementando renderização de páginas HTML dinâmicas para as rotas '/index' e '/usuario'.
- **Alterações**:
  - Adicionada a rota '/index' que renderiza 't_index.html' com uma variável dinâmica 'nome'.
  - Adicionada a rota '/usuario' que renderiza 't_usuario.html' com um dicionário de dados dinâmicos ('nome', 'profissão', 'disciplina').
  - Ajustados os templates 't_index.html' e 't_usuario.html' (já existentes em t_templates) para receber os dados dinâmicos corretamente.
  - Removido o arquivo 'aula05_paginas_dinamicas.py' para unificar o código.

### Aula 06
- **Descrição**: Adicionado o código da aula 06 ao 'app.py', implementando testes dinâmicos com herança de template e rotas dinâmicas avançadas. Foi criada uma nova branch (aula06-heranca-template) para testar essas funcionalidades.
- **Alterações**:
  - Adicionadas rotas dinâmicas:
    - /usuario/< id > - vai exibir saudação personalizada usando template 't_homepage_nome.html'
    - /usuario/< nome_usuario>;< nome_profissao>;< nome_disciplina> - rota com múltiplos parâmetros para exibir dados de usuário
  - Implementada herança de template com:
    - Template base 't_base.html'
    - Template 't_homepage_nome.html' estende o template base usando {% extends 't_base.html' %}
    - Criado o arquivo 't_homepage_nome.html' para suportar a nova funcionalidade de saudação personalizada
  - Mantidas todas as rotas anteriores funcionais
  - Removido o arquivo 'aula06_dinamico_URL.py' para unificar o código.

### Aula 07
- **Descrição**: Adicionado o código da aula 07 ao 'app.py', implementando rotas com valores padrão usando defaults para acesso sem parâmetros e múltiplas rotas para a mesma função.
- **Alterações**:
  - Adicionada rota /usuario com valores padrão usando defaults para quando não há passagem de argumentos
  - Implementada função única usuario() que trata ambos os casos: com e sem parâmetros
  - Agora a rota /usuario funciona tanto com quanto sem parâmetros.
  - Removido o arquivo 'aula07_template.py' para unificar o código.