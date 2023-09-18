# extend Python's functionality to work with JSON files
import json
# extend Python's functionality to work with file paths
import pathlib
# extend Python's functionality to print data in a readable way
import pprint
# give Python access to Blender's functionality
import bpy
# give Python access to Blender's mesh editing functionality
import bmesh
import numpy as np

import sys
argv = sys.argv
argv = argv[argv.index("--") + 1:]  # get all args after "--"

print(argv)  # --> ['example', 'args', '123']


def arg_max(list):
    index = -1
    for i in range(len(list)):
        if list[i] > 0:
            return i
    return index

def one_hot_vector(_id):
    number_of_class = 6
    assert _id < number_of_class
    return [1 if i == _id else 0 for i in range(number_of_class)]

def process_voxel_graph(voxel_graph):
    dimension_norm_factor = 100
    # Extract Node Feature
    unicode_to_node_id_map, node_id_to_program_unicode, projection_map = {}, {}, {}
    voxel_floor_index, voxel_feature, voxel_bool, voxel_label = [], [], [], []
    for i, n in enumerate(voxel_graph["voxel_node"]):
        voxel_bool.append(0 if n["type"] < 0 else 1)
        voxel_label.append(one_hot_vector(n["type"]))
        voxel_feature.append([*[x / dimension_norm_factor for x in n["dimension"] + n["coordinate"]], n["weight"]])
        unicode_to_node_id_map[tuple(n["location"])] = i
        node_id_to_program_unicode[i] = (n["type"], n["type_id"])
        voxel_floor_index.append(n["location"][0])

        horizontal_location = (n["location"][2], n["location"][1])  # x, y
        if projection_map.get(horizontal_location, None):
            projection_map.get(horizontal_location).append(i)
        else:
            projection_map[horizontal_location] = [i]

    voxel_projection_cluster = [-1] * len(voxel_graph["voxel_node"])
    for i, v in enumerate(projection_map.values()):
        for n_i in v:
            voxel_projection_cluster[n_i] = i
    assert(-1 not in voxel_projection_cluster)

    # Extract Edge Feature <- Already bi-directional
    voxel_edge_src, voxel_edge_dst = [], []
    for i, n_i in enumerate(voxel_graph["voxel_node"]):
        for unicode_j in n_i["neighbors"]:
            voxel_edge_src.append(i)
            voxel_edge_dst.append(unicode_to_node_id_map[tuple(unicode_j)])
    voxel_edge = [voxel_edge_src, voxel_edge_dst]

    return {"voxel_floor_index": voxel_floor_index,     # dict (F --> nodes in each floor)
            "voxel_projection_cluster": voxel_projection_cluster,  # N x 1
            "voxel_feature": voxel_feature,                 # N x 7
            "voxel_bool": voxel_bool,                       # N x 1
            "voxel_label": voxel_label,                     # N x C
            "voxel_edge": voxel_edge,                       # 2 x E
            "node_id_to_program_unicode": node_id_to_program_unicode  # voxel node id -> type, type id
            }

def add_cube(location, dimension, color_material, index, voxel_floor):
    # add a cube into the scene
    bpy.ops.mesh.primitive_cube_add(size=1, location=location, scale=dimension)
    #bpy.ops.mesh.primitive_cube_add(size=1, location=location)
    # get a reference to the currently active object
    current_cube = bpy.context.active_object
    
    # Name the voxel
    current_cube.name = "voxel_" + str(index)
    # Give it a color 
    current_cube.data.materials.append(color_material)
    
    # Remove object from all collections not used in a scene
    bpy.ops.collection.objects_remove_all()
    
    bpy.data.collections['Floor_'+str(voxel_floor)].objects.link(current_cube)

def create_floor_collections(number_of_floors):
    
    for floor in range(number_of_floors):
        # New Collection
        my_coll = bpy.data.collections.new("Floor_"+str(floor))

        # Add collection to scene collection
        bpy.context.scene.collection.children.link(my_coll)
    

def create_voxel_building(input_prgoram_graph):
    """
    Prepare data for visualization and add cubes to the scene
    """
    
    number_of_floors = max(input_prgoram_graph["voxel_floor_index"]) + 1 
    create_floor_collections(number_of_floors)
    
    # Alpha: opacity of the color
    alpha = 0.005

    # Prepare color materials for visualization
    brown_color = bpy.data.materials.new("Brown")
    brown_color.diffuse_color = (139,69,19, alpha) # saddle brown

    pink_color = bpy.data.materials.new("Pink") 
    pink_color.diffuse_color = (255,20,147, alpha) # deep pink
    
    yellow_color = bpy.data.materials.new("Yellow")
    yellow_color.diffuse_color = (255,255,0, alpha) # yellow
    
    green_color = bpy.data.materials.new("Green")
    green_color.diffuse_color = (0,128,0, alpha) # green
    
    blue_color = bpy.data.materials.new("Blue") 
    blue_color.diffuse_color = (0,0,205, alpha) # medium blue
    
    orange_color = bpy.data.materials.new("Orange") 
    orange_color.diffuse_color = (255,140,0, alpha) # dark orange

    black_color = bpy.data.materials.new("Orange") 
    black_color.diffuse_color = (0,0,0, alpha) # dark orange

    # Initialize the list of colors: one color for each type of voxels
    colors_materials = [ 
        brown_color, #"brown", 
        pink_color, #"pink", 
        yellow_color, #"yellow", 
        green_color,#"green", 
        blue_color, #"blue", 
        orange_color, #"orange"
        black_color
        ]

    for i in range(len(input_prgoram_graph["voxel_floor_index"])):
        # Get the floor of the current voxel
        voxel_floor = input_prgoram_graph["voxel_floor_index"][i]

        # Get dimension - coordinate - weight of each voxel
        z_dim, y_dim, x_dim, z_pos, y_pos, x_pos, weight = input_prgoram_graph["voxel_feature"][i]
        # Multiply the dimension and position by 100 to get the real values
        z_dim, y_dim, x_dim, z_pos, y_pos, x_pos = int(100 *z_dim), int(100 *y_dim), int(100 *x_dim), int(100 *z_pos), int(100 *y_pos), int(100 * x_pos)

        location = (x_pos+x_dim/2, y_pos+y_dim/2, z_pos+z_dim/2)
        dimension = (x_dim, y_dim, z_dim)
        
        # Voxel label
        voxel_label = arg_max(input_prgoram_graph["voxel_label"][i])
        
        # Color of the voxel
        colors_material = colors_materials[voxel_label]
        
        if voxel_label != -1: 
            # Add the voxel to the scene using location, dimension and give the color based on the type of node   
            add_cube(location, dimension, colors_material, i, voxel_floor)

# From YouTube tutorial    
def delete_all_objects():
    """Removing all of the objects from the scene and remove all collections"""
    # make sure that we are in object mode
    if bpy.context.active_object and bpy.context.active_object.mode == "EDIT":
            bpy.ops.object.mode_set(mode="OBJECT")

    # select all object in the scene
    bpy.ops.object.select_all(action="SELECT")

    # delete all selected objects in the scene
    bpy.ops.object.delete()
    
    #for collection in bpy.context.scene.collection.children:
    #    bpy.context.scene.collection.children.unlink(collection)

# Not used anymore
def get_path_to_mesh_data():
    # return pathlib.Path.home() / "Downloads" / "Building-GAN-Output-Visualisation" / "Data_Building_GAN" / "voxel_graph" / "voxel_000003.json"
    # Aubergenville generation using Building-GAN 
    return pathlib.Path.home() / "Downloads" / "Building_GAN_GUI_Visualizer" / "Data" / "voxel_data" / "sample_2023_09_01_19_33_40.984822.json"
    
    # Aubergenville generation using Building-GAN 
    #return pathlib.Path.home() / "Downloads" / "Building-GAN" / "inference" / "iccv2021" / "Aubergenville_with_two_diff_voxel_graphs" / "output" / "voxel_data" / "voxel_000004.json"

def load_data():
    # Static input filename 
    #path_to_file = get_path_to_mesh_data()

    # Get the filename from terminal 
    
    path_to_file = argv[0]

    # @todo: it is best to test that the file exists on disk before doing this
    # open the json file for reading and read the text from it
    with open(path_to_file, "r") as in_file_obj:
        text = in_file_obj.read()
        # convert the text into a dictionary
        data = json.loads(text)

    return data

def main():
    # delete all objects in the scene
    delete_all_objects()

    # Load the JSON file
    voxel_graph = load_data()

    # Process the raw input voxel JSON
    voxel_graph = process_voxel_graph(voxel_graph)

    # Add voxels to the scene and color each voxel based on its type
    create_voxel_building(voxel_graph)

main()