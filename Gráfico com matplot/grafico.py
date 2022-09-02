class Grafico:
    def __init__(self,titulo, x, y):
        self.titulo = titulo
        self.x = x
        self.y = y

    def __str__(self):
        return f'Grafico(titulo={self.titulo}, e_x={self.x}, e_y={self.y}'