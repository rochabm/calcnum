"""
Script para criar um fractal baseado no metodo de Newton-Raphson.
Adaptado de "Beginning Python Visualization", Shai Vaingast, Ch.7, Pg.224

Bernardo M. Rocha
"""

from PIL import Image
from math import *

delta = 1.0e-6   # precisao 
res =  500       # tamanho da imagem (qto menor mais rapido)
iters = 10       # numero de iteracoes (qto mais alto, mais brilho)

# area para desenhar (-1,-1) a (1,1)
xa,xb = -1.0, 1.0
ya,yb = -1.0, 1.0

# cria uma imagem para pintar, incialmente toda preta
img = Image.new("RGB", (res, res), (0,0,0))

# calcula solucoes de z**4 + 1 = 0
solutions = [cos((2*n+1)*pi/4)+1j*sin((2*n+1)*pi/4) for n in range(4)]
colors = [(1,0,0), (0,1,0), (0,0,1), (1,1,0)]
print solutions

# loop sobre as partes real/imaginaria para usar como chute inicial
for x in range(0,res):
    zx = x * (xb - xa) / (res - 1) + xa
    for y in range(0,res):
        zy = y * (yb - ya) / (res - 1) + ya
        z = complex(zx,zy)

        # metodo de Newton
        for i in range(iters):
            try:
                z -= (z**4+1)/(4*z**3)
            except ZeroDivisionError:
                # evita divisao por 0
                continue
            if (abs(z**4+1) < delta):
                break

        # brilho eh funcao do numero de iteracoes
        color_depth = int(iters-i)*255.0/iters

        # encontra para qual solucao este chute inicial convergiu
        err = [abs(z-root) for root in solutions]
        distances = zip(err, range(len(colors)))

        # seleciona a cor associada com a solucao
        color = [int(i*color_depth) for i in colors[min(distances)[1]]]
        img.putpixel((x,y), tuple(color))

# salva a imagem no diretorio atual
img.save('fractal_z4s_%03d_%03d_%03d.png' %
         (iters, res, abs(log10(delta))),
         dpi = (150, 150))
