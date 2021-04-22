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

class SliderProperties:
    tubeWidth = 0.008
    sliderLength = 0.008
    titleHeight = 0.02
    labelHeight = 0.02

    minimumValue = 0.0
    maximumValue = 40.0
    initialValue = 1.0

    p1 = [0.1, 0.1]
    p2 = [0.9, 0.1]

    title = None


def MakeSliderWidget(properties):
    slider = vtk.vtkSliderRepresentation2D()

    slider.SetMinimumValue(properties.minimumValue)
    slider.SetMaximumValue(properties.maximumValue)
    slider.SetValue(properties.initialValue)
    slider.SetTitleText(properties.title)

    slider.GetPoint1Coordinate().SetCoordinateSystemToNormalizedDisplay()
    slider.GetPoint1Coordinate().SetValue(properties.p1[0], properties.p1[1])
    slider.GetPoint2Coordinate().SetCoordinateSystemToNormalizedDisplay()
    slider.GetPoint2Coordinate().SetValue(properties.p2[0], properties.p2[1])

    slider.SetTubeWidth(properties.tubeWidth)
    slider.SetSliderLength(properties.sliderLength)
    slider.SetTitleHeight(properties.titleHeight)
    slider.SetLabelHeight(properties.labelHeight)

    sliderWidget = vtk.vtkSliderWidget()
    sliderWidget.SetRepresentation(slider)

    return sliderWidget


class SliderCallbackMetallic:
    def __init__(self, actorProperty):
        self.actorProperty = actorProperty

    def __call__(self, caller, ev):
        sliderWidget = caller
        value = sliderWidget.GetRepresentation().GetValue()
       # self.actorProperty.SetMetallic(value)
        warp = vtk.vtkWarpScalar()
        warp.SetInputConnection(geometry.GetOutputPort())
        warp.SetScaleFactor(value)
    
    #Use vtkMergeFilter to combine the original image with the warped geometry.
        merge = vtk.vtkMergeFilter()
        merge.SetGeometryConnection(warp.GetOutputPort())
        merge.SetScalarsConnection(imageReader.GetOutputPort())
        mapper = vtk.vtkDataSetMapper()
        mapper.SetInputConnection(merge.GetOutputPort())
       #self.actorProperty.SetScaleFactor(value)
        actor.SetMapper(mapper)

#############################################################################

#Loader for our structured dataset
imageReader = vtk.vtkXMLImageDataReader()
#imageReader = vtk.vtkBMPReader()
imageReader.SetFileName("./venus_topo.vti")
imageReader.Update()

#Print dimensions and range of the 3d image
dims = imageReader.GetOutput().GetDimensions()
print(imageReader.GetClassName())
print("Dimensions of image: " + str(dims[0]) + " x "
      + str(dims[1]) + " x " + str(dims[2]))
range = imageReader.GetOutput().GetScalarRange();
print("Range of image: " + str(range[0]) + " to " +  str(range[1]))

# Convert the image to a grey scale.
luminance = vtk.vtkImageLuminance()
luminance.SetInputConnection(imageReader.GetOutputPort())
    # Pass the data to the pipeline as polygons.
geometry = vtk.vtkImageDataGeometryFilter()
geometry.SetInputConnection(luminance.GetOutputPort())
    # Warp the data in a direction perpendicular to the image plane.
warp = vtk.vtkWarpScalar()
warp.SetInputConnection(geometry.GetOutputPort())
warp.SetScaleFactor(1)

#Use vtkMergeFilter to combine the original image with the warped geometry.
merge = vtk.vtkMergeFilter()
merge.SetGeometryConnection(warp.GetOutputPort())
merge.SetScalarsConnection(imageReader.GetOutputPort())
mapper = vtk.vtkDataSetMapper()
mapper.SetInputConnection(warp.GetOutputPort())
mapper.SetScalarRange(0, 255)
actor = vtk.vtkActor()
actor.SetMapper(mapper)

# Create the rendering window, renderer, and interactive renderer.
ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(renWin)
 
# Add the actors to the renderer, set the background and size.
ren.AddActor(actor)
ren.ResetCamera()
ren.SetBackground(colors.GetColor3d('BkgColor'))
ren.GetActiveCamera().SetViewUp(0.51, 0.54, 0.67)
ren.ResetCameraClippingRange()

renWin.SetSize(700, 700)
renWin.SetWindowName('ImageWarp')

height = 0.0
slwP = SliderProperties()
slwP.initialValue = height
slwP.title = 'Exaggeration'

sliderWidgetMetallic = MakeSliderWidget(slwP)
sliderWidgetMetallic.SetInteractor(interactor)
sliderWidgetMetallic.SetAnimationModeToAnimate()
sliderWidgetMetallic.EnabledOn()



# configure the basic properties
actor.GetProperty().SetMetallic(height)

# Create the slider callbacks to manipulate metallicity and roughness
sliderWidgetMetallic.AddObserver(vtk.vtkCommand.InteractionEvent, SliderCallbackMetallic(actor))



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
renWin.Render()
interactor.Start()




