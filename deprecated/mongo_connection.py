from deprecated.base_mongo_connection import BaseMongoConnection


class NormalConnection(BaseMongoConnection):
    def __init__(self, mongo_host, mongo_port, mongo_user, mongo_password, mongo_db, auth_db):
        super().__init__(mongo_host, mongo_port, mongo_user, mongo_password, mongo_db, auth_db)
