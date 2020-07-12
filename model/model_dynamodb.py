# File: model/model_dynamodb.py
# Description: the file provides the dynamodb backend storage for memoverse

"""
The memoverse data is stored in the dynamodb database and has the following look:

+-----------+-------------------+-------+--------------+
| Reference | Theme             | Verse | Fums         |
+===========+===================+=======+==============+
| EX.1.22   | State of the Dead | <p... | <script>...  |
+-----------+-------------------+-------+--------------+


This can be created with the following command (see implementation of this file):

resource = boto3.resource("dynamodb", region_name="us-east-1")
resource.create_table(TableName, KeySchema, AttributeDefinitions, ProvisionedThroughput)

"""

from datetime import date
from .model_abstract import Model
import boto3


class model(Model):
    def __init__(self):
        self.resource = boto3.resource("dynamodb", region_name="us-east-1")
        self.table = self.resource.Table("memoverse")
        # Makes sure the database exists
        try:
            self.table.load()
        # Creates a table if it does not exist
        except:
            self.resource.create_table(
                TableName="memoverse",
                KeySchema=[
                    {
                        "AttributeName": "reference",
                        "KeyType": "HASH"
                    },
                    {
                        "AttributeName": "theme",
                        "KeyType": "RANGE"
                    }
                ],
                AttributeDefinitions=[
                    {
                        "AttributeName": "reference",
                        "AttributeType": "S"
                    },
                    {
                        "AttributeName": "theme",
                        "AttributeType": "S"
                    }
                ],
                ProvisionedThroughput={
                    "ReadCapacityUnits": 1,
                    "WriteCapacityUnits": 1
                }
            )

    # Gets verses data from the database
    def select(self):
        """
        Gets all rows from the database
        Each row contains: reference, theme, verse, and fums
        :return: list of lists containing all rows of database
        :raises: error if the table scan failed
        """
        try:
            entries = self.table.scan()
        except Exception as e:
            return([["Failed to get reference", "Failed to get theme", "Failed to get verse", "Failed to get fums"]])

        return ([[entry["reference"], entry["theme"], entry["verse"], entry["fums"]] for entry in entries["Items"]])

    # Inserts verses data into the database
    def insert(self, reference, theme, verse, fums):
        """
        Inserts entry into database
		:param reference: String
        :param theme: String
        :param verse: String
        :param fums: String
        :return: True or False
        """
        aVerse = {
            "reference" : reference,
            "theme" : theme,
            "verse" : verse,
            "fums" : fums,
        }
        try:
            self.table.put_item(Item=aVerse)
        except:
            return False

        return True