import subprocess

def run_spider():
    spider_name = "coronaCrawler"
    subprocess.check_output(['scrapy', 'crawl', spider_name])
