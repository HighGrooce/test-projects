import scrapy
from wangyi.items import Wangyi2Item

class Job2Spider(scrapy.Spider):

    name = 'job2'
    allowed_domains = ['163.com']
    start_urls = ['https://hr.163.com/position/list.do?currentPage=1']

    def parse(self, response, *args, **kwargs):

            node_list = response.xpath('//*[@class="position-tb"]/tbody/tr')
            for num, node in enumerate(node_list):
                if num % 2 == 0:
                    item = Wangyi2Item()
                    item['name'] = node.xpath('./td[1]/a/text()').get()
                    item['link'] = response.urljoin(node.xpath('./td[1]/a/@href').get())
                    # item['link'] = 'https://hr.163.com/' +  node.xpath('./td[1]/a/@href')
                    item['depart'] = node.xpath('./td[2]/text()').get()
                    item['category'] = node.xpath('./td[3]/text()').get()
                    item['type'] = node.xpath('./td[4]/text()').get()
                    item['address'] = node.xpath('./td[5]/text()').get()
                    item['num'] = node.xpath('./td[6]/text()').get().strip()
                    item['date'] = node.xpath('./td[7]/text()').get()
                    yield item


            part_url = response.xpath('/html/body/div[2]/div[2]/div[2]/div/a[last()]/@href').get()
            if part_url != 'javascript:void(0)':
                next_url = response.urljoin(part_url)
                        # 构建请求对象返回给引擎
                yield scrapy.Request(
                    url=next_url,
                    callback=self.parse,
                )



        # def parse_detail(self, response):
        #     item = response.meta['item']
        #     item['duty'] = response.xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/div/text()').getall()
        #     item['require'] = response.xpath(
        #         '/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div/text()').getall()
        #     yield item
