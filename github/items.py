# -*- coding: utf-8 -*-
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GithubItem(scrapy.Item):
    _id = scrapy.Field()
    url = scrapy.Field()
    name_repo = scrapy.Field()
    about = scrapy.Field()
    site = scrapy.Field()
    amount = scrapy.Field()
    commits = scrapy.Field()
    last_commit_author = scrapy.Field()
    last_commit_text = scrapy.Field()
    last_commit_date = scrapy.Field()
    releases = scrapy.Field()
    last_release_version = scrapy.Field()
    last_release_date = scrapy.Field()
