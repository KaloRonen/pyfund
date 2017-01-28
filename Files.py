import sys
import pandas as pd

sensor_positions = pd.read_table("C:\Code\Data\sensors_position_data_file.txt", sep='\s+', header=None, names=["x", "y"])
sensor_heat_data = pd.read_table("C:\Code\Data\sensors_heat_data_file.txt", sep='\s+', header=None)

all_data = sensor_positions.add(sensor_heat_data, fill_value=0)
print(all_data)
print("OREN")


def main(filename):
    f = open(filename, mode='rt', encoding='utf-8')
    for line in f.readlines():
        sys.stdout.write(line)
    f.close()




if __name__ == 'main':
    main(sys.argv[1])
