# api/model.py

import joblib
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# بارگذاری داده‌ها
data = pd.read_csv(
    "/home/siyamak/Downloads/Meditation/Back/ML/housing_data.csv"
)  # فرض کنید داده‌ها در این فایل ذخیره شده‌اند

# جداسازی ویژگی‌ها و هدف
X = data[
    [
        "crim",
        "zn",
        "indus",
        "chas",
        "nox",
        "rm",
        "age",
        "dis",
        "rad",
        "tax",
        "ptratio",
        "b",
        "lstat",
    ]
]
y = data["medv"]


# بررسی و پر کردن مقادیر گمشده با استفاده از Imputer
imputer = SimpleImputer(strategy="mean")  # یا 'median' یا 'most_frequent'
X_imputed = imputer.fit_transform(X)  # پر کردن مقادیر گمشده در X

# تقسیم داده‌ها به مجموعه‌های آموزشی و آزمایشی
X_train, X_test, y_train, y_test = train_test_split(
    X_imputed, y, test_size=0.2, random_state=42
)

# ایجاد و آموزش مدل
model = LinearRegression()
model.fit(X_train, y_train)

# ذخیره مدل
joblib.dump(model, "boston_housing_model.pkl")
