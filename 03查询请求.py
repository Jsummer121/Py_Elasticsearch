# -*- coding: utf-8 -*-
# @Auther:Summer
from elasticsearch import Elasticsearch

es = Elasticsearch(['127.0.0.1:9200'])

# 查询全部文档
body = {
	"query": {
		"match_all": {}
	}
}

# 精确检索
body = {
	"query": {
		"match": {
			"account_number": "20"
		}
	}
}

# 全文检索
body = {
  "query": {
    "match": {
      "address": "mill"
    }
  }
}

# 短语匹配
body = {
  "query": {
    "match_phrase": {
      "address": "mill road"
    }
  }
}

# 多字段匹配
body = {
  "query": {
    "multi_match": {
      "query": "mill",
      "fields": ["address", "city"]
    }
  }
}

# 复合查询
## must
body = {
  "query": {
    "bool": {
      "must": [
        {"match": {
          "address": "mill"
        }},
        {"match": {
            "gender": "M"
          }}
      ]
    }
  }
}

## must_not
body = {
  "query": {
    "bool": {
      "must": [
        {"match": {
          "address": "mill"
        }},
        {"match": {
            "gender": "M"
          }}
      ],
      "must_not": [
        {"match": {
          "age": "38"
        }}
      ]
    }
  }
}

## should
body = {
  "query": {
    "bool": {
      "must": [
        {"match": {
          "address": "mill"
        }},
        {"match": {
            "gender": "M"
          }}
      ],
      "should": [
        {"match": {
          "age": "38"
        }}
      ]
    }
  }
}

# filter
body = {
  "query": {
    "bool": {
      "filter": {
        "range": {
          "balance": {
            "gte": 20000,
            "lte": 30000
          }
        }
      }
    }
  }
}

# term
body = {
  "query": {
    "term": {
      "balance": {
        "value": "32838"
      }
    }
  }
}

# terms
body = {
  "query": {
    "terms": {
      "firstname": [
        "Nanette",
        "Forbes"
      ]
    }
  }
}

#
body = {
  "query": {
    "match_all": {}
  },
  "aggs": {
    "aggAgg": {
      "terms": {
        "field": "age",
        "size": 100
      },
      "aggs": {
        "genderAgg": {
          "terms": {
            "field": "gender.keyword",
            "size": 10
          },
          "aggs": {
            "balanceAvg": {
              "avg": {
                "field": "balance"
              }
            }
          }
        },
        "ageBananceAvg":{
          "avg": {
            "field": "balance"
          }
        }
      }
    }
  },
  "size": 0
}

# 切片式查询
body = {
  "query": {
    "match_all": {}
  }
  , "from": 10
  , "size": 5
}

# sort
body = {
  "query": {
    "match_all": {}
  }
  , "sort": [
    {
      "age": {
        "order": "desc"
      }
    }
  ]
}

response = es.search(index="newbank", body=body)

print(response)
