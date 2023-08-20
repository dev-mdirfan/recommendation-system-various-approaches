import pandas as pd

# data = pd.read_csv("static/data/flipkart_com-ecommerce_sample.csv", na_values=["No rating available"])
# data = data.to_html(classes='data', header="true")
# # print(data)

'''
Remove duplicate rows from a DataFrame
'''
# data = pd.read_csv("static/data/autocomplete.csv", na_values=["No rating available"])
# data.drop_duplicates(subset=None, inplace=True)
# data.to_csv("static/data/autocomplete.csv", index=False)

'''
Displaying about of Datasets on website
'''

# about = pd.read_csv("static/data/flipkart_com-ecommerce_sample.csv", na_values=["No rating available"])
# rows = about.shape[0]
# columns = about.shape[1]
# print(rows, columns)

'''
exporting suggestion data to csv file for content Based
'''

# suggestData = pd.read_csv("./static/data/flipkart_com-ecommerce_sample.csv", na_values=["No rating available"])
# suggestData = suggestData['product_name']
# suggestData = suggestData.drop_duplicates()
# # to csv
# suggestData.to_csv("./static/data/autocomplete_content.csv", index=False)



'''
exporting suggestion data to csv file for collaborative filtering
'''

# data = pd.read_csv("./static/data/ratings_electronics.csv", names=['userId', 'productId','Rating','timestamp'])
# data = data.iloc[:1048576, 0:]
# data = data.groupby("productId").filter(lambda x:x['Rating'].count() >=50)
# data = data.head(10000)
# # taking product id only
# product_id = data['productId']
# # remove duplicate product id
# product_id = product_id.drop_duplicates()
# #  to csv
# product_id.to_csv("./static/data/autocomplete_collaborative.csv", index=False)


'''
exporting suggestion data to csv file for hybrid filtering
'''

# data = pd.read_csv("./static/data/ratings_electronics.csv", names=['userId', 'productId','Rating','timestamp'])
# # taking only user id
# user_id = data['userId']
# # remove duplicate user id
# user_id = user_id.drop_duplicates()
# #  to csv
# user_id.to_csv("./static/data/autocomplete_hybrid.csv", index=False)

# data = pd.read_csv("./static/data/ratings_electronics.csv", names=['userId', 'productId','Rating','timestamp'])
# # taking only product id
# product_id = data['productId']
# # remove duplicate product id
# product_id = product_id.drop_duplicates()
# #  to csv
# product_id.to_csv("./static/data/autocomplete_hybrid2.csv", index=False)









