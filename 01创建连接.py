# -*- coding: utf-8 -*-
# @Auther:Summer
from elasticsearch import Elasticsearch


## 指定连接
es = Elasticsearch(
    ['127.0.0.1:9200'],
    # 认证信息
    # http_auth=('elastic', 'changeme')
)


# ## 动态连接
# es = Elasticsearch(
#     ['esnode1:port', 'esnode2:port'],
#     # 在做任何操作之前，先进行嗅探
#     sniff_on_start=True,
#     # 节点没有响应时，进行刷新，重新连接
#     sniff_on_connection_fail=True,
#     # 每 60 秒刷新一次
#     sniffer_timeout=60
# )


print(es.cat.indices())  # 打印出ES的所有索引
