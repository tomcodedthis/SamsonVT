"""Task C of SamsonVT by Tom Howcroft (tomcodedthis)"""
import math
import bpy

def create_mandelbrot_fractal():
    """creates the fractal object"""
    verticies = get_vertex_positions()
    faces = get_faces_indicies()

    mesh = bpy.data.meshes.new("Mandelbrot")
    obj = bpy.data.objects.new("Mandelbrot", mesh)
    bpy.context.collection.objects.link(obj)

    mesh.from_pydata(verticies,[],faces)
    mesh.update(calc_edges=True)

def get_vertex_positions():
    """returns a list of all verticies positions (x, y, z)"""
    position_list = []

    for i in range(RESOLUTION):
        for j in range(RESOLUTION):
            pos_x = (i / RESOLUTION * 4) - 2
            pos_y = (j / RESOLUTION * 4) - 2

            z_x = 0
            z_y = 0

            for k in range(255):
                x_t = z_x * z_y
                z_x = z_x * z_x - z_y * z_y + pos_x
                z_y = 2 * x_t + pos_y

                if z_x * z_x + z_y * z_y > 4:
                    break

            pos_z = math.log1p(k) / 10

            if pos_z < 0.19:
                positions = (0, 0, 0)
            else:
                positions = (pos_x, pos_y, pos_z)

            position_list.append(positions)

    return position_list

def get_faces_indicies():
    """returns a list of all face indicies (a, b, c, d)"""
    indicies_list = []
    count = 0

    for i in range (RESOLUTION * (RESOLUTION - 1)):
        if count < RESOLUTION - 1:
            index_a = i
            index_b = i + 1
            index_c = (i + RESOLUTION) + 1
            index_d = (i + RESOLUTION)

            face_index = (index_a, index_b, index_c, index_d)
            indicies_list.append(face_index)

            count = count + 1
        else:
            count = 0

    return indicies_list

def color_object():
    """gives random color to all objects in scene"""
    obj = bpy.data.objects['Mandelbrot']

    mat = bpy.data.materials.new(name="Material")
    col = [1, 0, 0, 1]

    mat.diffuse_color = col
    obj.active_material = mat

def center_view():
    """centers the fractal object in 3D view"""
    area = next((area for area in bpy.context.screen.areas if area.type == 'VIEW_3D'), None)
    space = area.spaces.active

    v3d = space.region_3d
    v3d.view_location = (-0.5, 0, 0)
    v3d.view_distance = (4.0)
    v3d.view_rotation = (180.0, 0.0, 0.0, 0.0)


RESOLUTION = 1000

create_mandelbrot_fractal()
color_object()
center_view()
