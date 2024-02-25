import boto3
session = boto3.session.Session(profile_name='default')

breakpoint()
# Create AWS Personalize client
client = session.client('personalize-runtime')

try:
    # Call get_recommendations API
    response = client.get_recommendations(
        campaignArn='arn:aws:personalize:eu-west-1:219702648416:campaign/user-personalization-poc',
        userId='a2288579b87050b04d5e0188a96a54fb',
        numResults=10
    )

    # Iterate through recommended items
    for item in response['itemList']:
        print("Item recommended is {} with score of {}".format(item['itemId'], item['score']))

except botocore.exceptions.EndpointConnectionError as e:
    print("Error connecting to AWS Personalize endpoint:", e)
except botocore.exceptions.ClientError as e:
    print("An error occurred:", e)
