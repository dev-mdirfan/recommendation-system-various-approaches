'''
Search bar autocomplete using the product categories
from (product_category_tree) column of the dataset (col=1)
And match with the original dataset (col=15)
'''

class SearchBar:
    def __init__(self, data):
        self.data = data

    def autocomplete(self, query):
        '''
        :param query: search query
        :return: list of autocomplete suggestions
        '''
        # get all the product categories
        categories = self.data.iloc[:, 1].values
        # convert to list
        categories = list(categories)
        # convert to lowercase
        categories = [x.lower() for x in categories]
        # remove duplicates
        categories = list(set(categories))
        # sort the list
        categories.sort()
        # get the suggestions
        suggestions = [x for x in categories if x.startswith(query)]
        return suggestions

    def search(self, query):
        '''
        :param query: search query
        :return: list of search results
        '''
        # get all the product categories
        categories = self.data.iloc[:, 1].values
        # convert to list
        categories = list(categories)
        # convert to lowercase
        categories = [x.lower() for x in categories]
        # remove duplicates
        categories = list(set(categories))
        # sort the list
        categories.sort()
        # get the search results
        results = [x for x in categories if query in x]
        return results

    def match(self, query):
        '''
        :param query: search query
        :return: list of search results
        '''
        # get all the product categories
        categories = self.data.iloc[:, 1].values
        # convert to list
        categories = list(categories)
        # convert to lowercase
        categories = [x.lower() for x in categories]
        # remove duplicates
        categories = list(set(categories))
        # sort the list
        categories.sort()
        # get the search results
        results = [x for x in categories if query == x]
        return results

    def get_product(self, query):
        '''
        :param query: search query
        :return: product details
        '''
        # get the product details
        product = self.data[self.data['product_category_tree'] == query]
        # convert to list
        product = product.values.tolist()
        return product

    def get_product_details(self, query):
        '''
        :param query: search query
        :return: product details
        '''
        # get the product details
        product = self.data[self.data['product_category_tree'] == query]
        # convert to list
        product = product.values.tolist()
        # get the product details
        product_details = product[0][15]
        return product_details
    
    def get_product_name(self, query):
        '''
        :param query: search query
        :return: product name
        '''
        # get the product details
        product = self.data[self.data['product_category_tree'] == query]
        # convert to list
        product = product.values.tolist()
        # get the product details
        product_name = product[0][0]
        return product_name
    
    def get_product_price(self, query):
        '''
        :param query: search query
        :return: product price
        '''
        # get the product details
        product = self.data[self.data['product_category_tree'] == query]
        # convert to list
        product = product.values.tolist()
        # get the product details
        product_price = product[0][5]
        return product_price
    
    def get_product_rating(self, query):
        '''
        :param query: search query
        :return: product rating
        '''
        # get the product details
        product = self.data[self.data['product_category_tree'] == query]
        # convert to list
        product = product.values.tolist()
        # get the product details
        product_rating = product[0][6]
        return product_rating

    def get_product_image(self, query):
        '''
        :param query: search query
        :return: product image
        '''
        # get the product details
        product = self.data[self.data['product_category_tree'] == query]
        # convert to list
        product = product.values.tolist()
        # get the product details
        product_image = product[0][14]
        return product_image

    def get_product_url(self, query):
        '''
        :param query: search query
        :return: product url
        '''
        # get the product details
        product = self.data[self.data['product_category_tree'] == query]
        # convert to list
        product = product.values.tolist()
        # get the product details
        product_url = product[0][16]
        return product_url

    def get_product_specifications(self, query):
        '''
        :param query: search query
        :return: product specifications
        '''
        # get the product details
        product = self.data[self.data['product_category_tree'] == query]
        # convert to list
        product = product.values.tolist()
        # get the product details
        product_specifications = product[0][17]
        return product_specifications

    def get_product_brand(self, query):
        '''
        :param query: search query
        :return: product brand
        '''
        # get the product details
        product = self.data[self.data['product_category_tree'] == query]
        # convert to list
        product = product.values.tolist()
        # get the product details
        product_brand = product[0][1]
        return product_brand

    def get_product_category(self, query):
        '''
        :param query: search query
        :return: product category
        '''
        # get the product details
        product = self.data[self.data['product_category_tree'] == query]
        # get the product details
        product_category = product[0][2]
        return product_category

    def get_product_subcategory(self, query):
        '''
        :param query: search query
        :return: product subcategory
        '''
        # get the product details
        product = self.data[self.data['product_category_tree'] == query]
        # get the product details
        product_subcategory = product[0][3]
        return product_subcategory


if __name__ == '__main__':
    # load the dataset
    data = pd.read_csv('flipkart_com-ecommerce_sample.csv')
    # create an object of SearchBar class
    searchBar = SearchBar(data)
    # get the search results
    results = searchBar.search('clothing')
    # print the search results
    print(results)
    # get the product details
    product = searchBar.get_product('clothing')
    # print the product details
    print(product)
    # get the product name
    product_name = searchBar.get_product_name('clothing')
    # print the product name
    print(product_name)
    # get the product price
    product_price = searchBar.get_product_price('clothing')
    # print the product price
    print(product_price)
    # get the product rating
    product_rating = searchBar.get_product_rating('clothing')
    # print the product rating
    print(product_rating)
    # get the product image
    product_image = searchBar.get_product_image('clothing')
    # print the product image
    print(product_image)
    # get the product url
    product_url = searchBar.get_product_url('clothing')
    # print the product url
    print(product_url)
    # get the product specifications
    product_specifications = searchBar.get_product_specifications('clothing')
    # print the product specifications
    print(product_specifications)
    # get the product brand
    product_brand = searchBar.get_product_brand('clothing')
    # print the product brand
    print(product_brand)
    # get the product category
    product_category = searchBar.get_product_category('clothing')
    # print the product category
    print(product_category)
    # get the product subcategory
    product_subcategory = searchBar.get_product_subcategory('clothing')
    # print the product subcategory
    print(product_subcategory)
    # get the autocomplete suggestions
    suggestions = searchBar.autocomplete('clothing')
    # print the autocomplete suggestions
    print(suggestions)
    # get the search results
    results = searchBar.search('clothing')
    # print the search results
    print(results)
    # get the search results
    results = searchBar.match('clothing')
    # print the search results
    print(results)
    # get the product details
    product_details = searchBar.get_product_details('clothing')
    # print the product details
    print(product_details)
    # get the product name
    product_name = searchBar.get_product_name('clothing')
    # print the product name
    

