# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html



import json
import codecs
import os


class SpidertestPipeline(object):
    def __init__(self):
        return

    def process_item(self, item, spider):
        return


