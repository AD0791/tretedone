from app import app
import unittest
import json
import sys

class Testereketstok(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
    def testereketstok(self):
        repons=self.client.post('/', json=dict(
            kant=10,
            non="bannann",
            tip="aliman"
        ))
        rejson = json.loads(repons.get_data().decode(sys.getdefaultencoding()))
        self.assertEqual(len(rejson),10)




if __name__ == "__main__":
    unittest.main()

