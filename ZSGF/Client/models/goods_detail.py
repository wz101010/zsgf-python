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

class GoodsDetail(BaseModel):
    """
    GoodsDetail
    """ # noqa: E501
    alipay_goods_id: Optional[StrictStr] = Field(default=None, alias="alipayGoodsId")
    body: Optional[StrictStr] = None
    categories_tree: Optional[StrictStr] = Field(default=None, alias="categoriesTree")
    goods_category: Optional[StrictStr] = Field(default=None, alias="goodsCategory")
    goods_id: Optional[StrictStr] = Field(default=None, alias="goodsId")
    goods_name: Optional[StrictStr] = Field(default=None, alias="goodsName")
    out_item_id: Optional[StrictStr] = Field(default=None, alias="outItemId")
    out_sku_id: Optional[StrictStr] = Field(default=None, alias="outSkuId")
    price: Optional[StrictStr] = None
    quantity: Optional[StrictInt] = None
    show_url: Optional[StrictStr] = Field(default=None, alias="showUrl")
    __properties: ClassVar[List[str]] = ["alipayGoodsId", "body", "categoriesTree", "goodsCategory", "goodsId", "goodsName", "outItemId", "outSkuId", "price", "quantity", "showUrl"]

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
        """Create an instance of GoodsDetail from a JSON string"""
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
        # set to None if alipay_goods_id (nullable) is None
        # and model_fields_set contains the field
        if self.alipay_goods_id is None and "alipay_goods_id" in self.model_fields_set:
            _dict['alipayGoodsId'] = None

        # set to None if body (nullable) is None
        # and model_fields_set contains the field
        if self.body is None and "body" in self.model_fields_set:
            _dict['body'] = None

        # set to None if categories_tree (nullable) is None
        # and model_fields_set contains the field
        if self.categories_tree is None and "categories_tree" in self.model_fields_set:
            _dict['categoriesTree'] = None

        # set to None if goods_category (nullable) is None
        # and model_fields_set contains the field
        if self.goods_category is None and "goods_category" in self.model_fields_set:
            _dict['goodsCategory'] = None

        # set to None if goods_id (nullable) is None
        # and model_fields_set contains the field
        if self.goods_id is None and "goods_id" in self.model_fields_set:
            _dict['goodsId'] = None

        # set to None if goods_name (nullable) is None
        # and model_fields_set contains the field
        if self.goods_name is None and "goods_name" in self.model_fields_set:
            _dict['goodsName'] = None

        # set to None if out_item_id (nullable) is None
        # and model_fields_set contains the field
        if self.out_item_id is None and "out_item_id" in self.model_fields_set:
            _dict['outItemId'] = None

        # set to None if out_sku_id (nullable) is None
        # and model_fields_set contains the field
        if self.out_sku_id is None and "out_sku_id" in self.model_fields_set:
            _dict['outSkuId'] = None

        # set to None if price (nullable) is None
        # and model_fields_set contains the field
        if self.price is None and "price" in self.model_fields_set:
            _dict['price'] = None

        # set to None if show_url (nullable) is None
        # and model_fields_set contains the field
        if self.show_url is None and "show_url" in self.model_fields_set:
            _dict['showUrl'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GoodsDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "alipayGoodsId": obj.get("alipayGoodsId"),
            "body": obj.get("body"),
            "categoriesTree": obj.get("categoriesTree"),
            "goodsCategory": obj.get("goodsCategory"),
            "goodsId": obj.get("goodsId"),
            "goodsName": obj.get("goodsName"),
            "outItemId": obj.get("outItemId"),
            "outSkuId": obj.get("outSkuId"),
            "price": obj.get("price"),
            "quantity": obj.get("quantity"),
            "showUrl": obj.get("showUrl")
        })
        return _obj


