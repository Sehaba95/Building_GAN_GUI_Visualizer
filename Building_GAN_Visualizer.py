# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Building_GAN_Visualizer.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
import subprocess
import glob


class Ui_BuildingGAN(object):

    def __init__(self):
        self.input_values = {
            "number_of_floors": 3,
            "groud_floor_height": 0,
            "floor_height": 0,
            "x_intervals": 0,
            "y_intervals": 0,
            "number_of_buildings": 0,
            "voxel_graph_filename": "",
            "processed_data_filename": ""
        }

        self.output_hospitals = {}
    
    def setupUi(self, BuildingGAN):
        BuildingGAN.setObjectName("BuildingGAN")
        BuildingGAN.resize(1052, 590)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        BuildingGAN.setFont(font)
        BuildingGAN.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(BuildingGAN)
        self.centralwidget.setObjectName("centralwidget")
        self.far = QtWidgets.QLineEdit(self.centralwidget)
        self.far.setEnabled(False)
        self.far.setGeometry(QtCore.QRect(180, 70, 113, 23))
        self.far.setObjectName("far")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 70, 141, 21))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 110, 141, 21))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.tpr = QtWidgets.QLineEdit(self.centralwidget)
        self.tpr.setEnabled(False)
        self.tpr.setGeometry(QtCore.QRect(180, 110, 113, 23))
        self.tpr.setObjectName("tpr")
        self.site_x = QtWidgets.QLineEdit(self.centralwidget)
        self.site_x.setEnabled(False)
        self.site_x.setGeometry(QtCore.QRect(180, 150, 113, 23))
        self.site_x.setObjectName("site_x")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 150, 141, 21))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 190, 141, 21))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.site_y = QtWidgets.QLineEdit(self.centralwidget)
        self.site_y.setEnabled(False)
        self.site_y.setGeometry(QtCore.QRect(180, 190, 113, 23))
        self.site_y.setObjectName("site_y")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 230, 141, 21))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.num_floors = QtWidgets.QLineEdit(self.centralwidget)
        self.num_floors.setGeometry(QtCore.QRect(180, 230, 113, 23))
        self.num_floors.setObjectName("num_floors")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 310, 141, 21))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gf_height = QtWidgets.QLineEdit(self.centralwidget)
        self.gf_height.setGeometry(QtCore.QRect(180, 270, 113, 23))
        self.gf_height.setObjectName("gf_height")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(30, 350, 141, 21))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.floor_height = QtWidgets.QLineEdit(self.centralwidget)
        self.floor_height.setGeometry(QtCore.QRect(180, 310, 113, 23))
        self.floor_height.setObjectName("floor_height")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(30, 270, 141, 21))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(30, 390, 141, 21))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.x_intervals = QtWidgets.QLineEdit(self.centralwidget)
        self.x_intervals.setGeometry(QtCore.QRect(180, 350, 113, 23))
        self.x_intervals.setObjectName("x_intervals")
        self.y_intervals = QtWidgets.QLineEdit(self.centralwidget)
        self.y_intervals.setGeometry(QtCore.QRect(180, 390, 113, 23))
        self.y_intervals.setObjectName("y_intervals")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(10, 430, 161, 21))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.variation_num = QtWidgets.QLineEdit(self.centralwidget)
        self.variation_num.setGeometry(QtCore.QRect(180, 430, 113, 23))
        self.variation_num.setObjectName("variation_num")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 1031, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_12 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setAcceptDrops(False)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_2.addWidget(self.label_12)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label_13 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_2.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(340, 80, 407, 362))
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("../../Downloads/Aubergenville_Program_Graph (1).png"))
        self.label_14.setScaledContents(True)
        self.label_14.setObjectName("label_14")
        self.visualize_btn = QtWidgets.QPushButton(self.centralwidget)
        self.visualize_btn.setGeometry(QtCore.QRect(780, 500, 261, 23))
        self.visualize_btn.setObjectName("visualize_btn")
        self.output_list = QtWidgets.QListWidget(self.centralwidget)
        self.output_list.setGeometry(QtCore.QRect(780, 71, 261, 411))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.output_list.setFont(font)
        self.output_list.setAutoFillBackground(False)
        self.output_list.setStyleSheet("""QListWidget::item {
                                                border-bottom: 1px solid #000000; 
                                                padding-top:3px;
                                                padding-bottom:3px;
                                        }
                                        QListWidget::item:selected {
                                                background: #0336FF;
                                        }
                                        QListWidget QWidget[widgetItem=true] {
                                                background: transparent;
                                        }
                                        """)
        self.output_list.setTabKeyNavigation(False)
        self.output_list.setDragEnabled(False)
        self.output_list.setAlternatingRowColors(True)
        self.output_list.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.output_list.setObjectName("output_list")
        item = QtWidgets.QListWidgetItem()
        self.output_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.output_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.output_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.output_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.output_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.output_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.output_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.output_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.output_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.output_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.output_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.output_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.output_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.output_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.output_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.output_list.addItem(item)
        self.generate_btn = QtWidgets.QPushButton(self.centralwidget)
        self.generate_btn.setGeometry(QtCore.QRect(30, 500, 261, 32))
        self.generate_btn.setObjectName("generate_btn")
        self.is_visualise_voxel_graph = QtWidgets.QCheckBox(self.centralwidget)
        self.is_visualise_voxel_graph.setGeometry(QtCore.QRect(30, 470, 261, 20))
        self.is_visualise_voxel_graph.setObjectName("is_visualise_voxel_graph")
        BuildingGAN.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(BuildingGAN)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1052, 20))
        self.menubar.setObjectName("menubar")
        BuildingGAN.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(BuildingGAN)
        self.statusbar.setObjectName("statusbar")
        BuildingGAN.setStatusBar(self.statusbar)

        self.retranslateUi(BuildingGAN)
        QtCore.QMetaObject.connectSlotsByName(BuildingGAN)

        # Add button event
        self.generate_btn.clicked.connect(self.generate_btn_clicked)
        self.visualize_btn.clicked.connect(self.visualize_btn_clicked)

        #self.generate_btn.setEnabled(False)
        self.visualize_btn.setEnabled(False)


    def retranslateUi(self, BuildingGAN):
        _translate = QtCore.QCoreApplication.translate
        BuildingGAN.setWindowTitle(_translate("BuildingGAN", "MainWindow"))
        self.far.setText(_translate("BuildingGAN", "1.7494"))
        self.label.setText(_translate("BuildingGAN", "FAR (COS)"))
        self.label_3.setText(_translate("BuildingGAN", "TPR"))
        self.tpr.setText(_translate("BuildingGAN", "13,15,0,0,24,45"))
        self.site_x.setText(_translate("BuildingGAN", "50"))
        self.label_4.setText(_translate("BuildingGAN", "Site X"))
        self.label_5.setText(_translate("BuildingGAN", "Site Y"))
        self.site_y.setText(_translate("BuildingGAN", "50"))
        self.label_6.setText(_translate("BuildingGAN", "Floors"))
        self.num_floors.setText(_translate("BuildingGAN", "4"))
        self.label_7.setText(_translate("BuildingGAN", "Floor Height"))
        self.gf_height.setText(_translate("BuildingGAN", "7"))
        self.label_8.setText(_translate("BuildingGAN", "X Intervals"))
        self.floor_height.setText(_translate("BuildingGAN", "4"))
        self.label_9.setText(_translate("BuildingGAN", "Ground Floor Height"))
        self.label_10.setText(_translate("BuildingGAN", "Y Intervals"))
        self.x_intervals.setText(_translate("BuildingGAN", "3,3,7,4,7,5"))
        self.y_intervals.setText(_translate("BuildingGAN", "4,4,7,4,7,7"))
        self.label_11.setText(_translate("BuildingGAN", "# of hospitals to generate"))
        self.variation_num.setText(_translate("BuildingGAN", "10"))
        self.label_12.setText(_translate("BuildingGAN", "Building-GAN Voxel Graph"))
        self.label_2.setText(_translate("BuildingGAN", "Building-GAN Program Graph "))
        self.label_13.setText(_translate("BuildingGAN", "            Building-GAN Outputs"))
        self.visualize_btn.setText(_translate("BuildingGAN", "Visualize"))
        __sortingEnabled = self.output_list.isSortingEnabled()
        self.output_list.setSortingEnabled(False)
        self.output_list.setSortingEnabled(__sortingEnabled)
        self.generate_btn.setText(_translate("BuildingGAN", "Generate"))
        self.is_visualise_voxel_graph.setText(_translate("BuildingGAN", "   Visualise Voxel Graph"))

    # Check all the input values
    def input_checker(self):
        # Give the current files the following id 
        inference_id = datetime.now().strftime("%Y_%m_%d_%H_%M_%S_%f")

        # Set the default color of all inputs to black
        self.num_floors.setStyleSheet("border: 1px solid gray;")
        self.gf_height.setStyleSheet("border: 1px solid gray;")
        self.floor_height.setStyleSheet("border: 1px solid gray;")
        self.x_intervals.setStyleSheet("border: 1px solid gray;")
        self.y_intervals.setStyleSheet("border: 1px solid gray;")
        self.variation_num.setStyleSheet("border: 1px solid gray;")

        valid_inputs = True

        # Check the input values 
        # Get all the input values
        try:
            self.input_values["number_of_floors"] = int(self.num_floors.text())
        except:
            self.num_floors.setStyleSheet("border: 1px solid red;")
            valid_inputs = False
            self.generate_btn.setEnabled(True)

        try:
            self.input_values["groud_floor_height"] = int(self.gf_height.text())
        except:
            self.gf_height.setStyleSheet("border: 1px solid red;")
            valid_inputs = False
            self.generate_btn.setEnabled(True)

        try:
            self.input_values["floor_height"] = int(self.floor_height.text())
        except:
            self.floor_height.setStyleSheet("border: 1px solid red;")
            valid_inputs = False
            self.generate_btn.setEnabled(True)

        try:
            self.input_values["x_intervals"] = self.x_intervals.text()
            _ = [int(x) for x in self.x_intervals.text().split(",")]
        except:
            self.x_intervals.setStyleSheet("border: 1px solid red;")
            valid_inputs = False
            self.generate_btn.setEnabled(True)

        try:
            self.input_values["y_intervals"] = self.y_intervals.text()
            _ = [int(x) for x in self.y_intervals.text().split(",")]
        except:
            self.y_intervals.setStyleSheet("border: 1px solid red;")
            valid_inputs = False
            self.generate_btn.setEnabled(True)

        try:
            self.input_values["number_of_buildings"] = int(self.variation_num.text())
        except:
            self.variation_num.setStyleSheet("border: 1px solid red;")
            valid_inputs = False
            self.generate_btn.setEnabled(True)
        
        # Create the voxel graph filename 
        self.input_values["voxel_graph_filename"] = "Data/6types-raw_data/voxel_data/voxel_000000.json"
        # CHANGE
        #self.input_values["voxel_graph_filename"] = "Data/6types-raw_data/voxel_data/voxel_000002.json" # voxel_000002.json - voxel_000004.json

        # Create the processed data filename
        self.input_values["processed_data_filename"] = "Data/6types-processed_data/data_{}.pt".format(inference_id)

        return valid_inputs

    def clear_list_view(self):
        # TODO: Update the List in the GUI with results
        self.output_list.clear()

    # Add an event to Generate button
    def generate_btn_clicked(self):
        # Clear the ListView 
        self.clear_list_view()
        self.generate_btn.setEnabled(False)
        self.visualize_btn.setEnabled(False)

        # Check all the input values and raise error
        valid_inputs = self.input_checker()

        # If all the input value are in a correct format
        if valid_inputs:
            # Check if the user want to visualize the input voxel graph
            if self.is_visualise_voxel_graph.isChecked():        
                subprocess.run(["blender", "-P", "custom_input_voxel_graph_generator.py", "--",
                                str(self.input_values["number_of_floors"]), 
                                str(self.input_values["groud_floor_height"]), 
                                str(self.input_values["floor_height"]), 
                                str(self.input_values["x_intervals"]), 
                                str(self.input_values["y_intervals"]), 
                                self.input_values["voxel_graph_filename"] 
                                ]) 

            else:
                subprocess.run(["blender", "--background", "-P", "custom_input_voxel_graph_generator.py", "--",
                                str(self.input_values["number_of_floors"]), 
                                str(self.input_values["groud_floor_height"]), 
                                str(self.input_values["floor_height"]), 
                                str(self.input_values["x_intervals"]), 
                                str(self.input_values["y_intervals"]), 
                                self.input_values["voxel_graph_filename"] 
                                ]) 

            # Create the object of Building-GAN model using our voxel graph 
            subprocess.run(["python", "Data/process_data.py", 
                            self.input_values["voxel_graph_filename"], # The filename of the generated voxel graph 
                            self.input_values["processed_data_filename"] # The output filename
                            ])
            
            # Run inference
            subprocess.run(["python", "run_inference.py", 
                            "--input_object", self.input_values["processed_data_filename"], # The filename of the processed data 
                            "--variation_num", str(self.input_values["number_of_buildings"]) # Number of buildings to generate
                            ])

            # Get the path of the generated voxel graphs
            inference_output_folder = "output" + self.input_values["processed_data_filename"].split("/")[-1].split(".")[0].replace("data","")
            inference_output_path = "Data/outputs/" + inference_output_folder + "/voxel_data/"

            json_filename_list = sorted(glob.glob(inference_output_path+"*.json"))

            self.output_hospitals = {}
            counter = 1

            for json_filename in json_filename_list:
                self.output_hospitals["Hospital {}".format(counter)] = json_filename
                self.output_list.addItem("Hospital {}".format(counter))
                #self.output_list.addItem(json_filename.split("/")[-1])

                counter += 1

            self.visualize_btn.setEnabled(True)
            self.generate_btn.setEnabled(True)

    # Add an event to Visualize button
    def visualize_btn_clicked(self):
    
        # Get the path to the output folder
        #inference_output_folder = "output" + self.input_values["processed_data_filename"].split("/")[-1].split(".")[0].replace("data","")
        #inference_output_path = "Data/outputs/" + inference_output_folder + "/voxel_data/"

        # Get the filename of the selected value and the path
        selected_item = self.output_list.currentItem().text()

        #filename = inference_output_path + selected_item.text()

        filename = self.output_hospitals[selected_item]

        # Run Blender using the filename as argument
        subprocess.run(["blender", "-P", "standalone_output_visualization.py", "--", filename]) 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BuildingGAN = QtWidgets.QMainWindow()
    ui = Ui_BuildingGAN()
    ui.setupUi(BuildingGAN)
    BuildingGAN.show()
    sys.exit(app.exec_())
