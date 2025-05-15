from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timezone

# Define a URL do banco de dados SQLite
DATABASE_URL = "sqlite:///app.db"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define o modelo Cliente que representa a tabela 'clientes' no banco de dados
class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    contato = Column(String, nullable=True)
    endereco = Column(String, nullable=True)
    idade = Column(Integer, nullable=False)
    recencia = Column(Integer, nullable=False)
    frequencia = Column(Integer, nullable=False)
    monetario = Column(Float, nullable=False)
    gasto_total = Column(Float, nullable=False)
    diversidade_produtos = Column(Integer, nullable=False)
    taxa_retorno = Column(Float, nullable=False)
    produto = Column(String, nullable=False)
    genero = Column(String, nullable=False)
    pagamento_preferido = Column(String, nullable=False)
    cluster = Column(Integer, nullable=True)
    data_criacao = Column(DateTime, default=lambda: datetime.now(timezone.utc))

Base.metadata.create_all(bind=engine)