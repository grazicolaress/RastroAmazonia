# 🐆 Rastro Amazônia - Sistema de Adoção Virtual

## 📋 Sobre o Projeto

O **Rastro Amazônia** é uma aplicação web desenvolvida em Flask que permite a adoção virtual de animais da Amazônia. Os usuários podem criar contas, fazer login e "adotar" animais como botos-cor-de-rosa e onças-pintadas, acompanhando virtualmente esses animais monitorados por cientistas.

## 🎯 Objetivo

Conectar pessoas à conservação da fauna amazônica através de um sistema interativo de adoção virtual, onde cada adoção simboliza um apoio financeiro à pesquisa e preservação das espécies.

## 🛠️ Tecnologias Utilizadas

- **Backend:** Python + Flask
- **Frontend:** HTML5, CSS3, JavaScript
- **Templates:** Jinja2

## 📁 Estrutura do Projeto

```
rastroamazonia/
│
├── app.py                  # Aplicação principal Flask
├── README.md               # Documentação
│
├── t_templates/          # Templates HTML
│   ├── base.html         # Template base com navbar/footer
│   ├── index.html        # Página inicial
│   ├── t_login.html      # Página de login
│   ├── t_cadastro.html   # Página de cadastro
│   ├── t_galeria.html    # Galeria de animais
│   └── t_loja.html       # Loja virtual
│
└── static/
    ├── css/
    │   └── style.css     # Estilos principais
    ├── js/
    │   └── validacao.js  # Validações JavaScript
    └── imagens/           # Imagens dos animais
```


## 🔒 Validações Implementadas

### Validação de Senha
A senha deve conter:
- ✅ Mínimo de 6 caracteres
- ✅ Pelo menos 1 letra maiúscula
- ✅ Pelo menos 1 número
- ✅ Pelo menos 1 caractere especial

### Validação de Formulários
- ✅ Confirmação de senha
- ✅ E-mail único por usuário
- ✅ Campos obrigatórios
- ✅ Feedback de erro/sucesso


## 📄 Licença

Este projeto é para fins educacionais.

---

