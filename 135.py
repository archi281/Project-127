import pandas as pd
import matplotlib.pyplot as plt

file_path = 'stars_data.csv'
df = pd.read_csv(file_path)

star_names = df['Star_name'].tolist()
mass_values = df['Mass'].tolist()
radius_values = df['Radius'].tolist()
distance_values = df['Distance'].tolist()
gravity_values = df['Gravity'].tolist()

def plot_bar_chart(x_values, y_values, x_label, y_label, title):
    plt.bar(x_values, y_values, color='skyblue')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.xticks(rotation=45, ha='right')
    plt.show()

plot_bar_chart(star_names, mass_values, 'Star Name', 'Mass', 'Star Name vs Mass')
plot_bar_chart(star_names, radius_values, 'Star Name', 'Radius', 'Star Name vs Radius')
plot_bar_chart(star_names, distance_values, 'Star Name', 'Distance', 'Star Name vs Distance')
plot_bar_chart(star_names, gravity_values, 'Star Name', 'Gravity', 'Star Name vs Gravity')
