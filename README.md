# mentorHub-flask-utils

## Overview

This is collection of simple Flask utilities for MentorHub API projects. 

# Usage
Install the package
```sh
pipenv install mentorhub-flask-utils
```

### MongoJSONEncoder
This is a helper class that allows the flask.json method to properly handle ObjectID and datetime values by converting them to strings.
```py
from flask import Flask
from mentorhub_flask_utils import MongoJSONEncoder

# Initialize Flask App
app = Flask(__name__)
app.json = MongoJSONEncoder(app)
```
### Tokens
All API's will be secured with industry standard bearer tokens used to implement Role Based Access Control (RBAC). The create_token method will decode the token and extract claims for a user_id and roles, throwing an exception if the token is not found or not properly encoded. 
```json
{
    "user_id": "The users PersonID",
    "roles": ["Staff", "Mentor", "Member"]
}
```
Valid roles are listed in the mentorhub-mongodb repo's [enumerators file](https://github.com/agile-learning-institute/mentorHub-mongodb/blob/main/configurations/enumerators/enumerators.json) but the roles listed above are the only one's currently used in the mentorHub platform.

### Breadcrumbs
All database collections include a lastModified "breadcrumb" property used to track changes over time. The breadcrumb has the following properties:
```json
{
        "atTime": "date-time the document was last modified",
        "byUser": "UserID claim from the access token",
        "fromIp": "IP Address the request originated at",  
        "correlationId": "A correlationID to use in logging"
}
```

### Example
Here is how these methods are used in a Flask Route Handler
```py
from mentorhub_flask_utils import create_breadcrumb, create_token
token = create_token()
breadcrumb = create_breadcrumb(token)
MyService.doSomething(myData, ..., token, breadcrumb)
logger.info(f"Did Something completed successfully {breadcrumb.correlationId}")
```

## Contributing

### Prerequisites

- [Python](https://www.python.org/downloads/)
- [Pipenv](https://pipenv.pypa.io/en/latest/installation.html)

### Install Dependencies
```bash
pipenv install --dev
```

## Test package 
```bash
pipenv run test
```

## Clean package build path
```bash
pipenv run clean
```

### Build the Package
```bash
pipenv run build
```

## Twine check 
To check if the package is ready to publish
```bash
pipenv run check
```

# Publish the Package
You should successfully run ``clean``, ``build`` and ``check`` before publishing.
```bash
pipenv run publish
```
