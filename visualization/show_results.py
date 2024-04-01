from matplotlib import ticker
import pandas as pd
import matplotlib.pyplot as plt


if __name__ == '__main__':
    df = pd.read_csv(filepath_or_buffer='results.csv')
    grouped_data = df.groupby('measurement_degree')
    grouped_df = grouped_data.apply(lambda group: pd.Series({
        'group_size': len(group),
        'matching_spins': sum(group['first_particle_spin'] == group['second_particle_spin'])
    }))
    grouped_df['probability'] = grouped_df['matching_spins'] / grouped_df['group_size']
    # Extract the relevant data from the results DataFrame
    measurement_degrees = grouped_df.index.to_numpy()
    matching_spins = grouped_df['probability'].to_numpy()
    # Create the plot
    plt.figure(figsize=(10, 6))  # Adjust figure size if desired
    plt.plot(measurement_degrees, matching_spins)
    # Add labels and title
    plt.xlabel('Angle difference')
    plt.title('Experiment results')
    # Define the points for the linear plot
    x_linear = [0, 180, 360]
    y_linear = [0, 1, 0]
    # Add the linear plot to the existing plot
    plt.plot(x_linear, y_linear, color='black')
    # Customize x-axis grid
    ax = plt.gca()  # Get the current axis
    ax.xaxis.set_major_locator(ticker.MultipleLocator(30))  # Set major ticks every 30 units
    # Show the plot
    plt.grid(True, color='grey')  # Add a grid for clarity
    plt.show()
