# API

| HTTP Method | Path                             | Description |
| ----------- | -------------------------------- | ----------- |
| `GET`       | `/jobs`                          |             |
| `GET`       | `/jobs/:ghj_id`                  |             |
|             |                                  |             |
| `GET`       | `/joblists`                      |             |
| `GET`       | `/joblists/:uid`                 |             |
|             |                                  |             |
| `GET`       | `/jobseekers`                    |             |
| `GET`       | `/jobseekers/:uid`               |             |
|             |                                  |             |
| `GET`       | `/getghjobs/:uid`                |             |
| `GET`       | `/getghjobs/:uid/:search_params` |             |
|             |                                  |             |
| `GET`       | `/getsavedjobs/:uid`             |             |
|             |                                  |             |
| `POST`      | `/joblists`                      |             |
| `POST`      | `/jobseekers`                    |             |
|             |                                  |             |
| `PUT`       | `/joblists/:uid/:lid`            |             |
| `PUT`       | `/jobseekers/:uid`               |             |
|             |                                  |             |
| `DELETE`    | `/joblists/:uid/:lid`            |             |
| `DELETE`    | `/jobseekers/:uid`               |             |
|             |                                  |             |

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
