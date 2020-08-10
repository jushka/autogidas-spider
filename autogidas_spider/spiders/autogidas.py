import scrapy

class AutogidasSpider(scrapy.Spider):
  name = 'autogidas'

  def start_requests(self):
    urls = ['https://autogidas.lt/skelbimai/automobiliai/?f_1%5B0%5D=&f_model_14%5B0%5D=&f_215=&f_216=&f_41=&f_42=&f_376=']
    for url in urls:
      yield scrapy.Request(url=url, callback=self.parse)

  def parse(self, response):
    pass