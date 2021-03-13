# crypto_price_tracker
 Crypto price tracker which stores values in PostgresDB via a scheduler with manual trigger via REST API. Coingecko API is used to get the actual price. 

# Environment
    - POSTGRES=postgresql://python:python@localhost:25432/python
    - PORT=8000
    - SCHEDULERCOIN=bitcoin

# Swagger
    Link: http://localhost:8000/docs

# Technologies
- fastapi
- sqlalchemy
