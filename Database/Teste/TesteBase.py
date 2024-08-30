from DBConection import Database


class TesteBase:        
    def run(self):
        return [
            self.test_insert(),
            self.test_get_by_id(),
            self.test_get_all(),
            self.test_update(),
            # self.test_update_all(),
            self.test_delete(),
            # self.test_delete_all(),
        ]

    def test_insert(self):
        pass

    def test_update(self):
        pass

    def test_update_all(self):
        pass

    def test_delete(self):
        pass

    def test_delete_all(self):
        pass

    def test_get_by_id(self):
        pass

    def test_get_all(self):
        pass
