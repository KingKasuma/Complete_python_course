class MyCustomError(TypeError):
    def __init__(self, message, code):
        super().__init__(f'Eroor code {code}: {message}')
        self.code = code

raise MyCustomError('OUCH! An error happened.', 500)