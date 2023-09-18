"""
Folder structure:
raw_data
    - global_graph_data
    - local_graph_data
    - voxel_data

"""

import sys
sys.path.insert(0,'/home/maparia/Documents/Building-GAN')


import torch
from GraphConstructor import GraphConstructor
import os
import glob

import sys
argv = sys.argv
voxel_graph_filename = argv[1]
output_fname = argv[2]

g = GraphConstructor.load_graph_jsons(voxel_graph_filename)

torch.save(g, output_fname)

print("Data processing completed")
