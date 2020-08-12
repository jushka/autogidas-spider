# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class AutogidasSpiderPipeline:
    def process_item(self, item, spider):
        for param in ['make', 'model', 'fuel_type', 'body_type', 'gearbox_type']:
            if item[param] is not None:
                item[param] = item[param].strip()

        if item['price'] is not None:
            item['price'] = item['price'].replace(' €', '').replace(' ', '')

        if item['mfd_date'] is not None:
            item['mfd_date'] = item['mfd_date'][:4]
        
        if item['mileage'] is not None:
            item['mileage'] = item['mileage'].replace(' km', '')

        return item