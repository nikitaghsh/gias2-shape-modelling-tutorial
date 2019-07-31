# -*- coding: utf-8 -*-
"""

Created by Desney Greybe, 2018.

"""
#%%#########################################################################%%#
import os

from packages.pca import ShapeModel

#%%#########################################################################%%#
# Directory parameters
root_dir = os.getcwd()

pca_fold = os.path.join("shape_model")
mesh_fold = os.path.join("aligned_meshes")
bone_name = "l1"

#%%#########################################################################%%#
# Setup folder paths
pca_path = os.path.join(root_dir, pca_fold)
mesh_path = os.path.join(root_dir, mesh_fold)

# Run processes
# bone_name = "femur_l"

# Create PCA object
pca_model = ShapeModel(pca_path,bone_name)
pca_model.load_shape_model()
pca_model.load_mean_mesh() 


# Subject 1 ---- L1's
#weights =[131.92013851,  32.97935279,   69.11261573,  -64.41766781,    4.52108763,   19.57395783,   36.53112295,   32.34486336,    4.07804132,  -28.90113189,  -36.52143252,  -40.63178651,   10.82997502,   -6.41045908,   11.07321439]

weights = [ -8.41386651e+01,  -2.49091065e+00,  -2.48472048e+01,  -1.12865975e+01,
    1.02443707e+01,   8.01650591e+00,   6.71502663e+00,   4.54660509e+00,
    8.34805973e+00,   3.33579773e+00,  -3.98218186e+00,  -3.91636988e+00,
    8.15069619e-01,  -5.94624847e+00,   6.24785283e+00,   9.90052219e+00,
   -8.20504942e+00,   1.17889497e+00,   7.21459107e+00,  -4.39375656e+00,
    1.46907526e+00,  -5.41632216e+00,   5.02106626e-01,   1.19749956e+00,
   -5.38018775e+00,   4.09279849e+00,   5.68404970e+00,  -2.39090711e+00]
pca_model.create_mesh_from_weights(mesh_path, bone_name, weights)


# Subject 1
weights =[ 7.64727955e+02, -8.57061187e+01 , 1.00032400e+01 ,-7.47391174e+01,
  -5.81297862e+01 , 6.27034398e+01,  1.76780177e+01,  2.74698743e+01,
   2.75286096e+01]
pca_model.create_mesh_from_weights(mesh_path, bone_name, weights)
"""
# # Subject 2
# weights =   [ -82.17327925 ,   5.03543634  ,-37.62433398,  -17.54797086,   18.9439779,
#     26.0728638   , 15.05841175   ,23.40461974 , -24.36556553]
# pca_model.create_mesh_from_weights(mesh_path, bone_name, weights)
"""
# Subject 3
weights = [ 6.59884226e+01 , 2.13545230e+01 ,-4.96452455e+00  ,2.07322494e+01,
   6.44321452e+00, -1.71725548e+01 ,-6.29142392e+00 ,-9.08639601e+00,
  -1.08081006e+01]
pca_model.create_mesh_from_weights(mesh_path, bone_name, weights)

# Subject 4
weights =   [-3.86726130e+02, -2.45833332e+01 , 8.70990925e+00 ,-2.64233630e+01,
   2.32277524e+00 , 2.16459777e+01 , 9.52834148e+00,  1.31762486e+01,
   1.72262357e+01]
pca_model.create_mesh_from_weights(mesh_path, bone_name, weights)

# Subject 5
weights =  [-1.60206150e+02, -1.31308082e+01,  4.20552239e+00 ,-1.37322821e+01,
  -2.12320249e-01 , 1.12818745e+01,  4.74845451e+00 , 6.63273272e+00,
   8.48748296e+00]
pca_model.create_mesh_from_weights(mesh_path, bone_name, weights)
