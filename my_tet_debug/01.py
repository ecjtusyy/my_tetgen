import numpy as np
import utils

# 示例顶点和面数据
verts = np.random.rand(100, 3)
faces = np.random.randint(0, 100, size=(200, 3))
tet_cfg = {"quality": 1.0}

# 获取缓存文件路径
tet_path = get_tet_path(verts, faces, tet_cfg)
print(f"缓存文件路径: {tet_path}")