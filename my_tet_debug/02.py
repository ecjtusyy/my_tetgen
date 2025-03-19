import pyvista as pv
import tetgen

def load_obj(file_path):
    # 加载 OBJ 文件
    mesh = pv.read(file_path)
    return mesh

def is_triangles(mesh):
    # 检查并将网格三角化
    if not mesh.is_all_triangles():
        mesh = mesh.triangulate()
    return mesh

def ensure_triangulated(mesh):
    # 确保网格为三角形
    mesh = is_triangles(mesh)
    return mesh

def repair_mesh(mesh):
    # 修复网格，使其成为流形
    if not mesh.is_manifold:
        mesh = mesh.clean()
    return mesh

def tetrahedralize_mesh(mesh):
    # 使用 TetGen 进行四面体化
    tet = tetgen.TetGen(mesh)
    verts, elems = tet.tetrahedralize()
    return verts, elems

def main(file_path):
    # 加载并处理网格
    mesh = load_obj(file_path)
    mesh = ensure_triangulated(mesh)
    mesh = repair_mesh(mesh)
    verts, elems = tetrahedralize_mesh(mesh)
    return verts, elems

# 示例调用
if __name__ == "__main__":
    file_path = "/home/robot/文档/Genesis-main/Genesis/genesis/assets/meshes/cube.obj"
    verts, elems = main(file_path)
    print(f"顶点数: {len(verts)}, 元素数: {len(elems)}")