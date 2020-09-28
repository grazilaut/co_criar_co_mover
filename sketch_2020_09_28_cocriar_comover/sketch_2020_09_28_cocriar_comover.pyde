# modo 2: CREATE: insere quadrado com tamnho pré-definido de acordo com posição do mouse
# modo 3: RECREATE: altera parâmetro do quadrado 
# modo 0: MOVE: permite arratar o quadrados com o mouse
# modo 1: REMOVE: deleta o quadrado
# outros botões: passar a vez e/ou timer


#supor o que vou utilizar 
#alterar modo por tecla (keyPressed - imprimir no console qual modo estou)
from retangulos import Rect

modo = 0 # variavel global que gerencia os modos

acionadores = ((20, 10, 140, 40, "mover"),
               (20, 940, 190, 40, "remover"),
               (875, 10, 100, 40, "criar"),
               (830, 940, 140, 40, "recriar"))

retangulos = [Rect(200, 500, 200, 200),
              Rect(300, 500, 400, 400),
              Rect(0, 0, 600, 600),
              Rect(100, 100, 500, 500)] 
                
def setup():
    size(1000, 1000)
    textSize(50) 

def draw():
    background(200)
    strokeWeight(10) 
    noFill()
    stroke(0)
    strokeWeight(10) 
    rect(300, 300, 400, 400)
    
    for r in retangulos:
        if r.mouse_over():
            r.destaque = True
            break
    
    for r in reversed(retangulos):
        r.display(mousePressed)
        
    for i,a in enumerate(acionadores):
        x, y, w, h, p = a
        if i == modo:
            fill(200,0,0)
        else: 
            fill(0)
        #rect(x,y,w,h) #área clicável do texto dos acionadores
        text(p, x, y + 40)
        
def mousePressed():
    global modo
    for i, a in enumerate(acionadores):
        x, y, w, h, _ = a
        if (x<mouseX<x+w and y<mouseY<y+h):
            modo = i
            return
    if modo == 0: # mover
         for r in retangulos: 
            if r.mouse_over():
                r.arrastado = True
                break
    elif modo == 1: #remover
         for r in retangulos: 
            if r.mouse_over():
                retangulos.remove(r)
                break       
    elif modo == 2: #criar
        retangulos.append(Rect(mouseX, mouseY, 100, 100))
        
    elif modo == 3: # recriar
         for r in retangulos: 
            if r.mouse_over():
                r.arrastado = True
                break
        
def mouseReleased():
        for r in retangulos:
            r.arrastado = False
        
def mouseDragged():
    for r in retangulos:
        if r.arrastado:
            dx = mouseX - pmouseX
            dy = mouseY - pmouseY
            if modo == 0:
                x = r.x + dx
                y = r.y + dy
                na_tela = 0 < x < width - r.w and 0 < y < height - r.h
                if na_tela:
                    r.x = x
                    r.y = y 
            elif modo == 3:
                 r.w = r.w + dx
                 r.h = r.h + dy
               
                

    
        
 
        
