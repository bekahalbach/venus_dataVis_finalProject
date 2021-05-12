#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Final Project for Data Visualization Spring 2021 
Interactive Topographic Map of the Surface of venus 

@author: Bekah
"""

#!/usr/bin/env python

##################### TUTORIALS USED: ########################################

    #Project inspiration: https://www.cs.purdue.edu/homes/cs530/projects/project1.html
    #Image Warping code / guidance: https://kitware.github.io/vtk-examples/site/Python/Images/ImageWarp/
    #Also used bits of code from assignments 4 / 5 of this class 
    
##############################################################################

from __future__ import print_function
import vtk

##############################################################################

# Import Colors 
colors = vtk.vtkNamedColors()

# # #Interactor style 

# Interactor style for plane widget 
class vtkMyCallback(object):

    def __call__(self,caller,ev):
        
        planeHolder = vtk.vtkPlane();
        plane.GetPlane(planeHolder)

        self.parent = vtk.vtkRenderWindowInteractor()
        mapper.CroppingOn()
        xpoint = planeHolder.GetOrigin()
        mapper.SetCroppingRegionPlanes(xpoint[0],256,xpoint[1],256,xpoint[2],256)
        print(xpoint)

##############################################################################

# Interactor style for key press up / down (changes scale factor of warping)
class MyInteractorStyle(vtk.vtkInteractorStyleTrackballCamera):

    def __init__(self,parent=None):
        self.parent = vtk.vtkRenderWindowInteractor()
        if(parent is not None):
          self.parent = parent
        self.AddObserver("KeyPressEvent",self.keyPress)
    
    def keyPress(self,obj,event):
      key = self.parent.GetKeySym()
      global value 
      if(key == "Up"): # if UP is pressed, increases 0.002
            value+=0.002

            warp = vtk.vtkWarpScalar()
            warp.SetInputConnection(geometry.GetOutputPort())
            warp.SetScaleFactor(value)
        
            #merge = vtk.vtkMergeFilter()
            #merge.SetGeometryConnection(warp.GetOutputPort())
            #merge.SetScalarsConnection(imageReader.GetOutputPort())
            #mapper = vtk.vtkDataSetMapper()
            mapper = vtk.vtkPolyDataMapper()
            mapper.SetInputConnection(warp.GetOutputPort()) # warp 
            #mapper.SetScalarRange(0, 11687)
            mapper.SetLookupTable(ctf)
            actor.SetMapper(mapper)
            renWin.Render()

            print("Up")
            print(value)
            
      if(key == "Down"): # if DOWN is pressed, decreases 0.002 
            value-=0.002
            
            warp = vtk.vtkWarpScalar()
            warp.SetInputConnection(geometry.GetOutputPort())
            warp.SetScaleFactor(value)
        
            #merge = vtk.vtkMergeFilter()
            #merge.SetGeometryConnection(warp.GetOutputPort())
           # merge.SetScalarsConnection(imageReader.GetOutputPort())
           # mapper = vtk.vtkDataSetMapper()
            mapper = vtk.vtkPolyDataMapper()
            mapper.SetInputConnection(warp.GetOutputPort())
            #mapper.SetScalarRange(0, 11687)
            mapper.SetLookupTable(ctf)
            actor.SetMapper(mapper)
            
            print("Down")
            print(value)
           
###############################################################################

# Trying to do texture mapping or color 

# Read the image data from a file
# reader = vtk.vtkXMLStructuredGridReader()
# reader.SetFileName("./venus_texture_2_0.vts")
# reader.Update()

# Create texture object
# texture = vtk.vtkTexture()
# texture.InterpolateOn()
# texture.SetInputConnection(reader.GetOutputPort())
#texture.SetPosition(0,0.5,.7)
    
# COLOR TRANSFER FUNCTION
ctf = vtk.vtkColorTransferFunction();
ctf.AddRGBPoint(-32678,0.89016,.956863,0.984314)
ctf.AddRGBPoint(-5155.99,0.776471,0.764706,0.678431)
ctf.AddRGBPoint(-4399.33,0.827451,0.823529,0.737255)
ctf.AddRGBPoint(-3642.67,0.890196,0.890196,0.807843)
ctf.AddRGBPoint(-2886,0.952941,0.952941,0.894118)
ctf.AddRGBPoint(-2156,0.988235,0.988235,0.756863)
ctf.AddRGBPoint(-1428,0.980392,0.972549,0.670588)
ctf.AddRGBPoint(-699,0.980392,0.94902,0.596078)
ctf.AddRGBPoint(28.9457,0.972549,0.917647,0.513725)
ctf.AddRGBPoint(757.574,0.968627,0.878431,0.423529)
ctf.AddRGBPoint(1486.2,0.964706,0.827451,0.32549)
ctf.AddRGBPoint(2214.83,0.95241,0.768627,0.247059)
ctf.AddRGBPoint(2943.46,0.945098,0.709804,0.184314)
ctf.AddRGBPoint(3672.09,0.937255,0.643137,0.125169)
ctf.AddRGBPoint(4400.72,0.92549,0.580392,0.0784314)
ctf.AddRGBPoint(5129.34,0.917647,0.521569,0.0470588)
ctf.AddRGBPoint(5857.97,0.901961,0.458824,0.027451)
ctf.AddRGBPoint(6586.6,0.862745,0.380392,0.0117647)
ctf.AddRGBPoint(7315.23,0.788235,0.290196,0)
ctf.AddRGBPoint(8043.86,0.741176,0.227451,0.00392157)
ctf.AddRGBPoint(8772.49,0.662745,0.168627,0.0156863)
ctf.AddRGBPoint(9501.11,0.588235,0.113725,0.0235294)
ctf.AddRGBPoint(10229.7,0.494118,0.054902,0.0352941)
ctf.AddRGBPoint(10958.4,0.396078,0.0392157,0.0588235)
ctf.AddRGBPoint(11687,0.301961,0.047059,0.090196)

##############################################################################

# LOADING IMAGE 

#Loader for our structured dataset
imageReader = vtk.vtkXMLImageDataReader()
imageReader.SetFileName("./venus_topo.vti")
imageReader.Update()

#Print dimensions and range of the 3d image
dims = imageReader.GetOutput().GetDimensions()
print(imageReader.GetClassName())
print("Dimensions of image: " + str(dims[0]) + " x "
      + str(dims[1]) + " x " + str(dims[2]))
range = imageReader.GetOutput().GetScalarRange();
print("Range of image: " + str(range[0]) + " to " +  str(range[1]))

# Trying to filter out the NaN values of ~ -30000
filteredImage = vtk.vtkImageThreshold() 
filteredImage.SetInputConnection(imageReader.GetOutputPort())
filteredImage.ThresholdByLower(-5000)
filteredImage.Update()


##############################################################################
# WARPING AND MAPPING THE TOPO MAP 

# Convert the image to a grey scale.
#luminance = vtk.vtkImageLuminance()
#luminance.SetInputConnection(imageReader.GetOutputPort())
# Pass the data to the pipeline as polygons.
geometry = vtk.vtkImageDataGeometryFilter()
geometry.SetInputConnection(filteredImage.GetOutputPort()) #CHANGED
# Warp the data in a direction perpendicular to the image plane.
warp = vtk.vtkWarpScalar()
warp.SetInputConnection(geometry.GetOutputPort()) # used to say geometry
value = 0.002
warp.SetScaleFactor(value)

#Use vtkMergeFilter to combine the original image with the warped geometry.
#merge = vtk.vtkMergeFilter()
#merge.SetGeometryConnection(warp.GetOutputPort())
#merge.SetScalarsConnection(imageReader.GetOutputPort())
mapper = vtk.vtkDataSetMapper()
#mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(warp.GetOutputPort()) #used to say merge
#mapper.SetScalarRange(0, 11687)
mapper.SetLookupTable(ctf)

actor = vtk.vtkActor()
actor.SetMapper(mapper)
#actor.SetTexture(texture)

##############################################################################


# Create the rendering window, renderer, and interactive renderer.
ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

interactor = vtk.vtkRenderWindowInteractor()
interactor.SetInteractorStyle(MyInteractorStyle(parent = interactor))
interactor.SetRenderWindow(renWin)
 
# Add the actors to the renderer, set the background and size.
ren.AddActor(actor)
ren.ResetCamera()
ren.SetBackground(colors.GetColor3d('BkgColor'))
ren.GetActiveCamera().SetViewUp(0.0, 0.5, .7)
ren.ResetCameraClippingRange()

renWin.SetSize(1500, 700)
renWin.SetWindowName('VenusTopo')

##############################################################################
# IMPLICIT PLANE WIDGET

#create plane
plane = vtk.vtkImplicitPlaneRepresentation();
plane.SetPlaceFactor(1.00);
plane.SetOrigin(3000,500,17)
plane.OutsideBoundsOn();
plane.PlaceWidget(actor.GetBounds());
plane.OutlineTranslationOff();
plane.SetEdgeColor(255,255,255)
#plane.SetTranslationAxisOff();

#enable plane widget
planewidget = vtk.vtkImplicitPlaneWidget2();
planewidget.SetInteractor(interactor);
planewidget.SetRepresentation(plane);
watcher = vtkMyCallback()
planewidget.AddObserver('InteractionEvent',watcher)

##############################################################################
# ADD TEXT 

#text
txt = vtk.vtkTextActor()
txt.SetInput("Up Arrow: Increase vertical exaggeration of topography, Down Arrow: Decrease vertical exaggeration")
txtprop = txt.GetTextProperty()
txtprop.SetFontFamilyToArial()
#txtprop.BoldOn()
txtprop.SetFontSize(12)
txt.SetDisplayPosition(20, 30)
ren.AddActor(txt)

# more text 
txt2 = vtk.vtkTextActor()
txt2.SetInput("Topography of the Surface of Venus")
txt2prop = txt2.GetTextProperty()
txt2prop.SetFontFamilyToArial()
txt2prop.BoldOn()
txt2prop.SetFontSize(24)
txt2.SetDisplayPosition(20, 60)
ren.AddActor(txt2)

##############################################################################
# ADD AXIS 

axes = vtk.vtkAxesActor()

widget = vtk.vtkOrientationMarkerWidget()
rgba = [0.0, 0.0, 0.0, 0.0]
colors.GetColor("Carrot", rgba)
widget.SetOutlineColor(rgba[0], rgba[1], rgba[2])
widget.SetOrientationMarker(axes)
widget.SetInteractor(interactor)
widget.SetViewport(0.0, 0.2, 0.2, 0.4)
widget.SetEnabled(1)
widget.InteractiveOn()

##############################################################################
#scalarbar
scalebar = vtk.vtkScalarBarActor()
scalebar.SetLookupTable(ctf)
scalebar.SetTitle("Elevation (m)")
scalebar.SetVerticalTitleSeparation(20)
scalebar.SetBarRatio(.26)
scalebar.SetMaximumHeightInPixels(400)
scalebar.UnconstrainedFontSizeOn()
ren.AddActor(scalebar)

##############################################################################
# RENDER 

# Render the image
interactor.Initialize()
planewidget.On()
renWin.Render()
interactor.Start()

##############################################################################



