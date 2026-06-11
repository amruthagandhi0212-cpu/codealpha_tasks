import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("students.csv.xlsx")

plt.hist(df["Marks"], bins=5)

plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.savefig("histogram.png")
plt.show()