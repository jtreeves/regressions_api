"""empty message

Revision ID: 3e97ff4378d6
Revises: 
Create Date: 2021-06-11 17:23:58.968891

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '3e97ff4378d6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('key', sa.String(length=100), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('regressions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('source', sa.String(length=100), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('independent', sa.String(), nullable=False),
    sa.Column('dependent', sa.String(), nullable=False),
    sa.Column('precision', sa.Integer(), nullable=False),
    sa.Column('data_set', postgresql.ARRAY(sa.Float()), nullable=False),
    sa.Column('linear_coefficients', postgresql.ARRAY(sa.Float()), nullable=True),
    sa.Column('linear_points', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.Column('linear_correlation', sa.Float(), nullable=True),
    sa.Column('quadratic_coefficients', postgresql.ARRAY(sa.Float()), nullable=True),
    sa.Column('quadratic_points', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.Column('quadratic_correlation', sa.Float(), nullable=True),
    sa.Column('cubic_coefficients', postgresql.ARRAY(sa.Float()), nullable=True),
    sa.Column('cubic_points', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.Column('cubic_correlation', sa.Float(), nullable=True),
    sa.Column('hyperbolic_coefficients', postgresql.ARRAY(sa.Float()), nullable=True),
    sa.Column('hyperbolic_points', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.Column('hyperbolic_correlation', sa.Float(), nullable=True),
    sa.Column('exponential_coefficients', postgresql.ARRAY(sa.Float()), nullable=True),
    sa.Column('exponential_points', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.Column('exponential_correlation', sa.Float(), nullable=True),
    sa.Column('logarithmic_coefficients', postgresql.ARRAY(sa.Float()), nullable=True),
    sa.Column('logarithmic_points', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.Column('logarithmic_correlation', sa.Float(), nullable=True),
    sa.Column('logistic_coefficients', postgresql.ARRAY(sa.Float()), nullable=True),
    sa.Column('logistic_points', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.Column('logistic_correlation', sa.Float(), nullable=True),
    sa.Column('sinusoidal_coefficients', postgresql.ARRAY(sa.Float()), nullable=True),
    sa.Column('sinusoidal_points', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.Column('sinusoidal_correlation', sa.Float(), nullable=True),
    sa.Column('best_fit', sa.String(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('regressions')
    op.drop_table('users')
    # ### end Alembic commands ###