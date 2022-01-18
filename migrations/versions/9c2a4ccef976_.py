"""empty message

Revision ID: 9c2a4ccef976
Revises: 
Create Date: 2022-01-18 19:57:49.242067

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c2a4ccef976'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('carrinho',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('preco_frete', sa.Integer(), nullable=False),
    sa.Column('quantidade', sa.Integer(), nullable=False),
    sa.Column('preco_total', sa.Integer(), nullable=False),
    sa.Column('cupom_desconto', sa.Boolean(), nullable=False),
    sa.Column('usuario_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuario.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('carros',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('cor', sa.String(length=10), nullable=False),
    sa.Column('modelo', sa.String(length=20), nullable=False),
    sa.Column('marca', sa.String(length=20), nullable=False),
    sa.Column('ano_fabricacao', sa.Integer(), nullable=False),
    sa.Column('motor', sa.String(length=10), nullable=False),
    sa.Column('estoque', sa.Integer(), nullable=False),
    sa.Column('preco', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('motos',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('cor', sa.String(length=10), nullable=False),
    sa.Column('modelo', sa.String(length=20), nullable=False),
    sa.Column('marca', sa.String(length=20), nullable=False),
    sa.Column('ano_fabricacao', sa.Integer(), nullable=False),
    sa.Column('motor', sa.String(length=10), nullable=False),
    sa.Column('estoque', sa.Integer(), nullable=False),
    sa.Column('preco', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('usuario',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=30), nullable=False),
    sa.Column('cpf', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('telefone', sa.Integer(), nullable=False),
    sa.Column('endereço', sa.String(length=30), nullable=False),
    sa.Column('carrinho_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['carrinho_id'], ['carrinho.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cpf'),
    sa.UniqueConstraint('email')
    )
    op.create_table('carroscompra',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('quantidade', sa.Integer(), nullable=False),
    sa.Column('preco_unitario', sa.Integer(), nullable=False),
    sa.Column('preco_total', sa.Integer(), nullable=False),
    sa.Column('carrinho_id', sa.Integer(), nullable=True),
    sa.Column('carros_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['carrinho_id'], ['carrinho.id'], ),
    sa.ForeignKeyConstraint(['carros_id'], ['carros.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cupons',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('valor_desconto', sa.Integer(), nullable=False),
    sa.Column('quantidade', sa.Integer(), nullable=False),
    sa.Column('categoria', sa.String(length=20), nullable=False),
    sa.Column('usuario_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuario.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('motoscompra',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('quantidade', sa.Integer(), nullable=False),
    sa.Column('preco_unitario', sa.Integer(), nullable=False),
    sa.Column('preco_total', sa.Integer(), nullable=False),
    sa.Column('carrinho_id', sa.Integer(), nullable=True),
    sa.Column('motos_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['carrinho_id'], ['carrinho.id'], ),
    sa.ForeignKeyConstraint(['motos_id'], ['motos.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('requisicoes',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('data', sa.Date(), nullable=False),
    sa.Column('preco_frete', sa.Integer(), nullable=False),
    sa.Column('preco_total', sa.Integer(), nullable=False),
    sa.Column('usuario_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuario.id'], ),
    sa.PrimaryKeyConstraint('id', 'preco_frete', 'preco_total')
    )
    op.create_table('association_requisicoes_carros_compra',
    sa.Column('carroscompra', sa.Integer(), nullable=True),
    sa.Column('requisicoes', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['carroscompra'], ['carroscompra.id'], ),
    sa.ForeignKeyConstraint(['requisicoes'], ['requisicoes.id'], )
    )
    op.create_table('association_requisicoes_motos_compra',
    sa.Column('motoscompra', sa.Integer(), nullable=True),
    sa.Column('requisicoes', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['motoscompra'], ['motoscompra.id'], ),
    sa.ForeignKeyConstraint(['requisicoes'], ['requisicoes.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('association_requisicoes_motos_compra')
    op.drop_table('association_requisicoes_carros_compra')
    op.drop_table('requisicoes')
    op.drop_table('motoscompra')
    op.drop_table('cupons')
    op.drop_table('carroscompra')
    op.drop_table('usuario')
    op.drop_table('motos')
    op.drop_table('carros')
    op.drop_table('carrinho')
    # ### end Alembic commands ###
