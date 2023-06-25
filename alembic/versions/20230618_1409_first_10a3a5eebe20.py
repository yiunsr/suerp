"""first

Revision ID: 10a3a5eebe20
Revises: 
Create Date: 2023-06-18 14:09:16.668110

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '10a3a5eebe20'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('deal',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=1), server_default=sa.text("''"), nullable=False),
    sa.Column('status', sa.String(length=1), server_default=sa.text("''"), nullable=False),
    sa.Column('testmode', sa.String(length=1), server_default=sa.text("''"), nullable=False),
    sa.Column('ref_id1', sa.Integer(), nullable=True),
    sa.Column('ref_id0', sa.Integer(), nullable=True),
    sa.Column('create_user', sa.Integer(), nullable=False),
    sa.Column('update_user', sa.Integer(), nullable=False),
    sa.Column('data_jb', postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'{}'::jsonb"), nullable=True),
    sa.Column('tags_jb', postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'[]'::jsonb"), nullable=True),
    sa.Column('category_data_jb', postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'{}'::jsonb"), nullable=True),
    sa.Column('category_tags_jb', postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'[]'::jsonb"), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('organization',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), server_default=sa.text("''"), nullable=False),
    sa.Column('address_jb', postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'[]'::jsonb"), nullable=True),
    sa.Column('phone_jb', postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'[]'::jsonb"), nullable=True),
    sa.Column('email_jb', postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'[]'::jsonb"), nullable=True),
    sa.Column('messenger_jb', postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'[]'::jsonb"), nullable=True),
    sa.Column('url_jb', postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'[]'::jsonb"), nullable=True),
    sa.Column('testmode', sa.String(length=1), server_default=sa.text("''"), nullable=False),
    sa.Column('status', sa.String(length=1), server_default=sa.text("'A'"), nullable=False),
    sa.Column('ref_id0', sa.Integer(), nullable=True),
    sa.Column('ref_id1', sa.Integer(), nullable=True),
    sa.Column('ref_id2', sa.Integer(), nullable=True),
    sa.Column('ref_id3', sa.Integer(), nullable=True),
    sa.Column('created_user_id', sa.Integer(), nullable=True),
    sa.Column('updated_user_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('category', sa.Integer(), nullable=True),
    sa.Column('data_jb', postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'{}'::jsonb"), nullable=True),
    sa.Column('tags_jb', postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'[]'::jsonb"), nullable=True),
    sa.Column('category_data_jb', postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'{}'::jsonb"), nullable=True),
    sa.Column('category_tags_jb', postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'[]'::jsonb"), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('permission',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), server_default=sa.text("''"), nullable=False),
    sa.Column('detail', sa.String(length=256), server_default=sa.text("''"), nullable=False),
    sa.Column('key', sa.String(length=8), server_default=sa.text("''"), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('person',
    sa.Column('name', sa.String(length=64), server_default=sa.text("''"), nullable=False),
    sa.Column('first_name', sa.String(length=64), server_default=sa.text("''"), nullable=False),
    sa.Column('last_name', sa.String(length=64), server_default=sa.text("''"), nullable=False),
    sa.Column('address_jb', postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'[]'::jsonb"), nullable=True),
    sa.Column('phone_jb', postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'[]'::jsonb"), nullable=True),
    sa.Column('email_jb', postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'[]'::jsonb"), nullable=True),
    sa.Column('messenger_jb', postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'[]'::jsonb"), nullable=True),
    sa.Column('url_jb', postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'[]'::jsonb"), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('testmode', sa.String(length=1), server_default=sa.text("''"), nullable=False),
    sa.Column('status', sa.String(length=1), server_default=sa.text("'A'"), nullable=False),
    sa.Column('ref_id0', sa.Integer(), nullable=True),
    sa.Column('ref_id1', sa.Integer(), nullable=True),
    sa.Column('ref_id2', sa.Integer(), nullable=True),
    sa.Column('ref_id3', sa.Integer(), nullable=True),
    sa.Column('created_user_id', sa.Integer(), nullable=True),
    sa.Column('updated_user_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('category', sa.Integer(), nullable=True),
    sa.Column('data_jb', postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'{}'::jsonb"), nullable=True),
    sa.Column('tags_jb', postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'[]'::jsonb"), nullable=True),
    sa.Column('category_data_jb', postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'{}'::jsonb"), nullable=True),
    sa.Column('category_tags_jb', postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'[]'::jsonb"), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('person_organization',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('person_id', sa.Integer(), nullable=True),
    sa.Column('org_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('status', sa.String(length=1), server_default=sa.text("''"), nullable=False),
    sa.Column('testmode', sa.String(length=1), server_default=sa.text("''"), nullable=False),
    sa.Column('role_jsonb', postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'[]'::jsonb"), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product',
    sa.Column('name', sa.String(length=128), server_default=sa.text("''"), nullable=False),
    sa.Column('display', sa.String(length=128), server_default=sa.text("''"), nullable=False),
    sa.Column('owner_user_id', sa.Integer(), nullable=True),
    sa.Column('owner_group_id', sa.Integer(), nullable=True),
    sa.Column('owner_person_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('testmode', sa.String(length=1), server_default=sa.text("''"), nullable=False),
    sa.Column('status', sa.String(length=1), server_default=sa.text("'A'"), nullable=False),
    sa.Column('ref_id0', sa.Integer(), nullable=True),
    sa.Column('ref_id1', sa.Integer(), nullable=True),
    sa.Column('ref_id2', sa.Integer(), nullable=True),
    sa.Column('ref_id3', sa.Integer(), nullable=True),
    sa.Column('created_user_id', sa.Integer(), nullable=True),
    sa.Column('updated_user_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('category', sa.Integer(), nullable=True),
    sa.Column('data_jb', postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'{}'::jsonb"), nullable=True),
    sa.Column('tags_jb', postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'[]'::jsonb"), nullable=True),
    sa.Column('category_data_jb', postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'{}'::jsonb"), nullable=True),
    sa.Column('category_tags_jb', postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'[]'::jsonb"), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ugroup',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), server_default=sa.text("''"), nullable=False),
    sa.Column('detail', sa.String(length=64), server_default=sa.text("''"), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('data_jb', postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'{}'::jsonb"), nullable=True),
    sa.Column('testmode', sa.String(length=1), server_default=sa.text("''"), nullable=False),
    sa.Column('status', sa.String(length=1), server_default=sa.text("'A'"), nullable=False),
    sa.Column('ref_id0', sa.Integer(), nullable=True),
    sa.Column('ref_id1', sa.Integer(), nullable=True),
    sa.Column('ref_id2', sa.Integer(), nullable=True),
    sa.Column('ref_id3', sa.Integer(), nullable=True),
    sa.Column('created_user_id', sa.Integer(), nullable=True),
    sa.Column('updated_user_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ugroup_permission',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ugroup_id', sa.Integer(), nullable=True),
    sa.Column('permission_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_role', sa.String(length=1), server_default=sa.text("'N'"), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('name', sa.String(length=64), server_default=sa.text("''"), nullable=False),
    sa.Column('email', sa.String(length=256), nullable=False),
    sa.Column('first_name', sa.String(length=64), server_default=sa.text("''"), nullable=False),
    sa.Column('last_name', sa.String(length=64), server_default=sa.text("''"), nullable=False),
    sa.Column('display', sa.String(length=64), server_default=sa.text("''"), nullable=False),
    sa.Column('nickname', sa.String(length=64), server_default=sa.text("''"), nullable=False),
    sa.Column('avatar', sa.String(length=256), server_default=sa.text("''"), nullable=False),
    sa.Column('api_key', sa.String(length=256), server_default=sa.text("''"), nullable=False),
    sa.Column('api_key_last_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('hash_password', sa.String(length=256), server_default=sa.text("''"), nullable=False),
    sa.Column('password_last_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('last_join_dt', sa.DateTime(timezone=True), nullable=True),
    sa.Column('testmode', sa.String(length=1), server_default=sa.text("''"), nullable=False),
    sa.Column('status', sa.String(length=1), server_default=sa.text("'A'"), nullable=False),
    sa.Column('ref_id0', sa.Integer(), nullable=True),
    sa.Column('ref_id1', sa.Integer(), nullable=True),
    sa.Column('ref_id2', sa.Integer(), nullable=True),
    sa.Column('ref_id3', sa.Integer(), nullable=True),
    sa.Column('category', sa.Integer(), nullable=True),
    sa.Column('data_jb', postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'{}'::jsonb"), nullable=True),
    sa.Column('tags_jb', postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'[]'::jsonb"), nullable=True),
    sa.Column('category_data_jb', postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'{}'::jsonb"), nullable=True),
    sa.Column('category_tags_jb', postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'[]'::jsonb"), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('user_permission',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('permission_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_ugroup',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('ugroup_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###

    # direct query
    # conn = op.get_bind()   # noqa
    # raw_sql = """   """
    # conn.execute(text(raw_sql))


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_ugroup')
    op.drop_table('user_permission')
    op.drop_table('user')
    op.drop_table('ugroup_permission')
    op.drop_table('ugroup')
    op.drop_table('product')
    op.drop_table('person_organization')
    op.drop_table('person')
    op.drop_table('permission')
    op.drop_table('organization')
    op.drop_table('deal')
    # ### end Alembic commands ###

    # direct query
    # conn = op.get_bind()   # noqa
    # raw_sql = """   """"
    # conn.execute(raw_sql)