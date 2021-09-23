from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.sql import select


engine = create_engine('sqlite:///memory.db', echo=True)
metadata_obj = MetaData()
users = Table(
    'users', metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('fullname', String)
)

addresses = Table(
    'addresses', metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('user_id', None, ForeignKey('users.id')),
    Column('email_address', String, nullable=False)
)


def create_db():
    metadata_obj.create_all(engine)


def insert():
    ins = users.insert().values(name='Test', fullname='Test User')
    conn = engine.connect()
    result = conn.execute(ins)
    return result


def insert_user_dictionary(user_dictionary: dict):
    conn = engine.connect()
    ins = users.insert()
    result = conn.execute(ins, user_dictionary)
    return result


def insert_multi_into_addresses(address_list: list):
    conn = engine.connect()
    conn.execute(addresses.insert(), address_list)


def select_from_table(table: Table):
    conn = engine.connect()
    # s = users.select()
    s = select([table])
    result = conn.execute(s)
    return result


def select_fetch_one(table: Table):
    conn = engine.connect()
    s = select([table])
    result = conn.execute(s)
    return result.fetchone()


def select_by_column(columns: list):
    conn = engine.connect()
    s = select(columns)
    result = conn.execute(s)
    return result


def select_join():
    conn = engine.connect()
    s = select([users, addresses]).where(users.c.id == addresses.c.id)
    result = conn.execute(s)
    return result


def join():
    conn = engine.connect()
    s = select([users.c.fullname]).select_from(users.join(addresses,
                                                          addresses.c.email_address.like(users.c.name + '%')))
    result = conn.execute(s)
    return result


def update(current_name, new_name):
    conn = engine.connect()
    s = users.update().where(users.c.name == current_name).values(name=new_name)
    conn.execute(s)


def delete(id):
    conn = engine
    conn.execute(addresses.delete().where(addresses.c.id == id))


if __name__ == '__main__':
    # Creating tables:
    # create_db()

    # Insert one:
    # insert()

    # Insert with a dictionary
    # insert_user_dictionary({"id": 2, "name": "wendy", "fullname": "Wendy Williams"})

    # Insert multiple rows:
    # insert_multi_into_addresses(
    #     [
    #         {'user_id': 1, 'email_address': 'jack@yahoo.com'},
    #         {'user_id': 1, 'email_address': 'jack@msn.com'},
    #         {'user_id': 2, 'email_address': 'www@www.org'},
    #         {'user_id': 2, 'email_address': 'wendy@aol.com'},
    #     ]
    # )

    # Select:
    # res = select_from_table(users)
    # for row in res:
    #     print(row)

    # Select(Fetch One):
    # res = select_fetch_one(users)
    # print(res)

    # Select (By Column):
    # res = select_by_column([users.c.name, users.c.fullname])
    # for row in res:
    #     print(row)

    # Select(join)
    # res = select_join()
    # for row in res:
    #     print(row)

    # join
    # res = join()
    # for row in res:
    #     print(row)

    # update:
    # update('Test', 'UPDATED_NAME')

    # delete
    delete(6)