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
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class ExchangeCurrencyRequest(BaseModel):
    """
    ExchangeCurrencyRequest
    """ # noqa: E501
    from_currency: Annotated[str, Field(min_length=1, strict=True)] = Field(description="源虚拟币代码", alias="fromCurrency")
    currency: Annotated[str, Field(min_length=1, strict=True)] = Field(description="目标虚拟币代码")
    balance: StrictInt = Field(description="兑换额")
    remark: Optional[StrictStr] = Field(default=None, description="备注")
    description: Optional[StrictStr] = Field(default=None, description="描述")
    tags: Optional[StrictStr] = Field(default=None, description="标签")
    __properties: ClassVar[List[str]] = ["fromCurrency", "currency", "balance", "remark", "description", "tags"]

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
        """Create an instance of ExchangeCurrencyRequest from a JSON string"""
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
        # set to None if remark (nullable) is None
        # and model_fields_set contains the field
        if self.remark is None and "remark" in self.model_fields_set:
            _dict['remark'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if tags (nullable) is None
        # and model_fields_set contains the field
        if self.tags is None and "tags" in self.model_fields_set:
            _dict['tags'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ExchangeCurrencyRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fromCurrency": obj.get("fromCurrency"),
            "currency": obj.get("currency"),
            "balance": obj.get("balance"),
            "remark": obj.get("remark"),
            "description": obj.get("description"),
            "tags": obj.get("tags")
        })
        return _obj


