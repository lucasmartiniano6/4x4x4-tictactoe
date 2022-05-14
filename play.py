from ursina import *

app = Ursina()

class Plane(Entity):
  def __init__(self, x_start, y_start, clr=color.white):
    self.clr = clr
    self.player = 1
    self.cubes = []
    y = y_start
    z = 10
    for l in range(4):
      line = []
      x = x_start
      for col in range(4):
        cube = Entity(model='cube', collider='box', texture='white_cube', position=(Vec3(x,y,z)), on_click=self.clicked, rotation_x=250, color=self.clr)
        line.append(cube)
        x += 1.3
      self.cubes.append(line)
      y += 1.4
      z += 5
    
  def clicked(self):
    for l in self.cubes:
      for cube in l:
        if cube.hovered:
          if self.player == 1:
            cube.color = color.magenta
          else:
            cube.color = color.orange
          self.player *= -1


plane1 = Plane(-1.5,5, clr=color.light_gray)
plane2 = Plane(-1.5,2.5)
plane3 = Plane(-1.5,-1.5, clr=color.light_gray)
plane4 = Plane(-1.5,-5.5)

def input(key):
  speed = 3
  for plane in [plane1, plane2]:
    for l in plane.cubes:
      for cube in l:
        cube.rotation_x -= held_keys['w'] * time.dt *speed
        cube.rotation_x += held_keys['s'] * time.dt *speed
        cube.rotation_y -= held_keys['d'] * time.dt *speed
        cube.rotation_y += held_keys['a'] * time.dt *speed

def update():
  speed = 7
  camera.y += held_keys['w'] * time.dt * speed
  camera.y -= held_keys['s'] * time.dt * speed
  camera.x += held_keys['d'] * time.dt * speed
  camera.x -= held_keys['a'] * time.dt * speed

  camera.z += held_keys['e'] * time.dt * speed * 3
  camera.z -= held_keys['q'] * time.dt * speed * 3

app.run()
