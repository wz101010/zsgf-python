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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ZSGF.Client.models.user_currency import UserCurrency
from typing import Optional, Set
from typing_extensions import Self

class UserProfileResult(BaseModel):
    """
    UserProfileResult
    """ # noqa: E501
    app_key: Optional[StrictStr] = Field(default=None, alias="appKey")
    platform: Optional[StrictStr] = None
    union_id: Optional[StrictStr] = Field(default=None, alias="unionID")
    phone: Optional[StrictStr] = None
    create_date: Optional[datetime] = Field(default=None, alias="createDate")
    user_name: Optional[StrictStr] = Field(default=None, alias="userName")
    phone_is_valid: Optional[StrictBool] = Field(default=None, alias="phoneIsValid")
    data: Optional[StrictStr] = None
    email: Optional[StrictStr] = None
    email_is_valid: Optional[StrictBool] = Field(default=None, alias="emailIsValid")
    last_update: Optional[datetime] = Field(default=None, alias="lastUpdate")
    nick_name: Optional[StrictStr] = Field(default=None, alias="nickName")
    id: Optional[StrictInt] = None
    avatar: Optional[StrictStr] = None
    currencies: Optional[List[UserCurrency]] = None
    role: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["appKey", "platform", "unionID", "phone", "createDate", "userName", "phoneIsValid", "data", "email", "emailIsValid", "lastUpdate", "nickName", "id", "avatar", "currencies", "role"]

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
        """Create an instance of UserProfileResult from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in currencies (list)
        _items = []
        if self.currencies:
            for _item_currencies in self.currencies:
                if _item_currencies:
                    _items.append(_item_currencies.to_dict())
            _dict['currencies'] = _items
        # set to None if app_key (nullable) is None
        # and model_fields_set contains the field
        if self.app_key is None and "app_key" in self.model_fields_set:
            _dict['appKey'] = None

        # set to None if platform (nullable) is None
        # and model_fields_set contains the field
        if self.platform is None and "platform" in self.model_fields_set:
            _dict['platform'] = None

        # set to None if union_id (nullable) is None
        # and model_fields_set contains the field
        if self.union_id is None and "union_id" in self.model_fields_set:
            _dict['unionID'] = None

        # set to None if phone (nullable) is None
        # and model_fields_set contains the field
        if self.phone is None and "phone" in self.model_fields_set:
            _dict['phone'] = None

        # set to None if user_name (nullable) is None
        # and model_fields_set contains the field
        if self.user_name is None and "user_name" in self.model_fields_set:
            _dict['userName'] = None

        # set to None if data (nullable) is None
        # and model_fields_set contains the field
        if self.data is None and "data" in self.model_fields_set:
            _dict['data'] = None

        # set to None if email (nullable) is None
        # and model_fields_set contains the field
        if self.email is None and "email" in self.model_fields_set:
            _dict['email'] = None

        # set to None if nick_name (nullable) is None
        # and model_fields_set contains the field
        if self.nick_name is None and "nick_name" in self.model_fields_set:
            _dict['nickName'] = None

        # set to None if avatar (nullable) is None
        # and model_fields_set contains the field
        if self.avatar is None and "avatar" in self.model_fields_set:
            _dict['avatar'] = None

        # set to None if currencies (nullable) is None
        # and model_fields_set contains the field
        if self.currencies is None and "currencies" in self.model_fields_set:
            _dict['currencies'] = None

        # set to None if role (nullable) is None
        # and model_fields_set contains the field
        if self.role is None and "role" in self.model_fields_set:
            _dict['role'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserProfileResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "appKey": obj.get("appKey"),
            "platform": obj.get("platform"),
            "unionID": obj.get("unionID"),
            "phone": obj.get("phone"),
            "createDate": obj.get("createDate"),
            "userName": obj.get("userName"),
            "phoneIsValid": obj.get("phoneIsValid"),
            "data": obj.get("data"),
            "email": obj.get("email"),
            "emailIsValid": obj.get("emailIsValid"),
            "lastUpdate": obj.get("lastUpdate"),
            "nickName": obj.get("nickName"),
            "id": obj.get("id"),
            "avatar": obj.get("avatar"),
            "currencies": [UserCurrency.from_dict(_item) for _item in obj["currencies"]] if obj.get("currencies") is not None else None,
            "role": obj.get("role")
        })
        return _obj


