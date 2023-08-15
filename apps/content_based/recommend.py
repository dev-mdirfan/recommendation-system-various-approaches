import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
for dirname, _, filenames in os.walk('static/data/flipkart_com-ecommerce_sample.csv'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

def recommend(query):
    products = pd.read_csv('static/data/flipkart_com-ecommerce_sample.csv')
    # len(products['product_name'].unique()),len(products['uniq_id'].unique())
    products.isna().sum()
    from sklearn.feature_extraction.text import TfidfVectorizer
    tfv = TfidfVectorizer(max_features=None,
                            strip_accents='unicode',
                            analyzer='word',
                            min_df=10,
                            token_pattern=r'\w{1,}',
                            ngram_range=(1,3), # take the combination of 1-3 different kind of words
                            stop_words='english') # removes all the unnecessary characters like the,in etc.
    products['description'] = products['description'].fillna('')
    #fitting the description column.
    tfv_matrix = tfv.fit_transform(products['description']) # converting everythinng to sparse matrix.
    # tfv_matrix
    from sklearn.metrics.pairwise import sigmoid_kernel
    sig = sigmoid_kernel(tfv_matrix,tfv_matrix) # how description of first product is related to first product and so on.
    indices = pd.Series(products.index,index=products['product_name']).drop_duplicates()
    def product_recommendation(title,sig=sig):
        indx = indices[title]
        
        #getting pairwise similarity scores
        sig_scores = list(enumerate(sig[indx]))
        
        #sorting products
        sig_scores = sorted(sig_scores, key=lambda x: x[1], reverse=True)
        
        #50 most similar products score
        sig_scores = sig_scores[1:51]
        
        #product indexes
        product_indices = [i[0] for i in sig_scores]
        
        #Top 10 most similar products
        return products['product_name'].iloc[product_indices]
    # n=input("Enter the name of the product: ")
    # print("\nTop Recommended products are: \n")
    # print(product_recommendation(n).unique())
    recommend = product_recommendation(query).unique()
    df = pd.DataFrame(recommend, columns=['product_name'])
    df.to_csv("./static/data/recommendData.csv", index=False)
    # return render_template('index.html', query=query, recommend=recommend)
    return df