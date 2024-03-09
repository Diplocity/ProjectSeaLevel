import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Importing the data
df = pd.read_csv("epa-sea-level.csv")

# Creating scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], alpha=0.7)

# Getting slope and y-intercept of the line of best fit
slope, intercept, _, _, _ = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])

# Plotting the line of best fit through the year 2050
plt.plot(df["Year"], slope * df["Year"] + intercept, color="red", label="Line of Best Fit")

# Getting data from year 2000 onwards
df_recent = df[df["Year"] >= 2000]

# Getting slope and y-intercept of the line of best fit from year 2000 onwards
slope_recent, intercept_recent, _, _, _ = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])

# Plotting the line of best fit from year 2000 onwards through the year 2050
plt.plot(df_recent["Year"], slope_recent * df_recent["Year"] + intercept_recent, color="green", label="Line of Best Fit (2000 onwards)")

# Adding labels and title
plt.xlabel("Year")
plt.ylabel("Sea Level (inches)")
plt.title("Rise in Sea Level")

# Adding legend
plt.legend()

# Saving and showing the plot
plt.savefig("sea_level_prediction.png")
plt.show()

    # Create first line of best fit


    # Create second line of best fit


    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()