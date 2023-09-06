

import os
from shutil import copyfile


sub_folders = os.listdir("./")

global_paste_dir = "global_graph_data"
local_paste_dir = "local_graph_data"
voxel_paste_dir = "voxel_data"

if not os.path.exists("global_graph_data"):
    os.mkdir(global_paste_dir)
if not os.path.exists("local_graph_data"):
    os.mkdir(local_paste_dir)
if not os.path.exists("voxel_data"):
    os.mkdir(voxel_paste_dir)

subs = {"global_graph_data", "local_graph_data", "voxel_data"}

index = 0
data_id_length = 5
new_data_id_length = 6

l = 0
for sub_folder in sorted(sub_folders):
    if os.path.isdir(sub_folder) and sub_folder in subs:
        l = len(os.listdir(sub_folder))
        print(sub_folder + " has " + str(l) + " data")
        break

for data_id in range(l):

    global_copy_f = os.path.join("global_graph_data", "graph_global_"+str(data_id).zfill(data_id_length)+".json")
    local_copy_f = os.path.join("local_graph_data", "graph_local_" + str(data_id).zfill(data_id_length) + ".json")
    voxel_copy_f = os.path.join("voxel_data", "voxel_" + str(data_id).zfill(data_id_length) + ".json")


    index = data_id
    global_paste_f = os.path.join(global_paste_dir, "graph_global_"+str(index).zfill(new_data_id_length)+".json")
    local_paste_f = os.path.join(local_paste_dir, "graph_local_"+str(index).zfill(new_data_id_length)+".json")
    voxel_paste_f = os.path.join(voxel_paste_dir, "voxel_" + str(index).zfill(new_data_id_length) + ".json")

    os.remove(global_copy_f)
    os.remove(local_copy_f)
    os.remove(voxel_copy_f)








