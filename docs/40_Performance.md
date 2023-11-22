# Requests and limits
This section provides a brief overview of the service performance and recommendations about CPU and RAM requests and limits in order to reach optimal performances on common scenarios.

Results have been obtained through specific tests implementing a series of requests to the OCR Service.

Specifically, the following APIs have been tested to measure CPU and RAM usage:

- POST /extract-text

## Legenda
- `Replicas`: The number of static (or dynimic) replicas of OCR Service
- `Users`:  The number of users that use the service simultaneously (each user make a new request every second)
- `RPS`: The number of the requests that the OCR Service can handle per second
- `Failures`:  The rate of the requests that fails during the test

## Extract text
| Repliche | Utenti | CPU Request | CPU Limit | Memory Request | Memory Limit | RPS | Failures |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 - 3 | 1 | 150 | 300 | 100 | 150 | 0.3 | 0% |
| 1 - 3 | 5 | 150 | 300 | 100 | 150 | 1 | 0% |
| 1 - 3 | 5 | 300 | 500 | 100 | 150 | 1.7 | 0% |
| 1 - 3 | 10 | 300 | 500 | 100 | 150 | 2 | 5% |
| 1 - 3 | 20 | 500 | 1000 | 100 | 150 | 2.5 | 7% |