import pandas as pd
import json
pre_df = pd.read_csv("static/data/flipkart_com-ecommerce_sample.csv", na_values=["No rating available"])
# print(pre_df.shape)
product_category_tree = pre_df["product_category_tree"]
product_name = pre_df["product_name"]

# # Applying lambda function to product_category_tree column to remove the square brackets
# product_category_tree = product_category_tree.apply(lambda x: x.strip("[]"))
# # Applying lambda function to product_category_tree column to remove the double quotes
# product_category_tree = product_category_tree.apply(lambda x: x.strip('""'))

# print(product_category_tree[0].split(" >> "))

# #  Applying lambda function to all rows of product_category_tree column
# product_category_tree = product_category_tree.apply(lambda x: x.split(" >> "))

# print(product_category_tree)

# Addong aother column to store the length of the list of categories
# pre_df["category_count"] = product_category_tree.apply(lambda x: len(x))

# print the rows and cols dataframe
# print(pre_df.shape)

# write a funtion to add a column which has all the splited categories of product_category_tree column

# def get_category(x, index):
#     try:
#         return x[index]
#     except:
#         return None

# print(get_category(product_category_tree[0], 0))

# for i in range(0, 6):
#     pre_df["category_" + str(i)] = product_category_tree.apply(lambda x: get_category(x, i))

# print(pre_df.shape)

# Write a function to add only one new colum which has all the splited categories of product_category_tree column

# def get_category(x, index):
#     try:
#         return x[index]
#     except:
#         return None

# def add_category(df, index):
#     df["category_" + str(index)] = product_category_tree.apply(lambda x: get_category(x, index))
#     return df

# for i in range(0, 6):
#     pre_df = add_category(pre_df, i)

# print(pre_df.shape)

# def cleanify(x):
#     try:
#         return x.strip("[]").strip('""').split(" >> ")
#     except:
#         return None

# def get_category(x, index):
#     try:
#         return x[index]
#     except:
#         return None


# pre_df["all_category"] = pre_df["product_category_tree"].apply(lambda x: cleanify(x))
# all_categories = pre_df["all_category"]
# droping all the columns except product_name and all_category
pre_df = pre_df.drop(["pid", "product_url", "product_rating", "overall_rating", "product_specifications", 'uniq_id', 'crawl_timestamp', 'retail_price', 'discounted_price', 'image', 'is_FK_Advantage_product', 'description', 'brand', "product_name"], axis=1)

# for i in range(0, 6):
    # pre_df["category"] = all_categories.apply(lambda x: get_category(x, i))
# print(all_categories)
# print(pre_df["category"])
# print(pre_df.columns)


# print(pre_df.columns.values)



# print(pre_df.shape)

# Importing pandas package
# import pandas as pd

# Importing display attribute from Ipython
# from IPython.display import display

# Creating a dictionary
# d = {
#     "Product_id":[1,3,7],
#     "Product_code":["#101,#102,#103","#104","#105,#106"],
#     "Manufacturing_date":["22/6/2018","21/8/2019","27/11/2020"],
#     "Cities":["c1,c2,c3","c4","c5,c6"]
# }

# Creating a DataFrame
# df = pd.DataFrame(d)

# Display Original DataFrames
# print("Created DataFrame:\n",df,"\n")

print(pre_df.columns.values)

# splitting cities column
res = pre_df.apply(lambda x: x.str.split(' >> ').explode())
# res = pre_df["product_category_tree"].apply(lambda x: x.strip("[]").strip('""').split(" >> ")).reset_index()
res = res["product_category_tree"].apply(lambda x: x.strip('["')).reset_index()
res = res["product_category_tree"].apply(lambda x: x.strip('"]')).reset_index()
# res = res.to_string(index=False)
# Display result
res = res.drop(["index"], axis=1)
print("Result:\n",res)
print(res.columns.values)
# converting into a csv for further use
res.to_csv("static/data/autocomplete.csv", index=False)














# print(product_category_tree[1])

# converting product_category_tree to jason format
# product_category_tree = product_category_tree.to_json(orient='records')


# spliting the product_category_tree column into list of categories using >> seperator store all in list
# product_category_tree = [i.split(" >> ") for i in product_category_tree]
# Jasonfy the data
# product_category_tree = json.dumps(product_category_tree)
# product_name = json.dumps(product_name)

# print(product_category_tree[0])
# print(product_category_tree[1])
# print(product_name[0].split(">>"))



