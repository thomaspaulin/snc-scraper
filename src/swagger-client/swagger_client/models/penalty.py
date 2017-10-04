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


class Penalty(object):
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
        'period': 'int',
        'team': 'Team',
        'time': 'int',
        'offense': 'str',
        'offender': 'str',
        'pim': 'int'
    }

    attribute_map = {
        'period': 'period',
        'team': 'team',
        'time': 'time',
        'offense': 'offense',
        'offender': 'offender',
        'pim': 'pim'
    }

    def __init__(self, period=None, team=None, time=None, offense=None, offender=None, pim=None):
        """
        Penalty - a model defined in Swagger
        """

        self._period = None
        self._team = None
        self._time = None
        self._offense = None
        self._offender = None
        self._pim = None
        self.discriminator = None

        self.period = period
        self.team = team
        self.time = time
        self.offense = offense
        self.offender = offender
        if pim is not None:
          self.pim = pim

    @property
    def period(self):
        """
        Gets the period of this Penalty.

        :return: The period of this Penalty.
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """
        Sets the period of this Penalty.

        :param period: The period of this Penalty.
        :type: int
        """
        if period is None:
            raise ValueError("Invalid value for `period`, must not be `None`")

        self._period = period

    @property
    def team(self):
        """
        Gets the team of this Penalty.

        :return: The team of this Penalty.
        :rtype: Team
        """
        return self._team

    @team.setter
    def team(self, team):
        """
        Sets the team of this Penalty.

        :param team: The team of this Penalty.
        :type: Team
        """
        if team is None:
            raise ValueError("Invalid value for `team`, must not be `None`")

        self._team = team

    @property
    def time(self):
        """
        Gets the time of this Penalty.
        Seconds left in the period when the penalty was incurred

        :return: The time of this Penalty.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """
        Sets the time of this Penalty.
        Seconds left in the period when the penalty was incurred

        :param time: The time of this Penalty.
        :type: int
        """
        if time is None:
            raise ValueError("Invalid value for `time`, must not be `None`")

        self._time = time

    @property
    def offense(self):
        """
        Gets the offense of this Penalty.
        Title of the penalty

        :return: The offense of this Penalty.
        :rtype: str
        """
        return self._offense

    @offense.setter
    def offense(self, offense):
        """
        Sets the offense of this Penalty.
        Title of the penalty

        :param offense: The offense of this Penalty.
        :type: str
        """
        if offense is None:
            raise ValueError("Invalid value for `offense`, must not be `None`")

        self._offense = offense

    @property
    def offender(self):
        """
        Gets the offender of this Penalty.

        :return: The offender of this Penalty.
        :rtype: str
        """
        return self._offender

    @offender.setter
    def offender(self, offender):
        """
        Sets the offender of this Penalty.

        :param offender: The offender of this Penalty.
        :type: str
        """
        if offender is None:
            raise ValueError("Invalid value for `offender`, must not be `None`")

        self._offender = offender

    @property
    def pim(self):
        """
        Gets the pim of this Penalty.
        Penalty infraction minutes

        :return: The pim of this Penalty.
        :rtype: int
        """
        return self._pim

    @pim.setter
    def pim(self, pim):
        """
        Sets the pim of this Penalty.
        Penalty infraction minutes

        :param pim: The pim of this Penalty.
        :type: int
        """

        self._pim = pim

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
        if not isinstance(other, Penalty):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other