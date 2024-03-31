import sys
import vtk

plane_length = 8
measurement_plane_length = 2.5
plane_half_length = plane_length / 2
particle_1_center = (-1.5, 0, 0)
particle_2_center = (1.5, 0, 0)
static_scene = True

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


def get_arrow(
        center: tuple[float, float, float],
        spin_alpha_degree: float = 0,
        spin_theta_degree: float = 0
    ) -> vtk.vtkActor:
    arrow_source = vtk.vtkArrowSource()
    arrow_source.SetTipLength(0.3)  # Adjust arrow size 
    arrow_source.SetShaftRadius(0.05)  # Adjust arrow size
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(arrow_source.GetOutputPort())
    arrow_actor = vtk.vtkActor()
    arrow_actor.SetMapper(mapper)
    arrow_actor.SetPosition(center)
    # rotate based on args
    arrow_actor.RotateX(spin_alpha_degree)
    arrow_actor.RotateZ(spin_theta_degree)
    return arrow_actor


def get_measurement_plane(
        center: tuple[float, float, float],
        xz_degree: float = 0
    ) -> vtk.vtkActor:
    plane_source = vtk.vtkPlaneSource()
    measurement_plane_length_half = measurement_plane_length/2
    plane_source.SetOrigin(
        center[0] - measurement_plane_length_half,
        center[1] - measurement_plane_length_half,
        0
    )
    plane_source.SetPoint1(
        center[0] + measurement_plane_length_half,
        center[1] - measurement_plane_length_half,
        0
    )
    plane_source.SetPoint2(
        center[0] - measurement_plane_length_half,
        center[1] + measurement_plane_length_half,
        0
    )
    plane_source.SetXResolution(10)
    plane_source.SetYResolution(10)
    plane_source.Rotate(xz_degree, (0, 1, 0))
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(plane_source.GetOutputPort())
    plane_actor = vtk.vtkActor()
    plane_actor.SetMapper(mapper)
    plane_actor.GetProperty().SetColor(0, 0, 0.8)
    plane_actor.GetProperty().SetOpacity(0.5)
    return plane_actor


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
    spin_theta_degree: float = 0
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
    arrow1 = get_arrow(
        center=particle_1_center,
        spin_alpha_degree=spin_alpha_degree,
        spin_theta_degree=spin_theta_degree
    )
    arrow2 = get_arrow(
        center=particle_2_center,
        spin_alpha_degree=spin_alpha_degree,
        spin_theta_degree=spin_theta_degree
    )
    arrow2.RotateZ(180)  # Opposite orientation for singlet representation
    plane_actor = get_plane()
    grid_actor = get_grid()
    measurment_place_particle_1 = get_measurement_plane(center=particle_1_center)
    measurment_place_particle_2 = get_measurement_plane(center=particle_2_center, xz_degree=30)
    # add actors
    renderer.AddActor(sphere1)
    renderer.AddActor(sphere2)
    renderer.AddActor(arrow1)
    renderer.AddActor(arrow2)
    renderer.AddActor(plane_actor)
    renderer.AddActor(grid_actor)
    renderer.AddActor(measurment_place_particle_1)
    renderer.AddActor(measurment_place_particle_2)
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
    draw(
        spin_alpha_degree=spin_alpha_degree,
        spin_theta_degree=spin_theta_degree
    )
