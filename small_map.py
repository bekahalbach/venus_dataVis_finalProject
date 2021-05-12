#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 14:47:21 2021

@author: Bekah
"""

#!/usr/bin/env python

##################### TUTORIALS USED: #####################

    #
    
###############################################################

from __future__ import print_function

import vtk

colors = vtk.vtkNamedColors()

# # #Interactor style that handles mouse and keyboard events
class vtkMyCallback(object):

    def __call__(self,caller,ev):
        
        planeHolder = vtk.vtkPlane();
        plane.GetPlane(planeHolder)

        self.parent = vtk.vtkRenderWindowInteractor()
        mapper.CroppingOn()
        xpoint = planeHolder.GetOrigin()
        mapper.SetCroppingRegionPlanes(xpoint[0],256,xpoint[1],256,xpoint[2],256)
        print(xpoint)


class MyInteractorStyle(vtk.vtkInteractorStyleTrackballCamera):

    def __init__(self,parent=None):
        self.parent = vtk.vtkRenderWindowInteractor()
        if(parent is not None):
          self.parent = parent
        self.AddObserver("KeyPressEvent",self.keyPress)
    
    def keyPress(self,obj,event):
      key = self.parent.GetKeySym()
      global value 
      if(key == "Up"):
            value+=0.002
          #TODO: have this increase the isovalue
          # angle += 0.2
          # ren.GetActiveCamera().SetViewUp(0.0, 0.5, angle)
          # renWin.Render()
            warp = vtk.vtkWarpScalar()
            warp.SetInputConnection(geometry.GetOutputPort())
            warp.SetScaleFactor(value)
        
        #Use vtkMergeFilter to combine the original image with the warped geometry.
            #merge = vtk.vtkMergeFilter()
            #merge.SetGeometryConnection(warp.GetOutputPort())
            #merge.SetScalarsConnection(imageReader.GetOutputPort())
            #mapper = vtk.vtkDataSetMapper()
            mapper = vtk.vtkPolyDataMapper()
            mapper.SetInputConnection(warp.GetOutputPort()) # warp 
           #self.actorProperty.SetScaleFactor(value)
            mapper.SetScalarRange(0, 11687)

            actor.SetMapper(mapper)
            print("Up")
            print(value)
      if(key == "Down"):
          #TODO: have this decrease the isovalue
            value-=0.002
          #TODO: have this increase the isovalue
          # angle += 0.2
          # ren.GetActiveCamera().SetViewUp(0.0, 0.5, angle)
          # renWin.Render()
            warp = vtk.vtkWarpScalar()
            warp.SetInputConnection(geometry.GetOutputPort())
            warp.SetScaleFactor(value)
        
        #Use vtkMergeFilter to combine the original image with the warped geometry.
            #merge = vtk.vtkMergeFilter()
            #merge.SetGeometryConnection(warp.GetOutputPort())
           # merge.SetScalarsConnection(imageReader.GetOutputPort())
           # mapper = vtk.vtkDataSetMapper()
            mapper = vtk.vtkPolyDataMapper()
            mapper.SetInputConnection(warp.GetOutputPort())
           #self.actorProperty.SetScaleFactor(value)
            mapper.SetScalarRange(0, 11687)

            actor.SetMapper(mapper)
            print(value)
            renWin.Render()
            print("Down")

# def MakeButtonWidget(): 
    
#     upperRight = vtk.vtkCoordinate()
#     upperRight.SetCoordinateSystemToNormalizedDisplay()
#     upperRight.SetValue(1.0, 1.0)

#     bds = [0]*6
#     sz = 50.0
#     bds[0] = upperRight.GetComputedDisplayValue(ren)[0] - sz
#     bds[1] = bds[0] + sz
#     bds[2] = upperRight.GetComputedDisplayValue(ren)[1] - sz
#     bds[3] = bds[2] + sz
#     bds[4] = bds[5] = 0.0 

#     buttonRep = vtk.vtkTexturedButtonRepresentation()
#     buttonRep.SetNumberOfStates(2)
#     buttonRep.SetPlaceFactor(1)
#     buttonRep.PlaceWidget(bds)
    
#     buttonWidget = vtk.vtkButtonWidget()
#     buttonWidget.SetRepresentation(buttonRep)
    
#     return buttonWidget


# class SliderProperties:
#     tubeWidth = 0.008
#     sliderLength = 0.008
#     titleHeight = 0.02
#     labelHeight = 0.02

#     minimumValue = 0.0
#     maximumValue = .006
#     initialValue = 0.002
#     p1 = [0.1, 0.1]
#     p2 = [0.9, 0.1]

#     title = None


# def MakeSliderWidget(properties):
#     slider = vtk.vtkSliderRepresentation2D()

#     slider.SetMinimumValue(properties.minimumValue)
#     slider.SetMaximumValue(properties.maximumValue)
#     slider.SetValue(properties.initialValue)
#     slider.SetTitleText(properties.title)

#     slider.GetPoint1Coordinate().SetCoordinateSystemToNormalizedDisplay()
#     slider.GetPoint1Coordinate().SetValue(properties.p1[0], properties.p1[1])
#     slider.GetPoint2Coordinate().SetCoordinateSystemToNormalizedDisplay()
#     slider.GetPoint2Coordinate().SetValue(properties.p2[0], properties.p2[1])

#     slider.SetTubeWidth(properties.tubeWidth)
#     slider.SetSliderLength(properties.sliderLength)
#     slider.SetTitleHeight(properties.titleHeight)
#     slider.SetLabelHeight(properties.labelHeight)

#     sliderWidget = vtk.vtkSliderWidget()
#     sliderWidget.SetRepresentation(slider)

#     return sliderWidget


# class SliderCallbackMetallic:
#     def __init__(self, actorProperty):
#         self.actorProperty = actorProperty
 
#     def __call__(self, caller, ev):
#         sliderWidget = caller
#         value = sliderWidget.GetRepresentation().GetValue()
#        # self.actorProperty.SetMetallic(value)
#         warp = vtk.vtkWarpScalar()
#         warp.SetInputConnection(geometry.GetOutputPort())
#         warp.SetScaleFactor(value)
    
#     #Use vtkMergeFilter to combine the original image with the warped geometry.
#         #merge = vtk.vtkMergeFilter()
#         #merge.SetGeometryConnection(warp.GetOutputPort())
#        # merge.SetScalarsConnection(imageReader.GetOutputPort())
#         mapper = vtk.vtkDataSetMapper()
#         mapper.SetInputConnection(warp.GetOutputPort())
#        #self.actorProperty.SetScaleFactor(value)
#         actor.SetMapper(mapper)
        
# def buttonCallback(widget, event):
#     value = widget.GetRepresentation().GetState()
    
#     return

#############################################################################

#Loader for our structured dataset
imageReader = vtk.vtkXMLImageDataReader()
imageReader.SetFileName("./venus_topo.vti")
imageReader.Update()

filteredImage = vtk.vtkImageThreshold() 
filteredImage.SetInputConnection(imageReader.GetOutputPort())
filteredImage.ThresholdByLower(0)
filteredImage.Update()

# Read the image data from a file
# reader = vtk.vtkXMLStructuredGridReader()
# reader.SetFileName("./venus_texture_2_0.vts")
# reader.Update()

# Create texture object
# texture = vtk.vtkTexture()
# texture.InterpolateOn()
# texture.SetInputConnection(reader.GetOutputPort())
#texture.SetPosition(0,0.5,.7)
    
#Print dimensions and range of the 3d image
dims = imageReader.GetOutput().GetDimensions()
print(imageReader.GetClassName())
print("Dimensions of image: " + str(dims[0]) + " x "
      + str(dims[1]) + " x " + str(dims[2]))
range = imageReader.GetOutput().GetScalarRange();
print("Range of image: " + str(range[0]) + " to " +  str(range[1]))

# COLOR TRANSFER FUNCTION
ctf = vtk.vtkColorTransferFunction();

ctf.AddRGBPoint(0,0,0,0)
ctf.AddRGBPoint(16,0.090196,0,0)
ctf.AddRGBPoint(32,0.180392,0,0)

# Convert the image to a grey scale.
#luminance = vtk.vtkImageLuminance()
#luminance.SetInputConnection(imageReader.GetOutputPort())
    # Pass the data to the pipeline as polygons.
geometry = vtk.vtkImageDataGeometryFilter()
geometry.SetInputConnection(filteredImage.GetOutputPort()) #CHANGED
    # Warp the data in a direction perpendicular to the image plane.
warp = vtk.vtkWarpScalar()
warp.SetInputConnection(geometry.GetOutputPort()) # used to say geometry
warp.SetScaleFactor(.002)


#Use vtkMergeFilter to combine the original image with the warped geometry.
#merge = vtk.vtkMergeFilter()
#merge.SetGeometryConnection(warp.GetOutputPort())
#merge.SetScalarsConnection(imageReader.GetOutputPort())
#mapper = vtk.vtkDataSetMapper()
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(warp.GetOutputPort()) #used to say merge
mapper.SetScalarRange(0, 11687)
actor = vtk.vtkActor()
actor.SetMapper(mapper)
#actor.SetTexture(texture)


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

renWin.SetSize(700, 700)
renWin.SetWindowName('ImageWarp')

# height = 0.0
# slwP = SliderProperties()
# slwP.initialValue = height
# slwP.title = 'Exaggeration'

# sliderWidgetMetallic = MakeSliderWidget(slwP)
# sliderWidgetMetallic.SetInteractor(interactor)
# sliderWidgetMetallic.SetAnimationModeToAnimate()
# sliderWidgetMetallic.EnabledOn()

# contours 
# extractVOI = vtk.vtkExtractVOI()
# extractVOI.SetInputConnection(imageReader.GetOutputPort())
# #extractVOI.SetVOI(0, 255, 0, 255, 45, 45)

# scalarRange = extractVOI.GetOutput().GetScalarRange()

# isoMapper = vtk.vtkPolyDataMapper()
# isoMapper.SetScalarRange(scalarRange)

# contour = vtk.vtkContourFilter()
# contour.SetInputConnection(extractVOI.GetOutputPort())
# contour.GenerateValues(12, scalarRange)
# isoMapper.SetInputConnection(contour.GetOutputPort())

# isoMapper.ScalarVisibilityOn()
# isoMapper.SetScalarRange(scalarRange)

# isoActor = vtk.vtkActor()
# isoActor.SetMapper(isoMapper)
# isoActor.GetProperty().SetColor(colors.GetColor3d('Wheat'))

# ren.AddActor(isoActor)


# buttonWidget_a = MakeButtonWidget()
# buttonWidget_a.SetInteractor(interactor)
# buttonWidget_a.On()
# buttonWidget_a.AddObserver(vtk.vtkCommand.StateChangedEvent, buttonCallback)
# # 

# configure the basic properties
# actor.GetProperty().SetMetallic(height)

# Create the slider callbacks to manipulate metallicity and roughness
# sliderWidgetMetallic.AddObserver(vtk.vtkCommand.InteractionEvent, SliderCallbackMetallic(actor))

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

#text
txt = vtk.vtkTextActor()
txt.SetInput("Up Arrow: Increase vertical exaggeration of topography, Down Arrow: Decrease vertical exaggeration")
txtprop = txt.GetTextProperty()
txtprop.SetFontFamilyToArial()
txtprop.BoldOn()
txtprop.SetFontSize(12)
txt.SetDisplayPosition(20, 30)
ren.AddActor(txt)

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




# Render the image.
interactor.Initialize()
planewidget.On()
renWin.Render()
interactor.Start()




