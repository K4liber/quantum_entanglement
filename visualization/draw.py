import sys
import vtk

from common.constants import (
    plane_half_length,
    particle_1_center,
    particle_2_center
)
from common.functions import (
    get_arrow,
    get_measurement_plane,
    is_spin_up
)

static_scene = False

def get_sphere(center: tuple[float, float, float], radius: float) -> vtk.vtkActor:
    sphere = vtk.vtkSphereSource()
    sphere.SetCenter(center)
    sphere.SetRadius(radius)
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(sphere.GetOutputPort())
    sphere_actor = vtk.vtkActor()
    sphere_actor.GetProperty().SetOpacity(0.1)
    sphere_actor.SetMapper(mapper)
    return sphere_actor


def get_plane() -> vtk.vtkActor:
    plane_source = vtk.vtkPlaneSource()
    plane_source.SetOrigin(-plane_half_length, -plane_half_length, 0)
    plane_source.SetPoint1(plane_half_length, -plane_half_length, 0)
    plane_source.SetPoint2(-plane_half_length, plane_half_length, 0)
    plane_source.SetXResolution(10)
    plane_source.SetYResolution(10)
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(plane_source.GetOutputPort())
    plane_actor = vtk.vtkActor()
    plane_actor.SetMapper(mapper)
    plane_actor.GetProperty().SetColor(0.8, 0.8, 0.8)
    plane_actor.GetProperty().SetOpacity(0.5) 
    return plane_actor


def get_grid() -> vtk.vtkAxesActor:
    transform = vtk.vtkTransform()
    transform.Translate(-plane_half_length, -plane_half_length, 0)
    grid = vtk.vtkAxesActor()
    grid.SetUserTransform(transform)
    grid.SetXAxisLabelText("X")
    grid.SetYAxisLabelText("Y")
    grid.SetZAxisLabelText("Z")
    grid.SetShaftTypeToCylinder()
    # Change axis colors
    grid.GetXAxisTipProperty().SetColor(0.5, 0.5, 0.5)
    grid.GetXAxisShaftProperty().SetColor(0.5, 0.5, 0.5)
    grid.GetYAxisTipProperty().SetColor(0.5, 0.5, 0.5)
    grid.GetYAxisShaftProperty().SetColor(0.5, 0.5, 0.5)
    grid.GetZAxisTipProperty().SetColor(0.5, 0.5, 0.5)
    grid.GetZAxisShaftProperty().SetColor(0.5, 0.5, 0.5)
    ax_length = 2
    grid.SetTotalLength(ax_length, ax_length, ax_length)
    return grid


class ArrowInteractorStyle(vtk.vtkInteractorStyleTrackballActor):

    def __init__(self, renderer, arrow):
        self.AddObserver("LeftButtonPressEvent", self.leftButtonPressEvent)
        self.renderer = renderer
        self.arrow: vtk.vtkActor = arrow

    def leftButtonPressEvent(self, obj, event):
        clickPos = self.GetInteractor().GetEventPosition()
        picker = vtk.vtkCellPicker()
        picker.Pick(clickPos[0], clickPos[1], 0, self.renderer)
        self.click_position = picker.GetPickPosition()
        print(self.click_position)



def draw(
    spin_alpha_degree: float = 0,
    spin_theta_degree: float = 0,
    measurement_angle: float = 0
):
    # create render window
    render_window = vtk.vtkRenderWindow()
    render_window.SetSize(render_window.GetScreenSize())
    # create a renderer
    renderer = vtk.vtkRenderer()
    # create an interactor
    renderWindowInteractor = vtk.vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(render_window)

    if static_scene:
        interactor_style = ArrowInteractorStyle(renderer, None)
        renderWindowInteractor.SetInteractorStyle(interactor_style)
    # add renderer
    render_window.AddRenderer(renderer)
    # create actors
    sphere_radius = 1
    sphere1 = get_sphere(center=particle_1_center, radius=sphere_radius)
    sphere2 = get_sphere(center=particle_2_center, radius=sphere_radius)
    arrow_first, arrow_first_tip_coords = get_arrow(
        center=particle_1_center,
        spin_alpha_degree=spin_alpha_degree,
        spin_theta_degree=spin_theta_degree
    )
    arrow_second, arrow_second_tip_coords = get_arrow(
        center=particle_2_center,
        spin_alpha_degree=spin_alpha_degree,
        spin_theta_degree=spin_theta_degree,
        rotate_z=True
    )
    print(f'Particle 1 center: {particle_1_center}')
    print(f'Particle 2 center: {particle_2_center}')
    print(f'Particle 1 tip coords: {arrow_first_tip_coords}')
    print(f'Particle 2 tip coords: {arrow_second_tip_coords}')
    plane_actor = get_plane()
    grid_actor = get_grid()
    measurement_plane_first, measurement_plane_first_coefficients = get_measurement_plane(
        center=particle_1_center
    )
    measurement_plane_second, measurement_plane_second_coefficients = get_measurement_plane(
        center=particle_2_center, xz_degree=measurement_angle
    )

    if is_spin_up(
        tip_coords=arrow_first_tip_coords,
        measurement_plane_coefficients=measurement_plane_first_coefficients
    ):
        arrow_first.GetProperty().SetColor(1.0, 0.0, 0.0)
    else:
        arrow_first.GetProperty().SetColor(0.0, 0.0, 1.0)

    if is_spin_up(
        tip_coords=arrow_second_tip_coords,
        measurement_plane_coefficients=measurement_plane_second_coefficients
    ):
        arrow_second.GetProperty().SetColor(1.0, 0.0, 0.0)
    else:
        arrow_second.GetProperty().SetColor(0.0, 0.0, 1.0)

    # add actors
    renderer.AddActor(sphere1)
    renderer.AddActor(sphere2)
    renderer.AddActor(arrow_first)
    renderer.AddActor(arrow_second)
    renderer.AddActor(plane_actor)
    renderer.AddActor(grid_actor)
    renderer.AddActor(measurement_plane_first)
    renderer.AddActor(measurement_plane_second)
    renderer.SetBackground(0.2, 0.2, 0.2)
    # Set camera position
    camera = renderer.GetActiveCamera()
    camera.SetPosition(4, 10, 4)
    camera.SetViewUp(0, 0, 1)
    # Start the rendering
    render_window.Render()
    renderWindowInteractor.Start()


if __name__ == '__main__':
    spin_alpha_degree = float(sys.argv[1]) if len(sys.argv) > 1 else 0
    spin_theta_degree = float(sys.argv[2]) if len(sys.argv) > 2 else 0
    measurement_angle = float(sys.argv[3]) if len(sys.argv) > 3 else 0
    print(f'Alpha = {spin_alpha_degree}')
    print(f'Theta = {spin_theta_degree}')   
    draw(
        spin_alpha_degree=spin_alpha_degree,
        spin_theta_degree=spin_theta_degree,
        measurement_angle=measurement_angle
    )
