class Resource:

    def __init__(self, name):
        self.name = name
        self.state = 0

    def set_on(self):
        self.change_state(1)

    def set_off(self):
        self.change_state(0)

    def change_state(self, new_state):
        if self.state == new_state:
            return False
        self.state = new_state
        return True

    def __repr__(self):
        return f"{self.name}: {self.state}"


if __name__ == "__main__":
    """ TODO: remove this after, its only for
    testing purposes
    """
    r = Resource("Lamp")
    r.set_on()
    print(r)
    r.set_off()
    print(r)