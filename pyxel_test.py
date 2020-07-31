import pyxel

class App:
	
	def __init__(self):
		pyxel.init(160, 120, caption="Pyxel Bear")
		pyxel.image(0).load(0, 0, "bear_head.png" )
	
	def update(self):
		if pyxel.btnp(pyxel.KEY_Q):
			pyxel.quit()
	
	def draw(self):
		pyxel.cls(0)
		pyxel.text(55, 41, "That which does not kill you makes you stronger.", pyxel.frame_count % 16)
		pyxel.text(55, 45, "Except bears. Bears will kill you.", pyxel.frame_count % 16)
		pyxel.blt(61, 66, 0, 0, 0, 38, 16)



while True:
	App()
	