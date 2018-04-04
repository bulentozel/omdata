# -*- coding: utf-8 -*-
"""The unit testing module.

"""
import unittest
import sys
import os
sys.path.insert(0, os.path.abspath('../'))

from omdata.validator import check_json


ajson = {
  "id": 1,
  "name": "Roni Bulent",
  "projects": {
    "individual": 5,
    "team": 10
  },
  "tags": [
    "transparency",
    "green"
  ]
}

bjson = {k:v for k,v in ajson.items() if k not in ["id"]}

theschema = {
  "$id": "http://example.com/example.json",
  "required":["name","id"],
  "type": "object",
  "definitions": {},
  "$schema": "http://json-schema.org/draft-07/schema#",
  "properties": {
    "id": {
      "$id": "/properties/id",
      "type": "integer",
      "title": "The Id Schema ",
      "default": 0,
      "examples": [
        1
      ]
    },
    "name": {
      "$id": "/properties/name",
      "type": "string",
      "title": "The Name Schema ",
      "default": "",
      "examples": [
        "Roni Bulent"
      ]
    },
    "projects": {
      "$id": "/properties/projects",
      "type": "object",
      "properties": {
        "individual": {
          "$id": "/properties/projects/properties/individual",
          "type": "integer",
          "title": "The Individual Schema ",
          "default": 0
        },
        "team": {
          "$id": "/properties/projects/properties/team",
          "type": "integer",
          "title": "The Team Schema ",
          "default": 0,
          "examples": [
            10
          ]
        }
      }
    },
    "tags": {
      "$id": "/properties/tags",
      "type": "array",
      "items": {
        "$id": "/properties/tags/items",
        "type": "string",
        "title": "The 0th Schema ",
        "default": "",
        "examples": [
          "transparency",
          "green"
        ]
      }
    }
  }
}

class ValidatorTestSuite(unittest.TestCase):
    """Testing suit for the validator.
    """

    def test_true_positive(self):
        self.assertTrue(check_json(ajson, theschema))
  
    def test_true_negative(self):
        self.assertFalse(check_json(bjson, theschema))

if __name__ == '__main__':
    unittest.main()
