# Start Blender from terminal using the python script (without arguments)

	blender -P standalone_visualization_test.py

# Start Blender from terminal using the python script with argument (give the path to the voxel graph)

	blender -P standalone_visualization_test.py -- var_output1/voxel_data/voxel_000000.json

# Launch Qt Designer

	designer

# Convert GUI to Python script

	pyuic5 -x Buiding_GAN_Visualizer.ui -o Buiding_GAN_Visualizer.py


# Launch the visualizer

	python Buiding_GAN_Visualizer.py
