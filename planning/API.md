# API

| HTTP Method | Path                       | Description |
| ----------- | -------------------------- | ----------- |
| `GET`       | `/api/jobs`                |             |
| `GET`       | `/api/joblists`            |             |
| `GET`       | `/api/jobseekers`          |             |
|             |                            |             |
| `GET`       | `/api/searchnew/:location` |             |
| `GET`       | `/api/searchnew/:term`     |             |
|             |                            |             |
| `GET`       | `/api/searchsaved/:term`   |             |
|             |                            |             |
| `GET`       | `/api/jobs/:id`            |             |
| `GET`       | `/api/joblists/:id`        |             |
| `GET`       | `/api/jobseekers/:id`      |             |
|             |                            |             |
| `POST`      | `/api/jobs`                |             |
| `POST`      | `/api/joblists`            |             |
| `POST`      | `/api/jobseekers`          |             |
|             |                            |             |
| `PUT`       | `/api/jobs/:id`            |             |
| `PUT`       | `/api/joblists/:id`        |             |
| `PUT`       | `/api/jobseekers/:id`      |             |
|             |                            |             |
| `DELETE`    | `/api/jobs/:id`            |             |
| `DELETE`    | `/api/joblists/:id`        |             |
| `DELETE`    | `/api/jobseekers/:id`      |             |
|             |                            |             |

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
