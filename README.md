# Cliente de API de CEP

Projeto criado durante a trilha de estudos de IA com Python.

## Objetivo

Criar um programa em Python que consulta uma API pública de CEP, trata erros comuns de requisição e exibe os dados do endereço no terminal.

Este projeto faz parte da fase de estudo de HTTP, REST e consumo de APIs com Python.

## Funcionalidades

- Recebe um CEP digitado pelo usuário
- Normaliza o CEP removendo espaços e hífen
- Valida se o CEP possui 8 números
- Consulta a API ViaCEP
- Trata CEP inexistente
- Trata erro HTTP
- Trata timeout
- Trata falha de conexão
- Converte o JSON da API em um objeto `Endereco`
- Retorna o resultado usando a classe `ResultadoConsulta`

## Estrutura do projeto

```text
cliente_api_cep/
├── main.py
├── models/
│   ├── endereco.py
│   └── resultado_consulta.py
└── services/
    └── cep_service.py
```

## Como executar

Instale a dependência:

```bash
pip install requests
```

Execute o programa:

```bash
python main.py
```

## Exemplo de uso

```text
Digite o CEP: 01001000

CEP encontrado:
CEP: 01001-000
Logradouro: Praça da Sé
Bairro: Sé
Cidade: São Paulo
Estado: SP
```

## Tecnologias usadas

- Python
- Requests
- API ViaCEP
- Dataclasses
- Type hints

## Conceitos praticados

- Consumo de API REST
- Requisição HTTP com `requests.get()`
- Status code
- Conversão de JSON para objeto Python
- Tratamento de exceções
- Timeout
- Validação de entrada
- Organização em módulos
- Classes com `@dataclass`

## Próximas melhorias possíveis

- Salvar histórico de consultas em JSON
- Criar testes automatizados
- Publicar o projeto no GitHub
- Criar uma interface simples futuramente