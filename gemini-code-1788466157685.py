from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# ----------------------------------------------------------------------
# 1. DONO
# ----------------------------------------------------------------------
class Dono(db.Model):
    __tablename__ = 'donos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cpf_cnpj = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    numero_telefone = db.Column(db.String(20), nullable=True)

    # Relacionamento 1..N com Estabelecimento
    estabelecimentos = db.relationship('Estabelecimento', backref='dono', lazy=True, cascade="all, delete-orphan")


# ----------------------------------------------------------------------
# 2. ESTABELECIMENTO
# ----------------------------------------------------------------------
class Estabelecimento(db.Model):
    __tablename__ = 'estabelecimentos'

    id = db.Column(db.Integer, primary_key=True)
    id_dono = db.Column(db.Integer, db.ForeignKey('donos.id'), nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    endereco = db.Column(db.String(200), nullable=False)
    numero_telefone = db.Column(db.String(20), nullable=True)
    descricao = db.Column(db.Text, nullable=True)

    # Relacionamento 1..N com Cardápio
    cardapios = db.relationship('Cardapio', backref='estabelecimento', lazy=True, cascade="all, delete-orphan")


# ----------------------------------------------------------------------
# 3. CARDÁPIO
# ----------------------------------------------------------------------
class Cardapio(db.Model):
    __tablename__ = 'cardapios'

    id = db.Column(db.Integer, primary_key=True)
    id_estabelecimento = db.Column(db.Integer, db.ForeignKey('estabelecimentos.id'), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(20), default='Ativo')
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)

    # Relacionamento 1..N com Categoria
    categorias = db.relationship('Categoria', backref='cardapio', lazy=True, cascade="all, delete-orphan")


# ----------------------------------------------------------------------
# 4. CATEGORIA
# ----------------------------------------------------------------------
class Categoria(db.Model):
    __tablename__ = 'categorias'

    id = db.Column(db.Integer, primary_key=True)
    id_cardapio = db.Column(db.Integer, db.ForeignKey('cardapios.id'), nullable=False)
    nome = db.Column(db.String(80), nullable=False)
    descricao = db.Column(db.Text, nullable=True)

    # Relacionamento 1..N com Item Cardápio
    itens = db.relationship('ItemCardapio', backref='categoria', lazy=True, cascade="all, delete-orphan")
    
    # Relacionamento 1..N com Promoções (Opcional)
    promocoes = db.relationship('Promocao', backref='categoria', lazy=True, cascade="all, delete-orphan")


# ----------------------------------------------------------------------
# 5. ITEM CARDÁPIO
# ----------------------------------------------------------------------
class ItemCardapio(db.Model):
    __tablename__ = 'itens_cardapio'

    id = db.Column(db.Integer, primary_key=True)
    id_categoria = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    preco = db.Column(db.Numeric(10, 2), nullable=False)
    imagem = db.Column(db.String(255), nullable=True)
    disponibilidade = db.Column(db.Boolean, default=True)


# ----------------------------------------------------------------------
# 6. PROMOÇÕES (OPCIONAL)
# ----------------------------------------------------------------------
class Promocao(db.Model):
    __tablename__ = 'promocoes'

    id = db.Column(db.Integer, primary_key=True)
    id_categoria = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)
    itens_em_promocao = db.Column(db.Text, nullable=True)  # Pode armazenar IDs ou nomes de itens
    descricao_detalhes = db.Column(db.Text, nullable=True)
    imagem = db.Column(db.String(255), nullable=True)
    preco_original = db.Column(db.Numeric(10, 2), nullable=False)
    preco_promocional = db.Column(db.Numeric(10, 2), nullable=False)
    disponibilidade = db.Column(db.Boolean, default=True)