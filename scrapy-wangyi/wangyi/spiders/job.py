import scrapy
from bs4 import BeautifulSoup
from wangyi.items import WangyiItem
import re

class JobSpider(scrapy.Spider):
    name = 'job'
    allowed_domains = ['163.com']
    start_urls = ['https://hr.163.com/position/list.do?currentPage=1']


    def parse(self, response, *args ,**kwargs):
        # 提取数据
        # 获取所有职位节点列表
        # item = WangyiItem()
        # with open('wangyi.html', 'wb')as f:
        #     f.write(response.body)
        # file = open("./wangyi.html", "rb")
        # html = file.read().decode("utf-8")
        # //*[@class="position-tb"]/tbody/tr[1]

        # node_list = response.xpath('//*[@class="position-tb"]').get()
        # bs = BeautifulSoup(html,'html.parser')
        # print(html)
        # print(type(html))
        # with open('wangyi.html', 'wb')as f:
        #     f.write(response.body)
        node_list = response.xpath('//*[@class="position-tb"]/tbody/tr')
        for num, node in enumerate(node_list):
            if num % 2 == 0:
                item = WangyiItem()
                item['name'] = node.xpath('./td[1]/a/text()').get()
                item['link'] = response.urljoin(node.xpath('./td[1]/a/@href').get())
                # item['link'] = 'https://hr.163.com/' +  node.xpath('./td[1]/a/@href')
                item['depart'] = node.xpath('./td[2]/text()').get()
                item['category'] = node.xpath('./td[3]/text()').get()
                item['type'] = node.xpath('./td[4]/text()').get()
                item['address'] = node.xpath('./td[5]/text()').get()
                item['num'] = node.xpath('./td[6]/text()').get().strip()
                item['date'] = node.xpath('./td[7]/text()').get()
                # yield item
                # 构建详情页面的请求
                yield scrapy.Request(
                    url=item['link'],
                    callback=self.parse_detail,
                    meta = {'item': item}
                )
    #
        # 模拟翻页
        part_url = response.xpath('/html/body/div[2]/div[2]/div[2]/div/a[last()]/@href').get()
        # 判断最后一页
        if part_url != 'javascript:void(0)':
            next_url = response.urljoin(part_url)
            # 构建请求对象返回给引擎
            yield scrapy.Request(
                url=next_url,
                callback=self.parse,
            )
    #
    def parse_detail(self,response):
        item = response.meta['item']
        item['duty'] = response.xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/div/text()').getall()
        item['require'] = response.xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div/text()').getall()
        yield item