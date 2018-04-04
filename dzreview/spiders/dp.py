# -*- coding: utf-8 -*-
import scrapy


class DpSpider(scrapy.Spider):
    name = "dp"
    allowed_domains = ["dianping.com"]
    start_urls = (
        'http://www.dianping.com/guangzhou/ch10',
    )

    def parse(self, response):
        cate_list = response.xpath('//div[@id="classfy"]/a/@href').extract()[0:5]
        print(cate_list)
        for cate_url in cate_list:
            yield scrapy.Request(
                cate_url,
                headers={'Referer:http':'http://www.dianping.com/guangzhou/ch10/g210'},
                callback=self.parse_detail
            )

    def parse_detail(self,response):
        u = response.url
        file_name = u.split('/')[-1]
        with open('./'+file_name+'.html','w') as f:
            f.write(response.body.decode())
            print('>>>>>>>>>>>ok<<<<<<<<<<<')
