# jobswipe_be

# Back End API for JobSwipe

- [Planning docs](https://github.com/michelene/jobswipe_be/tree/master/planning)
- [API](https://github.com/michelene/jobswipe_be/blob/master/planning/API.md)

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

- I tried making 'ghj_id' (a CharField) into a Primary Key. This was successful, but it broke JobList. Error stack was as follows. I would like to try to CAST the Charfield into an int, but could not figure out how to do so.

So, I wasn't able to make 'ghj_id' be the Primary Key. :-(

````
The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/Users/michelenechon/.local/share/virtualenvs/jobswipe_be-maO3iCev/lib/python3.8/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/Users/michelenechon/.local/share/virtualenvs/jobswipe_be-maO3iCev/lib/python3.8/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/Users/michelenechon/.local/share/virtualenvs/jobswipe_be-maO3iCev/lib/python3.8/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/Users/michelenechon/.local/share/virtualenvs/jobswipe_be-maO3iCev/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/Users/michelenechon/.local/share/virtualenvs/jobswipe_be-maO3iCev/lib/python3.8/site-packages/django/views/generic/base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "/Users/michelenechon/.local/share/virtualenvs/jobswipe_be-maO3iCev/lib/python3.8/site-packages/rest_framework/views.py", line 505, in dispatch
    response = self.handle_exception(exc)
  File "/Users/michelenechon/.local/share/virtualenvs/jobswipe_be-maO3iCev/lib/python3.8/site-packages/rest_framework/views.py", line 465, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/Users/michelenechon/.local/share/virtualenvs/jobswipe_be-maO3iCev/lib/python3.8/site-packages/rest_framework/views.py", line 476, in raise_uncaught_exception
    raise exc
  File "/Users/michelenechon/.local/share/virtualenvs/jobswipe_be-maO3iCev/lib/python3.8/site-packages/rest_framework/views.py", line 502, in dispatch
    response = handler(request, *args, **kwargs)
  File "/Users/michelenechon/.local/share/virtualenvs/jobswipe_be-maO3iCev/lib/python3.8/site-packages/rest_framework/generics.py", line 239, in get
    return self.list(request, *args, **kwargs)
  File "/Users/michelenechon/.local/share/virtualenvs/jobswipe_be-maO3iCev/lib/python3.8/site-packages/rest_framework/mixins.py", line 46, in list
    return Response(serializer.data)
  File "/Users/michelenechon/.local/share/virtualenvs/jobswipe_be-maO3iCev/lib/python3.8/site-packages/rest_framework/serializers.py", line 760, in data
    ret = super().data
  File "/Users/michelenechon/.local/share/virtualenvs/jobswipe_be-maO3iCev/lib/python3.8/site-packages/rest_framework/serializers.py", line 260, in data
    self._data = self.to_representation(self.instance)
  File "/Users/michelenechon/.local/share/virtualenvs/jobswipe_be-maO3iCev/lib/python3.8/site-packages/rest_framework/serializers.py", line 677, in to_representation
    return [
  File "/Users/michelenechon/.local/share/virtualenvs/jobswipe_be-maO3iCev/lib/python3.8/site-packages/rest_framework/serializers.py", line 678, in <listcomp>
    self.child.to_representation(item) for item in iterable
  File "/Users/michelenechon/.local/share/virtualenvs/jobswipe_be-maO3iCev/lib/python3.8/site-packages/rest_framework/serializers.py", line 529, in to_representation
    ret[field.field_name] = field.to_representation(attribute)
  File "/Users/michelenechon/.local/share/virtualenvs/jobswipe_be-maO3iCev/lib/python3.8/site-packages/rest_framework/relations.py", line 533, in to_representation
    return [
  File "/Users/michelenechon/.local/share/virtualenvs/jobswipe_be-maO3iCev/lib/python3.8/site-packages/django/db/models/query.py", line 276, in __iter__
    self._fetch_all()
  File "/Users/michelenechon/.local/share/virtualenvs/jobswipe_be-maO3iCev/lib/python3.8/site-packages/django/db/models/query.py", line 1261, in _fetch_all
    self._result_cache = list(self._iterable_class(self))
  File "/Users/michelenechon/.local/share/virtualenvs/jobswipe_be-maO3iCev/lib/python3.8/site-packages/django/db/models/query.py", line 57, in __iter__
    results = compiler.execute_sql(chunked_fetch=self.chunked_fetch, chunk_size=self.chunk_size)
  File "/Users/michelenechon/.local/share/virtualenvs/jobswipe_be-maO3iCev/lib/python3.8/site-packages/django/db/models/sql/compiler.py", line 1151, in execute_sql
    cursor.execute(sql, params)
  File "/Users/michelenechon/.local/share/virtualenvs/jobswipe_be-maO3iCev/lib/python3.8/site-packages/django/db/backends/utils.py", line 100, in execute
    return super().execute(sql, params)
  File "/Users/michelenechon/.local/share/virtualenvs/jobswipe_be-maO3iCev/lib/python3.8/site-packages/django/db/backends/utils.py", line 68, in execute
    return self._execute_with_wrappers(sql, params, many=False, executor=self._execute)
  File "/Users/michelenechon/.local/share/virtualenvs/jobswipe_be-maO3iCev/lib/python3.8/site-packages/django/db/backends/utils.py", line 77, in _execute_with_wrappers
    return executor(sql, params, many, context)
  File "/Users/michelenechon/.local/share/virtualenvs/jobswipe_be-maO3iCev/lib/python3.8/site-packages/django/db/backends/utils.py", line 86, in _execute
    return self.cursor.execute(sql, params)
  File "/Users/michelenechon/.local/share/virtualenvs/jobswipe_be-maO3iCev/lib/python3.8/site-packages/django/db/utils.py", line 90, in __exit__
    raise dj_exc_value.with_traceback(traceback) from exc_value
  File "/Users/michelenechon/.local/share/virtualenvs/jobswipe_be-maO3iCev/lib/python3.8/site-packages/django/db/backends/utils.py", line 86, in _execute
    return self.cursor.execute(sql, params)
django.db.utils.ProgrammingError: operator does not exist: character varying = integer
LINE 1: ...obswipe_joblist_jobs" ON ("jobswipe_job"."ghj_id" = "jobswip...
                                                             ^
HINT:  No operator matches the given name and argument types. You might need to add explicit type casts.```
````

See also: https://stackoverflow.com/questions/38117069/django-charfield-suitable-for-a-primary-key
