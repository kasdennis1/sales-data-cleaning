import pandas as pd

df = pd.read_csv("data/broken_sales.csv")

print("DATASET INSPECTION")

print()
print("first 5 rows", df.head())

print()
print("Dataset shape", df.shape)

print()
print("columns", df.columns)

print()
print("Missing Values", df.isnull().sum())

print()
print("Data types", df.dtypes)

print()
print("Duplicates", df.duplicated())

print()
print("Dataset aggregate summary", df.describe())

print()
print("customers ", df["customer"].unique())
print("products", df["product"].unique())


print("DATASET CLEANING")

df_clean = df.copy()

# standardize customer and product names
df_clean["customer"] = df_clean["customer"].str.strip().str.title()

df_clean["product"] = df_clean["product"].str.strip().str.title()

# replace_missing_customers_sale
df_clean["customer"] = df_clean["customer"].fillna("unknown")

df_clean["sale"] = df_clean["sale"].fillna(0)

# remove_duplicates
df_clean = df_clean.drop_duplicates()

# flag_negative_sale_value
negative_sales = df_clean[df_clean["sale"] < 0]

print("NEGATIVE SALES:")
print(negative_sales)

# print_cleaned_dataset
print()
print("CLEANED DATASET")
print(df_clean)

# Business_risk_assessment
print()
print("BUSINESS RISK ASSESSMENT")

print(
    "The most critical risk identified is the negative sale transaction "
    "for David's Laptop sale of ₦-45,000. This transaction should be "
    "investigated before the dataset is used for financial reporting."
)

print(
    "The missing customer name was replaced with 'Unknown' and the "
    "missing sale value was replaced with ₦0. These records should be "
    "reviewed to determine whether the missing information can be recovered."
)

print(
    "Duplicate transactions were removed to prevent revenue from being "
    "overstated. The cleaned dataset should be validated before being "
    "used for further analysis or reporting."
)

# save_cleaned_dataset
df_clean.to_csv("data/cleaned_sales.csv", index=False)
