import pyxel

pyxel.init(160, 120, caption="Pyxel Bear")
		
pyxel.image(0).load(0, 0, "bear_head.png" )
	
def update():
		if pyxel.btnp(pyxel.KEY_Q):
			pyxel.quit()
	
def draw():
		pyxel.cls(0)
		pyxel.text(10, 10, "That which does not kill you...", pyxel.frame_count % 16)
		pyxel.text(10, 20, "makes you stronger.", pyxel.frame_count % 16)
		pyxel.text(10, 30, "Except bears. Bears will kill you.", pyxel.frame_count % 16)
		pyxel.blt(60, 40, 0, 0, 0, 32, 32)



pyxel.run(update, draw)
	