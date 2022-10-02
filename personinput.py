class PersonInput():

    def __init__(self, name=""):
        self.name = name
        self.got_name = False
        self.input_text = None

    def __repr__(self):
        return (self.name)
