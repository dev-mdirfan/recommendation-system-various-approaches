'''
    The hybrid model is a combination of content-based and collaborative filtering models.
'''

try:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    # %matplotlib inline
    from surprise import SVD, Reader, Dataset 
    from surprise.model_selection import cross_validate
except Exception as e:
    print("Some Modules are Missing {}".format(e))
    print("Please install the required modules")

class Hybrid:
    def __init__(self):
        column_names = ['userId','productId','rating','timestamp']
        self.df = pd.read_csv('static/data/ratings_electronics.csv', names = column_names)

    def analysis(self):
        plt.figure(figsize=(10,6))
        sns.countplot(x='rating', data = self.df, palette='winter')
        plt.xlabel('Rating', fontsize=12)
        plt.ylabel('Count', fontsize=12)
        plt.title('Number of Each Rating', fontsize=15)
        # plt.show()
        self.df_rating = pd.DataFrame({'Number of Rating':df.groupby('productId').count()['rating'], 'Mean Rating':df.groupby('productId').mean()['rating']})
        plt.figure(figsize=(18,6))

        plt.subplot(1,2,1)
        plt.hist(x='Number of Rating',data = self.df_rating,bins=30,color='teal')
        plt.title('Distribution of Number of Rating', fontsize=15)
        plt.xlabel('Number of Rating', fontsize=12)
        plt.ylabel('Frequency', fontsize=12)

        plt.subplot(1,2,2)
        plt.hist(x='Mean Rating',data = self.df_rating,bins=30, color='slateblue')
        plt.title('Distribution of Mean Rating', fontsize=15)
        plt.xlabel('Mean Rating', fontsize=12)
        plt.yticks([])
        # plt.show()
        plt.figure(figsize=(8,6))
        sns.jointplot(x='Number of Rating', y='Mean Rating', data = self.df_rating, color='g', height=7)
        plt.suptitle('Mean Rating Versus Number of Rating', fontsize=15, y=0.92)

        # plt.show()
    
    def popularity_based(self):
        self.df_rating['Mean Rating'].mean()
        self.df_rating['Number of Rating'].quantile(q=0.9)
        df_filtered = self.df_rating[self.df_rating['Number of Rating'] > self.df_rating['Number of Rating'].quantile(q=0.9)]
        def product_score(x):
            v=x['Number of Rating']
            m = self.df_rating['Number of Rating'].quantile(q=0.9)
            R = x['Mean Rating']
            C = self.df_rating['Mean Rating'].mean()
            return ((R*v)/(v+m))+((C*m)/(v+m))
        
        df_filtered['score'] = df_filtered.apply(product_score, axis=1)
        df_highscore = df_filtered.sort_values(by='score', ascending=False).head(10)

    def collaborative(self):
        self.svd = SVD()
        reader = Reader()
        data = Dataset.load_from_df(self.df[['userId', 'productId', 'rating']], reader)
        cross_validate(self.svd, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)
        trainset = data.build_full_trainset()
        self.svd.fit(trainset)
        self.df[self.df['userId'] == 'AKM1MP6P0OYPR']
        self.svd.predict(uid='A17HMM1M7T9PJ1', iid='0970407998', r_ui=None)
        self.svd.predict(uid='A17HMM1M7T9PJ1', iid='0970407998', r_ui=None).est
    
    def hybrid(self, userId, productId):
        df_users = self.df.groupby('userId').filter(lambda x: x['rating'].count()>=50)
        self.matrix = pd.pivot_table(data=df_users, values='rating', index='userId',columns='productId')
        # Function that takes in productId and useId as input and outputs up to 5 most similar products.
        def hybrid_recommendations(userId, productId):
            # Get the Id of the top five products that are correlated with the ProductId chosen by the user.
            top_five = self.matrix.corrwith(self.matrix[productId]).sort_values(ascending=False).head(5)
            
            # Predict the ratings the user might give to these top 5 most correlated products.
            est_rating=[]
            for x in list(top_five.index):
                if str(top_five[x])!='nan':
                    est_rating.append(self.svd.predict(userId, iid=x, r_ui=None).est)
                
            return pd.DataFrame({'productId':list(top_five.index)[:len(est_rating)], 'estimated_rating':est_rating}).sort_values(by='estimated_rating', ascending=False).reset_index(drop=True)
        
        return hybrid_recommendations(userId, productId)
    
    def get_recommendations(self, userId, productId):
        self.collaborative()
        results = self.hybrid(userId, productId)
        return results
    
    def get_user_id(self):
        data = pd.read_csv('static/data/autocomplete_hybrid.csv')
        # drop duplicate values
        data.drop_duplicates(subset ="userId", keep = False, inplace = True)
        return list(data['userId'])
    
    def get_product_id(self):
        data = pd.read_csv('static/data/autocomplete_hybrid2.csv')
        # drop duplicate values
        data.drop_duplicates(subset ="productId", keep = False, inplace = True)
        return list(data['productId'])

# if __name__ == '__main__':
#     obj = Hybrid()
#     ans = obj.get_recommendations('A2NYK9KWFMJV4Y', 'B00LI4ZZO8')
#     print(ans)







            