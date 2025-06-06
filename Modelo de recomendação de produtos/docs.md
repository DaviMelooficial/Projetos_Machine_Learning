# Documentação Técnica - API de Recomendacão de Produtos

## Sumário

* [Visão Geral](#visão-geral)
* [Como Executar o Projeto](#como-executar-o-projeto)
* [Estrutura do Projeto](#estrutura-do-projeto)
* [Modelo de Dados](#modelo-de-dados)
* [Endpoints da API](#endpoints-da-api)

  * [Clientes](#clientes)
  * [Recomendação](#recomendação)
* [Exemplos de Requisições](#exemplos-de-requisições)
* [Fluxo de Recomendação](#fluxo-de-recomendação)
* [Observações](#observações)
* [Contato](#contato)

---

## Visão Geral

Esta API oferece um sistema inteligente de recomendação de produtos baseado em perfis comportamentais de clientes, utilizando Flask, SQLAlchemy e modelos de machine learning. Suporta operações completas de CRUD e fornece recomendações personalizadas.

---

## Como Executar o Projeto

1. Instale as dependências:

   ```bash
   pip install flask sqlalchemy pandas joblib openpyxl
   ```

2. Inicie o servidor:

   ```bash
   python run.py
   ```

   A aplicação ficará disponível em `http://localhost:5000`.

---

## Estrutura do Projeto

```
app/
    __init__.py
    database.py
    models/
    routes/
        cliente.py
        recomendacao.py
    services/
        cliente_service.py
        pre_processamento.py
run.py
app.db
```

---

## Modelo de Dados

Tabela: `clientes`

| Campo                 | Tipo     | Obrigatório | Descrição                    |
| --------------------- | -------- | ----------- | ---------------------------- |
| id                    | Integer  | Sim         | Identificador único          |
| nome                  | String   | Sim         | Nome do cliente              |
| contato               | String   | Não         | Contato do cliente           |
| endereco              | String   | Não         | Endereço do cliente          |
| idade                 | Integer  | Sim         | Idade                        |
| recencia              | Integer  | Sim         | Recência                     |
| frequencia            | Integer  | Sim         | Frequência                   |
| monetario             | Float    | Sim         | Valor monetário              |
| gasto\_total          | Float    | Sim         | Gasto total                  |
| diversidade\_produtos | Integer  | Sim         | Diversidade de produtos      |
| taxa\_retorno         | Float    | Sim         | Taxa de retorno              |
| produto               | String   | Sim         | Produto principal            |
| genero                | String   | Sim         | Gênero                       |
| pagamento\_preferido  | String   | Sim         | Forma de pagamento preferida |
| cluster               | Integer  | Não         | Cluster atribuido            |
| data\_criacao         | DateTime | Não         | Data de criação do registro  |

---

## Endpoints da API

### Clientes

#### Criar Cliente

* **POST** `/cadastrar_clientes`
* **Body:**

```json
{
  "nome": "João",
  "idade": 30,
  "recencia": 10,
  "frequencia": 5,
  "monetario": 200.0,
  "gasto_total": 1000.0,
  "diversidade_produtos": 3,
  "taxa_retorno": 0.1,
  "produto": "Notebook",
  "genero": "Masculino",
  "pagamento_preferido": "Cartão"
}
```

#### Listar Clientes

* **GET** `/listar_clientes`

#### Obter Cliente por ID

* **GET** `/clientes/<int:cliente_id>`

#### Atualizar Cliente

* **PUT** `/atualizar_clientes/<int:cliente_id>`

#### Deletar Cliente

* **DELETE** `/deletar_clientes/<int:cliente_id>`

#### Recomendar Produtos para Cliente

* **GET** `/clientes/<int:cliente_id>/recomendacao`

### Recomendação

#### Novo Cliente

* **POST** `/recomendar`

**Body:**

```json
{
  "Nome": "Maria",
  "Idade": 28,
  "Recência": 5,
  "Frequência": 8,
  "Monetário": 300.0,
  "Gasto total": 1500.0,
  "Diversidade de produtos": 4,
  "Taxa de retorno": 0.2,
  "Produto": "Celular",
  "Gênero": "Feminino",
  "Pagamento preferido": "Boleto"
}
```

---

## Exemplos de Requisições

### Criar Cliente

```bash
curl -X POST http://localhost:5000/cadastrar_clientes \
  -H "Content-Type: application/json" \
  -d '{"nome":"João","idade":30,"recencia":10,"frequencia":5,"monetario":200,"gasto_total":1000,"diversidade_produtos":3,"taxa_retorno":0.1,"produto":"Notebook","genero":"Masculino","pagamento_preferido":"Cartão"}'
```

### Listar Clientes

```bash
curl http://localhost:5000/listar_clientes
```

### Recomendar para Cliente Existente

```bash
curl http://localhost:5000/clientes/1/recomendacao
```

### Recomendar para Novo Cliente

```bash
curl -X POST http://localhost:5000/recomendar \
  -H "Content-Type: application/json" \
  -d '{"Nome":"Maria","Idade":28,"Recência":5,"Frequência":8,"Monetário":300,"Gasto total":1500,"Diversidade de produtos":4,"Taxa de retorno":0.2,"Produto":"Celular","Gênero":"Feminino","Pagamento preferido":"Boleto"}'
```

---

## Fluxo de Recomendação

1. Envio dos dados do cliente via endpoint
2. Processamento e previsão do cluster via modelo ML
3. Consulta de perfil de produtos por cluster
4. Retorno dos produtos recomendados
5. Atualização no banco de dados, se aplicável

---

## Observações

* Todos os endpoints utilizam o formato JSON.
* Datas seguem o formato ISO 8601.
* Envie todos os campos obrigatórios.
* O endpoint `/recomendar` é ideal para clientes não cadastrados.
* Certifique-se de que os modelos estão carregados via `pre_processamento.py`.

---

## Contato

**Desenvolvido por:** Consumer Action
**Site:** [https://sites.google.com/cesar.school/consumeraction/in%C3%ADcio](https://sites.google.com/cesar.school/consumeraction/in%C3%ADcio)
