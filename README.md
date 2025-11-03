
# English Version
# Ho Chi Minh House Price Prediction

## 🌟 Introduction

This project focuses on **predicting house prices in Ho Chi Minh City (HCMC)** based on diverse property characteristics such as **location, area (sqm), number of rooms, legal documents**, and more.

By applying **Machine Learning** algorithms to real-world data, the model provides a useful tool to help **buyers, sellers, and analysts** make reasonable and well-informed estimations of residential property values.

---

## ✨ Key Features

* **Data Preprocessing & Normalization:** Handling, cleaning, and standardizing HCMC real estate data.
* **Factor Analysis:** Evaluating the main factors influencing house price fluctuations.
* **Model Building:** Training and comparing the performance of various price prediction algorithms.
* **Quality Assessment:** Using standard metrics (MAE, RMSE, R², etc.) to evaluate model quality.
* **Quick Prediction:** Estimating the value for new properties in just a few seconds.

---

## 🛠️ Technology & Algorithms

### 🧰 Technology

| Tool                | Description                                                                            |
| :------------------ | :-------------------------------------------------------------------------------------- |
| **Python**          | The main programming language                                                               |
| **Jupyter Notebook**| Development environment and data visualization tool                                      |
| **Libraries**       | `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`, `lazypredict`, etc.         |
| **Data**            | Dataset cloned from github :https://github.com/QuangTranUTE/Housing-Price-Prediction                                 |

---

### 🤖 Machine Learning Algorithms (Regressor)

The project implements and compares multiple prediction models:

* **Linear Models:** `Linear Regression`, `Ridge`, `Lasso`
* **Tree-Based Models:** `DecisionTreeRegressor`, `RandomForestRegressor`
* **Boosting Models:** `LightGBM (LGBMRegressor)`, `HistGradientBoostingRegressor`
* **Comprehensive Comparison:** Using `LazyRegressor` to benchmark model performance

---

## 🚀 Getting Started

Follow these steps to run and explore the project on your local machine.

### 🧩 Step 1: Clone the Repository

Use `git` to download the source code:

```bash
git clone [https://github.com/MonkeyNerdCoding/Vietnam-House-Price-Prediction.git](https://github.com/MonkeyNerdCoding/Vietnam-House-Price-Prediction.git)
cd Vietnam-House-Price-Prediction
````

### ⚙️ Step 2: Run project and Install Dependencies

Install all necessary libraries (listed in `requirements.txt`):

```bash
# Step 1 create venv
python -m venv venv         

#Step 2 activate venv
.\.venv\Scripts\Activate.ps1       # Windows

source venv/bin/activate    # macOS/Linux

#Step 3 install requirements
pip install -r requirements.txt
```

-----

## 📊 Generate Dataset (Just in case you need bigger data)

Data can be sourced from open-source repositories or simulated using the included script.

### 1️⃣ Command to run data generation with a specified number of data points

```bash
python generate_synthetic_vn_real_estate.py --count 250 --file "House_price/GiaChungCu_HCM_June2021_laydulieu_com.csv"
```

### 2️⃣ Command to run data generation with default settings

```bash
python generate_synthetic_vn_real_estate.py
```

After processing, the data is saved in the `/Complete_dataset` directory and is ready for use in the model training notebooks.

-----

============================================================================================


# Vietnamese Version
# Ho Chi Minh House Price Prediction
## 🌟 Giới thiệu

Dự án này tập trung vào việc **dự đoán giá nhà tại TP. Hồ Chí Minh** dựa trên các đặc điểm đa dạng của bất động sản như **vị trí, diện tích, số phòng, Giấy tờ**, v.v.

Bằng cách áp dụng các thuật toán **Học máy (Machine Learning)** trên dữ liệu thực tế, mô hình cung cấp một công cụ hữu ích giúp **người mua, người bán, và chuyên viên phân tích** đưa ra ước lượng hợp lý và có cơ sở về giá trị tài sản nhà ở.

---

## ✨ Tính năng nổi bật

* **Tiền xử lý & Chuẩn hóa Dữ liệu:** Xử lý, làm sạch và chuẩn hóa dữ liệu bất động sản TP. Hồ Chí Minh.
* **Phân tích Yếu tố:** Đánh giá các nhân tố chính ảnh hưởng đến biến động giá nhà.
* **Xây dựng Mô hình:** Huấn luyện và so sánh hiệu suất của nhiều thuật toán dự đoán giá khác nhau.
* **Đánh giá Chất lượng:** Sử dụng các chỉ số đo lường tiêu chuẩn (MAE, RMSE, R², v.v.) để đánh giá mô hình.
* **Dự đoán Nhanh:** Ước tính giá trị cho các bất động sản mới chỉ trong vài giây.

---

## 🛠️ Công nghệ & Thuật toán

### 🧰 Công nghệ

| Công cụ              | Mô tả                                                                           |
| :------------------- | :------------------------------------------------------------------------------ |
| **Python**           | Ngôn ngữ lập trình chính                                                        |
| **Jupyter Notebook** | Môi trường phát triển và trực quan hóa dữ liệu                                  |
| **Thư viện**         | `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`, `lazypredict`, v.v. |
| **Dữ liệu**          | Dataset clone từ github :https://github.com/QuangTranUTE/Housing-Price-Prediction               |

---

### 🤖 Thuật toán Học máy (Regressor)

Dự án triển khai và so sánh nhiều mô hình dự đoán khác nhau:

* **Mô hình Tuyến tính:** `Linear Regression`, `Ridge`, `Lasso`
* **Mô hình Dựa trên Cây:** `DecisionTreeRegressor`, `RandomForestRegressor`
* **Mô hình Boosting:** `LightGBM (LGBMRegressor)`, `HistGradientBoostingRegressor`
* **So sánh Tổng hợp:** Sử dụng `LazyRegressor` để benchmark hiệu suất mô hình

---

## 🚀 Hướng dẫn Bắt đầu

Thực hiện các bước sau để chạy và khám phá dự án trên máy tính của bạn.

### 🧩 Bước 1: Clone dự án

Sử dụng `git` để tải mã nguồn:

```bash
git clone https://github.com/MonkeyNerdCoding/Vietnam-House-Price-Prediction.git
cd Vietnam-House-Price-Prediction
```

### ⚙️ Bước 2: Chạy project và Cài đặt môi trường (Dependencies)

Cài đặt tất cả thư viện cần thiết (được liệt kê trong `requirements.txt`):

```bash
# Bước 1 tạo venv
python -m venv venv         

# Bước 2 : kích hoạt venv
.\.venv\Scripts\Activate.ps1       # Windows
source venv/bin/activate    # macOS/Linux

# Bước 3 cài đặt requirements
pip install -r requirements.txt
```

---

## 📊 Generate dataser (Just in case you need bigger data)

Dữ liệu có thể được lấy từ các nguồn mở hoặc tự sinh mô phỏng bằng script đi kèm.

### 1️⃣ Command run generate data with the number data you want 

```bash
python generate_synthetic_vn_real_estate.py --count 250 --file "House_price/GiaChungCu_HCM_June2021_laydulieu_com.csv"
```

### 2️⃣ Command run generate

```bash
python generate_synthetic_vn_real_estate.py
```

Sau khi xử lý, dữ liệu được lưu trong thư mục `/Complete_dataset` và sẵn sàng để sử dụng trong các notebook huấn luyện mô hình.

---




