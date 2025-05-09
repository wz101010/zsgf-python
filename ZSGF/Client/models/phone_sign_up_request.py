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

from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class PhoneSignUpRequest(BaseModel):
    """
    PhoneSignUpRequest
    """ # noqa: E501
    phone: Annotated[str, Field(min_length=1, strict=True)]
    phone_code: Annotated[str, Field(min_length=1, strict=True)] = Field(description="手机验证码", alias="phoneCode")
    pwd: Annotated[str, Field(min_length=6, strict=True, max_length=32)]
    email: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="邮箱")
    email_code: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="邮箱验证码（只有启用的邮箱验证码功能时，才需要传入）", alias="emailCode")
    nick_name: Optional[Annotated[str, Field(strict=True, max_length=99)]] = Field(default=None, description="昵称", alias="nickName")
    avatar: Optional[Annotated[str, Field(strict=True, max_length=999)]] = Field(default=None, description="头像")
    data: Optional[Annotated[str, Field(strict=True, max_length=9999)]] = Field(default=None, description="自定义数据")
    __properties: ClassVar[List[str]] = ["phone", "phoneCode", "pwd", "email", "emailCode", "nickName", "avatar", "data"]

    @field_validator('phone_code')
    def phone_code_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"\d{4,8}$", value):
            raise ValueError(r"must validate the regular expression /\d{4,8}$/")
        return value

    @field_validator('email')
    def email_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,5}$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,5}$/")
        return value

    @field_validator('email_code')
    def email_code_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"\d{4,8}$", value):
            raise ValueError(r"must validate the regular expression /\d{4,8}$/")
        return value

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
        """Create an instance of PhoneSignUpRequest from a JSON string"""
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
        # set to None if email (nullable) is None
        # and model_fields_set contains the field
        if self.email is None and "email" in self.model_fields_set:
            _dict['email'] = None

        # set to None if email_code (nullable) is None
        # and model_fields_set contains the field
        if self.email_code is None and "email_code" in self.model_fields_set:
            _dict['emailCode'] = None

        # set to None if nick_name (nullable) is None
        # and model_fields_set contains the field
        if self.nick_name is None and "nick_name" in self.model_fields_set:
            _dict['nickName'] = None

        # set to None if avatar (nullable) is None
        # and model_fields_set contains the field
        if self.avatar is None and "avatar" in self.model_fields_set:
            _dict['avatar'] = None

        # set to None if data (nullable) is None
        # and model_fields_set contains the field
        if self.data is None and "data" in self.model_fields_set:
            _dict['data'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PhoneSignUpRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "phone": obj.get("phone"),
            "phoneCode": obj.get("phoneCode"),
            "pwd": obj.get("pwd"),
            "email": obj.get("email"),
            "emailCode": obj.get("emailCode"),
            "nickName": obj.get("nickName"),
            "avatar": obj.get("avatar"),
            "data": obj.get("data")
        })
        return _obj


