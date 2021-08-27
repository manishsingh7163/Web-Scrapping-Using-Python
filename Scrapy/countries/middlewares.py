# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class CoronaSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.
    print("THIS IS CORONAPIDERMIDDLEWARE CLASS START")
    @classmethod
    def from_crawler(cls, crawler):
        # If present, this classmethod is called to create a middleware instance from a Crawler.
        #  It must return a new instance of the middleware. Crawler object provides access to all Scrapy
        #  core components like settings and signals; it is a way for middleware to access them and hook its functionality into Scrapy.



        # This method is used by Scrapy to create your spiders.
        print("THIS IS FROM_CRWALER FUNCTION INSIDER CORONSPIDERMIDDLEWARE CLASS")
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        print("tHIS IS PROCESS SPIDER INPUT FUNCTION")
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        print("THIS IS PROCESS SPIDER OUTPUT FUNCTION")
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        print("THIS IS PROCESS SPIDER EXCEPTION FUNCTION")
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        print("tHIS IS PROCESS START REQUEST")
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class CoronaDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        print("tHIS IS CORONADOWNLOADER MIDDLEWARE PROCESS REQUEST")
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        print("tHIS IS CORONADOWNLOADER MIDDLEWARE PROCESS RESPONSE")
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        print("tHIS IS CORONADOWNLOADER MIDDLEWARE PROCESS EXCEPTION")
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
