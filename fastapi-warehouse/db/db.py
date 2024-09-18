from redis_om import get_redis_connection
import os
if not os.getenv('PRODUCTION'):
  from dotenv import load_dotenv
  load_dotenv() 

redis = get_redis_connection(
    host = os.getenv('REDIS_HOST'),
    port = os.getenv('REDIS_PORT'),
    password = os.getenv('REDIS_PASSWORD'),
    decode_responses = True
)