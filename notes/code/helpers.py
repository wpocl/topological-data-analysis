import numpy as np

def sample_from_torus(num_points, major_radius, minor_radius):
    # Generate random angles
    theta = 2 * np.pi * np.random.rand(num_points)
    phi = 2 * np.pi * np.random.rand(num_points)

    # Calculate x, y, z coordinates on the torus
    x = (major_radius + minor_radius * np.cos(phi)) * np.cos(theta)
    y = (major_radius + minor_radius * np.cos(phi)) * np.sin(theta)
    z = minor_radius * np.sin(phi)

    return x, y, z