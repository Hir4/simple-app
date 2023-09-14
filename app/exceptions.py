class AccountAlreadyCreated(Exception):
    def __init__(self, message="Username duplicated, already exists."):
        self.message = message
        super().__init__(self.message)

    def get_message(self):
        return self.message
