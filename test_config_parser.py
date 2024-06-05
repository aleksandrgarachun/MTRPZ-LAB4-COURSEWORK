import unittest
import os
from config_parser import ConfigParser

class TestConfigParser(unittest.TestCase):

    def setUp(self):
        self.config_file = 'test_config.yaml'
        with open(self.config_file, 'w') as file:
            file.write("""
database:
  host: "localhost"
  port: 5432
  username: "user"
  password: "pass"
debug: true
logfile: "/var/log/app.log"
""")

    def tearDown(self):
        if os.path.exists(self.config_file):
            os.remove(self.config_file)

    def test_parse(self):
        config_parser = ConfigParser(self.config_file)
        config = config_parser.parse()
        expected_config = {
            'database': {
                'host': "localhost",
                'port': 5432,
                'username': "user",
                'password': "pass"
            },
            'debug': True,
            'logfile': "/var/log/app.log"
        }
        self.assertEqual(config, expected_config)

if __name__ == '__main__':
    unittest.main()
