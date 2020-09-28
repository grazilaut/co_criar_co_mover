class Rect:
    
    def __init__ (self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.arrastado = False
        self.destaque = False
        
    def display(self, mp):
        colorMode(HSB)
        area = abs(self.w * self.h)
        matiz = area * 255/(width*height)
        stroke(matiz, 255, 255)
        colorMode(RGB)
        
        if self.arrastado:
            strokeWeight(5)
            
        elif self.destaque and not mp:
            stroke(255)
            strokeWeight(20)
            self.destaque = False
        else:
            strokeWeight(2)
        
        rect (self.x, self.y, self.w, self.h)
    
    def mouse_over(self):
        if self.w > 0:
            dentro_horizontal = self.x < mouseX < self.x + self.w
        else:
            dentro_horizontal = self.x + self.w < mouseX < self.x
       
        if self.h > 0:
            dentro_vertical = self.y < mouseY < self.y + self.h
        else:
            dentro_vertical = self.y + self.h < mouseY < self.y
        
        return dentro_horizontal and dentro_vertical 
                
        
    
        
