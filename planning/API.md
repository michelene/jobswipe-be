# API

| HTTP Method | Path                                   | Description                              |
| ----------- | -------------------------------------- | ---------------------------------------- |
| `POST`      | `api/v1/rest-auth/login`               | Email not required; returns a REST token |
| `POST`      | `api/v1/rest-auth/logout`              | Email not required                       |
| `POST`      | `api/v1/rest-auth/registration`        | Returns 201 and REST token if successful |
|             |                                        |                                          |
| `POST`      | `api/v1/api-token-auth`                | Request a JWT token                      |
| `POST`      | `api/v1/api-token-refresh`             | Refresh a JWT token                      |
| `POST`      | `api/v1/api-token-verify`              | Verify a JWT token                       |
|             |                                        |                                          |
| `GET`       | `api/v1/users`                         | See all users                            |
|             |                                        |                                          |
| `GET`       | `api/v1/rest-auth/login`               | Log in; returns a REST token             |
| `GET`       | `api/v1/rest-auth/logout`              | Log out; returns nothing                 |
| `GET`       | `api/v1/rest-auth/registration`        | Create a new account                     |
|             |                                        |                                          |
| `GET`       | `api/v1/jobs`                          | See all jobs                             |
| `GET`       | `api/v1/jobs/:ghj_id`                  |                                          |
|             |                                        |                                          |
| `GET`       | `api/v1/joblists`                      | See all joblists                         |
| `GET`       | `api/v1/joblists/:uid`                 |                                          |
|             |                                        |                                          |
| `GET`       | `api/v1/getghjobs/:uid`                |                                          |
| `GET`       | `api/v1/getghjobs/:uid/:search_params` |                                          |
|             |                                        |                                          |
| `GET`       | `api/v1/getsavedjobs/:uid`             |                                          |
|             |                                        |                                          |
| `POST`      | `api/v1/joblists`                      |                                          |
|             |                                        |                                          |
| `PUT`       | `api/v1/joblists/:uid/:lid`            |                                          |
|             |                                        |                                          |
| `DELETE`    | `api/v1/joblists/:uid/:lid`            |                                          |
|             |                                        |                                          |

# User Auth

| Error Code                       | Meaning                                                   |
| -------------------------------- | --------------------------------------------------------- |
| 200 OK                           |  HTTP operation is successful.                            |
| 201 CREATED                      |  When POST method to create a new resource is successful. |
| 202 ACCEPTED                     |  Acknowledge the request sent to the server.              |
| 400 BAD REQUEST                  |  Client side input validation fails.                      |
| 401 UNAUTHORIZED / 403 FORBIDDEN | Unauthorised to perform operation.                        |
| 404 NOT FOUND                    | Resource not available in the system.                     |
| 500 INTERNAL SERVER ERROR        |  If the system fails.                                     |
| 502 BAD GATEWAY                  |  Received an invalid response from the upstream server.   |
|                                  |                                                           |
