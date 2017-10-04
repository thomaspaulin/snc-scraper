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


class Team(object):
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
        'id': 'int',
        'name': 'str',
        'logo_url': 'str',
        'division': 'str',
        'players': 'list[Player]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'logo_url': 'logoUrl',
        'division': 'division',
        'players': 'players'
    }

    def __init__(self, id=None, name=None, logo_url=None, division=None, players=None):
        """
        Team - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._logo_url = None
        self._division = None
        self._players = None
        self.discriminator = None

        if id is not None:
          self.id = id
        self.name = name
        self.logo_url = logo_url
        self.division = division
        if players is not None:
          self.players = players

    @property
    def id(self):
        """
        Gets the id of this Team.

        :return: The id of this Team.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Team.

        :param id: The id of this Team.
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Team.

        :return: The name of this Team.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Team.

        :param name: The name of this Team.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def logo_url(self):
        """
        Gets the logo_url of this Team.

        :return: The logo_url of this Team.
        :rtype: str
        """
        return self._logo_url

    @logo_url.setter
    def logo_url(self, logo_url):
        """
        Sets the logo_url of this Team.

        :param logo_url: The logo_url of this Team.
        :type: str
        """
        if logo_url is None:
            raise ValueError("Invalid value for `logo_url`, must not be `None`")

        self._logo_url = logo_url

    @property
    def division(self):
        """
        Gets the division of this Team.

        :return: The division of this Team.
        :rtype: str
        """
        return self._division

    @division.setter
    def division(self, division):
        """
        Sets the division of this Team.

        :param division: The division of this Team.
        :type: str
        """
        if division is None:
            raise ValueError("Invalid value for `division`, must not be `None`")

        self._division = division

    @property
    def players(self):
        """
        Gets the players of this Team.

        :return: The players of this Team.
        :rtype: list[Player]
        """
        return self._players

    @players.setter
    def players(self, players):
        """
        Sets the players of this Team.

        :param players: The players of this Team.
        :type: list[Player]
        """

        self._players = players

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
        if not isinstance(other, Team):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
