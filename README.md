# Recommendation Systems

I have created multiple recommendation systems using different techniques. The following are the techniques used:

- Content Based Filtering
- Collaborative Filtering
- Hybrid Filtering

## Preview

![preview](/demo-video.gif)


## Setup

1. Clone the repository
2. Install the dependencies
3. Run the following command to start the server

```bash
# Install the virtual environment
python3 -m venv venv

# Activate the virtual environment
.\venv\Scripts\activate

# Install the dependencies
pip install -r requirements.txt

# Run the server
python app.py
```

## Video Preview of the Web Application

[Preview](https://youtu.be/jZcMbm6Nm1E)



## Problem Statement: Personalized  Product  Recommendations

The aim is to enhance user experience by implementing a personalized product ranking system.

Your task is to develop an algorithm or model that can generate accurate and relevant product rankings for individual users. The ranking system should consider factors such as user preferences, past interactions, product popularity, and user similarity. It should be able to predict the most suitable products for a user based on their unique characteristics and preferences.

You are not provided with a specific dataset for this challenge. Instead, you are expected to design and implement a solution that simulates user interactions and generates personalized rankings. You can define user profiles, product categories, and interaction patterns within your
solution.

To evaluate the effectiveness of your solution, you should define appropriate metrics for measuring the accuracy and relevance of the rankings. You should also provide a report explaining your approach, describing the algorithms or techniques used, and discussing the
strengths and limitations of your solution.

## Dataset

- For content based - [Kaggle](https://www.kaggle.com/datasets/PromptCloudHQ/flipkart-products?select=flipkart_com-ecommerce_sample.csv)
- For collaborative - [Kaggle](https://www.kaggle.com/datasets/pritech/ratings-electronics?select=ratings_Electronics.csv)


## Solution Approach

The problem statement provided by Flipkart Grid 5.0 does not explicitly mention whether you need to implement both the frontend and backend of a web application. However, it does focus on developing an algorithm or model to create personalized product rankings for individual users. This implies that you should primarily focus on designing the algorithmic solution rather than building a complete web application. Here's how you could approach this problem:

1. **Algorithm Design:**
   - Create User Profiles: Define characteristics and preferences that describe individual users. This can include factors like demographics, past interactions, purchase history, product categories of interest, etc.
   - Product Categories: Categorize the products available in your simulated system. Each product should belong to one or more categories.
   - Interaction Patterns: Simulate user interactions, such as clicks, views, purchases, etc., for a certain period of time to create a synthetic dataset.
   - User Similarity: Define a similarity metric to measure how similar one user is to another. This can be based on shared preferences, interactions, or other relevant features.

2. **Ranking Algorithm:**
   - Collaborative Filtering: Utilize collaborative filtering techniques to generate recommendations based on user behaviors and similarities. Collaborative filtering methods include User-Based CF and Item-Based CF.
   - Content-Based Filtering: Create recommendations based on the attributes of products and users' preferences. This can involve using machine learning models to predict user preferences for different product categories.
   - Hybrid Approaches: Combine collaborative and content-based filtering for improved accuracy and coverage.

3. **Evaluation Metrics:**
   - Define appropriate metrics to evaluate the effectiveness of your personalized ranking system. Common metrics include Precision, Recall, F1-score, Mean Average Precision, and Normalized Discounted Cumulative Gain (NDCG).

4. **Strengths and Limitations:**
   - In your report, discuss the strengths and limitations of your solution. For example, strengths could include accurate recommendations, personalization, and adaptability to user preferences. Limitations could involve data sparsity, cold start problem for new users and products, and scalability challenges.

5. **Reporting:**
   - Prepare a comprehensive report that explains your approach, the algorithms or techniques used, and the reasoning behind your design decisions.
   - Describe how you simulated user interactions and generated the synthetic dataset.
   - Present the results of your evaluation metrics, showcasing how well your algorithm performs.

It's important to note that while you don't need to implement a full web application for this challenge, you should focus on the algorithmic aspect of generating personalized product rankings. If the competition organizers have provided any specific guidelines or expectations regarding frontend or backend implementation, make sure to adhere to those guidelines accordingly.


## Future Scope

1. **Search Engine:** I used pandas substring matching to find the most similar products. This can be improved by using a search engine like **Elasticsearch** or **Solr**. I also plan to use **ElasticSearch** to find the most similar products. But we have limited time to implement this.
2. **Content Based Filtering:** I used TF-IDF to find the most similar products. This can be improved by using **Word2Vec** or **Doc2Vec** to find the most similar products.
3. **Collaborative Filtering:** I used **Surprise** library to implement collaborative filtering. This can be improved by using **TensorFlow** or **PyTorch** to implement collaborative filtering.
4. **Hybrid Filtering:** I used **Surprise** library to implement hybrid filtering. This can be improved by using **TensorFlow** or **PyTorch** to implement collaborative filtering.
5. **Evaluation:** I used **RMSE** to evaluate the models. This can be improved by using **Precision** and **Recall** to evaluate the models.

## References

- Youtube
- Kaggle
- Articles / Blogs
- Stackoverflow







