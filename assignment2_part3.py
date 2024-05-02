
import os, sys, math, pdb

## PyQt5 libraries
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from PyQt5.QtOpenGL import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

## OpenGL libraries (pip install pyOpenGL)
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GL import *
import OpenGL.GL as gl
from PyQt5.QtWidgets import QWidget

## numpy libraries
import numpy as np
from numpy import linalg

## scipy libraries
# from scipy import linalg

## imageio libraries (pip install imageio)
import imageio
from imageio.v2 import imsave
from imageio.v2 import imread

## Import the class "Ui_MainWindow" from the file "GUI.py"
from GUI_perfect import Ui_MainWindow
from parameter_pca import Ui_Ui_Form

## Import the class "OBJ" and "OBJFastV" from the file "OBJ.py"
from OBJ import OBJ, OBJFastV

from functools import partial


import glob


############################################################
# Texture Parameter Window
################################################################

class Parameter_Window(QWidget):
    def __init__(self, parent):
        super(Parameter_Window, self).__init__()
        
        self.parent = parent
        
        QWidget.__init__(self)
        Ui_Ui_Form.__init__(self)
        
        self.p_ui = Ui_Ui_Form()
        self.p_ui.setupUi(self)
        

        self.p_ui.tComp0.valueChanged.connect(self.get_t_values)
        self.p_ui.tComp1.valueChanged.connect(self.get_t_values)
        self.p_ui.tComp2.valueChanged.connect(self.get_t_values)
        self.p_ui.tComp3.valueChanged.connect(self.get_t_values)
        self.p_ui.tComp4.valueChanged.connect(self.get_t_values)
        self.p_ui.tComp5.valueChanged.connect(self.get_t_values)
        self.p_ui.tComp6.valueChanged.connect(self.get_t_values)
        self.p_ui.tComp7.valueChanged.connect(self.get_t_values)
        self.p_ui.tComp8.valueChanged.connect(self.get_t_values)
        self.p_ui.tComp9.valueChanged.connect(self.get_t_values)
        self.p_ui.tComp10.valueChanged.connect(self.get_t_values)
        
        
        self.p_ui.gComp0.valueChanged.connect(self.get_g_values)
        self.p_ui.gComp1.valueChanged.connect(self.get_g_values)
        self.p_ui.gComp2.valueChanged.connect(self.get_g_values)
        self.p_ui.gComp3.valueChanged.connect(self.get_g_values)
        self.p_ui.gComp4.valueChanged.connect(self.get_g_values)
        self.p_ui.gComp5.valueChanged.connect(self.get_g_values)
        self.p_ui.gComp6.valueChanged.connect(self.get_g_values)
        self.p_ui.gComp7.valueChanged.connect(self.get_g_values)
        self.p_ui.gComp8.valueChanged.connect(self.get_g_values)
        self.p_ui.gComp9.valueChanged.connect(self.get_g_values)
        self.p_ui.gComp10.valueChanged.connect(self.get_g_values)
        self.p_ui.gComp11.valueChanged.connect(self.get_g_values)
        self.p_ui.gComp12.valueChanged.connect(self.get_g_values)
        self.p_ui.gComp13.valueChanged.connect(self.get_g_values)
        self.p_ui.gComp14.valueChanged.connect(self.get_g_values)
        self.p_ui.gComp15.valueChanged.connect(self.get_g_values)
        self.p_ui.gComp16.valueChanged.connect(self.get_g_values)
        self.p_ui.gComp17.valueChanged.connect(self.get_g_values)
        self.p_ui.gComp18.valueChanged.connect(self.get_g_values)
        self.p_ui.gComp19.valueChanged.connect(self.get_g_values)
        self.p_ui.gComp20.valueChanged.connect(self.get_g_values)
        self.p_ui.gComp21.valueChanged.connect(self.get_g_values)
        #self.p_ui.gComp22.valueChanged.connect(self.get_g_values)
        
        self.show()
        
    def get_t_values(self):
        self.tblocksignals(True)
        z = [
            self.p_ui.tComp0.value(),
            self.p_ui.tComp1.value(),
            self.p_ui.tComp2.value(),
            self.p_ui.tComp3.value(),
            self.p_ui.tComp4.value(),
            self.p_ui.tComp5.value(),
            self.p_ui.tComp6.value(),
            self.p_ui.tComp7.value(),
            self.p_ui.tComp8.value(),
            self.p_ui.tComp9.value(),
            
        ]
        
        self.parent.T_SliderValueChange(z)
        
        
        self.p_ui.tComp0.setValue(z[0])
        self.p_ui.tComp1.setValue(z[1])
        self.p_ui.tComp2.setValue(z[2])
        self.p_ui.tComp3.setValue(z[3])
        self.p_ui.tComp4.setValue(z[4])
        self.p_ui.tComp5.setValue(z[5])
        self.p_ui.tComp6.setValue(z[6])
        self.p_ui.tComp7.setValue(z[7])
        self.p_ui.tComp8.setValue(z[8])
        self.p_ui.tComp9.setValue(z[9])
        
        self.tblocksignals(False)
        
        
    def get_g_values(self):
        
        self.gblocksignals(True)
        z = [
            self.p_ui.gComp0.value(),
            self.p_ui.gComp1.value(),
            self.p_ui.gComp2.value(),
            self.p_ui.gComp3.value(),
            self.p_ui.gComp4.value(),
            self.p_ui.gComp5.value(),
            self.p_ui.gComp6.value(),
            self.p_ui.gComp7.value(),
            self.p_ui.gComp8.value(),
            self.p_ui.gComp9.value(),
            self.p_ui.gComp10.value(),
            self.p_ui.gComp11.value(),
            self.p_ui.gComp12.value(),
            self.p_ui.gComp13.value(),
            self.p_ui.gComp14.value(),
            self.p_ui.gComp15.value(),
            self.p_ui.gComp16.value(),
            self.p_ui.gComp17.value(),
            self.p_ui.gComp18.value(),
            self.p_ui.gComp19.value(),
            self.p_ui.gComp20.value(),
            self.p_ui.gComp21.value(),
        
        ]
        
        self.parent.G_SliderValueChange(z)
        
        self.p_ui.gComp0.setValue(z[0])
        self.p_ui.gComp1.setValue(z[1])
        self.p_ui.gComp2.setValue(z[2])
        self.p_ui.gComp3.setValue(z[3])
        self.p_ui.gComp4.setValue(z[4])
        self.p_ui.gComp5.setValue(z[5])
        self.p_ui.gComp6.setValue(z[6])
        self.p_ui.gComp7.setValue(z[7])
        self.p_ui.gComp8.setValue(z[8])
        self.p_ui.gComp9.setValue(z[9])
        self.p_ui.gComp10.setValue(z[10])
        self.p_ui.gComp11.setValue(z[11])
        self.p_ui.gComp12.setValue(z[12])
        self.p_ui.gComp13.setValue(z[13])
        self.p_ui.gComp14.setValue(z[14])
        self.p_ui.gComp15.setValue(z[15])
        self.p_ui.gComp16.setValue(z[16])
        self.p_ui.gComp17.setValue(z[17])
        self.p_ui.gComp18.setValue(z[18])
        self.p_ui.gComp19.setValue(z[19])
        self.p_ui.gComp20.setValue(z[20])
        self.p_ui.gComp21.setValue(z[21])
        
        self.gblocksignals(False)
        
        
    def tblocksignals(self,cond):
       
        self.p_ui.tComp0.blockSignals(cond)
        self.p_ui.tComp1.blockSignals(cond)
        self.p_ui.tComp2.blockSignals(cond)
        self.p_ui.tComp3.blockSignals(cond)
        self.p_ui.tComp4.blockSignals(cond)
        self.p_ui.tComp5.blockSignals(cond)
        self.p_ui.tComp6.blockSignals(cond)
        self.p_ui.tComp7.blockSignals(cond)
        self.p_ui.tComp8.blockSignals(cond)
        self.p_ui.tComp9.blockSignals(cond)
        
    def gblocksignals(self,cond):
        
        self.p_ui.gComp0.blockSignals(cond)
        self.p_ui.gComp1.blockSignals(cond)
        self.p_ui.gComp2.blockSignals(cond)
        self.p_ui.gComp3.blockSignals(cond)
        self.p_ui.gComp4.blockSignals(cond)
        self.p_ui.gComp5.blockSignals(cond)
        self.p_ui.gComp6.blockSignals(cond)
        self.p_ui.gComp7.blockSignals(cond)
        self.p_ui.gComp8.blockSignals(cond)
        self.p_ui.gComp9.blockSignals(cond)
        self.p_ui.gComp10.blockSignals(cond)
        self.p_ui.gComp11.blockSignals(cond)
        self.p_ui.gComp12.blockSignals(cond)
        self.p_ui.gComp13.blockSignals(cond)
        self.p_ui.gComp14.blockSignals(cond)
        self.p_ui.gComp15.blockSignals(cond)
        self.p_ui.gComp16.blockSignals(cond)
        self.p_ui.gComp17.blockSignals(cond)
        self.p_ui.gComp18.blockSignals(cond)
        self.p_ui.gComp19.blockSignals(cond)
        self.p_ui.gComp20.blockSignals(cond)
        self.p_ui.gComp21.blockSignals(cond)
        
        
   
        
        # Sliders
        # Connect the slider to the function T_SliderValueChange
        #self.ui.Tslider.valueChanged.connect(self.T_SliderValueChange)
        # Connect the slider to the function G_SliderValueChange
        #self.ui.Gslider.valueChanged.connect(self.G_SliderValueChange)

        # Disable buttons/sliders before PCA
        #self.ui.Tslider.setEnabled(False)
        #self.ui.Gslider.setEnabled(False)
        
        
        
        
    
        
        

####################################################################################################
# The Main Window (GUI) --- TASKS TO DO HERE
####################################################################################################
class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)  # The 2 lines here are always presented like this
        QMainWindow.__init__(self, parent)  # Just to initialize the window

        # All the elements from our GUI are added in "ui"
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Default param
        self.InputModelLoaded = False
        self.InputTextureLoaded = False
        self.InputListCreated = False
        self.InputTexturePath = []
        self.InputModel = []
        self.InputTextureDim = 256

        self.TargetModelLoaded = False
        self.TargetTextureLoaded = False
        self.TargetListCreated = False
        self.TarTexturePath = []
        self.TarModel = []

        self.bg_color = 0.0
        self.Root = {}
        self.Tval =  np.zeros([10,1,1,1])
        self.Gval = np.zeros([22,1,1])
        self.P_Tval = self.P_Gval = 0
        self.Tx = self.Ty = 0
        self.Tz = 1
        self.r_mode = self.c_mode = "Faces"
        self.bg_color = 0.0
        self.LeftXRot = self.LeftYRot = 0
        self.b_Ready = False
        self.Updated = False
        self.b_ProcessDone = self.b_Process2Done = self.b_Ready = self.PCA_done = False
        self.old_Gval = self.old_Tval = 0

        # Add a GLWidget (will be used to display our 3D object)
        self.glWidget = GLWidget(parent=self)
        # Add the widget in "frame_horizontalLayout", an element from the GUI
        self.ui.frame_horizontalLayout.addWidget(self.glWidget)

        # Update Widgets
        # Connect a signal "updated" between the GLWidget and the GUI, just to have a link between the 2 classes
        self.glWidget.updated.connect(self.updateFrame)

        # RadioButton (Rendering Mode)
        # Connect the radiobutton to the function on_rendering_button_toggled
        self.ui.rbFaces.toggled.connect(self.rendering_button_toggled)
        # It will be used to switch between 2 modes, full/solid model or cloud of points
        self.ui.rbPoints.toggled.connect(self.rendering_button_toggled)

        # RadioButton (Background Color)
        # Connect the radiobutton to the function on_bgcolor_button_toggled
        self.ui.rbWhite.toggled.connect(self.bgcolor_button_toggled)
        # Just an example to change the background of the 3D frame
        self.ui.rbBlack.toggled.connect(self.bgcolor_button_toggled)

        # Buttons
        # Connect the button to the function LoadFileClicked (will read the 3D file)
        self.ui.LoadFile.clicked.connect(self.LoadFileClicked)
        # Connect the button to the function ProcessClicked (will process PCA)
        self.ui.Process.clicked.connect(self.ProcessClicked)
        # Connect the button to the function SaveOBJ (will write a 3D file)
        self.ui.exportResult.clicked.connect(self.SaveOBJ)
        
        self.ui.actionOpen_New_Window.triggered.connect(self.ShowParameters)
        self.ui.actionOpen_New_Window.setEnabled(False)


        # Sliders
        # Connect the slider to the function T_SliderValueChange
        #self.ui.Tslider.valueChanged.connect(self.T_SliderValueChange)
        # Connect the slider to the function G_SliderValueChange
        #self.ui.Gslider.valueChanged.connect(self.G_SliderValueChange)

        
        # Progress Bars
        self.ui.prog1.setStyleSheet('color: green;')
        self.ui.prog2.setStyleSheet('color: red;')
        
        self.ui.prog1.setValue(0)
        self.ui.prog2.setValue(0)

    def LoadFileClicked(self):
        try:
            # To display a popup window that will be used to select a file (.obj or .png)
            # The .obj and .png should have the same name!
            self.myFile = QFileDialog.getOpenFileName(None, 'OpenFile', "", "3D object(*.obj);;Texture(*.png)")
            self.myPath = self.myFile[0]
            # If the extension is .obj (or .png), will remove the 4 last characters (== the extension)
            self.GlobalNameWithoutExtension = self.myPath[:-4]
            self.FileNameWithExtension = QFileInfo(self.myFile[0]).fileName()  # Just the filename
            if self.myFile[0] == self.myFile[1] == '':
                # No file selected or cancel button clicked - so do nothing
                pass
            else:
                self.InputModel = self.TarModel = []
                self.InputModelLoaded = self.InputTextureLoaded = self.InputListCreated = False
                self.InputTexturePath = self.GlobalNameWithoutExtension[:-1] + ".png"
               
                
                
                # Will use the class OBJ to read our 3D file and extract everything
                self.InputModel = OBJ(self.GlobalNameWithoutExtension + ".obj")

                imsave("TarTexture" + ".png", imread(self.InputTexturePath))

                self.TarTexturePath = '/'.join(self.myPath.split('/')[:-1]) + '/TarTexture.png'
                self.TarModel = self.InputModel

                # We read the 2 files, so we can now set the boolean value to True
                # (the GLWidget will now display it automatically because of the 2 variables used there)
                self.InputModelLoaded = self.InputTextureLoaded = True
                self.PCA_done = False
                self.glWidget.update()

        except IOError as e:
            print("I/O error({0}): {1}".format(e.errno, e.strerror))
            print(self.myFile)
        except ValueError:
            print("Value Error.")
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise

    def ProcessClicked(self):
        
        self.ui.prog1.setValue(0)
        self.ui.prog2.setValue(0)

        # For the bonus task, you will need to call the thread instead of the PCA function

        self.PCA_Tex()  # Run the function to do the PCA on textures
        
        
    def pca_tex_done(self):
        
        self.b_ProcessDone = True
        print("PCA TEX DONE")

        self.PCA_Geo()  # Run the function to do the PCA on vertices
        
    def pca_geo_done(self):
        
        self.b_Process2Done = True
        print("PCA GEO DONE")

        self.PCA_done = True
        self.ui.actionOpen_New_Window.setEnabled(True)
        
        self.paramWindow = Parameter_Window(parent=self)
        self.paramWindow.get_g_values()
        self.paramWindow.get_t_values()

        

    def PCA_Tex(self):

        ###########################################
        # TASK 1 FOR THE ASSIGNMENT
        ###########################################

        ## Note: You will be evaluated on each task
        ## If it doesn't work, you will be evaluated on your efforts and the quality of the code by trying to do it

        ## Guideline: Read model1.png and model2.png
        ## Do the PCA with the 2 textures, similar to what we did in session 5

        try:
            self.Root['Tex'] = {}
            folder_path = r'Database\Texture'
            file_paths = []
            file_paths = glob.glob(os.path.join(folder_path, '**', '*'), recursive=True)
            
                    
            #samples = [np.float32(imread(i)) for i in ["model1.png", "model2.png"]]
            self.tex_thread = PCAThread(file_paths, 'Tex')
            self.tex_thread.finished_signal.connect(self.handle_tex_result)   
            self.tex_thread.finished_flag.connect(self.pca_tex_done)  
            self.tex_thread.update_p.connect(self.updateBar1)
            self.tex_thread.start()

        except Exception as e:
            print('PCA_Tex Error:', e)
            
        


    def PCA_Geo(self):

        ###########################################
        # TASK 2 FOR THE ASSIGNMENT
        ###########################################

        ## Guideline: Read model1.obj and model2.obj with the "OBJFastV(...)" function to extract quickly the vertices
        ## Do the PCA with the vertices (similar to the function PCA_Tex(), try to do the same but with the vertices)
        ## Or adapt the code a bit


        
        try:
            self.Root['models'] = {}
            folder_path = 'Database\Geometry'
            file_paths = []
            file_paths = glob.glob(os.path.join(folder_path, '**', '*'), recursive=True)
            #file_paths = ["model1.obj", "model2.obj"]
            #samples = [np.float32(OBJFastV(i).vertices) for i in ["model1.obj", "model2.obj"]]
            self.geo_thread = PCAThread(file_paths, 'Geo')
            self.geo_thread.finished_signal.connect(self.handle_geo_result)
            self.geo_thread.finished_flag.connect(self.pca_geo_done)
            self.geo_thread.update_p.connect(self.updateBar2)
            self.geo_thread.start()
        except Exception as e:
            print('PCA_Geo Error:', e)
            
            
    def handle_tex_result(self, result):
        self.Root['Tex']['VrTex'] = result['Vr']
        self.Root['Tex']['XmTex'] = result['Xm']
        self.Root['Tex']['WTex']  = result['W']


    def handle_geo_result(self, result):
        self.Root['models']['VrGeo'] = result['Vr']
        self.Root['models']['XmGeo'] = result['Xm']
        self.Root['models']['WGeo'] =  result['W']


    def updateBar1(self, value):
        self.ui.prog1.setValue(value)


    def updateBar2(self, value):
        self.ui.prog2.setValue(value)

        
        
    def T_SliderValueChange(self, value):
        self.Tval[:,0,0,0] = value
        values = value
        
        

        ###########################################
        # TASK 3 FOR THE ASSIGNMENT
        ###########################################

        ## Texture slider ( PCA : Input Texture <----> Target Texture )
        if self.b_ProcessDone == True and self.b_Process2Done == True:
            ## You have to create the new texture by using the formula of the PCA
            ## As a reminder, Texture = Mean + W1 * E1 + W2 * E2 + ....
            ## Mean is: self.Root['Tex']['XmTex']
            ## W is: Tval  (weight is linked to the slider value "Tval")
            ## E is: self.Root['Tex']['VrTex'][0]
            ## The product Wi * Ei must be done using np.dot(value1, value2)

            try:

                ## >>> ADD CODE BELOW <<<
            
                # self.N_TarTex = ...

                self.N_TarTex = self.Root['Tex']['XmTex'] 
                for i in range(10):
                    if len(values) == 1:
                        break
                        
                    self.N_TarTex += np.dot(self.Root['Tex']['VrTex'][i],values[i] )


                

            except Exception as e:
                print('New target texture Error', e)


            ## Reshape the variable self.N_TarTex to have the real texture size 256*256*4 (RGBA) instead of 1D array
            ## Convert astype np.uint8 to be usable
            try:

                ## >>> ADD CODE BELOW <<<

                # self.TarTexture = ...

                self.TarTexture = self.N_TarTex.astype(np.uint8)
                self.TarTexture = self.TarTexture.reshape(256,256,4)
            except Exception as e:
                print('TarTexture Error:', e)

            # Save the new texture
            try:
                imageio.v2.imsave("TarTexture" + ".png", self.TarTexture)
            except Exception as e:
                print('TarTexture Save error:', e)

        #self.p_ui.sComp0.setValue(value)

    def G_SliderValueChange(self, value):
        self.Gval[:,0,0] = value
        values = value

        ###########################################
        # TASK 4 FOR THE ASSIGNMENT
        ###########################################

        ## Geometry slider ( model1 <----> model2 )
        if self.b_ProcessDone == True and self.b_Process2Done == True:
            ## You have to create the new geometry by using the formula of the PCA
            ## As a reminder, 3DFace = Mean + W1 * E1 + W2 * E2 + ....
            ## Mean is: self.Root['models']['XmGeo']
            ## W is: Gval  (weight is linked to the slider value "Gval")
            ## E is: self.Root['models']['VrGeo']
            ## The product W * E must be done using np.dot(value1, value2)


            try:

                ## >>> ADD CODE BELOW <<<

                # self.N_TarModel = ...
                
                self.N_TarModel = self.Root['models']['XmGeo']
                for i in range(10):
                    if len(values) == 1:
                        break
                        
                    self.N_TarModel += np.dot(values[i],self.Root['models']['VrGeo'][0])

            except Exception as e:
                print('New target model', e)



            ## Reshape the variable self.N_TarModel to have the real geometry format : x y z
            ## For info, the 1D array is like this: x x x x ... y y y y ... z z z z (5904 values 3 times)
            ## The first 5904 values in self.N_TarModel are X, next 5904 are Y, last 5904 are Z
            ## Final format should be : 5904 rows and 3 columns :
            ## x y z
            ## x y z
            ## ....

            arr_3d = np.zeros((5904, 3))
            count = 0
            
            arr_3d = self.N_TarModel

            ## Use for loops to reconstruct completely and save the new vertices in self.TarModel.vertices
            ## Do not forget to concatenate x, y and z together (as a float)

            ## >>> ADD CODE BELOW <<<
            #for i in range(5904):
            #    arr_3d[i,:] = [self.N_TarModel[i, 0],self.N_TarModel[i, ], self.N_TarModel[i+2*5904, :]]


            ## self.TarModel.vertices is the new 3D model
            try:
                # self.TarModel.vertices = ...
                self.TarModel.vertices = arr_3d
                
            except Exception as e:
                print(e)



    def ShowParameters(self):
        self.paramWindow.show()
        
        
    def SaveOBJ(self):
        ###########################################
        # TASK 5 FOR THE ASSIGNMENT
        ###########################################

        ## Try to see how the OBJ class works (file OBJ.py)
        ## Instead of reading, you should now write in a file
        ## You will need to add everything in the .obj, not only vertices!

        ## Open the model1.obj with a text editor for example to see what you have in it
        ## The new file will be similar but with the new vertices (v)
        ## You can reuse the original file to add back vt, vn, f...

        ## >>> ADD CODE BELOW <<<

        # ....
        # Open the output file in write mode

        
        
        with open(self.myPath, 'r') as f_original:
            # Extract non-vertex data (texture coordinates, normal vectors, and faces)
            vt = []
            vn = []
            faces = []
            for line in f_original:
                if line.startswith('vt'):
                    # Extract texture coordinates
                    uv = line.split()[1:]
                    vt.append([float(uv[0]), float(uv[1])])
                elif line.startswith('vn'):
                    # Extract normal vectors
                    norm = line.split()[1:]
                    vn.append([float(norm[0]), float(norm[1]), float(norm[2])])
                elif line.startswith('f'):
                    # Extract faces
                    face_data = line.split()[1:]
                    face = []
                    for vertex_index in face_data:
                        vertex_index = int(vertex_index.split('/')[0])
                        face.append(vertex_index)
                    faces.append(face)

        # Create new OBJ file in write mode
        with open('model1_updated.obj', 'w') as f_updated:
            # Write non-vertex data to the new file
            for vertex in self.TarModel.vertices:
                f_updated.write("v {} {} {}\n".format(vertex[0], vertex[1], vertex[2]))
            for vt_coord in vt:
                f_updated.write('vt {} {}\n'.format(vt_coord[0], vt_coord[1]))
            for vn_vector in vn:
                f_updated.write('vn {} {} {}\n'.format(vn_vector[0], vn_vector[1], vn_vector[2]))

            # Write faces data to the new file (if included)
            for face in faces:
                f_updated.write('f {} {} {}\n'.format(*face))

        

        
        
        imageio.v2.imsave('model1_updated.png', self.TarTexture)
        
        print("Saved File")
        
        # Write faces data
        #for face in self.faces:
        #    f.write("f {} {} {}\n".format(face[0], face[1], face[2]))

        pass

    def checkSign(self, W1, W2):
        ## Check the weights, to know which one is negative/positive
        ## Important for the sliders to have the - on the left and + on the right
        if W1 < 0:
            res = 1
        else:
            res = -1
        return res



    def rendering_button_toggled(self):
        radiobutton = self.sender()

        if radiobutton.isChecked():
            self.r_mode = radiobutton.text()  # Save "Faces" or "Points" in r_mode
        self.Updated = True
        self.glWidget.update()

    def bgcolor_button_toggled(self):
        radiobutton = self.sender()  # Catch the click
        if radiobutton.isChecked():  # Will check which button is checked
            # Will store and use the text of the radiobutton
            # to store a value in the variable "bg_color" that will be used in the GLWidget
            color = radiobutton.text()
            if color == "White":
                self.bg_color = 1.0
            elif color == "Black":
                self.bg_color = 0.0

    def updateFrame(self):
        self.glWidget.update()

####################################################################################################
# The OpenGL Widget --- it's normally not needed to touch this part especially paintGL
####################################################################################################
class GLWidget(QGLWidget):
    updated = pyqtSignal(int)  # pyqtSignal is used to allow the GUI and the OpenGL widget to sync
    xRotationChanged = pyqtSignal(int)
    yRotationChanged = pyqtSignal(int)
    zRotationChanged = pyqtSignal(int)

    def __init__(self, parent):
        super(GLWidget, self).__init__(parent)
        self.xRot = 0
        self.yRot = 0
        self.zRot = 0
        self.lastPos = QPoint()

        self.Tx = self.Ty = 0
        self.Tz = 1
        self.LeftXRot = self.LeftYRot = 0

        self.parent = parent

        self.InputListCreated = False
        self.TargetListCreated = False

    def initializeGL(self):
        glEnable(GL_TEXTURE_2D)
        self.tex = glGenTextures(1)

    def paintGL(self):

        self.InputModelLoaded = self.parent.InputModelLoaded
        self.InputTextureLoaded = self.parent.InputTextureLoaded
        self.InputTexturePath = self.parent.InputTexturePath
        self.InputModel = self.parent.InputModel
        self.InputTextureDim = self.parent.InputTextureDim

        self.TargetModelLoaded = self.parent.TargetModelLoaded
        self.TargetTextureLoaded = self.parent.TargetTextureLoaded
        self.TarTexturePath = self.parent.TarTexturePath
        self.TarModel = self.parent.TarModel

        self.bg_color = self.parent.bg_color
        self.Root = self.parent.Root
        self.Tval = self.parent.Tval
        self.Gval = self.parent.Gval
        self.P_Tval = self.parent.P_Tval
        self.P_Gval = self.parent.P_Gval

        self.r_mode = self.parent.r_mode
        self.c_mode = self.parent.c_mode
        self.bg_color = self.parent.bg_color
        self.b_Ready = self.parent.b_Ready
        self.Updated = self.parent.Updated
        self.b_ProcessDone = self.parent.b_ProcessDone
        self.b_Process2Done = self.parent.b_Process2Done
        self.PCA_done = self.parent.PCA_done
        self.old_Gval = self.parent.old_Gval
        self.old_Tval = self.parent.old_Tval

        # If we have nothing to display, no model loaded: just a default background with axis
        if not self.InputModelLoaded:
            glClearColor(self.bg_color, self.bg_color, self.bg_color, 1.0)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()  # identity matrix, resets the matrix back to its default state

            # field of view (angle), ratio, near plane, far plane: all values must be > 0
            gluPerspective(60, self.aspect, 0.01, 10000)

            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()
            glTranslate(self.Tx, self.Ty, -self.Tz)

            glRotated(self.xRot / 16, 1.0, 0.0, 0.0)
            glRotated(self.yRot / 16, 0.0, 1.0, 0.0)
            glRotated(self.zRot / 16, 0.0, 0.0, 1.0)

            self.qglColor(Qt.red)
            self.renderText(10, 20, "X")
            self.qglColor(Qt.green)
            self.renderText(10, 40, "Y")
            self.qglColor(Qt.blue)
            self.renderText(10, 60, "Z")

            glLineWidth(2.0)  # Width of the lines
            # To start creating lines (you also have glBegin(GL_TRIANGLES), glBegin(GL_POLYGONES), etc....
            # depending on what you want to draw)
            glBegin(GL_LINES)
            # X axis (red)
            glColor3ub(255, 0, 0)
            glVertex3d(0, 0, 0)  # The first glVertex3d is the starting point and the second the end point
            glVertex3d(1, 0, 0)
            # Y axis (green)
            glColor3ub(0, 255, 0)
            glVertex3d(0, 0, 0)
            glVertex3d(0, 1, 0)
            # Z axis (blue)
            glColor3ub(0, 0, 255)
            glVertex3d(0, 0, 0)
            glVertex3d(0, 0, 1)
            glEnd()  # Stop
            glLineWidth(1.0)  # Change back the width to default if you want to draw something else after normally

        else:
            PCA_done = self.parent.PCA_done
            # If a model is loaded but PCA is not done, display only the model
            if PCA_done == False:
                # display input 3D model
                if self.InputModelLoaded == True and self.InputTextureLoaded == True:
                    self.updated.emit(1)
                    glClearColor(self.bg_color, self.bg_color, self.bg_color, 1.0)
                    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
                    glMatrixMode(GL_PROJECTION)
                    glLoadIdentity()  # identity matrix, resets the matrix back to its default state
                    # field of view (angle), ratio, near plane, far plane, all values must be > 0
                    gluPerspective(60, self.aspect, 0.01, 10000)
                    glMatrixMode(GL_MODELVIEW)
                    glLoadIdentity()
                    glTranslate(self.Tx, self.Ty, -self.Tz)
                    glRotated(self.xRot / 16, 1.0, 0.0, 0.0)
                    glRotated(self.yRot / 16, 0.0, 1.0, 0.0)
                    glRotated(self.zRot / 16, 0.0, 0.0, 1.0)
                    # Move 3D object to center
                    glPushMatrix()  # Save any translate/scale/rotate operations that you previously used
                    # In InputModel.vertices you have the coordinates of the vertices (X,Y,Z)
                    InputModel_Xs = [row[0] for row in self.InputModel.vertices]  # Here you will extract X
                    InputModel_Ys = [row[1] for row in self.InputModel.vertices]  # Here you will extract Y
                    InputModel_Zs = [row[2] for row in self.InputModel.vertices]  # Here you will extract Z
                    # A 3D object can have coordinates not always centered on 0
                    # So we are calculating u0,v0,w0 (center of mass/gravity of the 3D model)
                    # To be able to move it after to the center of the scene
                    u0 = (min(InputModel_Xs) + max(InputModel_Xs)) / 2
                    v0 = (min(InputModel_Ys) + max(InputModel_Ys)) / 2
                    w0 = (min(InputModel_Zs) + max(InputModel_Zs)) / 2
                    # Here we are calculating the best zoom factor by default (to see the 3D model entirely)
                    d1 = max(InputModel_Xs) - min(InputModel_Xs)
                    d2 = max(InputModel_Ys) - min(InputModel_Ys)
                    d3 = max(InputModel_Zs) - min(InputModel_Zs)
                    Q = 0.5 / ((d1 + d2 + d3) / 3)
                    glScale(Q, Q, Q)
                    glTranslate(-u0, -v0, -w0)  # Move the 3D object to the center of the scene
                    # Display 3D Model via a CallList (GOOD, extremely fast!)
                    # If the list is not created, we will do it
                    if self.InputModelLoaded == True and self.InputTextureLoaded == True and self.InputListCreated == False:
                        # pdb.set_trace()
                        ## This is how to set up a display list, whose invocation by glCallList
                        self.glinputModel = glGenLists(1)  # Allocate one list into memory
                        glNewList(self.glinputModel, GL_COMPILE)  # Begin building the passed in list
                        self.addTexture(self.InputTexturePath)  # Call function to add texture
                        self.addModel(self.InputModel)  # Call function to add 3D model
                        glEndList()  # Stop list creation
                        self.InputListCreated = True
                        self.c_mode = self.r_mode
                        glCallList(self.glinputModel)  # Call the list (display the model)
                    # If the list is already created, no need to process again and loose time, just display it
                    elif self.InputModelLoaded == True and self.InputTextureLoaded == True and self.InputListCreated == True:
                        # however, if we are changing the mode (Faces/Points), we need to recreate again the list
                        if self.Updated == True:
                            # Here we have to create the list again because it's not exactly the same list
                            # if we want to show just the points or the full model
                            self.glinputModel = glGenLists(1)
                            glNewList(self.glinputModel, GL_COMPILE)
                            self.addTexture(self.InputTexturePath)
                            self.addModel(self.InputModel)
                            glEndList()
                            self.c_mode = self.r_mode
                            glCallList(self.glinputModel)
                            self.Updated = False
                            self.parent.Updated = False
                        else:
                            glCallList(self.glinputModel)
                    glPopMatrix()  # Will reload the old model view matrix
                else:
                    print(0)

            # If the PCA is done, we will display the new model here
            else:

                glClearColor(self.bg_color, self.bg_color, self.bg_color, 1.0)
                glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
                glMatrixMode(GL_PROJECTION)
                glLoadIdentity()  # identity matrix, resets the matrix back to its default state
                gluPerspective(60, self.aspect, 0.01, 10000)
                glMatrixMode(GL_MODELVIEW)
                glLoadIdentity()
                glTranslate(self.Tx, self.Ty, -self.Tz)
                glRotated(self.xRot / 16, 1.0, 0.0, 0.0)
                glRotated(self.yRot / 16, 0.0, 1.0, 0.0)
                glRotated(self.zRot / 16, 0.0, 0.0, 1.0)
                # Move 3D object to center
                glPushMatrix()  # Save any translate/scale/rotate operations that you previously used
                # In InputModel.vertices you have the coordinates of the vertices (X,Y,Z), here you will extract X
                InputModel_Xs = [row[0] for row in self.InputModel.vertices]
                InputModel_Ys = [row[1] for row in self.InputModel.vertices]  # Here you will extract Y
                InputModel_Zs = [row[2] for row in self.InputModel.vertices]  # Here you will extract Z
                u0 = (min(InputModel_Xs) + max(InputModel_Xs)) / 2
                v0 = (min(InputModel_Ys) + max(InputModel_Ys)) / 2
                w0 = (min(InputModel_Zs) + max(InputModel_Zs)) / 2
                # Here we are calculating the best zoom factor by default (to see the 3D model entirely)
                d1 = max(InputModel_Xs) - min(InputModel_Xs)
                d2 = max(InputModel_Ys) - min(InputModel_Ys)
                d3 = max(InputModel_Zs) - min(InputModel_Zs)
                Q = 0.5 / ((d1 + d2 + d3) / 3)
                glScale(Q, Q, Q)
                glTranslate(-u0, -v0, -w0)  # Move the 3D object to the center of the scene
                self.setXRotation(self.LeftXRot)
                self.setYRotation(self.LeftYRot)
                self.updated.emit(1)
                if self.TargetListCreated == False:
                    self.targetModel = glGenLists(1)
                    glNewList(self.targetModel, GL_COMPILE)
                    self.applyTarTexture(self.parent.TarTexture)
                    self.addModel(self.InputModel)
                    glEndList()
                    self.TargetListCreated = True
                    self.c_mode = self.r_mode
                    glCallList(self.targetModel)
                elif self.TargetListCreated == True:
                    if self.c_mode == self.r_mode and (self.old_Gval == self.Gval).all() and (self.old_Tval == self.Tval).all():
                        glCallList(self.targetModel)
                    else:
                        self.targetModel = glGenLists(1)
                        glNewList(self.targetModel, GL_COMPILE)
                        self.applyTarTexture(self.parent.TarTexture)
                        self.addModel(self.InputModel)
                        glEndList()
                        self.c_mode = self.r_mode
                        glCallList(self.targetModel)
                self.old_Gval = self.Gval
                self.old_Tval = self.Tval
                glPopMatrix()

    def addModel(self, InputModel):
        if self.r_mode == "Faces":
            glEnable(GL_TEXTURE_2D)
            glEnable(GL_DEPTH_TEST)  # to show all faces
            # glEnable(GL_CULL_FACE) # To hide non visible faces
            glBindTexture(GL_TEXTURE_2D, self.tex)
            glBegin(GL_TRIANGLES)
            for i in InputModel.faces:
                F = i[0]
                for j in F:
                    glColor3ub(255, 255, 255)
                    glTexCoord2f(InputModel.texcoords[j-1][0], InputModel.texcoords[j-1][1])
                    glNormal3d(InputModel.normals[j-1][0], InputModel.normals[j-1][1], InputModel.normals[j-1][2])
                    glVertex3d(InputModel.vertices[j-1][0], InputModel.vertices[j-1][1], InputModel.vertices[j-1][2])
            glEnd()
            glDisable(GL_TEXTURE_2D)
        elif self.r_mode == "Points":
            glEnable(GL_TEXTURE_2D)
            glBindTexture(GL_TEXTURE_2D, self.tex)
            glBegin(GL_POINTS)
            for i in range(len(InputModel.vertices)):
                glColor3ub(255, 255, 255)
                glTexCoord2f(InputModel.texcoords[i][0], InputModel.texcoords[i][1])
                glNormal3d(InputModel.normals[i][0], InputModel.normals[i][1], InputModel.normals[i][2])
                glVertex3d(int(InputModel.vertices[i][0]), int(InputModel.vertices[i][1]), int(InputModel.vertices[i][2]))
            glEnd()
            glDisable(GL_TEXTURE_2D)

    def addTexture(self, TexturePath):
        img = QImage(TexturePath)
        img = QGLWidget.convertToGLFormat(img)
        glBindTexture(GL_TEXTURE_2D, self.tex)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, img.width(), img.height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, img.bits().asstring(img.byteCount()))


    def applyTarTexture(self, TarTexture):
        img = QImage("TarTexture.png")
        img = QGLWidget.convertToGLFormat(img)
        glBindTexture(GL_TEXTURE_2D, self.tex)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, img.width(), img.height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, img.bits().asstring(img.byteCount()))

    def mousePressEvent(self, event):
        self.lastPos = event.pos()

    def wheelEvent(self, event):
        numDegrees = event.angleDelta() / 8
        orientation = numDegrees.y()
        if orientation > 0:
            self.Tz -= 0.1  # zoom out
        else:
            self.Tz += 0.1  # zoom in
        self.updateGL()

    def mouseMoveEvent(self, event):
        dx = event.x() - self.lastPos.x()
        dy = event.y() - self.lastPos.y()
        if event.buttons() & Qt.LeftButton:  # holding left button of mouse and moving will rotate the object
            self.setXRotation(self.xRot + 8 * dy)
            self.setYRotation(self.yRot + 8 * dx)
            self.LeftXRot = self.xRot + 8 * dy
            self.LeftYRot = self.yRot + 8 * dx
        elif event.buttons() & Qt.RightButton:  # holding right button of mouse and moving will translate the object
            self.Tx += dx / 100
            self.Ty -= dy / 100
            self.updateGL()
        elif event.buttons() & Qt.MidButton:  # holding middle button of mouse and moving will reset zoom/translations
            self.Tx = Ty = 0
            self.Tz = 1
            self.setXRotation(0)
            self.setYRotation(90)
            self.updateGL()

        self.lastPos = event.pos()

    def resizeGL(self, width, height):
        side = min(width, height)
        if side < 50:
            return

        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        self.aspect = float(width) / float(height)
        gluPerspective(60.0, self.aspect, 0.01, 10000)
        glMatrixMode(GL_MODELVIEW)

    def setClearColor(self, c):
        gl.glClearColor(c.redF(), c.greenF(), c.blueF(), c.alphaF())

    def setColor(self, c):
        gl.glColor4f(c.redF(), c.greenF(), c.blueF(), c.alphaF())

    def setXRotation(self, angle):
        angle = self.normalizeAngle(angle)
        if angle != self.xRot:
            self.xRot = angle
            self.xRotationChanged.emit(angle)
            self.update()

    def setYRotation(self, angle):
        angle = self.normalizeAngle(angle)
        if angle != self.xRot:
            self.yRot = angle
            self.yRotationChanged.emit(angle)
            self.update()

    def setZRotation(self, angle):
        angle = self.normalizeAngle(angle)
        if angle != self.xRot:
            self.zRot = angle
            self.zRotationChanged.emit(angle)
            self.update()

    def normalizeAngle(self, angle):
        while angle < 0:
            angle += 360 * 16
        while angle > 360 * 16:
            angle -= 360 * 16
        return angle


class PCAThread(QThread):
    #progress_signal = pyqtSignal(int)
    finished_signal = pyqtSignal(dict)
    finished_flag = pyqtSignal()
    update_p = pyqtSignal(int)

    def __init__(self, file_paths, data_type):
        super(PCAThread, self).__init__()
        self.file_paths = file_paths
        self.data_type = data_type
        self.running = True

    def run(self):
        if self.running == True:
            self.PCA()
            
    def PCA(self):

        try:
            if self.data_type == 'Tex':
                samples = [np.float32(imread(i)) for i in self.file_paths]
            else:
                samples = [np.float32(OBJFastV(i).vertices) for i in self.file_paths]
            

            imsize = samples[0].shape
            row = len(samples)
            

            if self.data_type == 'Tex':
                data = np.zeros((row, imsize[0]*imsize[1]*imsize[2]), dtype=np.float32)
            
            else:
                data = np.zeros((row, imsize[0]*imsize[1]), dtype=np.float32)

            self.update_p.emit(20)
            for i in range(row):
                sample = samples[i].flatten()
                data[i,:] = sample
                
            self.update_p.emit(50)
            mu = np.mean(data,0)
            ma_data = data - mu

            e_faces, sigma, v = linalg.svd(ma_data.transpose(), full_matrices=False)
            weights = np.dot(ma_data, e_faces)
            
            
            eigenvectors = e_faces.transpose()
            
            self.update_p.emit(90)
            eigenFaces = []
            for eigenvector in eigenvectors:
                eigenFace = eigenvector.reshape(imsize)
                eigenFaces.append(eigenFace)

            averageFace = mu.reshape(imsize)
            
            results = {'Vr': eigenFaces, 'Xm': averageFace, 'W': weights[:,0]}
            self.update_p.emit(100)
            self.finished_signal.emit(results)
            self.finished_flag.emit()
            self.running = False
            
            
            
            
        except Exception as e:
            print(f'PCA_{self.data_type} Error:', e)
            
            
            
        self.running = False
            
            


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
