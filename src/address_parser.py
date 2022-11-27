from abc import ABC, abstractmethod
import pyap
import requests
from commonregex import CommonRegex
from bs4 import BeautifulSoup
from bs4.element import Comment
import spacy
from spacy.tokens import Span
from spacy.language import Language
from spacy.matcher import Matcher, PhraseMatcher
from spacy.lang.en import English

class AddressParser(ABC):
    def tag_visible(self, element):
        if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
            return False
        if isinstance(element, Comment):
            return False
        return True

    def text_from_html(self, body):
        soup = BeautifulSoup(body, 'html.parser')
        texts = soup.findAll(text=True)
        visible_texts = filter(self.tag_visible, texts)
        return u" ".join(t.strip() for t in visible_texts)

    @abstractmethod
    def parse(self, url: str) -> str:
        pass

class PyapParser(AddressParser):
    def parse(self, url: str) -> str:
        req = requests.get(url)
        addresses = pyap.parse(self.text_from_html(req.text), country="us")
        return list(set([str(address) for address in addresses]))

class CommonRegexParser(AddressParser):
    def __init__(self):
        self.parser = CommonRegex()

    def parse(self, url: str) -> str:
        req = requests.get(url)
        addresses = self.parser.street_addresses(self.text_from_html(req.text))
        return list(set([str(address) for address in addresses]))

class SpacyParser(AddressParser):

    def parse(self, url: str) -> str:
        req = requests.get(url)
    #    nlp = spacy.load("en_core_web_sm")
        nlp = English()

        matcher = Matcher(nlp.vocab)
        matcher.add("address", [
            [
                {"ENT_TYPE": 'BUILDING_NO'},
                {"ENT_TYPE": 'STREET_NAME', "OP": "+"},
                {"IS_PUNCT": True},
                {"ENT_TYPE": 'CITY'},
                {"IS_PUNCT": True},
                {"ENT_TYPE": 'STATE'},
                {"ENT_TYPE": 'BUILDING_NO'}
            ]
        ])

        doc = nlp(self.text_from_html(req.text))
        addresses = set()
        for match_id, start, end in matcher(doc):
            addresses.add(doc[start:end].text)
        return list(addresses)
"""

matcher.add("address", [[{"ENT_TYPE": 'BUILDING_NO'}, {"ENT_TYPE": 'STREET_NAME', "OP": "+"}, {"IS_PUNCT": True}, {"ENT_TYPE": 'CITY'}, {"IS_PUNCT": True}, {"ENT_TYPE": 'STATE'}, {"ENT_TYPE": 'BUILDING_NO'}]])

        ('315', 'BUILDING_NO'), ('Shawmut Ave', 'STREET_NAME'), ('Boston', 'CITY'), ('MA', 'STATE'), ('02118', 'BUILDING_NO')
        matcher.add("address", [
            nlp("5313 Ballard Ave NW #3148, Seattle, WA 98107"),
            nlp("5313 Ballard Ave NW Ste A, Seattle, WA 98107"),
            nlp("5313 Ballard Ave NW, Seattle, WA 98107"),
            nlp("5313 Ballard Ave N, Seattle, WA 98107"),
            nlp("5313 NW Ballard Ave, Seattle, WA 98107"),
            nlp("5313 NW 12th St, Seattle, WA 98107"),
            nlp("5313 NW 12th St #3148, Seattle, WA 98107"),
            nlp("531 N 12th St, Seattle, WA 98107"),
            nlp("531 N Ballard Way, Seattle, WA 98107"),
            nlp("89 Holland St, Somerville, MA 02144"),
            nlp("8 Holland St, Somerville, MA 02144"),
        ])

"""