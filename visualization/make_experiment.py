from collections import defaultdict
import random
from typing import Any

import pandas as pd

from common.constants import (
    DO_2D_ROTATION,
    PARTICLE_1_CENTER,
    PARTICLE_2_CENTER
)
from common.functions import (
    get_arrow,
    get_measurement_plane,
    is_spin_up
)


def perform_single_test(
    spin_alpha_degree: float,
    spin_theta_degree: float | None,
    results_dict: dict[str, list[Any]]
) -> None:
    _, arrow_first_tip_coords = get_arrow(
        center=PARTICLE_1_CENTER,
        spin_alpha_degree=spin_alpha_degree,
        spin_theta_degree=spin_theta_degree
    )
    _, arrow_second_tip_coords = get_arrow(
        center=PARTICLE_2_CENTER,
        spin_alpha_degree=spin_alpha_degree,
        spin_theta_degree=spin_theta_degree,
        rotate_z=True
    )
    _, measurement_plane_first_coefficients = get_measurement_plane(
        center=PARTICLE_1_CENTER
    )
    _, measurement_plane_second_coefficients = get_measurement_plane(
        center=PARTICLE_2_CENTER,
        xz_degree=measurement_degree
    )
    first_particle_spin = is_spin_up(
        tip_coords=arrow_first_tip_coords,
        measurement_plane_coefficients=measurement_plane_first_coefficients
    )
    second_particle_spin = is_spin_up(
        tip_coords=arrow_second_tip_coords,
        measurement_plane_coefficients=measurement_plane_second_coefficients
    )
    results_dict['spin_alpha_degree'].append(spin_alpha_degree)
    results_dict['spin_theta_degree'].append(spin_theta_degree)
    results_dict['measurement_degree'].append(measurement_degree)
    results_dict['first_particle_spin'].append(first_particle_spin)
    results_dict['second_particle_spin'].append(second_particle_spin)
 

if __name__ == '__main__':
    no_experiments_per_degree = 10000
    output_file = 'results.csv'
    df = pd.DataFrame(
        columns=[
            'spin_alpha_degree',
            'spin_theta_degree',
            'measurement_degree',
            'first_particle_spin',
            'second_particle_spin'
        ]
    )

    for measurement_degree in range(37):
        measurement_degree = measurement_degree * 10
        print(f'Runs for angle = {measurement_degree} degree')
        results_dict = defaultdict(list)

        for _ in range(no_experiments_per_degree):
            spin_alpha_degree = random.random() * 360

            if DO_2D_ROTATION:
                spin_theta_degree = None
            else:
                spin_theta_degree = random.random() * 360
            
            perform_single_test(
                spin_alpha_degree=spin_alpha_degree,
                spin_theta_degree=spin_theta_degree,
                results_dict=results_dict
            )

        df_new = pd.DataFrame.from_dict(results_dict)
        df = pd.concat([df, df_new], ignore_index=True)

    df.to_csv(output_file)
