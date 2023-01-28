from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from github import settings
from github.spiders.github_spider import GithubSpider


if __name__ == "__main__":
    repo = ""

    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(GithubSpider, repo=repo)
    process.start()
