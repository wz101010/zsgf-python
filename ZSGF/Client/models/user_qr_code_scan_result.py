# coding: utf-8

"""
    全部  API 文档

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class UserQRCodeScanResult(BaseModel):
    """
    UserQRCodeScanResult
    """ # noqa: E501
    app_id: Optional[StrictInt] = Field(default=None, alias="appID")
    name: Optional[StrictStr] = None
    logo: Optional[StrictStr] = None
    website: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    tags: Optional[StrictStr] = None
    scopes: Optional[StrictStr] = None
    remark: Optional[StrictStr] = None
    scheme: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["appID", "name", "logo", "website", "description", "tags", "scopes", "remark", "scheme"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of UserQRCodeScanResult from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if logo (nullable) is None
        # and model_fields_set contains the field
        if self.logo is None and "logo" in self.model_fields_set:
            _dict['logo'] = None

        # set to None if website (nullable) is None
        # and model_fields_set contains the field
        if self.website is None and "website" in self.model_fields_set:
            _dict['website'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if tags (nullable) is None
        # and model_fields_set contains the field
        if self.tags is None and "tags" in self.model_fields_set:
            _dict['tags'] = None

        # set to None if scopes (nullable) is None
        # and model_fields_set contains the field
        if self.scopes is None and "scopes" in self.model_fields_set:
            _dict['scopes'] = None

        # set to None if remark (nullable) is None
        # and model_fields_set contains the field
        if self.remark is None and "remark" in self.model_fields_set:
            _dict['remark'] = None

        # set to None if scheme (nullable) is None
        # and model_fields_set contains the field
        if self.scheme is None and "scheme" in self.model_fields_set:
            _dict['scheme'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserQRCodeScanResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "appID": obj.get("appID"),
            "name": obj.get("name"),
            "logo": obj.get("logo"),
            "website": obj.get("website"),
            "description": obj.get("description"),
            "tags": obj.get("tags"),
            "scopes": obj.get("scopes"),
            "remark": obj.get("remark"),
            "scheme": obj.get("scheme")
        })
        return _obj


