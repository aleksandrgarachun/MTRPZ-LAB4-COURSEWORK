import unittest
from config_schema import ConfigSchema

class TestConfigSchema(unittest.TestCase):

    def setUp(self):
        # Визначення схеми конфігурації
        self.schema = {
            'database': {
                'host': str,
                'port': int,
                'username': str,
                'password': str
            },
            'debug': bool,
            'logfile': str
        }
        self.config_schema = ConfigSchema(self.schema)

    def test_valid_config(self):
        config = {
            'database': {
                'host': "localhost",
                'port': 5432,
                'username': "user",
                'password': "pass"
            },
            'debug': True,
            'logfile': "/var/log/app.log"
        }
        self.assertTrue(self.config_schema.validate(config))

    def test_missing_key(self):
        config = {
            'database': {
                'host': "localhost",
                'username': "user",
                'password': "pass"
            },
            'debug': True,
            'logfile': "/var/log/app.log"
        }
        with self.assertRaises(ValueError):
            self.config_schema.validate(config)

    def test_incorrect_type(self):
        config = {
            'database': {
                'host': "localhost",
                'port': "5432",
                'username': "user",
                'password': "pass"
            },
            'debug': True,
            'logfile': "/var/log/app.log"
        }
        with self.assertRaises(TypeError):
            self.config_schema.validate(config)

if __name__ == '__main__':
    unittest.main()
