# Github Crawler


A crawler for crawling github repositories using python and the scrapy framework.

The service collects the following data for each link:

+ Repository name (str);
+ Link to the user's (or project's) page(str);
+ Description (if any, str);
+ Link to the site (if any, str);
+ Number of stars (int);
+ Number of forks (int);
+ Number of followers (int);
+ Number of commits (int);
+ The author of the last commit (str);
+ The name of the last commit (str);
+ Last commit date (srt);
+ Number of releases (int);
+ Latest release version (if any, str)
+ Last release date (if any, str).

The data is stored in the MongoDB database. 


## Crawler installation and run



1. Clone this repo
```git clone git@github.com:Witaly3/github_scraping.git```
2. Enter repo folder
3. In  ```runner.py``` add necessary links. Examples:

```
if __name__ == '__main__':
    repo = 'https://github.com/Witaly3'
```
or

```
if __name__ == '__main__':
    repo = 'https://github.com/Witaly3, https://github.com/scrapy, https://github.com/celery'
```

4. In  ```pipelines.py``` by the address ``` github/ ```  set your settings for connecting to MongoDB. Example:

```
class GithubPipeline(object):
    def __init__(self):
        MONGO_URI = 'mongodb://172.17.0.2:27017/' 
        MONGO_DATABASE = 'github_db'
``` 

5. ``` sudo docker-compose up```



6. ```sudo docker-compose down```

