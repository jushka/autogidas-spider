import scrapy

class AutogidasSpider(scrapy.Spider):
  name = 'autogidas'

  def start_requests(self):
    # urls = ['https://autogidas.lt/skelbimai/automobiliai/?f_1%5B0%5D=&f_model_14%5B0%5D=&f_215=&f_216=&f_41=&f_42=&f_376=']
    urls = ['https://autogidas.lt/skelbimai/automobiliai/?f_1%5B0%5D=BMW&f_model_14%5B0%5D=Serija+7&f_215=&f_216=&f_41=&f_42=&f_376=']
    for url in urls:
      yield scrapy.Request(url=url, callback=self.parse)

  def parse(self, response):
    for ad in response.css('article.list-item'):
      yield {
        'make_model': ad.css('h2.item-title::text').get()
      }

    next_page = response.css('div.next-page-block > a::attr(href)').get()
    if next_page is not None:
      yield response.follow(next_page, callback=self.parse)