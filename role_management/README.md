# QuickSight User Roles Management Script
This script helps you manage AWS QuickSight user roles. It can fetch QuickSight users and their permission levels, update user roles, and export user permissions to an Excel file.

## Prerequisites
- Python 3.x
- Boto3 library
- Pandas library
- AWS credentials with QuickSight access

Install the required libraries using pip:

`pip install boto3 pandas`

## Usage
### Fetch user permission level
To fetch the permission level for a specific user, use the `-name` flag followed by the username:
`python quicksight_user_roles.py -name <username>`

### Update user role
To update the role for a specific user, use the `-name` flag followed by the username and the `-role` flag followed by the new role (READER, AUTHOR, or ADMIN):
`python quicksight_user_roles.py -name <username> -role <new_role>`

### Export user permissions to Excel
If no flags are provided, the script fetches all users and their permissions and exports the data to an Excel file named `quicksight_users_and_permissions.xlsx`:

`python quicksight_user_roles.py`

## Functions
The script includes the following functions:
- `get_quicksight_users(client)`: Fetches all QuickSight users
- `get_user_permission(client, username)`: Fetches a specific user's permission level
- `update_user_role(client, username, new_role)`: Updates a specific user's role
