# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class AutogidasSpiderPipeline:
    def process_item(self, item, spider):
        item['make'] = item['make'].strip()
        item['model'] = item['model'].strip()
        item['fuel_type'] = item['fuel_type'].strip()
        item['body_type'] = item['body_type'].strip()
        item['gearbox_type'] = item['gearbox_type'].strip()
        item['price'] = item['price'].replace(' €', '').replace(' ', '')
        item['mfd_date'] = item['mfd_date'][:4]
        if item['mileage'] is not None:
            item['mileage'] = item['mileage'].replace(' km', '')

        return item