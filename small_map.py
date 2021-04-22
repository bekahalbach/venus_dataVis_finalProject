#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 14:47:21 2021

@author: nadim
"""

#!/usr/bin/env python

##################### TUTORIALS USED: #####################

    #ColorTransferFunction: https://kitware.github.io/vtk-js/api/Rendering_Core_ColorTransferFunction.html
    #ScaleBar: https://python.hotexamples.com/examples/vtk/-/vtkScalarBarActor/python-vtkscalarbaractor-function-examples.html
    #MarchingCubes: https://lorensen.github.io/VTKExamples/site/Python/Medical/MedicalDemo1/
    
###############################################################

from __future__ import print_function

import vtk

colors = vtk.vtkNamedColors()

# # #Interactor style that handles mouse and keyboard events


#Loader for our structured dataset
imageReader = vtk.vtkXMLImageDataReader()
#imageReader = vtk.vtkBMPReader()
imageReader.SetFileName("./map.vti")
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
warp.SetScaleFactor(20)
# footmapper = vtk.vtkGPUVolumeRayCastMapper()
# footmapper.SetInputConnection(imageReader.GetOutputPort())
# #footmapper.ScalarVisibilityOff()

#Use vtkMergeFilter to combine the original image with the warped geometry.
merge = vtk.vtkMergeFilter()
merge.SetGeometryConnection(warp.GetOutputPort())
merge.SetScalarsConnection(imageReader.GetOutputPort())
mapper = vtk.vtkDataSetMapper()
mapper.SetInputConnection(merge.GetOutputPort())
mapper.SetScalarRange(0, 255)
actor = vtk.vtkActor()
actor.SetMapper(mapper)

# Create the rendering window, renderer, and interactive renderer.
ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

# Add the actors to the renderer, set the background and size.
ren.AddActor(actor)
ren.ResetCamera()
ren.SetBackground(colors.GetColor3d('BkgColor'))
# ren.GetActiveCamera().Azimuth(20)
# ren.GetActiveCamera().Elevation(30)
# ren.ResetCameraClippingRange()
# ren.GetActiveCamera().Zoom(1.3)
# ren.GetActiveCamera().SetPosition(0, 0, 0)
# ren.GetActiveCamera().SetFocalPoint(0, 0, 0)
ren.GetActiveCamera().SetViewUp(0.51, 0.54, 0.67)
ren.ResetCameraClippingRange()

renWin.SetSize(700, 700)
renWin.SetWindowName('ImageWarp')

# Render the image.
iren.Initialize()
renWin.Render()
iren.Start()

# volume_property = vtk.vtkVolumeProperty()

# #volume_property.SetGradientOpacity(volume_gradient_opacity)
# volume_property.SetInterpolationTypeToLinear()
# volume_property.ShadeOn()
# volume_property.SetAmbient(0.4)
# volume_property.SetDiffuse(0.6)
# volume_property.SetSpecular(0.2)

# volume = vtk.vtkVolume()
# volume.SetMapper(footmapper)
# volume.SetProperty(volume_property)

# #################################################################

# # #Insert isosurfacing, scalebar, and text code here
# # hydrogen = vtk.vtkMarchingCubes()
# # hydrogen.SetInputData(imageReader.GetOutput());
# # hydrogen.ComputeNormalsOn();
# # hydrogen.SetValue(0,isovalue)

# # # The mapper is responsible for pushing the geometry into the graphics
# # # library. It may also do color mapping, if scalars or other
# # # attributes are defined.
# # colors = vtk.vtkNamedColors()
# # hydrogenMapper = vtk.vtkPolyDataMapper()
# # hydrogenMapper.SetInputConnection(hydrogen.GetOutputPort())
# # hydrogenMapper.ScalarVisibilityOff()

# # #hydrogenActor
# # hydrogenActor = vtk.vtkVolume()
# # volumeprop = vtk.vtkVolumeProperty()
# # #hydrogenActor.SetMapper(hydrogenMapper)
# # #hydrogenActor.GetProperty().EdgeVisibilityOn()
# # #hydrogenActor.GetProperty().SetColor(ctf.GetColor(isovalue))
# # #hydrogenActor.GetProperty().SetColor(ctf.GetColor(isovalue));
# # #hydrogenActor.SetScalarOpacity(opf);
# # volumeprop.SetScalarOpacity(opf);


# #A renderer that renders our geometry into the render window
# renderer = vtk.vtkRenderer()
# renderer.SetBackground(0.1, 0.1, 0.2)

# # #text stuff
# # txt = vtk.vtkTextActor()
# # txt.SetInput("Isovalue: "+str(isovalue))
# # txtprop = txt.GetTextProperty()
# # txtprop.SetFontFamilyToArial()
# # txtprop.BoldOn()
# # txtprop.SetFontSize(24)
# # txtprop.ShadowOn()
# # txtprop.SetShadowOffset(4, 4)
# # txtprop.SetColor(colors.GetColor3d("White"))
# # txt.SetDisplayPosition(20, 30)

# #Add actors to our renderer
# renderer.AddViewProp(volume)
# # renderer.AddActor(txt)
# #TODO: You'll probably need to add additional actors to the scene


# camera = renderer.GetActiveCamera()
# c = volume.GetCenter()
# camera.SetViewUp(0, 0, -1)
# camera.SetPosition(c[0], c[1] - 800, c[2])
# camera.SetFocalPoint(c[0], c[1], c[2])
# camera.Azimuth(0.0)
# camera.Elevation(90.0)

# #The render window
# renwin = vtk.vtkRenderWindow()
# renwin.SetSize(850, 850);
# renwin.AddRenderer(renderer)

# #scalarbar
# # scalebar = vtk.vtkScalarBarActor()
# # scalebar.SetLookupTable(ctf)
# # renderer.AddActor(scalebar)

# #Interactor to handle mouse and keyboard events
# interactor = vtk.vtkRenderWindowInteractor()
# #interactor.SetInteractorStyle(MyInteractorStyle(parent = interactor))
# interactor.SetRenderWindow(renwin)


# plane = vtk.vtkImplicitPlaneRepresentation();
# plane.SetPlaceFactor(1.00);
# plane.SetOrigin(0,125,125)
# plane.OutsideBoundsOn();
# plane.OutlineTranslationOff();
# plane.SetTranslationAxisOff();

# planewidget = vtk.vtkImplicitPlaneWidget2();
# planewidget.SetInteractor(interactor);
# planewidget.SetRepresentation(plane);

# interactor.Initialize()
# planewidget.On()
# interactor.Start()

