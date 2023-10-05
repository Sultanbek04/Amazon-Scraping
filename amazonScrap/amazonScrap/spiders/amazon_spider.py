import scrapy
from ..items import AmazonscrapItem


class AmazonSpiderSpider(scrapy.Spider):
    name = "amazon"
    page_number = 2
    start_urls = [
        "https://www.amazon.co.uk/s?rh=n%3A15512062031&language=en_GB&brr=1&content-id=amzn1.sym.3642feb9-f459-485e-b5f9-8e67b609eacd&pd_rd_r=071c4dbd-133e-4fc4-b0a4-b3c21f1b6ef1&pd_rd_w=lYgkZ&pd_rd_wg=ZpnGZ&pf_rd_p=3642feb9-f459-485e-b5f9-8e67b609eacd&pf_rd_r=7NKGH8HV1VD46ZGQTWSP&rd=1&ref=Oct_d_odnav_d_4511104031_2"
    ]

    def parse(self, response):
        items = AmazonscrapItem()
        product_name = response.css('.a-color-base.a-text-normal').css('::text').extract()
        product_author = response.css('.a-color-secondary .a-size-base+ .a-size-base').css('::text').extract()
        product_imagelink = response.css('.s-image::attr(src)').extract()

        items['product_name'] = product_name
        items['product_author'] = product_author
        items['product_imagelink'] = product_imagelink

        yield items

        next_page = 'https://www.amazon.co.uk/s?i=stripbooks&rh=n%3A15512062031&page=' + str(
            AmazonSpiderSpider.page_number) + '&language=en_GB&brr=1&content-id=amzn1.sym.3642feb9-f459-485e-b5f9-8e67b609eacd&pd_rd_r=071c4dbd-133e-4fc4-b0a4-b3c21f1b6ef1&pd_rd_w=lYgkZ&pd_rd_wg=ZpnGZ&pf_rd_p=3642feb9-f459-485e-b5f9-8e67b609eacd&pf_rd_r=7NKGH8HV1VD46ZGQTWSP&qid=1696542353&rd=1&ref=sr_pg_2'

        if AmazonSpiderSpider.page_number <= 75:
            AmazonSpiderSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
