from hedonicRegression import hedonicPrice,histogram 
from kriging import Kriging
def choose():   
    print("Chọn chương trình bạn muốn thực hiện:")
    print(" 1-Chạy chương trình Hedonic pricing model")
    print(" 2-Vẽ biểu đồ từ mô hình Hedonic")
    print(" 3-Thực hiện Kriging")
    print(" 0-Dừng chường trình")
    try: 
        choice = int(input())
        if (choice == 1):
            execute_1()
        elif (choice == 2):
            execute_2()
        elif (choice == 3):
            execute_3()
        elif (choice == 0):
            exit
    except Exception as e:
        print(e)

def execute_1():
    hedonicPrice()
    choose()
def execute_2():
    histogram()
    choose()
def execute_3():
    Kriging()
    choose()

choose()