import numpy as np
import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt
def extractData():
  df= pd.read_csv('Tuongquan.csv')
  X = df[['Dien_tich','Vi_tri', 'Giaitri']]
  data_array =X.values
  actual_value= df['Giadat']
  
  df1 = pd.read_csv('DuLieu_QuanHoa.csv')
  X_value = df1[['Dien_tich','Vi_tri', 'Giaitri']]
  Y_value = df1['Giadat']
  return X_value, Y_value, data_array, actual_value

def hedonicPrice():          
  X_value, Y_value, data_array, actual_value = extractData()
  x_train = pd.DataFrame({
     'Dien_tich' : X_value['Dien_tich'],
     'Vi_tri': X_value['Vi_tri'],
     'Giaitri': X_value["Giaitri"]
  })
  y_train = Y_value
  regr = linear_model.LinearRegression()
  regr.fit(x_train, y_train)

  coef =regr.coef_
  intercept = regr.intercept_
  print("Hệ số chặn: " , intercept)
  print("Hệ số hồi quy: ",coef)
  

def histogram():
  X_value, Y_value, data_array, actual_value = extractData()
  regr = linear_model.LinearRegression()
  regr.fit(X_value, Y_value)
  y_pred = 0
  predict_value = []
  for item in data_array:
      y_pred = regr.predict([item])
      predict_value.append(y_pred[0])
  error = np.array(actual_value.values)- np.array(predict_value)
  #Vẽ Histogram

  print("Chọn chương trình bạn muốn thực hiện:")
  print(" 1-Vẽ biểu đồ giá trị dự đoán")
  print(" 2-vẽ biểu đồ giá trị sai số")
  print(" 0-Dừng chường trình")
  try: 
    choice = int(input())
    if (choice == 1):
      plt.figure(figsize=(10, 5))
      plt.subplot(1, 2, 1)
      plt.hist(predict_value, color='blue', alpha=0.7, edgecolor = "black")
      plt.title('Histogram of predict value')
      plt.xlabel('Predict values')
      plt.ylabel('Quantity')
      plt.show()
    elif (choice == 2):
      plt.figure(figsize=(10, 5))
      plt.subplot(1, 2, 1)
      plt.hist(error, color='blue', alpha=0.7, edgecolor = "black")
      plt.title('Histogram of error value')
      plt.xlabel('Error')
      plt.ylabel('Quantity')
      plt.show()
    elif (choice == 0):
      exit
  except Exception as e:
        print(e)  
  #output_df = pd.DataFrame({ 'Predicted_Value': predict_value})
  # Lưu DataFrame vào file CSV
  #output_df.to_csv('output.csv', index=False)
  """
  - Hàm LinearRegression() được sử dụng để xây dựng mô hình hồi quy tuyến tính.
    Mô hình hồi quy tuyến tính được sử dụng để dự đoán một biến mục tiêu liên tục dựa trên các biến độc lập có liên quan.
  B1: Khi tạo một đối tượng mô hình hồi quy tuyến tính cú pháp: "model =Linear.Regression()"
  B2: Sử dụng phương thức ".fit()" để huấn luyện mô hình dựa trên dữ liệu đầu vào và biến mục tiêu y
      "model.fit(X,y)"
  B3: Sử dụng phương thức '.predict()' để dự đoán  giá trị biến mục tiêu dựa trên dữ liệu mới

  """