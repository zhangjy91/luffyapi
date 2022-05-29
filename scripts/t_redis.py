# from redis import Redis
#
# conn = Redis(host='127.0.0.1', port=6379)
# result = conn.get('name')
# print(result)

import redis

from t_redis_pool import POOL


r = redis.Redis(connection_pool=POOL)
result = r.get('name')
print(result)

# r.set('name', 'zx',5)
# r.set('height', '190',5)
#
# r.incr('guest')
# vistors = str(r.incr('guest'))
# print('访问人数：' +vistors)

# r.hset('hash1', 'name', 'zhangsan')
# r.lpush('list1',11,22,33)
# r.rpush('list1',44)
# r.lpop('list1')

pipe = r.pipeline(transaction=True)
pipe.multi()
pipe.set('sex',1)
pipe.set('is_disabled',0)

pipe.execute()