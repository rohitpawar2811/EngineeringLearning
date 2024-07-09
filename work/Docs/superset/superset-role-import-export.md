# Superset role-Import/Export


# Import-Exports the roles

[
   {
        "name": "Menu-Databases1",
        "permissions": [
            {
                "permission": {
                    "name": "menu_access"
                },
                "view_menu": {
                    "name": "Access requests"
                }
            },
            {
                "permission": {
                    "name": "menu_access"
                },
                "view_menu": {
                    "name": "Databases"
                }
            },
            {
                "permission": {
                    "name": "menu_access"
                },
                "view_menu": {
                    "name": "User's Statistics"
                }
            }
        ]
    }
]

we can simply import export the roles by using flask fab cmd --help

$ flask fab <command> <parameters>
To Run your application on development:

$ flask run --with-threads --reload
Take a quick look to the current possibilities. (The bold ones require app context)

babel-compile - Babel, Compiles all translations
babel-extract - Babel, Extracts and updates all messages.
create-admin - Creates an admin user
create-user - Create user with arbitrary role
create-app - Create a Skeleton application (SQLAlchemy or MongoEngine).
create-addon - Create a Skeleton AddOn.
create-db - Create all your database objects (SQLAlchemy only)
collect-static - Copies static files from flask-appbuilder to your static folder. Nice to have on certain deploys
export-roles - Export roles with permissions and view menus to JSON file.
import-roles - Import roles with permissions and view menus from JSON file.
list-users - List all users on the database.
list-views - List all registered views.
reset-password - Resets a user’s password.
security-cleanup - Cleanup unused permissions from views and roles. Security
security-converge - Converges all security view and permission names from all your roles. Security
upgrade-db - Upgrade your database after F.A.B upgrade.
version - Flask-AppBuilder package version.
Command Line uses the excellent click package, so you can have a detailed help for each command, for instance:

## Here is the location where this code written

venv/lib/python3.8/site-packages/flask_appbuilder/security/sqla/manager.py

and for exposing in the cmdline , cmdline.py file contains the scripts to do that 