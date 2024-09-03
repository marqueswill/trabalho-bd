from DBConection import Database


class DBOperation:
    def __init__(self, teste=False):
        self.db = Database(teste=teste)
        if teste:
            self.setup()

    def reset(self):
        with open("setup.sql", "r") as file:
            setup_query = file.read()
        with open("triggers.sql", "r") as file:
            triggers_query = file.read()
        with open("procedures.sql", "r") as file:
            procedures_query = file.read()
        with open("views.sql", "r") as file:
            views_query = file.read()

        
        self.db.execute_query(
            setup_query + triggers_query + procedures_query + views_query
        )

    def seed(self):
        with open("seed.sql", "r") as file:
            seed_query = file.read()
        self.db.execute_query(seed_query)

    def setup(self):
        self.reset()
        self.seed()

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
