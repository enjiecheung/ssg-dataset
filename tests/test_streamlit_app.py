from streamlit_app import Badge

class TestBadge:
    def setup_method(self):
        self.b = Badge("SSG", "43", "pink")
        self.url = "http://www.nba.com"

    def test_start(self):
        assert self.b.image().startswith("<svg xmlns=")

    def test_end(self):
        assert self.b.image().endswith("</svg>")

    def test_link(self):
        assert self.url in self.b.image_with_link(self.url)