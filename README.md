python .\generate_synthetic_vn_real_estate.py --count 250 --file "House_price\GiaChungCu_HCM_June2021_laydulieu_com.csv"


python .\generate_synthetic_vn_real_estate.py --count 250 --file "House_price\GiaChungCu_HCM_June2021_laydulieu_com.csv"

python .\generate_synthetic_vn_real_estate.py


1952
Dự án này tập trung vào việc **dự đoán giá nhà tại Việt Nam** dựa trên các đặc điểm đa dạng của bất động sản như **vị trí, diện tích, số phòng, tiện nghi**, v.v.

Bằng cách áp dụng các thuật toán **Học máy (Machine Learning)** trên dữ liệu thực tế, mô hình cung cấp một công cụ hữu ích giúp **người mua, người bán, và chuyên viên phân tích** đưa ra ước lượng hợp lý và có cơ sở về giá trị tài sản nhà ở.

---

## ✨ Tính năng nổi bật

* **Tiền xử lý & Chuẩn hóa Dữ liệu:** Xử lý, làm sạch và chuẩn hóa dữ liệu bất động sản Việt Nam.
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

### ⚙️ Bước 2: Cài đặt phụ thuộc

Cài đặt tất cả thư viện cần thiết (được liệt kê trong `requirements.txt`):

```bash
pip install -r requirements.txt
```

---

## 📊 Generate dataser (Just in case you need bigger data)

Dữ liệu có thể được lấy từ các nguồn mở hoặc tự sinh mô phỏng bằng script đi kèm.

### 1️⃣ Sinh dữ liệu từ tệp có sẵn

```bash
python generate_synthetic_vn_real_estate.py --count 250 --file "House_price/GiaChungCu_HCM_June2021_laydulieu_com.csv"
```

### 2️⃣ Sinh dữ liệu tổng hợp (mặc định)

```bash
python generate_synthetic_vn_real_estate.py
```

Sau khi xử lý, dữ liệu được lưu trong thư mục `/Complete_dataset` và sẵn sàng để sử dụng trong các notebook huấn luyện mô hình.

---



