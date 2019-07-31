# -*- coding: utf-8 -*-
"""
This script calculates the RMS difference between a pair of bone meshes.
This is done using the fitted bone meshes that have nodal correspondence. The 
absolute distance between each corresponding vertex is calculated. The following
statistics are exported:
	mean, standard deviation, minimum, maximum, and the specified percentiles.

Created by Desney Greybe, 2018.

"""
#%%#########################################################################%%#
import os

from packages.stl_mesh import STL

from packages.calculate import Calculate, Write

#%%#########################################################################%%#
# Directory parameters
root_dir = os.getcwd()

mesh_1_fold = os.path.join("3_aligned")
mesh_1_sub_fold = os.path.join("femur_l")
mesh_2_fold = os.path.join("6a_s3_pca_meshes")
mesh_2_sub_fold = os.path.join("femur_l")
data_fold = os.path.join("6bb_rms_dist")
data_sub_fold = os.path.join("femur_l")

percentiles = [50, 60, 70, 80, 90, 95, 99]

#%%#########################################################################%%#
mesh_1_path = os.path.join(root_dir, mesh_1_fold, mesh_1_sub_fold)
mesh_2_path = os.path.join(root_dir, mesh_2_fold, mesh_2_sub_fold)
data_path = os.path.join(root_dir, data_fold,data_sub_fold)
if not os.path.exists(data_path):
    os.makedirs(data_path)

bone_1_name = "66_left-femur_rbfreg_rigidreg"
bone_2_name = "femur_l"

# Step through meshes
stl_mesh_1 = STL(bone_1_name)
stl_mesh_2 = STL(bone_2_name)

stl_mesh_1.load_stl(mesh_1_path)
stl_mesh_2.load_stl(mesh_2_path)
stl_mesh_1.unique_vertices()
stl_mesh_2.unique_vertices()
               
# Calculate RMS distances
rms = Calculate.rms_distance(stl_mesh_1.vertices, stl_mesh_2.vertices)

# Calculate summary statistics
data = Calculate.statistics(rms, percentiles)
        
# Save RMS distances
Write.rms_distance(bone_1_name, data, percentiles, data_path)
  
 #%%#########################################################################%%#
