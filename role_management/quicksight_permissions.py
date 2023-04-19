import boto3
import pandas as pd
import argparse


def get_quicksight_users(client):
    """
    Function to fetch all QuickSight users
    """
    users = []
    response = client.list_users(AwsAccountId=accountId, Namespace='default')
    users.extend(response['UserList'])
    return users


def get_user_permission(client, username):
    """
    Function to fetch a specific user's permission level
    """
    response = client.describe_user(
        AwsAccountId=accountId,
        Namespace='default',
        UserName=username
    )
    return response['User']['Role']


def update_user_role(client, username, new_role):
    """
    Function to update a specific user's role
    """
    response = client.update_user(
        AwsAccountId=accountId,
        Namespace='default',
        UserName=username,
        Role=new_role
    )
    return response


# Argument parser setup
parser = argparse.ArgumentParser(description='Process QuickSight user roles.')
parser.add_argument('-name', type=str, help='User name')
parser.add_argument('-role', type=str, choices=[
                    'READER', 'AUTHOR', 'ADMIN'], help='Role to be updated for the specified user')
args = parser.parse_args()

print("Setting up AWS credentials and region...")
accountId = '408686880651'
mysession = boto3.Session()
quicksight_client = mysession.client('quicksight', region_name='us-east-1')

print("Initializing QuickSight client...")
quicksight_client = boto3.client('quicksight')

# Check if the flags are passed and optimize the requests to QuickSight
if args.name:
    # If a name is specified, update the user's role (if a new role is provided) and fetch the user's permission level
    if args.role:
        print(f"Updating role for user {args.name} to {args.role}...")
        update_user_role(quicksight_client, args.name, args.role)
        print(f"Role updated for user {args.name} to {args.role}")
    print(
        f"Permission level for user {args.name}: {get_user_permission(quicksight_client, args.name)}")
else:
    # If no flags are passed, fetch all users and their permissions, and write the data to an Excel file
    print("Fetching QuickSight users and their permissions...")
    users = get_quicksight_users(quicksight_client)
    permissions = {user['UserName']: get_user_permission(
        quicksight_client, user['UserName']) for user in users}

    # Create a DataFrame from the permissions dictionary
    df = pd.DataFrame.from_dict(permissions, orient='index', columns=['Role'])
    df.reset_index(inplace=True)
    df.rename(columns={'index': 'Username'}, inplace=True)

    # Write the DataFrame to an Excel file
    output_file = 'quicksight_users_and_permissions.xlsx'
    df.to_excel(output_file, index=False)
    print(f"QuickSight users and permissions saved to {output_file}")
