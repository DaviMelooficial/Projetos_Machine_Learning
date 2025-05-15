from app.database import SessionLocal, Cliente

# Função para criar um novo cliente no banco de dados
def criar_cliente(dados):
    db = SessionLocal()
    cliente = Cliente(**dados)
    db.add(cliente)
    db.commit()
    db.refresh(cliente)
    db.close()
    return cliente

# Função para listar todos os clientes cadastrados
def listar_clientes():
    db = SessionLocal()
    clientes = db.query(Cliente).all()
    db.close()
    return clientes

# Função para obter um cliente pelo ID
def obter_cliente(cliente_id):
    db = SessionLocal()
    cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()
    db.close()
    return cliente

# Função para atualizar os dados de um cliente existente
def atualizar_cliente(cliente_id, dados):
    db = SessionLocal()
    cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()
    if not cliente:
        db.close()
        return None
    for key, value in dados.items():
        setattr(cliente, key, value)
    db.commit()
    db.refresh(cliente)
    db.close()
    return cliente

# Função para deletar um cliente pelo ID
def deletar_cliente(cliente_id):
    db = SessionLocal()
    cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()
    if not cliente:
        db.close()
        return False
    db.delete(cliente)
    db.commit()
    db.close()
    return True