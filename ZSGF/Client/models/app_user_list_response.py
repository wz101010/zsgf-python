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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class AppUserListResponse(BaseModel):
    """
    AppUserListResponse
    """ # noqa: E501
    id: Optional[StrictInt] = None
    union_id: Optional[StrictStr] = Field(default=None, alias="unionID")
    platform: Optional[StrictStr] = None
    user_name: Optional[StrictStr] = Field(default=None, alias="userName")
    nick_name: Optional[StrictStr] = Field(default=None, alias="nickName")
    email: Optional[StrictStr] = None
    phone: Optional[StrictStr] = None
    avatar: Optional[StrictStr] = None
    role: Optional[StrictStr] = None
    role_id: Optional[StrictInt] = Field(default=None, alias="roleID")
    create_date: Optional[datetime] = Field(default=None, alias="createDate")
    last_update: Optional[datetime] = Field(default=None, alias="lastUpdate")
    __properties: ClassVar[List[str]] = ["id", "unionID", "platform", "userName", "nickName", "email", "phone", "avatar", "role", "roleID", "createDate", "lastUpdate"]

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
        """Create an instance of AppUserListResponse from a JSON string"""
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
        # set to None if union_id (nullable) is None
        # and model_fields_set contains the field
        if self.union_id is None and "union_id" in self.model_fields_set:
            _dict['unionID'] = None

        # set to None if platform (nullable) is None
        # and model_fields_set contains the field
        if self.platform is None and "platform" in self.model_fields_set:
            _dict['platform'] = None

        # set to None if user_name (nullable) is None
        # and model_fields_set contains the field
        if self.user_name is None and "user_name" in self.model_fields_set:
            _dict['userName'] = None

        # set to None if nick_name (nullable) is None
        # and model_fields_set contains the field
        if self.nick_name is None and "nick_name" in self.model_fields_set:
            _dict['nickName'] = None

        # set to None if email (nullable) is None
        # and model_fields_set contains the field
        if self.email is None and "email" in self.model_fields_set:
            _dict['email'] = None

        # set to None if phone (nullable) is None
        # and model_fields_set contains the field
        if self.phone is None and "phone" in self.model_fields_set:
            _dict['phone'] = None

        # set to None if avatar (nullable) is None
        # and model_fields_set contains the field
        if self.avatar is None and "avatar" in self.model_fields_set:
            _dict['avatar'] = None

        # set to None if role (nullable) is None
        # and model_fields_set contains the field
        if self.role is None and "role" in self.model_fields_set:
            _dict['role'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AppUserListResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "unionID": obj.get("unionID"),
            "platform": obj.get("platform"),
            "userName": obj.get("userName"),
            "nickName": obj.get("nickName"),
            "email": obj.get("email"),
            "phone": obj.get("phone"),
            "avatar": obj.get("avatar"),
            "role": obj.get("role"),
            "roleID": obj.get("roleID"),
            "createDate": obj.get("createDate"),
            "lastUpdate": obj.get("lastUpdate")
        })
        return _obj


