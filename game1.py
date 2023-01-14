from ursina import *

app = Ursina()
me = Animation('assets\player',collider ='box',y=1,)
Sky()
camera.orthographic = True
camera.fov = 20
Entity(
    model = 'quad',
    texture = 'assets\BG',
    scale=50,z=5
    
   
)
def update():
    me.y += held_keys['w']*6*time.dt
    me.y += held_keys['s']*6*time.dt
    
app.run()