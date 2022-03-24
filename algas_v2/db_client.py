from abc import ABC, abstractmethod

class Client(ABC):
    def __init__(self, schema: dict) -> None:
        super().__init__()
        self.schema = schema

    @abstractmethod
    def batch_insert(data: list):
        pass

class SqlLiteClient(Client):
    def __init__(self, schema: dict) -> None:
        super().__init__(schema)

    def batch_insert(data: list):
        return super().batch_insert()

    def __create_dml(self):
        fields = self.schema["fields"]
        dml_insert = ",".join(field["name"] for field in fields)
        dml_values = ""
        for field in fields:
            if field["type"] in ["DATE", "DATETIME", "TIME", "STRING"]:
                dml_values += f"'%{field['name']}'"
            else:
                dml_values += f"%{field['name']}"
                
        return f"{dml_insert}({dml_values})"

    def __format_date(self):
        raise NotImplementedError()
        


