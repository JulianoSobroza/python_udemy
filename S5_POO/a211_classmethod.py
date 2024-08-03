# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)

class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, paassword):
        connection = cls()
        connection.user = user
        connection.password = paassword
        return connection

# para usar com set
c1 = Connection()
c1.set_user('Juliano')
c1.set_password('123')
print(c1.user, c1.password)

# para usar com classmethod
c2 = Connection.create_with_auth('Nicole', '147')
print (c2.user, c2.password)