import scrapy

class AutogidasSpider(scrapy.Spider):
  name = 'autogidas'

  def start_requests(self):
    # urls = ['https://autogidas.lt/skelbimai/automobiliai/?f_1%5B0%5D=&f_model_14%5B0%5D=&f_215=&f_216=&f_41=&f_42=&f_376='] #all ads
    # urls = ['https://autogidas.lt/skelbimai/automobiliai/?f_1%5B0%5D=Alfa+Romeo&f_model_14%5B0%5D=&f_215=&f_216=&f_41=&f_42=&f_376='] #alfa romeo: 24 ads
    urls = ['https://autogidas.lt/skelbimai/automobiliai/?f_1%5B0%5D=BMW&f_model_14%5B0%5D=Serija+7&f_215=&f_216=&f_41=&f_42=&f_376='] #bmw 7 series: 74 ads
    # urls = ['https://autogidas.lt/skelbimai/automobiliai/?f_1%5B0%5D=BMW&f_model_14%5B0%5D=&f_215=&f_216=&f_41=&f_42=&f_376='] #bmw: 1061 ads
    for url in urls:
      yield scrapy.Request(url=url, callback=self.parse)

  def parse(self, response):
    ads_links = response.css('article.list-item > a::attr(href)').getall()
    yield from response.follow_all(ads_links, self.parse_ad)

    next_page = response.css('div.next-page-block > a::attr(href)').get()
    if next_page is not None:
      yield response.follow(next_page, self.parse)

  def parse_ad(self, response):
    params_block = response.xpath('//div[@class="params-block"][2]')
    keys = params_block.xpath('.//div[@class="left"]/text()').getall()
    values = params_block.xpath('.//div[@class="right"]/text()').getall()
    params = dict(zip(keys, values))
    price = response.xpath('//div[@class="params-block"][1]//div[@class="price"]/text()').get()
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