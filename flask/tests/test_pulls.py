import unittest
from handlers import pulls


class TestPulls(unittest.TestCase):

    def test_get_response_open(self):
        self.assertEqual(pulls.get_response("open")[0]["state"], "open")

    def test_get_response_closed(self):
        self.assertEqual(pulls.get_response("closed")[0]["state"], "closed")

    def test_get_outputs(self):
        expected = ['link', 'num', 'title']
        actual = []
        for item in pulls.get_outputs("needs work")[0]:
            actual.append(item)
        self.assertEqual(actual, expected)

    def test_get_outputs_else(self):
        expected = ['link', 'num', 'title']
        actual = []
        for item in pulls.get_outputs("open")[0]:
            actual.append(item)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
