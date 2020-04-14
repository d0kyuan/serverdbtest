import pprint
import os
import redis
import time
import json
# from sqlalchemy import (BigInteger, Boolean, Column, DateTime, Enum, Float,
#                         ForeignKey, Integer, MetaData, String, Table, Text,
#                         create_engine)
# from sqlalchemy.dialects import mysql
# from sqlalchemy.ext.declarative import declarative_base
import datetime
import yaml
# with open('./tmp.yml', "r+", encoding='UTF-8') as f:
#     data = yaml.load(f)
r1 = redis.Redis(host='localhost', port=6379, db=1)
r2 = redis.Redis(host='localhost', port=6379, db=2)
r3 = redis.Redis(host='localhost', port=6379, db=3)
r4 = redis.Redis(host='localhost', port=6379, db=4)
r5 = redis.Redis(host='localhost', port=6379, db=5)
rp5 = r5.pipeline()
r6 = redis.Redis(host='localhost', port=6379, db=6)
r7 = redis.Redis(host='localhost', port=6379, db=7)
r8 = redis.Redis(host='localhost', port=6379, db=8)
r9 = redis.Redis(host='localhost', port=6379, db=9)
pipe = r9.pipeline()
r10 = redis.Redis(host='localhost', port=6379, db=10)
rp10 = r10.pipeline()
r11 = redis.Redis(host='localhost', port=6379, db=11)
r12 = redis.Redis(host='localhost', port=6379, db=12)
r13 = redis.Redis(host='localhost', port=6379, db=13)
rp13 = r13.pipeline()
r15 = redis.Redis(host='localhost', port=6379, db=45)
rp15 = r10.pipeline()
r17 = redis.Redis(host='localhost', port=6379, db=17)
rp17 = r17.pipeline()
r18 = redis.Redis(host='localhost', port=6379, db=18)
rp18 = r18.pipeline()
r21 = redis.Redis(host='localhost', port=6379, db=21)
host = 'localhost'
# print(list())

r31 = redis.Redis(host=host, port=6379, db=31)
# rp15 = r15.pipeline()
r32 = redis.Redis(host=host, port=6379, db=32)
r45 = redis.Redis(host='localhost', port=6379, db=45)


r16 = redis.Redis(host='localhost', port=6379, db=46)
r17 = redis.Redis(host='localhost', port=6379, db=47)

for i in r16.scan_iter():
    config_data = r16.lrange(str(i), 0, -1)
    print("config_data", config_data)
# rp15 = r15.pipeline()
r6 = redis.Redis(host='localhost', port=6379, db=43)
r7 = redis.Redis(host='localhost', port=6379, db=44)
rp7 = r7.pipeline()
time_data = r6.zrangebyscore(
    "tag_pos", "-inf", "+inf")
# print("time_data",time_data)
for o in time_data:
    rp7.lrange(o, 0, -1)
pos_time_data = rp7.execute()
# pos_time_data = None
temp_time = ""
for o in pos_time_data:
    # print("o",o)
    for pos_data in o:
        # print(pos_data)
        new_pos_data = json.loads(pos_data)
        print(new_pos_data)
# r31.set("1", json.dumps(dict(
#         id="1",
#         tag_id="d30524000127",
#         f_zone="ed8955b0-0ae7-4ea2-aed8-bf564a4fa05e",
#         s_zone="8433a7d6-3da3-4be4-a0bc-e2e3a9ebbace",
#         time_standard='5',
#         between='5',
#         allowable_rate='1'
#         )))
# r31.set("2", json.dumps(dict(
#         id="2",
#         tag_id="d30524000127",
#         f_zone="8433a7d6-3da3-4be4-a0bc-e2e3a9ebbace",
#         s_zone="ed8955b0-0ae7-4ea2-aed8-bf564a4fa05e",
#         time_standard='5',
#         between='5',
#         allowable_rate='1'
#         )))
# print(list(r11.zrangebyscore("sensor_info","-inf","+inf")))
# print("21")
# print(list(r21.scan_iter()))
# for o in r15.scan_iter():
#     print(o)
#     print(r15.get(o))
#     print("\r\n")
# r2.set("CoordSys002",json.loads( {
#         "background_images": [
#             {
#                 "filename": "CoordSys002_Background001.png",
#                 "height": 10.856594362770556,
#                 "origin_x": 0.001223986175157954,
#                 "origin_y": -0.0002957438206063756,
#                 "width": 8.342796172778888
#             }
#         ],
#         "id": "CoordSys002",
#         "name": "Starwing"
#     }))
# for o in r32.scan_iter():
#     print(o)
#     print(r32.lrange(o,0,-1))
#     print("\r\n")
# print("total",len(list(r21.scan_iter())))
# print("10")
# print(list(r10.scan_iter()))
# print("total",len(list(r10.scan_iter())))
# for o in r11.zrangebyscore("sensor_info","-inf","+inf"):

# for a in :
# print(len(list(r12.lrange(o,0,-1))))
# print("\r\n")
# for i in r3.scan_iter():
#     print(i)
#     print(json.loads(r3.get(i)))


# field  = []
# for i in r2.scan_iter():
#     field.append(dict(id=i.decode(),name=r2.get(i).decode()))
# print(field)
# r15.set(11, json.dumps(dict(
# {'id': 11, 'type': 'inside', 'time_standard': '1', 'allowable_rate': 0.2}
# )))
# print(r15.get(11))
# r15.set("99",json.dumps(dict(
#     id="99",
#     tag_id="d30524000127",
#     zone_id="Zone001",
#     type='inside',
#     time_standard='1',
#     allowable_rate='0.1',
#     stime='9',
#     etime='11'
# )))
# r15.set("100",json.dumps(dict(
#     id="100",
#     tag_id="d30524000128",
#     zone_id="Zone001",
#     type='inside',
#     time_standard='1',
#     allowable_rate='0.1',
#     stime='9',
#     etime='11'
# )))
# rp15.execute()
# r15.set("1", json.dumps(dict(
#     id="1",
#     tag_id="d30524000128",
#     zone_id="Zone001",
#     type="inside",
#     time_standard="2",
#     allowable_rate="0.1"
# )))


# """
# # id, first_tag_id, second_tag_id, type, distance, time_standard, allowable_rate, updated_at, created_at
# '251', '2', '7', 'under', '1', '1', '0.1', '2019-07-10 16:32:10', '2019-07-10 16:32:10'

# """

# r17 = redis.Redis(host=host, port=6379, db=17)
# rp17 = r17.pipeline()

# # # rp17.lset("1243",-1,"asdbb")

r18.set("1", json.dumps(dict(
    id="1",

    first_tag_id="d30524000128",
    second_tag_id="a4da22e1520c",
    type='under',
    distance="1",
    time_standard='1',
    allowable_rate='0.1'
)))
r18.set("5", json.dumps(dict(
    id="5",

    first_tag_id="d30524000128",
    second_tag_id="a4da22e15233",
    type='under',
    distance="1",
    time_standard='1',
    allowable_rate='0.1'
)))
r18.set("6", json.dumps(dict(
    id="6",
    first_tag_id="d30524000128",
    second_tag_id="a4da22e15147",
    type='under',
    distance="1",
    time_standard='1',
    allowable_rate='0.1'
)))
# rp18.execute()
# a = r17.lrange("1243",0,-1)
# print(list(r17.scan_iter()))
# print(a[:1])
# print(list(r17.lrange("1243",0,-1)).reverse())

# ar = [1,2,3,4,5,6]
# print(ar)
# print(ar[-2:])


t = time.time()
print(t)
# print(list(r8.scan_iter()))
# print(len(list(r4.scan_iter())))
count = 0
# for o in r7.scan_iter():
# pipe = redis.pipeline()

# count+=1

now = datetime.datetime.now()

start = (now - datetime.timedelta(0, 2)).timestamp()
end = now.timestamp()
print("now", end)
# print(start*100)
# print(end*100)
# # pipe.watch('tag_pos')
# data_count = 0
# r20 = redis.Redis(host='localhost', port=6379, db=20)
# rp20 = r17.pipeline()
# # print(list(r20.scan_iter()))
# print(r20.zrangebyscore("tag_to_tag", "-inf","+inf"))
# print(r6.zrangebyscore("tag_pos", start,end))
#     # pipe.watch(o)
#     # pipe.multi()

#     data_count += len(pipe.lrange(o,0,-1))
#     count+=1
# # pipe.execute()
# # print(r6.zrangebyscore("tag_pos", "-inf","+inf"))

# # # r8.hgetall()
# # #     count+=1
# # # # print(data)
# # # r7.lrange("-inf","+inf")
# # # # print(len(data))
# # # print(r7.zcount("-inf","+inf"))
# print(count,data_count)
# t2 = time.time() - t
# print(t2, time.time())


# print("with out pipe")
# t = time.time()
# print(t)
# print(list(r18.scan_iter()))
# print(r2.scan_iter())
# for k in r10.scan_iter():
#     print(k)
#     # print(r10.get(k))
#     # pprint.pprint(json.loads(r10.get(k)))
#     print("==========================\r\n")
# print("===============================================")

# for s in r13.scan_iter():
#     print(r13.get(s))
#     pprint.pprint(json.loads(r13.get(s)))
#     print("==========================\r\n")
# print(r5.get(k))
# count = 0
# # for o in r7.scan_iter():
# # pipe = redis.pipeline()

#     # count+=1

# now = datetime.datetime.now()

# start = (now - datetime.timedelta(0, 1000)).timestamp()
# end = int(now.timestamp())
# print(start*100)
# print(end*100)
# # pipe.watch('tag_pos')
# # print(r6.zrangebyscore("tag_pos", "-inf","+inf"))
# for o in  r6.zrangebyscore("tag_pos", "-inf","+inf"):
#     # pipe.watch(o)
#     # pipe.multi()
#     (r8.lrange(o,0,-1))
#     count+=1
# # pipe.execute()
# # print(r6.zrangebyscore("tag_pos", "-inf","+inf"))

# # r8.hgetall()
# #     count+=1
# # # print(data)
# # r7.lrange("-inf","+inf")
# # # print(len(data))
# # print(r7.zcount("-inf","+inf"))
# print(count)
# t2 = time.time() - t
# print(t2, time.time())


# """
# 1562137880501


# """
# # for o in range(0,10000):
# #     ndict[pickle.dumps(SomeCustomObject())] = o
# # r.zadd("d2",ndict)
# # print( r.zrange('d2',0, 100000,withscores=True))
# # t =time.time()


# # rd.lrange("tag",0,-1)


# # t =time.time()
# # print(t)

# # r.hmset("sm", {"test": "123", "test2": "1223"})
# # print(r.hmget("sm", ["test", "test2"]))
# # cursor_number, keys = r.scan(0,"test:*")
# # print(keys)
# # while True:
# #     if cursor_number == 0:
# #         break
# #     cursor_number, keys = r.scan(cursor_number,"test:*")

# # t2 =   time.time() - t
# # print(t2)
# # print(rd.zrangebyscore("2",0,100000))
# # print(rd.zrangebylex("2","-","[data99999"))
# # print( rd.zcard(2))
# # print("====field====",datetime.datetime.now())
# # for key in rd.scan_iter("field_*"):
# #     print(key, rd.get(key))
# # print(datetime.datetime.now())

# # print("====background_image====",datetime.datetime.now())
# # for key in rd.scan_iter("background_image:*"):
# #     print(key, rd.get(key))
# # print(datetime.datetime.now())

# # print("====zone====",datetime.datetime.now())
# # count = 0
# # t =time.time()
# # print("====tag====",t)
# # # for key in rd.scan_iter():
# # #     print(key, rd.get(key))
# # #     count +=1
# # # print(list(rd.scan_iter()))
# # print(rd.get(f'test:0'))
# # t2 =   time.time() - t
# # print(t2)
# # print(count)
# # print(datetime.datetime.now())

# # print("====positioningEngine====",datetime.datetime.now())
# # for key in rd.scan_iter("positioningEngine"):
# #     print(key, rd.get(key))
# # print(datetime.datetime.now())

# # count = 0
# # t =time.time()
# # print("====tag====",t)
# # engine = create_engine(
# #                 'mysql://root:sw24571275@localhost:3306/sips-middleware')
# # with engine.connect() as con:
# #     rs = con.execute('select * from zones')
# #     for row in rs:
# #         count += 1
# #     # data = [row for row in rs]
# #     # print(data)

# # t2 =   time.time() - t
# # print(t2)
# # print(count)


# # count = 0
# # t =time.time()
# # print("====tag====",t)
# # for key in rd.scan_iter("tag:*"):
# #     # print(key, rd.get(key),"\r\n")
# #     count += 1
# # t2 =   time.time() - t
# # print(t2)
# # print(count)


# # t =time.time()
# # for i in range(0,100):
# #     print(i)
# # t2 =   time.time() - t
# # print(t2)


# # t =time.time()
# # print(t)

# # rd.lrange("tag",0,-1)
# # t2 =   time.time() - t
# # print(t2)
# os.environ['TZ']='Asia/Taipei'
# "1562119720612"
# "1562138547.00"
# print(1562138786192/1000)
# print(datetime.datetime.now().timestamp())
# print(datetime.datetime.fromtimestamp(1562138786192/1000))
# import orjson
# all_config  = {
#     "sips-ip" :"http://192.168.100.241"
# }
# import requests
# s = requests.session()
# s.keep_alive = False
# r = s.get(all_config['sips-ip'] + '/api/v1/data/fieldconfig')
# if r.status_code == 200:
#     data = orjson.loads(r.text)
#     r31 = redis.Redis(host='localhost', port=6379, db=31)
#     rp31 = r31.pipeline()
#     r18 = redis.Redis(host='localhost', port=6379, db=18)
#     rp18 = r18.pipeline()
#     for data_details in data:
#         if 'zone_a' in data_details:
#             # zone to zone

#             tmp_config = dict(
#                     id=data_details['id'],
#                     tag_id=data_details['tag_id'],
#                     f_zone=data_details['zone_a'],
#                     s_zone=data_details['zone_b'],
#                     time_standard='1',
#                     between=data_details['time_standard'],
#                     allowable_rate='0.1',
#                     stime=data_details['stime'] if not data_details['stime']=="null" else "-1",
#                     etime=data_details['etime'] if not data_details['etime']=="null" else "-1"
#                 )
#             rp31.set(data_details['id'], json.dumps(tmp_config))
#         elif 'first_tag_id' in data_details:
#             # tag to tag
#             tmp_config = dict(
#                 id=data_details['id'],
#                 first_tag_id=data_details['first_tag_id'],
#                 second_tag_id=data_details['second_tag_id'],
#                 type=data_details['type'],
#                 distance=data_details['distance'],
#                 time_standard=data_details['time_standard'],
#                 allowable_rate=data_details['allowable_rate'],
#                 stime=data_details['stime'] if not data_details['stime']=="null" else "-1",
#                 etime=data_details['etime'] if not data_details['etime']=="null" else "-1"
#             )
#             r18.set(data_details['id'], json.dumps(tmp_config))
#         else:
#             # tag to zone
#             r15 = redis.Redis(host='localhost', port=6379, db=15)
#             rp15 = r15.pipeline()


#             tmp_config = dict(
#                 id=data_details['id'],
#                 tag_id=data_details['tag_id'],
#                 zone_id=data_details['zone_id'],
#                 type=data_details['type'],
#                 time_standard=data_details['time_standard'],
#                 allowable_rate=data_details['allowable_rate'],
#                 stime=data_details['stime'] if not data_details['stime']=="null" else "-1",
#                 etime=data_details['etime'] if not data_details['etime']=="null" else "-1"
#             )
#             r15.set(data_details['id'], json.dumps(tmp_config))
#     rp15.execute()
#     rp18.execute()
#     rp31.execute()
