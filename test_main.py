from unittest import TestCase
import main
from pathlib import Path


class Test(TestCase):
    def setUp(self):
        self.test_html = Path("./fixtures/web_scraping_archive.html").read_text()

    def test_parse_html_no_result(self):
        assert main.parse_html("") == {}

    def test_parse_html_success(self):
        assert main.parse_html(self.test_html) == {}