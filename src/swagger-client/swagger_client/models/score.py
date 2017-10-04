# coding: utf-8

"""
    SNC API

    This is an API server for the data scraped from the SNC website.

    OpenAPI spec version: 1.0.0
    Contact: not-an-email@example.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Score(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'score': 'float',
        'team': 'str'
    }

    attribute_map = {
        'score': 'score',
        'team': 'team'
    }

    def __init__(self, score=None, team=None):
        """
        Score - a model defined in Swagger
        """

        self._score = None
        self._team = None
        self.discriminator = None

        self.score = score
        self.team = team

    @property
    def score(self):
        """
        Gets the score of this Score.

        :return: The score of this Score.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """
        Sets the score of this Score.

        :param score: The score of this Score.
        :type: float
        """
        if score is None:
            raise ValueError("Invalid value for `score`, must not be `None`")

        self._score = score

    @property
    def team(self):
        """
        Gets the team of this Score.
        Which team to update, home or away

        :return: The team of this Score.
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team):
        """
        Sets the team of this Score.
        Which team to update, home or away

        :param team: The team of this Score.
        :type: str
        """
        if team is None:
            raise ValueError("Invalid value for `team`, must not be `None`")
        allowed_values = ["home", "away"]
        if team not in allowed_values:
            raise ValueError(
                "Invalid value for `team` ({0}), must be one of {1}"
                .format(team, allowed_values)
            )

        self._team = team

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Score):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
