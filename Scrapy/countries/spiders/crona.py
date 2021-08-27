import scrapy


class CronaSpider(scrapy.Spider):

    name = "crona"
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        country = response.xpath("//td/a")
        for con in country:
            name = con.xpath("./text()").get()
            link = con.xpath("./@href").get()
            absolute = response.urljoin(link)

            # yield response.follow(link, self.parse2, meta = {"name":name, "link":absolute})

    # def parse2(self, response):
    #     name = response.request.meta['name']
    #     link = response.request.meta['link']
    #     rows = response.xpath("//table[@class='table table-striped table-bordered table-hover table-condensed table-list']/tbody/tr")
    #
    #     for row in rows:
    #         year = row.xpath(".//td[1]/text()").get()
    #         population = row.xpath(".//td[2]/strong/text()").get()
    #         median_age = row.xpath(".//td[4]/text()").get()
    #         density = row.xpath(".//td[6]/text()").get()
    #         world_pop_share = row.xpath(".//td[9]/text()").get()
            yield{
            "name":name,
            "link":link}
            # "year":year,
            # "population":population,
            # "median_age":median_age,
            # "density":density,
            # "world_pop_share":world_pop_share
            # }
