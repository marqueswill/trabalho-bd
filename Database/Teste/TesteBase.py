from DBConection import Database


class TesteBase:

    def run(self):
        print(f"{self.__class__.__name__}:")

        results = {
            "insert   ": self.test_insert(),
            "get_by_id": self.test_get_by_id(),
            "get_all  ": self.test_get_all(),
            "update   ": self.test_update(),
            # "update_all": self.test_update_all(),
            "delete   ": self.test_delete(),
            # "delete_all": self.test_delete_all(),
        }

        failed_tests = [name for name, result in results.items() if result != "Success"]

        for name, result in results.items():
            print(f"    {name}: {result}")

        if not failed_tests:
            print("All tests passed")
        else:
            print("Tests failed: " + ", ".join(failed_tests))

        print("\n")

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
