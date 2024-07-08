# Write a Python program to merge 2 Data Frames.
# The 2 Data Frames to be merged are given as part of the template code
# Print the First Data Frame
# Print the Second Data Frame
# Merge the 2 Data Frames and rearrange the columns in the order student_name , department , sem1_cgpa, sem2_cgpa
# Print the entire contents of the merged Data Frame

import pandas as pd

df1 = pd.DataFrame([["Anitha",7.8,8.9], ["Baskar",5.6,6.9]], columns = ["student_name","sem1_cgpa", "sem2_cgpa"])
df2 = pd.DataFrame([["Anitha","CSE"], ["Baskar","IT"]], columns = ["student_name","department"])

print("DataFrame1")

print(df1)

print("DataFrame2")

print(df2)

merged_df = pd.merge(df1, df2, on = "student_name")

merged_df = merged_df[["student_name", "department", "sem1_cgpa", "sem2_cgpa"]]

print("Merged DataFrame")

print(merged_df)
