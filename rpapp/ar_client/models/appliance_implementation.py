# coding: utf-8

"""
    Appliance Registry API

    Store appliances with the Appliance Registry API.

    OpenAPI spec version: 0.1.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
    
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
    
        http://www.apache.org/licenses/LICENSE-2.0
    
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class ApplianceImplementation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ApplianceImplementation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'image_name': 'str',
            'site': 'str',
            'appliance': 'str',
            'scripts': 'list[int]'
        }

        self.attribute_map = {
            'name': 'name',
            'image_name': 'image_name',
            'site': 'site',
            'appliance': 'appliance',
            'scripts': 'scripts'
        }

        self._name = None
        self._image_name = None
        self._site = None
        self._appliance = None
        self._scripts = None

    @property
    def name(self):
        """
        Gets the name of this ApplianceImplementation.
        Name of the appliance implementation

        :return: The name of this ApplianceImplementation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ApplianceImplementation.
        Name of the appliance implementation

        :param name: The name of this ApplianceImplementation.
        :type: str
        """
        
        self._name = name

    @property
    def image_name(self):
        """
        Gets the image_name of this ApplianceImplementation.
        Name of the image that will be used by the appliance implementation

        :return: The image_name of this ApplianceImplementation.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        """
        Sets the image_name of this ApplianceImplementation.
        Name of the image that will be used by the appliance implementation

        :param image_name: The image_name of this ApplianceImplementation.
        :type: str
        """
        
        self._image_name = image_name

    @property
    def site(self):
        """
        Gets the site of this ApplianceImplementation.
        Name of the site to use

        :return: The site of this ApplianceImplementation.
        :rtype: str
        """
        return self._site

    @site.setter
    def site(self, site):
        """
        Sets the site of this ApplianceImplementation.
        Name of the site to use

        :param site: The site of this ApplianceImplementation.
        :type: str
        """
        
        self._site = site

    @property
    def appliance(self):
        """
        Gets the appliance of this ApplianceImplementation.
        ID (name) of the appliance

        :return: The appliance of this ApplianceImplementation.
        :rtype: str
        """
        return self._appliance

    @appliance.setter
    def appliance(self, appliance):
        """
        Sets the appliance of this ApplianceImplementation.
        ID (name) of the appliance

        :param appliance: The appliance of this ApplianceImplementation.
        :type: str
        """
        
        self._appliance = appliance

    @property
    def scripts(self):
        """
        Gets the scripts of this ApplianceImplementation.


        :return: The scripts of this ApplianceImplementation.
        :rtype: list[int]
        """
        return self._scripts

    @scripts.setter
    def scripts(self, scripts):
        """
        Sets the scripts of this ApplianceImplementation.


        :param scripts: The scripts of this ApplianceImplementation.
        :type: list[int]
        """
        
        self._scripts = scripts

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

