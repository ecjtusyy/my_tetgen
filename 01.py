import pyvista as pv

def load_obj(file_path):
    mesh=pv.read(file_path)
    return mesh


def is_triangles(mesh):
    mesh=pv.PolyData.triangulate(mesh)
    return mesh

def ensure_triangulated(mesh):
    mesh=is_triangles(mesh)
    return mesh

import tetgen

def tetrahedralize_mesh(mesh):
    tet = tetgen.TetGen(mesh)
    verts, elems = tet.tetrahedralize()
    return verts, elems


def main(file_path):
    mesh=load_obj(file_path)
    mesh=ensure_triangulated(mesh)
    dict=tetrahedralize_mesh(mesh)
    print(dict)


# main("/home/robot/文档/Genesis-main/Genesis/genesis/assets/meshes/jikeng_centre1.0.obj")
main("/home/robot/文档/Genesis-main/Genesis/genesis/assets/meshes/cube.obj")
