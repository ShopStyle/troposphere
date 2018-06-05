import unittest
from troposphere import cloudfront


class TestCloudfront(unittest.TestCase):

    def test_logging(self):

        logging = cloudfront.Logging(
            Bucket='mytestbucket',
            IncludeCookies=True,
            Prefix='myprefix',
        )

        d = logging.to_dict()
        self.assertEquals(d['IncludeCookies'], True)


if __name__ == '__main__':
    unittest.main()
