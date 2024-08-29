from DBConection import Database


class DBOperation:
    def __init__(self):
        self.db = Database()
        with open("setup.sql", "r") as file:
            setup_query = file.read()
        self.db.execute_query(setup_query)

    def setup(self):
        with open("setup.sql", "r") as file:
            setup_query = file.read()
        self.db.execute_query(setup_query)

    def create_table(self):
        raise NotImplementedError("Subclasses should implement this method")

    def insert(self, obj):
        raise NotImplementedError("Subclasses should implement this method")

    def update(self, obj):
        raise NotImplementedError("Subclasses should implement this method")

    def delete(self, id):
        raise NotImplementedError("Subclasses should implement this method")

    def delete_all(self):
        raise NotImplementedError("Subclasses should implement this method")

    def get_by_id(self, id):
        raise NotImplementedError("Subclasses should implement this method")

    def get_all(self):
        raise NotImplementedError("Subclasses should implement this method")
