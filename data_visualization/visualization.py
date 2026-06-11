import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel("students.csv.xlsx")

# Display first few records
print("Dataset Preview:")
print(df.head())

# -------------------------
# BAR CHART
# -------------------------
plt.figure(figsize=(8, 5))

plt.bar(df["Student"], df["Marks"])

plt.title("Student Marks Comparison")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.savefig("bar_chart.png")

plt.show()

# -------------------------
# PIE CHART
# -------------------------
plt.figure(figsize=(8, 8))

plt.pie(
    df["Marks"],
    labels=df["Student"],
    autopct="%1.1f%%"
)

plt.title("Marks Distribution")

plt.savefig("pie_chart.png")

plt.show()

# -------------------------
# HISTOGRAM
# -------------------------
plt.figure(figsize=(8, 5))

plt.hist(df["Marks"], bins=5)

plt.title("Marks Distribution Histogram")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.savefig("histogram.png")

plt.show()

print("Visualization completed successfully!")
print("Generated files:")
print("- bar_chart.png")
print("- pie_chart.png")
print("- histogram.png")
plt.pie(
    df["Marks"],
    labels=df["Student"],
    autopct="%1.1f%%"
)