import scrapy


class NepalTradeSpider(scrapy.Spider):
    name = 'nepal_import'

    fiscal_year = '2079/2080'
    date_type = '1'  # 1 for fiscal year
    data_type = 'Export'  # Import or Export
    _date = '1694326512719'  # epoch time
    # start_urls = ['https://nepaltradeportal.gov.np/api1/normal-report/static-report/by/commodity/only?dataType=Import&dateType=1&fiscalYear=2079/2080&_=1694326512719']
    start_urls = [
        f'https://nepaltradeportal.gov.np/api1/normal-report/static-report/by/commodity/only?dataType={data_type}&dateType={date_type}&fiscalYear={fiscal_year}&_={_date}']

    def parse(self, response):
        data = response.json()
        json_data = data.get('data')
        for data_ in json_data:  #
            yield data_
