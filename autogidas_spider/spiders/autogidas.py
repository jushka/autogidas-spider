import scrapy

class AutogidasSpider(scrapy.Spider):
  name = 'autogidas'
  start_urls = [
    'https://autogidas.lt/skelbimai/automobiliai/?f_1%5B0%5D=&f_model_14%5B0%5D=&f_215=&f_216=&f_41=&f_42=&f_376='
  ]

  def parse(self, response):
    ads_links = response.css('article.list-item > a::attr(href)').getall()
    yield from response.follow_all(ads_links, self.parse_ad)

    next_page = response.css('div.next-page-block > a::attr(href)').get()
    if next_page is not None:
      yield response.follow(next_page, self.parse)

  def parse_ad(self, response):
    params_blocks = response.xpath('//div[@class="params-block"]')
    keys = params_blocks[1].xpath('.//div[@class="left"]/text()').getall()
    values = params_blocks[1].xpath('.//div[@class="right"]/text()').getall()
    params = dict(zip(keys, values))
    price = params_blocks[0].xpath('.//div[@class="price"]/text()').get()
    img_url = response.xpath('//div[@class="big-photo"]/img/@src').get()

    yield {
      'make': params.get('Markė'),
      'model': params.get('Modelis'),
      'mfd_date': params.get('Metai'),
      'fuel_type': params.get('Kuro tipas'),
      'body_type': params.get('Kėbulo tipas'),
      'gearbox_type': params.get('Pavarų dėžė'),
      'mileage': params.get('Rida, km'),
      'price': price,
      'img_url': img_url
    }