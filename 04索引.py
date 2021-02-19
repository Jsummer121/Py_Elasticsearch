# -*- coding: utf-8 -*-
# @Auther:Summer
from elasticsearch import Elasticsearch
from elasticsearch import helpers

es = Elasticsearch(["127.0.0.1:9200"])

# 创建索引
es.indices.create("index_name")

# 指定mapping
# es.indices.create("index_name", body = mapping)

# 删除索引
es.indices.delete("index_name")

# 重建索引
body = {"query": {"match_all": {}}}
helpers.reindex(client=es,
                source_index="old_index_name",
                target_index="new_index_name",
                target_client=es,
                query=body)

# 查看所有索引
indexs = es.indices.get("*")

# 查看es中索引的索引名
index_name = indexs.keys()

# 查看某个索引
index = es.indices.get("index_name")

# 判断某个索引是否存在
es.indices.exists("index_name")
