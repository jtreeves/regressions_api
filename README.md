# Regressionz API

This [API](https://github.com/jtreeves/regressions_api) will directly pull information from the library. Anyone can use it after getting an API key. It can provide regression models for various data sets.

**Contents**

1. [Models](https://github.com/jtreeves/regressions_api#models)
2. [Routes](https://github.com/jtreeves/regressions_api#routes)
3. [File Structure](https://github.com/jtreeves/regressions_api#file-structure)
4. [User Stories](https://github.com/jtreeves/regressions_api#user-stories)
5. [Designs](https://github.com/jtreeves/regressions_api#designs)

## Models

![ERD](/images/erd.png)

## Routes

| Method | Model       | Path       | File     | Description                   |
| ------ | ----------- | ---------- | -------- | ----------------------------- |
| POST   | users       | /signup/   | views.py | Sign up a new user            |
| POST   | regressions | /          | views.py | Create a new regression       |
| GET    | regressions | /\<int:pk\>/ | views.py | Get an existing regression    |
| PUT    | regressions | /\<int:pk\>/ | views.py | Update an existing regression |
| DELETE | regressions | /\<int:pk\>/ | views.py | Delete an existing regression |

## File Structure

```
regressions_api
|-- configurations
|   |-- __init__.py
|   |-- asgi.py
|   |-- settings.py
|   |-- urls.py
|   |-- wsgi.py
|-- regressions
|   |-- middleware
|   |-- migrations
|   |-- templates
|   |   |-- regressions
|   |   |-- about.html
|   |   |-- base.html
|   |   |-- index.html
|   |   |-- math.html
|   |   |-- signup.html
|   |   |-- usage.html
|   |-- __init__.py
|   |-- admin.py
|   |-- apps.py
|   |-- models.py
|   |-- tests.py
|   |-- urls.py
|   |-- views.py
```

## User Stories

- As a potential user, I want to know about its appeal, so I have a reason to sign up.
- As a potential user, I want to see specific examples of how it can be used by customers, so I know how I can implement it.
- As a potential user, I want to understand the mathematical logic that it implements and how it differs from any competitors, so I can understand the logic.
- As a potential user, I want to be able to sign up for an API key, so I can use it.
- As a user, I want to be able to upload my data to their database by using my API key, so I can access it.
- As a user, I want to be able to view my data stored in their database by using my API key, so I can access it.
- As a user, I want to know that no one else can access my data, so I know it is secure.
- As a user, I want to get extensive info from the API, so I know that it was worth signing up for.
- As a user, I want to get the data in a raw format, so I can easily customize it to my needs.

## Designs

**Home Page**
![Home Page](/images/design1.png)

**Math Explanation**
![Math Explanation](/images/design2.png)

**Usage Guide**
![Usage Guide](/images/design3.png)

**Sign Up**
![Sign Up](/images/design4.png)