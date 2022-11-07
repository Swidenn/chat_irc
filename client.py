

class Client:
    def __init__(self, name):
        self.name = name

    """
    METHODE getMessage(message)
        but: Récupère le message du client
        args:
            None
        return:
            None
    """
    def getMessage(self):
        return input(f"[{self.name}]: ")