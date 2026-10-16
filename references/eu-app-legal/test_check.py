"""Offline regression tests for the legal-reference fingerprint extractor."""

import unittest

from check import ReadableText, normalize_text


class ReadableTextTests(unittest.TestCase):
    def test_prefers_article_and_ignores_navigation(self):
        html = (
            "<html><body><nav>Navigation changes daily</nav>"
            "<main><article>" + ("Privacy and account data. " * 30) + "</article></main>"
            "<footer>Copyright 2026</footer>"
            "<script>tracker_secret = 'not a policy'</script></body></html>"
        )
        parser = ReadableText()
        parser.feed(html)
        actual = parser.text()
        self.assertIn("Privacy and account data", actual)
        self.assertNotIn("Navigation changes", actual)
        self.assertNotIn("tracker_secret", actual)
        self.assertNotIn("Copyright 2026", actual)

    def test_normalization_is_stable_across_whitespace_and_entities(self):
        a = normalize_text("Title \n\n GDPR &amp; Privacy   Notice")
        b = normalize_text("Title GDPR & Privacy Notice")
        self.assertEqual(a, b)

    def test_fallback_if_no_article_or_main(self):
        parser = ReadableText()
        parser.feed("<body>Legal <p>Privacy requirements</p><footer>skip me</footer></body>")
        self.assertEqual(parser.text(), "Legal Privacy requirements")


if __name__ == "__main__":
    unittest.main()
