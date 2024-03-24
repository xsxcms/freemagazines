import scrapy

class MySpider(scrapy.Spider):
    name = "myspider"
    start_urls = [
        # 'https://freemagazines.top/?s=economist',
        'https://freemagazines.top/technology-science',
    ]

    def parse(self, response):
        # Extracting links from current page
        post_image_divs = response.css('div.post-image')
        for post_image_div in post_image_divs:
            first_a_tag = post_image_div.css('a').attrib['href']
            if first_a_tag.startswith('https://vk.com/doc'):
                # If link starts with 'https://vk.com/doc', save it
                with open('vk_links.txt', 'a') as f:
                    f.write(first_a_tag + '\n')

        # Getting next page link and follow it
        next_page_link = response.css('a.next.page-numbers').attrib['href']
        if next_page_link:
            yield response.follow(next_page_link, callback=self.parse)

        # Follow each link in div.post-image to find VK links
        for post_image_div in post_image_divs:
            link = post_image_div.css('a').attrib['href']
            yield response.follow(link, callback=self.parse_vk_document)

    def parse_vk_document(self, response):
        # Parsing the VK document page
        vk_links = response.css('a').xpath('@href').extract()
        for link in vk_links:
            if link.startswith('https://vk.com/doc'):
                # If link starts with 'https://vk.com/doc', save it
                with open('vk_links.txt', 'a') as f:
                    f.write(link + '\n')

