"""Task A of SamsonVT by Tom Howcroft (tomcodedthis)"""
import random
import string
import bpy
import numpy as np

def build_mesh_cubes(amount):
    """builds (x)amount of mesh cubes"""
    for i in range(amount):
        bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False,
        align='WORLD', location=(i, 0, get_sine_values()[i]), scale=(1, 1, 1))

def name_scene_objects():
    """names all current scene objects"""
    for obj in bpy.data.objects:
        obj.name = rdm_letters(3)+'/'+rdm_numbers(3)

def rdm_letters(amount):
    """returns (x)amount of random letters"""
    return str(''.join(random.choices(string.ascii_letters, k = amount)))

def rdm_numbers(amount):
    """returns (x)amount of random numbers"""
    return str(''.join(random.choices(string.digits, k = amount)))

def get_sine_values():
    """returns list of z-axis values (-10 to 10) of a sine wave"""
    z_axis = np.sin(np.arange(0, 15, 0.3))

    for count, value in enumerate(z_axis):
        z_axis[count] = round(value * 10, 0)

    return z_axis

def print_totals():
    """counts total vertices in scene"""
    scene = bpy.context.scene
    objects = scene.objects

    objects_count = len(objects)
    vertices_count = 0
    materials_count = 0

    for obj in objects:
        vertices_count += len(obj.data.vertices)
        materials_count += len(obj.data.materials)

    print(f'Total number of objects: {objects_count}')
    print(f'Total number of vertices: {vertices_count}')
    print(f'Total number of materials: {materials_count}')

build_mesh_cubes(50)
name_scene_objects()
print_totals()
