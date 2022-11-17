"""Task A of SamsonVT by Tom Howcroft (tomcodedthis)"""
import random
import string
import bpy

cubes_positions = [
[4,6,3],
[6,6,3],
[3,3,3],
[3,2,3],
[7,3,3],
[7,2,3],
[4,1,3],
[5,1,3],
[6,1,3]
]

def create_cubes(positions):
    """creates mesh cubes given their positions(x, y , z) as a list"""
    for position in positions:
        pos_x = position[0]
        pos_y = position[1]
        pos_z = position[2]

        bpy.ops.mesh.primitive_cube_add(size=1,
                                        enter_editmode=False,
                                        align='WORLD',
                                        location=(pos_x, pos_y, pos_z),
                                        rotation=(rdm_numbers(1), rdm_numbers(1), rdm_numbers(1)),
                                        scale=(1, 1, 1))

def color_cubes():
    """gives random color to all objects in scene"""
    for obj in bpy.data.objects:
        mat = bpy.data.materials.new(name=f"Material.{rdm_numbers(2)}")
        col = [rdm_numbers(1), rdm_numbers(1), rdm_numbers(1), rdm_numbers(1)]

        mat.diffuse_color = col
        obj.active_material = mat

def rdm_numbers(amount):
    """returns int (x)amount of random numbers"""
    return int(''.join(random.choices(string.digits, k = amount)))

create_cubes(cubes_positions)
color_cubes()
