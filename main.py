from flask import Flask, jsonify
from flask_restplus import Api, Resource

from src.address_parser import PyapParser, CommonRegexParser
from src.crawler import EaterCrawler

app = Flask(__name__)
api = Api(app)

pyap_parser = PyapParser()
commonregex_parser = CommonRegexParser()
#lexnlp_parser = LexnlpParser()

@api.route("/parse/regex/pyap$url=<path:url>")
class RegexPyapParse(Resource):
    @api.doc(params={'url': 'URL containing address to crawl'})
    def get(self, url):
        return jsonify(pyap_parser.parse(url))

@api.route("/parse/regex/commonregex$url=<path:url>")
class RegexCommonRegexParse(Resource):
    @api.doc(params={'url': 'URL containing address to crawl'})
    def get(self, url):
        return jsonify(commonregex_parser.parse(url))

@api.route("/parse/lexnlp=<path:url>")
class SpaCyParse(Resource):
    @api.doc(params={'url': 'URL containing address to crawl'})
    def get(self, url):
        return jsonify(lexnlp_parser.parse(url))


eater_crawler = EaterCrawler()
@api.route("/parse/crawler$url=<path:url>")
class CrawlerParse(Resource):
    @api.doc(params={'url': 'URL containing address to crawl'})
    def get(self, url):
        if ("eater" in url):
            return eater_crawler.crawl(url)


if __name__ == "__main__":
    app.run()