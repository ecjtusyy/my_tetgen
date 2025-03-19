import pyvista as pv
import tetgen


def load_obj(file_path):
    mesh = pv.read(file_path)
    return mesh


def is_triangles(mesh):
    mesh = mesh.triangulate()
    return mesh


def ensure_triangulated(mesh):
    mesh = is_triangles(mesh)
    return mesh


def tetrahedralize_mesh(mesh):
    tet = tetgen.TetGen(mesh)
    verts, elems = tet.tetrahedralize()
    return verts, elems


def visualize_mesh(verts, elems):
    # 创建一个包含每个四面体的单元格类型的数组
    celltypes = [pv.CellType.TETRA] * len(elems)
    # 创建一个包含每个单元格的点数的数组
    cell_connectivity = elems.flatten()
    n_points_per_cell = 4
    cell_offsets = n_points_per_cell * np.arange(len(elems))

    # 创建四面体网格
    grid = pv.UnstructuredGrid(cell_offsets, celltypes, cell_connectivity, points=verts)

    # 创建绘图窗口
    plotter = pv.Plotter()
    plotter.add_mesh(grid, show_edges=True, opacity=0.6)
    plotter.show()


import numpy as np

def main(file_path):
    mesh = load_obj(file_path)
    mesh = ensure_triangulated(mesh)
    verts, elems = tetrahedralize_mesh(mesh)
    visualize_mesh(verts, elems)


main("/home/robot/文档/Genesis-main/Genesis/genesis/assets/meshes/cube.obj")
