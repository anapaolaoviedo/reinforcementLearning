import numpy as np

# first 
data = {
    'diametro_cm': [3.88, 4.09, 3.92, 3.97, 4.02, 3.92, 4.03, 3.92, 3.98, 4.96],
    'altura_cm': [27.32, 28, 28.14, 27.45, 27.90, 27.88, 27.40, 28.03, 27.95, 27.42],
    'masa_g': [159.2, 158.6, 158.1, 159.6, 159, 158.4, 158.3, 158.8, 159.2, 158.9],
    'temperatura_C': [28.2, 28.3, 28.3, 27.9, 27.8, 28.5, 28.2, 27.8, 27.3, 28.6]
}

# Convert the dictionary to an array for easier calculation
diameters = np.array(data['diametro_cm'])
heights = np.array(data['altura_cm'])

# Calculate the volume for each bottle using the formula for the volume of a cylinder
# V = πr^2h where r is radius (diameter / 2) and h is height
radii = diameters / 2
volumes_cm3 = np.pi * (radii ** 2) * heights

# Convert volumes to liters (1cm^3 = 1mL; 1000mL = 1L)
volumes_l = volumes_cm3 / 1000

# Calculate average volume
average_volume_l = np.mean(volumes_l)

# Calculate absolute error as standard deviation of the volumes
absolute_error_l = np.std(volumes_l)

# Calculate relative error (as a percentage)
relative_error_percentage = (absolute_error_l / average_volume_l) * 100

# Print out all the results
print(average_volume_l, absolute_error_l, relative_error_percentage, volumes_l)
