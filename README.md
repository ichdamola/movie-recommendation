# Movie Recommendation
The Video Recommendation System is a personalized recommendation engine built using AWS services like Amazon Personalize, Amazon S3, AWS Lambda, and API Gateway. The system aims to provide users with personalized video recommendations based on their past interactions with videos, such as watching duration and engagement.

## Acrhitecture
![ai drawio](https://github.com/ichdamola/movie-recommendation/assets/20647487/6836e127-2c3d-422f-92b1-9257672fe427)

## Process
### Data Preprocessing:
  Before training the recommendation models, data preprocessing is performed to prepare the dataset for training. The main preprocessing steps include:
  - Deciding Whether a Video was Watched or Clicked: This step involves determining whether a user's interaction with a video constitutes watching or just clicking based on the watching duration. For example, if a user watches more than 50% of a video's duration, it can be considered as watched, otherwise, it's considered as clicked.
  - Factorization Matrix: The dataset is transformed into a factorization matrix where each row represents a user and each column represents an item (video). The matrix is then used as input for training the recommendation models in Amazon Personalize.
### Recommendation Generation: 
  - Once the recommendation models are trained using the preprocessed dataset, they are ready to generate personalized video recommendations. The recommendation generation process involves the following steps:
  - Training Models: Amazon Personalize trains multiple recommendation models based on the dataset provided. These models include user-personalization, item-personalization, and related algorithms.
  - Retrieving Recommendations: When a user makes a request for video recommendations through the API Gateway endpoint, a Lambda function is triggered. The Lambda function interacts with Amazon Personalize to retrieve personalized recommendations for the user based on their past interactions.
  - Formatting Recommendations: The retrieved recommendations are formatted into a user-friendly response, typically in JSON format. Each recommendation includes details such as the recommended video's ID, title, URL, and relevance score. Returning Recommendations: The formatted recommendations are returned to the user through the API Gateway endpoint, where they can be consumed by client applications, such as web or mobile apps.

