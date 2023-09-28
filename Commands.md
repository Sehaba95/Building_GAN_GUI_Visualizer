# To run the project, you need to first activate the virtual environment and run the following script

	conda activate "building_gan"
	python Building_GAN_Visualizer.py

# Add the project to the python system path 

	import sys
	sys.path.insert(0,'/home/maparia/Documents/Building-GAN')

# Start Blender from terminal using the python script (without arguments)

	blender -P standalone_visualization_test.py

# Start Blender from terminal using the python script with argument (give the path to the voxel graph)

	blender -P standalone_visualization_test.py -- var_output1/voxel_data/voxel_000000.json

# Launch Qt Designer

	designer

# Convert GUI to Python script

	pyuic5 -x Building_GAN_Visualizer.ui -o Building_GAN_Visualizer_NEW.py


# Launch the visualizer

	python3 Building_GAN_Visualizer.py


# Launch one inference

	python run_inference.py --input_object Data/6types-processed_data/data_2023_09_12_15_03_42_831573.pt --variation_num 5
