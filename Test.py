from ggame import App, Sprite, RectangleAsset, Color, LineStyle

black = Color(0x000000, 1.0)

class Test(App):
    
    def __init__(self):
        super().__init__()
        Sprite(RectangleAsset(100, 100, LineStyle(1.0, black), black), (100, 100))
        
app = Test()
