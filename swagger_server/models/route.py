# coding: utf-8

from __future__ import absolute_import
from swagger_server.models.route_point import RoutePoint
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Route(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, route_id: str=None, agent_type: str=None, route_number: str=None, departure_station_id: str=None, arrival_station_id: str=None, departure_time: str=None, arrival_time: str=None, travel_time: str=None, periodicity: str=None, route_points: List[RoutePoint]=None):
        """
        Route - a model defined in Swagger

        :param route_id: The route_id of this Route.
        :type route_id: str
        :param agent_type: The agent_type of this Route.
        :type agent_type: str
        :param route_number: The route_number of this Route.
        :type route_number: str
        :param departure_station_id: The departure_station_id of this Route.
        :type departure_station_id: str
        :param arrival_station_id: The arrival_station_id of this Route.
        :type arrival_station_id: str
        :param departure_time: The departure_time of this Route.
        :type departure_time: str
        :param arrival_time: The arrival_time of this Route.
        :type arrival_time: str
        :param travel_time: The travel_time of this Route.
        :type travel_time: str
        :param periodicity: The periodicity of this Route.
        :type periodicity: str
        :param route_points: The route_points of this Route.
        :type route_points: List[RoutePoint]
        """
        self.swagger_types = {
            'route_id': str,
            'agent_type': str,
            'route_number': str,
            'departure_station_id': str,
            'arrival_station_id': str,
            'departure_time': str,
            'arrival_time': str,
            'travel_time': str,
            'periodicity': str,
            'route_points': List[RoutePoint]
        }

        self.attribute_map = {
            'route_id': 'route_id',
            'agent_type': 'agent_type',
            'route_number': 'route_number',
            'departure_station_id': 'departure_station_id',
            'arrival_station_id': 'arrival_station_id',
            'departure_time': 'departure_time',
            'arrival_time': 'arrival_time',
            'travel_time': 'travel_time',
            'periodicity': 'periodicity',
            'route_points': 'route_points'
        }

        self._route_id = route_id
        self._agent_type = agent_type
        self._route_number = route_number
        self._departure_station_id = departure_station_id
        self._arrival_station_id = arrival_station_id
        self._departure_time = departure_time
        self._arrival_time = arrival_time
        self._travel_time = travel_time
        self._periodicity = periodicity
        self._route_points = route_points

    @classmethod
    def from_dict(cls, dikt) -> 'Route':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Route of this Route.
        :rtype: Route
        """
        return deserialize_model(dikt, cls)

    @property
    def route_id(self) -> str:
        """
        Gets the route_id of this Route.

        :return: The route_id of this Route.
        :rtype: str
        """
        return self._route_id

    @route_id.setter
    def route_id(self, route_id: str):
        """
        Sets the route_id of this Route.

        :param route_id: The route_id of this Route.
        :type route_id: str
        """

        self._route_id = route_id

    @property
    def agent_type(self) -> str:
        """
        Gets the agent_type of this Route.

        :return: The agent_type of this Route.
        :rtype: str
        """
        return self._agent_type

    @agent_type.setter
    def agent_type(self, agent_type: str):
        """
        Sets the agent_type of this Route.

        :param agent_type: The agent_type of this Route.
        :type agent_type: str
        """

        self._agent_type = agent_type

    @property
    def route_number(self) -> str:
        """
        Gets the route_number of this Route.

        :return: The route_number of this Route.
        :rtype: str
        """
        return self._route_number

    @route_number.setter
    def route_number(self, route_number: str):
        """
        Sets the route_number of this Route.

        :param route_number: The route_number of this Route.
        :type route_number: str
        """

        self._route_number = route_number

    @property
    def departure_station_id(self) -> str:
        """
        Gets the departure_station_id of this Route.

        :return: The departure_station_id of this Route.
        :rtype: str
        """
        return self._departure_station_id

    @departure_station_id.setter
    def departure_station_id(self, departure_station_id: str):
        """
        Sets the departure_station_id of this Route.

        :param departure_station_id: The departure_station_id of this Route.
        :type departure_station_id: str
        """

        self._departure_station_id = departure_station_id

    @property
    def arrival_station_id(self) -> str:
        """
        Gets the arrival_station_id of this Route.

        :return: The arrival_station_id of this Route.
        :rtype: str
        """
        return self._arrival_station_id

    @arrival_station_id.setter
    def arrival_station_id(self, arrival_station_id: str):
        """
        Sets the arrival_station_id of this Route.

        :param arrival_station_id: The arrival_station_id of this Route.
        :type arrival_station_id: str
        """

        self._arrival_station_id = arrival_station_id

    @property
    def departure_time(self) -> str:
        """
        Gets the departure_time of this Route.

        :return: The departure_time of this Route.
        :rtype: str
        """
        return self._departure_time

    @departure_time.setter
    def departure_time(self, departure_time: str):
        """
        Sets the departure_time of this Route.

        :param departure_time: The departure_time of this Route.
        :type departure_time: str
        """

        self._departure_time = departure_time

    @property
    def arrival_time(self) -> str:
        """
        Gets the arrival_time of this Route.

        :return: The arrival_time of this Route.
        :rtype: str
        """
        return self._arrival_time

    @arrival_time.setter
    def arrival_time(self, arrival_time: str):
        """
        Sets the arrival_time of this Route.

        :param arrival_time: The arrival_time of this Route.
        :type arrival_time: str
        """

        self._arrival_time = arrival_time

    @property
    def travel_time(self) -> str:
        """
        Gets the travel_time of this Route.

        :return: The travel_time of this Route.
        :rtype: str
        """
        return self._travel_time

    @travel_time.setter
    def travel_time(self, travel_time: str):
        """
        Sets the travel_time of this Route.

        :param travel_time: The travel_time of this Route.
        :type travel_time: str
        """

        self._travel_time = travel_time

    @property
    def periodicity(self) -> str:
        """
        Gets the periodicity of this Route.

        :return: The periodicity of this Route.
        :rtype: str
        """
        return self._periodicity

    @periodicity.setter
    def periodicity(self, periodicity: str):
        """
        Sets the periodicity of this Route.

        :param periodicity: The periodicity of this Route.
        :type periodicity: str
        """

        self._periodicity = periodicity

    @property
    def route_points(self) -> List[RoutePoint]:
        """
        Gets the route_points of this Route.

        :return: The route_points of this Route.
        :rtype: List[RoutePoint]
        """
        return self._route_points

    @route_points.setter
    def route_points(self, route_points: List[RoutePoint]):
        """
        Sets the route_points of this Route.

        :param route_points: The route_points of this Route.
        :type route_points: List[RoutePoint]
        """

        self._route_points = route_points

