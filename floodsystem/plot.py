import matplotlib.pyplot as plt

def plot_water_levels(station,dates,levels):
    '''plots water level data against time including lines for typical low and high levels'''
    plt.plot(dates,levels,label = f'Station {station.name}')

    low_values = [station.typical_range[0] for _ in range(len(dates))]
    plt.plot(dates,low_values,label = "Typical low value")

    high_values = [station.typical_range[1] for _ in range(len(dates))]
    plt.plot(dates,high_values,label = "Typical high value")
    
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(f"Station {station.name}")
    plt.legend()

    plt.tight_layout()
    plt.show()
