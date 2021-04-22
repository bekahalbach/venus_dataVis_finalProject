# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 22:20:57 2021

@author: bekah
"""
import vtk 
colors = vtk.vtkNamedColors()

file_name="./map.vti"
reader = vtk.vtkXMLImageDataReader()
reader.SetFileName(file_name)

dims = reader.GetOutput().GetDimensions()
print(reader.GetClassName())
print("Dimensions of image: " + str(dims[0]) + " x "
      + str(dims[1]) + " x " + str(dims[2]))
range = reader.GetOutput().GetScalarRange();
print("Range of image: " + str(range[0]) + " to " +  str(range[1]))

# Create the mapper that creates graphics elements
mapper = vtk.vtkDataSetMapper()
mapper.SetInputConnection(reader.GetOutputPort())

# Create the Actor
actor = vtk.vtkActor()
actor.SetMapper(mapper)
# show the edges of the image grid
actor.GetProperty().SetRepresentationToWireframe()

# Create the Renderer
renderer = vtk.vtkRenderer()
renderer.AddActor(actor)
renderer.ResetCamera()
renderer.SetBackground(colors.GetColor3d('Silver'))

# Create the RendererWindow
renderer_window = vtk.vtkRenderWindow()
renderer_window.AddRenderer(renderer)
renderer_window.SetWindowName('ReadImageData')

# Create the RendererWindowInteractor and display the vti file
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(renderer_window)
interactor.Initialize()
interactor.Start()
