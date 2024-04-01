import vtk

from common.constants import measurement_plane_length


def is_spin_up(
        tip_coords: tuple[float, float, float],
        measurement_plane_coefficients: tuple[float, float, float, float]
) -> bool:
    A, B, C, D = measurement_plane_coefficients
    result = A * tip_coords[0] + B * tip_coords[1] + C * tip_coords[2] + D
    return result > 0


def get_arrow(
        center: tuple[float, float, float],
        spin_alpha_degree: float = 0,
        spin_theta_degree: float = 0,
        rotate_z: bool = False
    ) -> tuple[vtk.vtkActor, tuple[float, float, float]]:
    arrow_source = vtk.vtkArrowSource()
    arrow_source.SetTipLength(0.3)  # Adjust arrow size 
    arrow_source.SetShaftRadius(0.05)  # Adjust arrow size
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(arrow_source.GetOutputPort())
    arrow_actor = vtk.vtkActor()
    arrow_actor.SetMapper(mapper)
    arrow_source.Update()
    # Original tip is pointing along x-axis
    original_tip = (1, 0, 0)
    # Create a transform to apply the rotations
    transform = vtk.vtkTransform()
    transform.Translate(center)
    transform.RotateX(spin_alpha_degree)
    transform.RotateZ(spin_theta_degree)

    if rotate_z:
        transform.RotateZ(180)

    arrow_actor.SetUserTransform(transform)
    # Apply the transform to the original tip coordinates
    transform_filter = vtk.vtkTransformPolyDataFilter()
    transform_filter.SetTransform(transform)
    point_data = vtk.vtkPolyData()
    points = vtk.vtkPoints()
    points.InsertNextPoint(original_tip)
    point_data.SetPoints(points)
    transform_filter.SetInputData(point_data)
    transform_filter.Update()
    tip_coords = transform_filter.GetOutput().GetPoint(0)
    return arrow_actor, tip_coords


def get_measurement_plane(
        center: tuple[float, float, float],
        xz_degree: float = 0
    ) -> tuple[vtk.vtkActor, tuple[float, float, float, float]]:
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
    plane_source.Update()
    # Calculate plane coefficients (Ax + By + Cz + D = 0)
    normal = plane_source.GetNormal()
    origin = plane_source.GetOrigin()
    A, B, C = normal
    D = -(A * origin[0] + B * origin[1] + C * origin[2])
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(plane_source.GetOutputPort())
    plane_actor = vtk.vtkActor()
    plane_actor.SetMapper(mapper)
    plane_actor.GetProperty().SetColor(0, 0, 0.8)
    plane_actor.GetProperty().SetOpacity(0.5)
    return plane_actor, (A, B, C, D)
