import boto3
import os

AWS_REGION = os.environ.get('AWS_REGION', 'us-east-1')
USER_POOL_ID = os.environ.get('USER_POOL_ID')

client = boto3.client('cognito-idp', region_name=AWS_REGION)


def create_cognito_user(email: str, password: str):
    if not USER_POOL_ID:
        raise ValueError('USER_POOL_ID environment variable is required for Cognito integration')
    if not email or not password:
        raise ValueError('Email and password are required')

    response = client.admin_create_user(
        UserPoolId=USER_POOL_ID,
        Username=email,
        UserAttributes=[
            {'Name': 'email', 'Value': email},
            {'Name': 'email_verified', 'Value': 'true'},
        ],
        MessageAction='SUPPRESS',
        DesiredDeliveryMediums=['EMAIL'],
    )

    client.admin_set_user_password(
        UserPoolId=USER_POOL_ID,
        Username=email,
        Password=password,
        Permanent=True,
    )

    attributes = response.get('User', {}).get('Attributes', [])
    sub_attr = next((attr.get('Value') for attr in attributes if attr.get('Name') == 'sub'), None)

    if not sub_attr:
        raise RuntimeError('Could not retrieve Cognito sub from created user response')

    return sub_attr