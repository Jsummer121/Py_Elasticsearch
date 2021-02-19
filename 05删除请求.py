# -*- coding: utf-8 -*-
# @Auther:Summer
from elasticsearch import Elasticsearch

es = Elasticsearch(["127.0.0.1:9200"])

# 删除数据
body = {
	"query": {
		"match": {
			"address": "mill"
		}
	}
}
es.delete_by_query(index="newbank", body=body)
# 指定标识符删除
es.delete(index="newbank", id="pre_val")
