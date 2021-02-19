# -*- coding: utf-8 -*-
# @Auther:Summer
from elasticsearch import Elasticsearch
from elasticsearch import helpers

es = Elasticsearch(["127.0.0.1:9200"])


# 使用普通的分词器进行分词
body = {
    "analyzer":"standard",
    "text":"我是中国人"
}

body = {
    "analyzer":"ik_smart",
    "text":"我是中国人"
}
print(es.indices.analyze(body=body))