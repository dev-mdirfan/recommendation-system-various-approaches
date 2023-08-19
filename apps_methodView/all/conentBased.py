try:
    import pandas as pd
    import numpy as np
    import seaborn as sns
    import matplotlib.pyplot as plt
    import string
    import re
    # %matplotlib inline

    from nltk.corpus import stopwords 
    from nltk.tokenize import word_tokenize
    from nltk.stem.wordnet import WordNetLemmatizer 
    lem = WordNetLemmatizer()
    stop_words = set(stopwords.words('english')) 
    exclude = set(string.punctuation)
    from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
    from sklearn.metrics.pairwise import linear_kernel, cosine_similarity
except Exception as e:
    print("Some modules are missing {}".format(e))

class Recommend:
    """
    A class for generating product recommendations using cosine similarity based on product metadata.

    Attributes:
        title (str): The title of the product for which recommendations are to be generated.
    """
    def __init__(self) -> None:
        """
        The constructor for Recommend class.
        Args:
            title (str, optional): The title of the product for which recommendations are to be generated.
        """
    
    def Preprocess(self):
        """
        Preprocess the original data by removing duplicates and unnecessary columns.
        Returns:
            smd (DataFrame): Preprocessed data without duplicates.
            pre_df (DataFrame): Original data after preprocessing steps.
        """
        pre_df=pd.read_csv("static/data/flipkart_com-ecommerce_sample.csv", na_values=["No rating available"])
        # pre_df.head()
        # pre_df.info()
        pre_df['product_category_tree']=pre_df['product_category_tree'].map(lambda x:x.strip('[]'))
        pre_df['product_category_tree']=pre_df['product_category_tree'].map(lambda x:x.strip('"'))
        pre_df['product_category_tree']=pre_df['product_category_tree'].map(lambda x:x.split('>>'))
        
        # column list
        self.col_list = ['uniq_id', 'crawl_timestamp', 'product_url', 'product_name', 'product_category_tree', 'pid', 'retail_price', 'discounted_price', 'image', 'is_FK_Advantage_product']
        self.original_data = pre_df.drop_duplicates(subset ="product_name", keep = "first", inplace = False)

        #delete unwanted columns
        del_list=['crawl_timestamp','product_url','image',"retail_price","discounted_price","is_FK_Advantage_product","product_rating","overall_rating","product_specifications"]
        pre_df=pre_df.drop(del_list,axis=1)

        # pre_df.shape
        smd=pre_df.copy()
        # drop duplicate produts
        smd.drop_duplicates(subset ="product_name", keep = "first", inplace = True)
        # smd.shape
        return smd, pre_df
    
    def Cleaning(self):
        """
        Perform data cleaning by filtering keywords, removing stop words, and lemmatizing.
        """
        def filter_keywords(doc):
            doc=doc.lower()
            stop_free = " ".join([i for i in doc.split() if i not in stop_words])
            punc_free = "".join(ch for ch in stop_free if ch not in exclude)
            word_tokens = word_tokenize(punc_free)
            filtered_sentence = [(lem.lemmatize(w, "v")) for w in word_tokens]
            return filtered_sentence
        
        self.smd['product'] = self.smd['product_name'].apply(filter_keywords)
        self.smd['description'] = self.smd['description'].astype("str").apply(filter_keywords)
        self.smd['brand'] = self.smd['brand'].astype("str").apply(filter_keywords)

        self.smd["all_meta"] = self.smd['product'] + self.smd['brand']+ self.pre_df['product_category_tree'] + self.smd['description']
        self.smd["all_meta"] = self.smd["all_meta"].apply(lambda x: ' '.join(x))
        self.smd = self.smd.reset_index()
        # smd["all_meta"].head()
    
    def CosineSimilarity(self):
        """
        Calculate the cosine similarity between product metadata.
        
        Returns:
            cosine_sim (array): Cosine similarity matrix between product metadata.
        """
        # count = CountVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0, stop_words='english')
        # count_matrix = count.fit_transform(smd['all_meta'])
        tf = TfidfVectorizer(analyzer='word',ngram_range=(1, 2), min_df = 0.0, stop_words='english')
        tfidf_matrix = tf.fit_transform(self.smd['all_meta'])
        cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
        return cosine_sim

    def recommendations_30(self, title):
        self.titles = self.smd['product_name']
        self.indices = pd.Series(self.smd.index, index = self.smd['product_name'])
        # print(self.indices)
        idx = self.indices[title]
        sim_scores = list(enumerate(self.cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        # 50 Recommendations
        sim_scores = sim_scores[1:31]
        product_indices = [i[0] for i in sim_scores]
        self.data = self.titles.iloc[product_indices]
        df = pd.DataFrame(self.data, columns=['product_name'])  
        df.to_csv("./static/data/recommendData_content.csv", index=False)

    def get_recommendations(self, title):
        """
        Generate product recommendations based on cosine similarity.
        
        Args:
            title (str): The title of the product for which recommendations are to be generated.
            
        Returns:
            recommendations (Series): Series of recommended product names.
        """
        # Initialize the Recommend class with optional title.
        self.smd, self.pre_df = self.Preprocess()
        self.Cleaning()
        self.cosine_sim = self.CosineSimilarity()
        self.recommendations_30(title)
        results = pd.read_csv("./static/data/recommendData_content.csv")
        tables =  results.to_html(classes="product_name", header="true")
        data1 = self.data
        data2 = self.original_data
        data = pd.merge(data1, data2, on='product_name', how='inner')
        data = data.to_dict('records')
        data = [tuple(x.values()) for x in data]
        return data, tables

    def get_product_name(self):
        """
        Get the product names of the recommended products.
        
        Returns:
            df (DataFrame): DataFrame of recommended product names.
        """
        suggestData = pd.read_csv("./static/data/autocomplete_content.csv")
        return list(suggestData['product_name'])