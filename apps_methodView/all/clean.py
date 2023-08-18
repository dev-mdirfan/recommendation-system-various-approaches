import pandas as pd

'''
Remove duplicate rows from a DataFrame
'''
# data = pd.read_csv("static/data/autocomplete.csv", na_values=["No rating available"])
# data.drop_duplicates(subset=None, inplace=True)
# data.to_csv("static/data/autocomplete.csv", index=False)

'''
Displaying about of Datasets on website
'''

about = pd.read_csv("static/data/flipkart_com-ecommerce_sample.csv", na_values=["No rating available"])
rows = about.shape[0]
columns = about.shape[1]
print(rows, columns)








# data = pd.read_csv("static/data/flipkart_com-ecommerce_sample.csv", na_values=["No rating available"])
# data = data.to_html(classes='data', header="true")
# # print(data)





