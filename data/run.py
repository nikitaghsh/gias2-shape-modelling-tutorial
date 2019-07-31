# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
from subprocess import call


###############################################################################

root_dir = os.getcwd()
print root_dir

batch_fold = "batch_files"
segmented_fold = "segmentations"
#aligned_1_fold = "1_aligned"
fitted_fold = "fitted_meshes"
aligned_2_fold = "aligned_meshes"
pca_fold = "shape_model"

###############################################################################
bone = "femur_5"
# data = "data"

batch_path = os.path.join(root_dir, batch_fold)
print batch_path
# batch_path = "C:\Users\ngho752\Documents\Alignment codes\code\0_segmented_wrl\femur_l"
segmented_path = os.path.join(root_dir, segmented_fold)
#aligned_1_path = os.path.join(root_dir, aligned_1_fold)
fitted_path = os.path.join(root_dir, fitted_fold)
aligned_2_path = os.path.join(root_dir, aligned_2_fold)
pca_path = os.path.join(root_dir, pca_fold)

#if not os.path.exists(aligned_1_path):
    #os.makedirs(aligned_1_path)
if not os.path.exists(fitted_path):
    os.makedirs(fitted_path)
if not os.path.exists(aligned_2_path):
    os.makedirs(aligned_2_path)    
if not os.path.exists(pca_path):
    os.makedirs(pca_path)
    
###############################################################################
## Align 1
##batch_file = os.path.join(batch_path, "1_rigidreg_" + bone + ".txt")
##call(["gias-rigidreg", "corr_r", "-b", batch_file, "-d", aligned_1_path, "--outext", ".stl"])
##print "- Completed initial registration"

## Fit
# batch_file = os.path.join(batch_path, "1_rigidreg_" + bone + ".txt")
batch_file = os.path.join(batch_path, "rbfreg_list" + ".txt")
print batch_file
# call(["gias-rbfreg", "-b", batch_file, "-d", fitted_path, "--outext", ".ply"],shell=True)
call(["gias-rbfreg", "-b", batch_file, "-d", fitted_path, "--outext", ".ply"])
#call(["gias-rbfreg", "-b", batch_file, "-d", fitted_path, "--outext", ".stl"])
print "- Completed fit"

## Align 2
batch_file = os.path.join(batch_path, "rigidreg_list"  + ".txt")
#call(["gias-rigidreg", "corr_r", "-b", batch_file, "-d", aligned_2_path, "--outext", ".stl"])
call(["gias-rigidreg", "corr_r", "-b", batch_file, "-d", aligned_2_path, "--outext", ".ply"])

print "- Completed post-registration"

# PCA
batch_file = os.path.join(batch_path, "pca_list"  + ".txt")
pca_file = os.path.join(pca_path)
#call(["gias-trainpcashapemodel", batch_file, "-n", "9", "-r", "0", "1", "2", "-o", pca_file, "--plot_pcs", "9", "-v"])
call(["gias-trainpcashapemodel", batch_file, "-n", "28", "-r", "0", "1", "2", "3", "-o", pca_file, "--plot_pcs", "28", "-v"])

print "- Completed pca"
