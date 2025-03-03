class Store:
    def __init__(self, key_type, value_type):
        self.data = {}
        self.key_type = key_type
        self.value_type = value_type
        self.in_transaction = False
        self.pending_changes = []

    def set(self, key, value):
        if not isinstance(key, self.key_type):
            raise ValueError(f"Key must be of type {self.key_type}")
        if not isinstance(value, self.value_type):
            raise ValueError(f"Value must be of type {self.value_type}")

        if self.in_transaction:
            self.pending_changes.append(("set", key, value))
        else:
            self.data[key] = value

    def get(self, key):
        return self.data.get(key)

    def delete(self, key):
        if self.in_transaction:
            self.pending_changes.append(("delete", key))
        else:
            del self.data[key]

    def begin(self):
        self.pending_changes = []
        self.in_transaction = True

    def commit(self):
        if not self.in_transaction:
            raise RuntimeError("No transaction to commit")

        for change in self.pending_changes:
            if change[0] == "set":
                self.data[change[1]] = change[2]
            elif change[0] == "delete":
                del self.data[change[1]]
        self.pending_changes = []
        self.in_transaction = False

    def rollback(self):
        if not self.in_transaction:
            raise RuntimeError("No transaction to rollback")
        self.pending_changes = []
        self.in_transaction = False
