#!/usr/bin/env python
#coding=utf8

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")

import time
from .sample_common import MNSSampleCommon
from mns.account import Account
from mns.topic import *

#从sample.cfg中读取基本配置信息
## WARNING： Please do not hard code your accessId and accesskey in next line.(more information: https://yq.aliyun.com/articles/55947)
accid,acckey,endpoint,token = MNSSampleCommon.LoadConfig()

#初始化 my_account, my_topic
my_account = Account(endpoint, accid, acckey, token)
topic_name = sys.argv[1] if len(sys.argv) > 1 else "MySampleTopic"
my_topic = my_account.get_topic(topic_name)

#删除主题
try:
    my_topic.delete()
    print("Delete Topic Succeed! TopicName:%s\n" % topic_name)
except MNSExceptionBase as e:
    print("Delete Topic Fail! Exception:%s\n" % e)
