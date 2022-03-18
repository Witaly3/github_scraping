# -*- coding: utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface

from pymongo import MongoClient


class GithubPipeline(object):
    def __init__(self):
        MONGO_URI = "mongodb+srv://witl:FWULU642L6YwsLof@cluster0.55iic.mongodb.net/myFirstDatabase?retryWrites=true&w=majority" 
        MONGO_DATABASE = 'github_db'
    
        client = MongoClient(MONGO_URI)
        self.mongo_base = client[MONGO_DATABASE]

    def process_item(self, item, spider):
        url = 'https://github.com' + item['url']
        name_repo = item['name_repo']
        about = item['about'].strip() if item['about'] else item['about']
        site = item['site']
        stars = self._integer_1(item['amount'][0]) if item['amount'] else 0
        forks = self._integer_1(item['amount'][2]) if item['amount'] else 0
        watching = self._integer_1(item['amount'][1]) if item['amount'] else 0
        commits = self._integer_2(item['commits']) if item['commits'] else 0
        last_commit_author = item['last_commit_author']
        last_commit_text = self._commit_text(item['last_commit_text'])
        last_commit_date = item['last_commit_date']
        releases = int(item['releases']) if item['releases'] else 0
        last_release_version = item['last_release_version']
        last_release_date = item['last_release_date']

        github_json = {
            'url': url,
            'name_repo': name_repo,
            'about': about,
            'site': site,
            'stars': stars,
            'forks': forks,
            'watching': watching,
            'commits': commits,
            'last_commit_author': last_commit_author,
            'last_commit_text': last_commit_text,
            'last_commit_date': last_commit_date,
            'releases': releases,
            'last_release_version': last_release_version,
            'last_release_date': last_release_date
        }

        collection = self.mongo_base[spider.name]
        collection.insert_one(github_json)

        return github_json

    def _integer_1(self, value):
        return (float(value[:-1]) * 1000) if 'k' in value else int(value)

    def _integer_2(self, value):
        return int(value.replace(',', ''))  if ',' in value else int(value)
    
    def _commit_text(self, text):
        return text[:-2] if text[-1] == '(' else text
