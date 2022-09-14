from PIL import Image
from PIL.ImageDraw import Draw


class Carpet:
    def __init__(self, profundidade):
        self.profundidade = profundidade
        tamanho = 3 ** profundidade
        self.img = Image.new('RGB', (tamanho, tamanho), color="white")
        self.desenhar(self.profundidade, (0, 0, tamanho, tamanho))

    def desenhar(self, n, coordenadas):

        origem = (coordenadas[0], coordenadas[1])
        destino = (coordenadas[2], coordenadas[3])
        x = destino[0] - origem[0] # tamanho

        retangulo = (x/3 + origem[0], x/3 + origem[1], 2*x/3 + origem[0], 2*x/3 + origem[1])
        preto = (0, 0, 0)
        draw_ = Draw(self.img)
        draw_.rectangle(retangulo, preto)
        if n <= 2:
            return

        #   ----------------------------
        #   |   1    |   2   |    3    |
        #   |---------------------------
        #   |   4    |   C   |    5    |
        #   |---------------------------
        #   |   6    |   7   |    8    |
        #   ----------------------------

        #   linha 1
        Q1 = (0, 0, x/3, x/3)
        Q2 = (0, x/3, x/3, 2*x/3)
        Q3 = (0, 2*x/3, x/3, x)

        #   linha 2
        Q4 = (x/3, 0, 2*x/3, x/3)
        Q5 = (x/3, 2*x/3, 2*x/3, x)

        #   linha 3
        Q6 = (2*x/3, 0, x, x/3)
        Q7 = (2*x/3, x/3, x, 2*x/3)
        Q8 = (2*x/3, 2*x/3, x, x)

        for i in [Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8]:
            self.desenhar(n-1, (i[0] + origem[0], i[1] + origem[1], i[2] + origem[0], i[3] + origem[1]))


carpet = Carpet(9)
carpet.img.show()
carpet.img.save("out.png")


