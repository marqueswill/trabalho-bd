from DBConection import Database


class TesteBase:
    def __init__(self):
        self.db = Database(teste=True)
        with open("setup.sql", "r") as file:
            setup_query = file.read()  # Read the entire file into a string
        self.db.execute_query(setup_query)

    def run(self):
        # self.delete_all()
        return [
            self.test_insert(),
            # self.test_get_by_id(),
            # self.test_get_all(),
            # self.test_delete(),
        ]

    def test_insert(self):
        pass

    def test_update(self):
        pass

    def test_delete(self):
        pass

    def delete_all(self):
        pass

    def test_get_by_id(self):
        pass

    def test_get_all(self):
        pass
