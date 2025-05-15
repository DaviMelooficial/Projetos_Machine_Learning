from flask import Blueprint, request, jsonify
from app.services.cliente_service import (
    criar_cliente, listar_clientes, obter_cliente, atualizar_cliente, deletar_cliente
)
from app.services.pre_processamento import recomendar_produtos_para_cliente

cliente_bp = Blueprint('cliente', __name__)

# Rota para criar um novo cliente
@cliente_bp.route('/clientes', methods=['POST'])
def criar():
    dados = request.json
    cliente = criar_cliente(dados)
    return jsonify({'id': cliente.id}), 201

# Rota para listar todos os clientes
@cliente_bp.route('/clientes', methods=['GET'])
def listar():
    clientes = listar_clientes()
    return jsonify([{
        'id': c.id,
        'nome': c.nome,
        'contato': c.contato,
        'endereco': c.endereco,
        'idade': c.idade,
        'recencia': c.recencia,
        'frequencia': c.frequencia,
        'monetario': c.monetario,
        'gasto_total': c.gasto_total,
        'diversidade_produtos': c.diversidade_produtos,
        'taxa_retorno': c.taxa_retorno,
        'produto': c.produto,
        'genero': c.genero,
        'pagamento_preferido': c.pagamento_preferido,
        'cluster': c.cluster,
        'data_criacao': c.data_criacao.isoformat() if c.data_criacao else None
    } for c in clientes])

# Rota para obter um cliente pelo ID
@cliente_bp.route('/clientes/<int:cliente_id>', methods=['GET'])
def obter(cliente_id):
    cliente = obter_cliente(cliente_id)
    if not cliente:
        return jsonify({'erro': 'Cliente não encontrado'}), 404
    return jsonify({
        'id': cliente.id,
        'nome': cliente.nome,
        'contato': cliente.contato,
        'endereco': cliente.endereco,
        'idade': cliente.idade,
        'recencia': cliente.recencia,
        'frequencia': cliente.frequencia,
        'monetario': cliente.monetario,
        'gasto_total': cliente.gasto_total,
        'diversidade_produtos': cliente.diversidade_produtos,
        'taxa_retorno': cliente.taxa_retorno,
        'produto': cliente.produto,
        'genero': cliente.genero,
        'pagamento_preferido': cliente.pagamento_preferido,
        'cluster': cliente.cluster,
        'data_criacao': cliente.data_criacao.isoformat() if cliente.data_criacao else None
    })

# Rota para atualizar um cliente existente
@cliente_bp.route('/clientes/<int:cliente_id>', methods=['PUT'])
def atualizar(cliente_id):
    dados = request.json
    cliente = atualizar_cliente(cliente_id, dados)
    if not cliente:
        return jsonify({'erro': 'Cliente não encontrado'}), 404
    return jsonify({'mensagem': 'Cliente atualizado com sucesso'})

# Rota para deletar um cliente pelo ID
@cliente_bp.route('/clientes/<int:cliente_id>', methods=['DELETE'])
def deletar(cliente_id):
    sucesso = deletar_cliente(cliente_id)
    if not sucesso:
        return jsonify({'erro': 'Cliente não encontrado'}), 404
    return jsonify({'mensagem': 'Cliente deletado com sucesso'})

# Rota para recomendar produtos para um cliente específico
@cliente_bp.route('/clientes/<int:cliente_id>/recomendacao', methods=['GET'])
def recomendar_para_cliente(cliente_id):
    cliente = obter_cliente(cliente_id)
    if not cliente:
        return jsonify({'erro': 'Cliente não encontrado'}), 404

    # Monta os dados necessários para o modelo
    dados_para_treino = {
        'Idade': cliente.idade,
        'Recência': cliente.recencia,
        'Frequência': cliente.frequencia,
        'Monetário': cliente.monetario,
        'Gasto total': cliente.gasto_total,
        'Diversidade de produtos': cliente.diversidade_produtos,
        'Taxa de retorno': cliente.taxa_retorno,
        'Produto': cliente.produto,
        'Gênero': cliente.genero,
        'Pagamento preferido': cliente.pagamento_preferido
    }

    # Chama a função de recomendação e retorna o resultado
    resultado = recomendar_produtos_para_cliente(dados_para_treino)
    
    return jsonify(resultado)