import random
import pkgutil
import bpy
class MyPackage:
    
    def __init__(self):
        pass
    
    def sum(self, x, y):
        return x + y
    
    def multiply(self, x, y):
        return x * y
    
    def random(self):
        return random.random()
    
    def test_bpy(self):
        bpy.ops.import_scene.obj(filepath="data/Cube.obj")