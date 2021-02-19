# -*- coding: utf-8 -*-
# @Auther:Summer
from elasticsearch import Elasticsearch


es = Elasticsearch(["127.0.0.1:9200"])

# 查看索引的映射
response = es.indices.get_mapping(index="newbank")
#
# # 获取某个字段的映射
response = es.indices.get_field_mapping(fields="address", index="newbank")

# 添加映射
body = {
  "properties": {
    "email":{
      "type": "keyword",
    }
  }
}
es.indices.put_mapping(body=body, index="new_index")
response = es.indices.get_mapping(index="new_index")
print(response)
