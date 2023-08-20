'''
    Collaborative Filtering
'''

try:
    import numpy as np # linear algebra
    import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
    import os
    from IPython.core.interactiveshell import InteractiveShell
    InteractiveShell.ast_node_interactivity = "all"
    import math
    import json
    import time
    import matplotlib.pyplot as plt
    import seaborn as sns
    from sklearn.metrics.pairwise import cosine_similarity
    from sklearn.model_selection import train_test_split
    from sklearn.neighbors import NearestNeighbors
    # from sklearn.externals import joblib
    # import sklearn.external.joblib as extjoblib
    import joblib
    import scipy.sparse
    from scipy.sparse import csr_matrix
    from scipy.sparse.linalg import svds
    import warnings; warnings.simplefilter('ignore')
    # %matplotlib inline
    for dirname, _, filenames in os.walk('./data/'):
        for filename in filenames:
            print(os.path.join(dirname, filename))
except Exception as e:
    print("Some Modules are Missing {}".format(e))

class Collaborative:
    def __init__(self):
        pass

    def preprocess(self):
        self.electronics_data=pd.read_csv("static/data/ratings_electronics.csv", names=['userId', 'productId','Rating','timestamp'])
        #Taking subset of the dataset
        self.electronics_data = self.electronics_data.iloc[:1048576, 0:]

        #Find the minimum and maximum ratings
        # print('Minimum rating is: %d' %(electronics_data.Rating.min()))
        # print('Maximum rating is: %d' %(electronics_data.Rating.max()))

        # Check the distribution of the rating
        # with sns.axes_style('white'):
        # #     g = sns.factorplot("Rating", data=electronics_data, aspect=2.0,kind='count')     ### Deprecated
        #     g = sns.catplot(x="Rating", data=electronics_data, aspect=2.0, kind='count')
        #     g.set_ylabels("Total number of ratings")
        #     print("Total data ")
        # print("-"*50)
        # print("\nTotal no of ratings :",electronics_data.shape[0])
        # print("Total No of Users   :", len(np.unique(electronics_data.userId)))
        # print("Total No of products  :", len(np.unique(electronics_data.productId)))

    def cleaning(self):
        #Dropping the Timestamp column
        self.electronics_data.drop(['timestamp'], axis=1,inplace=True)
        #Analysis of rating given by the user 
        no_of_rated_products_per_user = self.electronics_data.groupby(by='userId')['Rating'].count().sort_values(ascending=False)

        quantiles = no_of_rated_products_per_user.quantile(np.arange(0,1.01,0.01), interpolation='higher')
        plt.figure(figsize=(10,10))
        plt.title("Quantiles and their Values")
        # quantiles.plot()
        # quantiles with 0.05 difference
        plt.scatter(x=quantiles.index[::5], y=quantiles.values[::5], c='orange', label="quantiles with 0.05 intervals")
        # quantiles with 0.25 difference
        plt.scatter(x=quantiles.index[::25], y=quantiles.values[::25], c='m', label = "quantiles with 0.25 intervals")
        plt.ylabel('No of ratings by user')
        plt.xlabel('Value at the quantile')
        plt.legend(loc='best')
        # plt.show()

        # print('\n No of rated product more than 50 per user : {}\n'.format(sum(no_of_rated_products_per_user >= 50)) )

    def popularity_based(self):
        #Getting the new dataframe which contains users who has given 50 or more ratings
        new_df = self.electronics_data.groupby("productId").filter(lambda x:x['Rating'].count() >=50)
        no_of_ratings_per_product = new_df.groupby(by='productId')['Rating'].count().sort_values(ascending=False)

        fig = plt.figure(figsize=plt.figaspect(.5))
        ax = plt.gca()
        plt.plot(no_of_ratings_per_product.values)
        plt.title('# RATINGS per Product')
        plt.xlabel('Product')
        plt.ylabel('No of ratings per product')
        ax.set_xticklabels([])
        # plt.show()
        new_df.groupby('productId')['Rating'].mean().sort_values(ascending=False)

        #Total no of rating for product

        new_df.groupby('productId')['Rating'].count().sort_values(ascending=False)

        ratings_mean_count = pd.DataFrame(new_df.groupby('productId')['Rating'].mean())

        ratings_mean_count['rating_counts'] = pd.DataFrame(new_df.groupby('productId')['Rating'].count())

        ratings_mean_count['rating_counts'].max()

        plt.figure(figsize=(8,6))
        plt.rcParams['patch.force_edgecolor'] = True
        ratings_mean_count['rating_counts'].hist(bins=50)

        plt.figure(figsize=(8,6))
        plt.rcParams['patch.force_edgecolor'] = True
        ratings_mean_count['Rating'].hist(bins=50)

        plt.figure(figsize=(8,6))
        plt.rcParams['patch.force_edgecolor'] = True
        sns.jointplot(x='Rating', y='rating_counts', data=ratings_mean_count, alpha=0.4)

        popular_products = pd.DataFrame(new_df.groupby('productId')['Rating'].count())
        most_popular = popular_products.sort_values('Rating', ascending=False)
        most_popular.head(30).plot(kind = "bar")
        self.new_df = new_df
    
    def collaborative_filtering(self):
        ### Collaborative Filtering (Item-Item recommedation)
        try:
            from surprise import KNNWithMeans
            from surprise import Dataset
            from surprise import accuracy
            from surprise import Reader
            import os
            from surprise.model_selection import train_test_split
        except Exception as e:
            print("Some Modules are Missing {}".format(e))
        #Reading the dataset
        reader = Reader(rating_scale=(1, 5))
        data = Dataset.load_from_df(self.new_df,reader)

        #Splitting the dataset
        trainset, testset = train_test_split(data, test_size=0.3,random_state=10)

        # Use user_based true/false to switch between user-based or item-based collaborative filtering
        algo = KNNWithMeans(k=5, sim_options={'name': 'pearson_baseline', 'user_based': False})
        algo.fit(trainset)

        # run the trained model against the testset
        test_pred = algo.test(testset)

        # get RMSE
        # print("Item-based Model : Test Set")
        accuracy.rmse(test_pred, verbose=True)

    def Model_based_collaborative_filtering(self, product_id):
        ### Model-based collaborative filtering system
        self.new_df1 = self.new_df.head(10000)
        self.original_data = self.new_df1.copy()
        ratings_matrix = self.new_df1.pivot_table(values='Rating', index='userId', columns='productId', fill_value=0)
        X = ratings_matrix.T
        X1 = X

        #Decomposing the Matrix
        from sklearn.decomposition import TruncatedSVD
        SVD = TruncatedSVD(n_components=10)
        decomposed_matrix = SVD.fit_transform(X)
        decomposed_matrix.shape

        #Correlation Matrix

        correlation_matrix = np.corrcoef(decomposed_matrix)
        correlation_matrix.shape

        X.index[75]

        i = product_id

        product_names = list(X.index)
        product_ID = product_names.index(i)
        product_ID

        correlation_product_ID = correlation_matrix[product_ID]
        correlation_product_ID.shape

        Recommend = list(X.index[correlation_product_ID > 0.65])

        # Removes the item already bought by the customer
        Recommend.remove(i) 

        # print(Recommend[0:24])

        df = pd.DataFrame(Recommend[0:24], columns=['productId'])
        df.to_csv("./static/data/recommendData_collaborative.csv", index=False)

    def get_recommendations(self, product_id):
        self.preprocess()
        self.cleaning()
        self.popularity_based()
        self.collaborative_filtering()
        self.Model_based_collaborative_filtering(product_id)
        results = pd.read_csv("./static/data/recommendData_collaborative.csv")
        tables =  results.to_html(classes="productId", header="true")
        data1 = results
        data2 = pd.read_csv("./static/data/autocomplete_collaborative.csv")
        data = pd.merge(data1, data2, on='productId', how='inner')
        data = data.to_dict('records')
        data = [tuple(x.values()) for x in data]
        return data, tables

    def get_product_id(self):
        product_id = pd.read_csv("./static/data/autocomplete_collaborative.csv")
        # remove duplicate product id
        product_id = product_id.drop_duplicates()
        return list(product_id["productId"])
    
    def get_column_names(self):
        col_list = ['User ID', 'Product ID', 'Rating', 'Timestamp']
        return col_list


# if __name__ == "__main__":
#     obj = Collaborative()
#     obj.get_recommendations()


