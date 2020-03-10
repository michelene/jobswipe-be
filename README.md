# jobswipe-be

# Back End API for JobSwipe

- [Planning docs](https://github.com/michelene/jobswipe-be/tree/master/planning)
- [API](https://github.com/michelene/jobswipe-be/blob/master/planning/API.md)

## Things I have learned/incorporated in the course of building the back end:

- [Django `ManyToManyField`](https://docs.djangoproject.com/en/3.0/ref/models/fields/#manytomanyfield)
- [Django `JSONField`](https://docs.djangoproject.com/en/3.0/ref/contrib/postgres/fields/#jsonfield)
- [Django: Seeding data using `fixtures`](https://docs.djangoproject.com/en/3.0/howto/initial-data/#providing-data-with-fixtures)
- [Python `requests` module](https://pypi.org/project/requests/)
- [Create `django` user for testing](https://stackoverflow.com/questions/14186055/django-test-app-error-got-an-error-creating-the-test-database-permission-deni)
- [I wrote a custom function-based DRF view to call a 3rd party API](https://www.django-rest-framework.org/api-guide/views/#function-based-views)

- [Django `APIView`](https://www.django-rest-framework.org/api-guide/views/)
- [Substituting a custom User model](https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project)
  - Also used this [tutorial](https://wsvincent.com/django-rest-framework-user-authentication-tutorial/)
- Add user registration using the [django-allauth](https://django-rest-auth.readthedocs.io/en/latest/installation.html#registration-optional) package

## Implementation Details

### User Auth

- To provide login, logout, signup, and JWT, I used a combination of these 3 packages:
  - (1) [django-rest-auth](https://django-rest-auth.readthedocs.io/en/latest/introduction.html)
    - Provides `rest-auth/{login|logout}`
    - Returns a token key
    - Also provides `rest-auth/password/{reset|change}` # Did not use
    - Also provides `rest-auth/user/ (GET, PUT, PATCH)` # Did not use
  - (2) [django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
    - This provides a "standard registration process"
    - Can be extended via to provide social auth by adding `allauth.socialaccount` as an app
  - (3) [djangorestframework-jwt](https://jpadilla.github.io/django-rest-framework-jwt/)
    - Instead of returning a token key, it returns a JWT
    - Uses paths `api-token-{auth|refresh|verify}`
    - Expects that the JWT will come in the header

## Unresolved Issues

- I tried making 'ghj_id' (a CharField) into a Primary Key. This was successful, but it broke UnreviewedJobs. Error stack was as follows. I would like to try to CAST the Charfield into an int, but could not figure out how to do so.

So, I wasn't able to make 'ghj_id' be the Primary Key. :-(

````
The above exception was the direct cause of the following exception:

Traceback (most recent call last):
    return self.cursor.execute(sql, params)
django.db.utils.ProgrammingError: operator does not exist: character varying = integer
LINE 1: ...obswipe_joblist_jobs" ON ("jobswipe_job"."ghj_id" = "jobswip...
                                                             ^
HINT:  No operator matches the given name and argument types. You might need to add explicit type casts.```
````

See also: https://stackoverflow.com/questions/38117069/django-charfield-suitable-for-a-primary-key
