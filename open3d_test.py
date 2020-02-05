import open3d as o3d

if __name__ == "__main__":
    mesh = o3d.io.read_point_cloud("airplane.pcd", format='ply')
    
    o3d.io.write_triangle_mesh("copy_of_crate.obj", mesh, write_triangle_uvs=False)