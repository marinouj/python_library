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
    
    def test_bpy(self, filepath):
        bpy.ops.import_scene.obj(filepath=filepath)
        return 0
    
    
    def test_bpy2(self, context):
        for obj in context.selected_objects:
            print(obj.name)
        return 0