class Store:
    def __init__(self, key_type, value_type):
        self.data = {}
        self.key_type = key_type
        self.value_type = value_type
        self.pending_changes = []

    def set(self, key, value):
        if not isinstance(key, self.key_type):
            raise ValueError(f"Key must be of type {self.key_type}")
        if not isinstance(value, self.value_type):
            raise ValueError(f"Value must be of type {self.value_type}")
        self.pending_changes.append(("set", key, value))

    def get(self, key):
        return self.data.get(key)

    def delete(self, key):
        self.pending_changes.append(("delete", key))

    def begin(self):
        self.pending_changes = []

    def commit(self):
        for change in self.pending_changes:
            if change[0] == "set":
                self.data[change[1]] = change[2]
            elif change[0] == "delete":
                del self.data[change[1]]
        self.pending_changes = []

    def rollback(self):
        self.pending_changes = []
