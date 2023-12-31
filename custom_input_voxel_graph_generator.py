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

# Save the argument values in a dictionary
input_values = {}

input_values["number_of_floors"] = int(argv[0])
input_values["groud_floor_height"] = int(argv[1]) 
input_values["floor_height"] = int(argv[2]) 
input_values["x_intervals"] = [int(x) for x in argv[3].split(",")] 
input_values["y_intervals"] = [int(x) for x in argv[4].split(",")]
input_values["filename"] = argv[5]

def add_cube(location, dimension, color, index, voxel_floor):
    # add a cube into the scene
    bpy.ops.mesh.primitive_cube_add(size=1, location=location, scale=dimension)
    #bpy.ops.mesh.primitive_cube_add(size=1, location=location)
    # get a reference to the currently active object
    current_cube = bpy.context.active_object
    
    # Name the voxel
    current_cube.name = "voxel_" + str(index)
    # Give it a color 
    current_cube.data.materials.append(color)
    
    # Remove object from all collections not used in a scene
    bpy.ops.collection.objects_remove_all()
    
    bpy.data.collections['Floor_'+str(voxel_floor)].objects.link(current_cube)

def create_floor_collections(number_of_floors):
    
    for floor in range(number_of_floors):
        # New Collection
        my_coll = bpy.data.collections.new("Floor_"+str(floor))

        # Add collection to scene collection
        bpy.context.scene.collection.children.link(my_coll)
    
def create_voxel_building():
    """
    Prepare data for visualization and add cubes to the scene
    """
    
    # Initialize the header of the JSON file
    output_json = {
        "voxel_node": []
    }

    number_of_floors = input_values["number_of_floors"] 
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
    
    # Position of the voxels
    pos_x, pos_y, pos_z = 0, 0, 0

    # Indices of the voxel for the JSON file
    x, y, z = 0, 0, 0

    i = 0
    

    # Iterate over the values and create the voxel graph 
    for floor in range(number_of_floors):
        if floor == 0:
            dim_z = input_values["groud_floor_height"]
        else:
            dim_z = input_values["floor_height"]

        pos_x = 0
        pos_y = 0

        x = 0
        y = 0
        
        for dim_y in input_values["y_intervals"]:
            pos_x = 0
            x = 0
                        
            for dim_x in input_values["x_intervals"]:
                location = (pos_x+dim_x/2, pos_y+dim_y/2, pos_z+dim_z/2)                            
                dimension = (dim_x, dim_y, dim_z)
                
                add_cube(location, dimension, orange_color, i, z)

                # Add voxel node to the JSON dictionary
                output_json["voxel_node"].append({
                                                    "location": [z, y, x], 
                                                    "type": -1, 
                                                    "type_id": 0, 
                                                    "coordinate": [pos_z, pos_y, pos_x], 
                                                    "dimension": [dim_z, dim_y, dim_x], 
                                                    "weight": 0, 
                                                    "neighbors": []} 
                )
                
                pos_x += dim_x 
                
                i += 1
                x += 1
                
            # Go to the next line/row of voxels
            pos_y += dim_y
            y += 1
        
        # Go to the next floor
        pos_z += dim_z
        z += 1

    create_json(output_json)

def create_json(output_json):
    # Serializing json
    json_object = json.dumps(output_json)
     
    # Writing to sample.json
    filename = input_values["filename"]
    with open(filename, "w") as outfile:
        outfile.write(json_object)
            
def delete_all_objects():
    """Removing all of the objects from the scene and remove all collections"""
    # make sure that we are in object mode
    if bpy.context.active_object and bpy.context.active_object.mode == "EDIT":
            bpy.ops.object.mode_set(mode="OBJECT")

    # select all object in the scene
    bpy.ops.object.select_all(action="SELECT")

    # delete all selected objects in the scene
    bpy.ops.object.delete()

def main():    
    # delete all objects in the scene
    delete_all_objects()

    # Add voxels to the scene and color each voxel based on its type
    create_voxel_building()

main()