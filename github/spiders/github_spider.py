# -*- coding: utf-8 -*-

import scrapy
from github.items import GithubItem


class GithubSpider(scrapy.Spider):
    name = "github"

    def __init__(self, repo):
        super(GithubSpider, self).__init__()
        self.start_urls = []

        for row in repo.split(", "):
            self.start_urls.append(row)

    def parse(self, response):
        next_page = response.css("a.UnderlineNav-item::attr(href)")[1].get()
        yield response.follow(next_page, callback=self.parse_repo)

    def parse_repo(self, response):
        for link in response.css("h3.wb-break-all a::attr(href)").getall():
            yield response.follow(link, callback=self.parse_content)

        next_page_repo1 = response.css(
            "a.btn.btn-outline.BtnGroup-item::attr(href)"
        ).get()
        next_page_repo2 = response.css("a.next_page::attr(href)").get()
        next_page_repo = next_page_repo1 if next_page_repo1 else next_page_repo2

        if next_page_repo:
            yield response.follow(next_page_repo, callback=self.parse_repo)

    def parse_content(self, response):
        item = GithubItem()

        item["url"] = response.css(".url::attr(href)").get()
        item["name_repo"] = response.css("strong.mr-2.flex-self-stretch a::text").get()
        item["about"] = response.css("p.f4.my-3::text").get()
        item["site"] = response.css(
            "div.my-3:nth-child(3) > span:nth-child(2) > a:nth-child(1)::text"
        ).get()
        item["amount"] = response.css("a.Link--muted strong::text").getall()
        item["commits"] = response.css(
            "a.pl-3 > span:nth-child(2) > strong:nth-child(1)::text"
        ).get()
        item["releases"] = response.css(
            "div.BorderGrid-row:nth-child(2) > div:nth-child(1) > h2:nth-child(1) > a:nth-child(1) > span:nth-child(1)::text"
        ).get()
        item["last_release_version"] = response.css(
            "span.mr-2:nth-child(1)::text"
        ).get()
        item["last_release_date"] = response.css(
            "div.BorderGrid-row:nth-child(2) > div:nth-child(1) > a:nth-child(2) > div:nth-child(2) > div:nth-child(2) > relative-time:nth-child(1)::attr(datetime)"
        ).get()

        next_page_commit = response.css("a.pl-3::attr(href)").get()

        return response.follow(
            next_page_commit, self.parse_commit, cb_kwargs=dict(item=item)
        )

    def parse_commit(self, response, item):
        item["last_commit_author"] = response.css(".commit-author::text").get()
        item["last_commit_text"] = response.css(
            "a.Link--primary.text-bold.js-navigation-open.markdown-title::text"
        ).get()
        item["last_commit_date"] = response.css(
            "relative-time.no-wrap::attr(datetime)"
        ).get()

        return item
