import numpy as np
from pykrige.ok import OrdinaryKriging
import matplotlib.pyplot as plt
import pandas as pd

def extract_data():
    df= pd.read_csv('VN2000 - WGS84.csv')

    lats = df['WGS84 - Lat']
    lons = df['WGS84 - Long']

    df1 = pd.read_csv('output.csv')
    predic_value= df1['Predicted_Value']
    df2 = pd.read_csv("QHoa.csv")
    actual_value = df2['Giadat'] 

    lats= lats.values
    lons= lons.values
    predic_value =predic_value.values
    actual_value = actual_value.values
    error =predic_value - actual_value 
    abs_error = abs(error)
    max_error = max(abs_error)
    standard_error = error/max_error
    return lats, lons, predic_value, standard_error

def Kriging():
    lats, lons, predic_value, standard_error = extract_data()
    print("Chọn chương trình bạn muốn thực hiện:")
    print(" 1-Kriging dữ liệu giá nhà đất")
    print(" 2-Kriging dữ liệu sai số trong sử dụng mô hình Hedonic")
    print(" 3-Vẽ đồ thị dữ liệu giá nhà")
    print(" 4-Vẽ dồ thị dữ liệu sai số")
    print(" 0-Dừng chường trình")
    try: 
        choice = int(input())
        if (choice == 1):
            execute_1()
        elif (choice == 2):
            execute_2()
        elif (choice == 3):
            execute_3()
        elif (choice == 4):
            execute_4()
        elif (choice == 0):
            exit
    except Exception as e:
        print(e)

def execute_3():    #Vẽ đồ thị giá nhà dự đoán
    lats, lons, predic_value, standard_error = extract_data()
    cax = plt.scatter(lats,lons, c= predic_value)
    cbar = plt.colorbar(cax,fraction =0.03)
    plt.xlabel('Latitude')
    plt.ylabel('Longtitude')
    plt.show()
def execute_4():    #Vẽ đồ thị sai số
    lats, lons, predic_value, standard_error = extract_data()
    polar_color_scale = plt.cm.seismic
    cax = plt.scatter(lats,lons, c= standard_error, cmap = polar_color_scale, vmin=-1, vmax= 1 )
    cbar = plt.colorbar(cax,fraction =0.03)
    plt.xlabel('Latitude')
    plt.ylabel('Longtitude')
    plt.show()
def execute_1():    #kriging
    lats, lons, predic_value, standard_error = extract_data()
    print("Chọn chương trình bạn muốn thực hiện:")
    print(" 1-Kriging với mô hình exponential")
    print(" 2-Kriging với mô hình linear")
    print(" 3-Kriging với mô hình spherical")
    print(" 4-Kriging với mô hình gaussian")
    print(" 0-Dừng chường trình")
    try:
        choice = int(input())
        if (choice == 1):
            Kriging_with("exponential") 
        elif(choice == 2):
            Kriging_with("linear")
        elif(choice == 3):
            Kriging_with("spherical")
        elif(choice == 4):
            Kriging_with("gaussian")
    except Exception as e:
        print(e)

def execute_2():    #kriging
    lats, lons, predic_value, standard_error = extract_data()
    OK = OrdinaryKriging(
        lats,
        lons,
        standard_error,
        variogram_model = 'exponential',
        verbose = False,
        enable_plotting= False
    )
    min_lon = min(lons)
    min_lat = min(lats)
    max_lon = max(lons)
    max_lat = max(lats)
    grid_space = 0.0001
    grid_lon = np.arange(min_lon+0.0001,max_lon, grid_space) 
    grid_lat = np.arange(min_lat+0.0001, max_lat, grid_space)
    z_value, variance = OK.execute('grid', grid_lat, grid_lon)

    polar_color_scale = plt.cm.seismic
    cax=plt.imshow(z_value ,extent=(min_lat,max_lat, min_lon, max_lon), origin='lower', cmap = polar_color_scale, vmin= -1, vmax= 1, alpha=0.8)
    plt.scatter(lats,lons,c =standard_error, cmap= polar_color_scale, marker='.')
    cbar = plt.colorbar(cax,fraction =0.03)
    plt.title("Kriging error")
    plt.xlabel("Latitude")
    plt.ylabel("Longtitude")
    plt.show()

def Kriging_with(param):
    lats, lons, predic_value, standard_error = extract_data()
    OK = OrdinaryKriging(
        lats,
        lons,
        predic_value,
        variogram_model = param,
        verbose = False,
        enable_plotting= False
    )
    min_lon = min(lons)
    min_lat = min(lats)
    max_lon = max(lons)
    max_lat = max(lats)
    grid_space = 0.0001
    grid_lon = np.arange(min_lon+0.0001,max_lon, grid_space) 
    grid_lat = np.arange(min_lat+0.0001, max_lat, grid_space)
    z_value, variance = OK.execute('grid', grid_lat, grid_lon)

    cax=plt.imshow(z_value ,extent=(min_lat,max_lat, min_lon, max_lon), origin='lower', alpha=0.8)
    plt.scatter(lats,lons,c =predic_value, marker='x')
    cbar = plt.colorbar(cax,fraction =0.03)
    plt.title("Kriging with " + param) 
    plt.xlabel("Latitude")
    plt.ylabel("Longtitude")
    plt.show()
