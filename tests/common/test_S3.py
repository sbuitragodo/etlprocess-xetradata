"""TestS3BucketConnectorMethods"""
import os
import unittest

import boto3
from moto import mock_s3

from xetra.common.s3 import S3BucketConnector


class TestS3BucketConnectorMethods(unittest.TestCase):
    """
    Testing S3BucketConnector class
    """

    def setUp(self):
        """
        Setting up the environment
        """
        # Mocking s3 connection start
        self.mock_s3 = mock_s3()
        self.mock_s3.start
        # Defining the class arguments
        self.s3_access_key = 'AWS_ACCESS_KEY_ID'
        self.s3_secret_key = 'AWS_SECRET_ACCESS_KEY'
        self.s3_endpoint_url = 'https://s3.us-east-1.amazonaws.com'
        self.s3_bucket_name = 'test-bucket'
        # Creating S3 environment variables
        os.environ[self.s3_access_key] = 'KEY1'
        os.environ[self.s3_secret_key] = 'KEY2'
        # Creting the mocked in the S3
        self.s3 = boto3.resource(service_name='s3', endpoint_url=self.s3_endpoint_url)
        self.s3.create_bucket(Bucket=self.s3_bucket_name,
                              CreateBucketConfiguration={
                                  'LocationConstraint': 'us-east-1'
                              })
        self.s3_bucket = self.s3.Bucket(self.s3_bucket_name)

    def tearDown(self):
        """
        Executing after unittest
        """
        pass

    def test_list_files_in_prefix_ok(self):
        """
        Test the list_files_in_prefix method for getting2 file keys
        as list on the mocked s3 bucket
        """
        pass

    def test_list_files_in_prefix_wrong_prefix(self):
        """
        Test the list_file_in_prefix method in case of a
        wrong or not existing prefix
        """
        pass

    if __name__ == "__main__":
        unittest.main()