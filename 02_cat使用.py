# -*- coding: utf-8 -*-
# @Auther:Summer
from elasticsearch import Elasticsearch


es = Elasticsearch(["127.0.0.1:9200"])

# 查看健康状况
print(es.cat.health())
# 结果： 1613725331 09:02:11 elasticsearch yellow 1 1 8 8 0 0 2 0 - 80.0%

# 查看所有索引
print(es.cat.indices())

# 查看所有节点
print(es.cat.nodes())
# 127.0.0.1 33 95 3 0.00 0.00 0.00 cdhilmrstw * 2df5b3cb139d

# 查看主节点
print(es.cat.master())
# ZEFpNCg7T3mM19HZX6rgbQ 127.0.0.1 127.0.0.1 2df5b3cb139d