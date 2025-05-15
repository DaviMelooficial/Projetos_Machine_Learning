from flask import Blueprint, request, jsonify
from sqlalchemy.orm import Session
from app.services.pre_processamento import recomendar_produtos_para_cliente
from app.database import SessionLocal, Cliente

recomendacao_bp = Blueprint('recomendacao', __name__)

# Lista de campos obrigatórios para a recomendação
CAMPOS_OBRIGATORIOS = [
    'Nome', 'Idade', 'Recência', 'Frequência', 'Monetário', 'Gasto total',
    'Diversidade de produtos', 'Taxa de retorno', 'Produto', 'Gênero', 'Pagamento preferido'
]

# Rota para recomendar produtos a partir dos dados enviados
@recomendacao_bp.route('/recomendar', methods=['POST'])
def recomendar():
    dados = request.json

    # Verificar se todos os campos obrigatórios estão presentes
    campos_faltantes = [campo for campo in CAMPOS_OBRIGATORIOS if campo not in dados]
    if campos_faltantes:
        return jsonify({
            'erro': 'Campos obrigatórios ausentes',
            'campos_faltantes': campos_faltantes
        }), 400

    # Salvar os dados no banco de dados
    db: Session = SessionLocal()
    cliente = Cliente(
        nome=dados['Nome'],
        contato=dados.get('Contato'),  # Campo opcional
        endereco=dados.get('Endereço'),  # Campo opcional
        idade=dados['Idade'],
        recencia=dados['Recência'],
        frequencia=dados['Frequência'],
        monetario=dados['Monetário'],
        gasto_total=dados['Gasto total'],
        diversidade_produtos=dados['Diversidade de produtos'],
        taxa_retorno=dados['Taxa de retorno'],
        produto=dados['Produto'],
        genero=dados['Gênero'],
        pagamento_preferido=dados['Pagamento preferido']
    )
    db.add(cliente)
    db.commit()
    db.refresh(cliente)

    # Filtrar apenas os dados relevantes para o modelo
    dados_para_treino = {
        'Idade': dados['Idade'],
        'Recência': dados['Recência'],
        'Frequência': dados['Frequência'],
        'Monetário': dados['Monetário'],
        'Gasto total': dados['Gasto total'],
        'Diversidade de produtos': dados['Diversidade de produtos'],
        'Taxa de retorno': dados['Taxa de retorno'],
        'Produto': dados['Produto'],
        'Gênero': dados['Gênero'],
        'Pagamento preferido': dados['Pagamento preferido']
    }

    # Chamar a função de recomendação
    resultado = recomendar_produtos_para_cliente(dados_para_treino)

    # Atualizar o cluster previsto no banco de dados
    cliente.cluster = resultado['Cluster previsto']
    db.commit()

    # Fechar a sessão do banco de dados
    db.close()

    # Retorna o resultado da recomendação
    return jsonify(resultado)