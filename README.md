# 📋 Acompanhamento e Aprovação de Histórias de Usuário (HUs)


Este projeto consiste em duas aplicações Streamlit que facilitam o gerenciamento e a aprovação de Histórias de Usuário (HUs) por stakeholders. Ele foi desenvolvido para ajudar equipes a acompanhar o progresso das HUs e garantir que todas sejam revisadas e aprovadas de forma eficiente.

# 🚀 Funcionalidades
1. Backoffice - Cadastro de HUs
Cadastro de HUs: Adicione novas HUs com informações como ID, descrição, link do Confluence e status.

Geração de Link de Aprovação: Cada HU cadastrada gera um link único para aprovação.

Visualização de HUs Cadastradas: Veja todas as HUs cadastradas em uma lista organizada.

2. Página de Aprovação
Aprovação de HUs: Os stakeholders podem aprovar, reprovar ou adicionar observações às HUs.

Visualização do Confluence: A página de aprovação exibe o conteúdo do Confluence diretamente em um iframe.

Atualização de Status: O status da HU é atualizado automaticamente após a aprovação ou reprovação.

# 🛠️ Tecnologias Utilizadas
Streamlit: Framework para criação de aplicações web em Python.

Pandas: Biblioteca para manipulação de dados em formato tabular (CSV/TSV).

GitHub: Hospedagem do código e integração com o Streamlit Cloud.

Streamlit Cloud: Hospedagem das aplicações para acesso online.

# 📂 Estrutura do Projeto
O projeto é composto por dois arquivos principais:

backoffice.py:

Interface para cadastrar e visualizar HUs.

Gera links de aprovação para cada HU.

approval.py:

Interface para aprovação de HUs pelos stakeholders.

Exibe detalhes da HU e permite atualizar o status.

Além disso, os dados das HUs são armazenados em um arquivo TSV (hus.tsv), que contém as seguintes colunas:

ID: Identificador único da HU.

Descrição: Descrição detalhada da HU.

Link Confluence: Link para a documentação da HU no Confluence.

Link Aprovação: Link gerado para a página de aprovação da HU.

Status: Status atual da HU (Pendente, Aprovado, Reprovado, etc.).

Observação: Comentários ou observações adicionais.

# 🚀 Como Usar
1. Executando Localmente
Clone o repositório:

bash
Copy
git clone https://github.com/seu-usuario/seu-repositorio.git
Instale as dependências:

bash
Copy
pip install streamlit pandas
Execute o backoffice.py:

bash
Copy
streamlit run backoffice.py
Execute o approval.py:

bash
Copy
streamlit run approval.py
2. Acessando no Streamlit Cloud
O projeto está hospedado no Streamlit Cloud e pode ser acessado pelos seguintes links:

Backoffice: https://backofficepo.streamlit.app/

Página de Aprovação: https://aprovacaodehu.streamlit.app/

# 📝 Fluxo de Trabalho
Cadastro de HUs:

No Backoffice, cadastre uma nova HU com ID, descrição e link do Confluence.

Um link de aprovação será gerado automaticamente.

Aprovação de HUs:

Os stakeholders acessam o link de aprovação.

Na página de aprovação, eles visualizam os detalhes da HU, o conteúdo do Confluence e podem aprovar, reprovar ou adicionar observações.

Atualização de Status:

Após a aprovação ou reprovação, o status da HU é atualizado no arquivo TSV.

# 📸 Screenshots
Backoffice
Backoffice

Página de Aprovação
Aprovação

# 🤝 Contribuição
Contribuições são bem-vindas! Se você quiser melhorar o projeto, siga os passos abaixo:

Faça um fork do repositório.

Crie uma branch para sua feature (git checkout -b feature/nova-feature).

Commit suas mudanças (git commit -m 'Adicionando nova feature').

Faça push para a branch (git push origin feature/nova-feature).

Abra um Pull Request.

# 📄 Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.

# 🙏 Agradecimentos
À equipe do Streamlit por fornecer uma ferramenta incrível para criação de aplicações web.

Aos stakeholders e usuários que testaram e forneceram feedback valioso.
