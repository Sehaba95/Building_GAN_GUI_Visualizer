# Building_GAN_GUI_Visualizer
Non-official implementation of the visualiser of the Building-GAN model.

In this repository, I have created a GUI using PyQt5 to visualize the output of the model Building-GAN. The input program was created manually. 


# Launch the visualizer

	python Buiding_GAN_Visualizer.py


# TODO 

	1. Create a process script that uses Aubergenville's input graph, and the new generated voxel graph 
	2. Save the output in a specific file (with the same name of the voxel graph)
	3. Load the processed data file in the inference script
	4. Run the inference script using the processed data, and save the results in a specific folder, and give the folder the same name as the voxel graph filename
	5. Print the IDs in the ListView in the UI
