# Autenticando com uso da lib Flask-JWT

from user import User


users = [User(1, 'Jose', 'Mypass'),
         User(2, 'Maria', 'secret')
]

# funções JWT
# linka cada user ao seu name num dic, e dps seu id num dic
username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

def authenticate(username, password):

    # tenta buscar um user na tabela e retorna None caso n exista
    user = username_table.get(username, None)
    if user and password == user.password:
        return user

def identity(payload):

    user_id = payload['identity']
    return userid_table.get(user_id, None)