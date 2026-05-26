# 🏋️‍♂️ Personal Trainer IA — Gerador de Cronograma de Treinos

[![Licença](https://img.shields.io/github/license/cdnjs/cdnjs.svg?style=flat-square)](LICENSE)
[![Tailwind CSS v4](https://img.shields.io/badge/Tailwind_CSS-v4.0-38bdf8?style=flat-square&logo=tailwind-css)](https://tailwindcss.com)
[![Vanilla JS](https://img.shields.io/badge/JavaScript-Vanilla-f7df1e?style=flat-square&logo=javascript)](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript)

Uma aplicação web de página única (*SPA*) elegante, intuitiva e de alta performance que atua como um assistente de educação física baseado em Inteligência Artificial. O sistema processa o perfil do usuário e gera uma rotina de treinamento estruturada, anatômica e segura.

---

## 📋 Resumo do Projeto
O **Personal Trainer IA** permite que usuários criem cronogramas de treinos personalizados combinando qualquer modalidade de forma inteligente. A interface conecta-se de forma assíncrona a uma API externa para transformar objetivos, níveis de experiência e limitações físicas em um planejamento semanal completo, calculando inclusive o volume e o tempo de descanso ideal para as séries.

---

## ✨ Funcionalidades

* **Perfil de Treino Customizado:** Entrada dinâmica de dados como objetivos principais, nível de experiência e limitações/dores físicas.
* **Gerenciador de Tags Dinâmico:** Adicione múltiplas modalidades de interesse (ex: Musculação, Jiu-Jitsu, Corrida, Crossfit) em tempo real pressionando `Enter` ou `,`.
* **Estados de Interface Fluídos:**
    * *Placeholder State:* Mensagem amigável de orientação antes do primeiro envio.
    * *Loading State:* Spinner animado e mensagem contextual enquanto a IA calcula a rotina ideal.
    * *Result State:* Exibição limpa do cronograma ativo, cartões diários detalhados e alertas de cuidados gerais.
* **Design Avançado com Tailwind v4:** Interface escura (*Dark Mode*) nativa usando as novas diretivas de gradientes e bordas da versão mais recente do Tailwind CSS.
* **Responsividade Total:** Adaptado perfeitamente para visualização em smartphones, tablets e desktops.

---

## 🛠️ Tecnologias Utilizadas

* **HTML5:** Estrutura semântica e acessível.
* **Tailwind CSS v4 (via CDN):** Estilização utilitária de última geração.
* **JavaScript (Vanilla):** Manipulação de DOM, gerenciamento de estado local (tags) e consumo assíncrono de API via `Fetch`.

---

## 🚀 Como Executar o Projeto

Como o projeto é baseado puramente em arquivos estáticos front-end, você não precisa instalar nenhuma dependência do Node.js em sua máquina.

### 1. Clonar o Repositório
```bash
git clone [https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git](https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git)
cd NOME-DO-REPOSITORIO
