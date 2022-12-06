from flask import Flask, jsonify
from flask_restplus import Api, Resource

from src.api.address_parser import PyapParser, CommonRegexParser, SpacyParser
from src.api.crawler import EaterCrawler

app = Flask(__name__)
api = Api(app, doc="/doc")

pyap_parser = PyapParser()
commonregex_parser = CommonRegexParser()
spacy_parser = SpacyParser()

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

@api.route("/parse/nlp/spacy=<path:url>")
class SpaCyParse(Resource):
    @api.doc(params={'url': 'URL containing address to crawl'})
    def get(self, url):
        return jsonify(spacy_parser.parse(url))



eater_crawler = EaterCrawler()
@api.route("/parse/crawler$url=<path:url>")
class CrawlerParse(Resource):
    @api.doc(params={'url': 'URL containing address to crawl'})
    def get(self, url):
        if ("eater" in url):
            return eater_crawler.crawl(url)


if __name__ == "__main__":
    app.run()