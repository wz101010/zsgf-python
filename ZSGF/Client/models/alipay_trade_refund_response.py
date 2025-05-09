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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ZSGF.Client.models.preset_pay_tool_info import PresetPayToolInfo
from ZSGF.Client.models.refund_charge_info import RefundChargeInfo
from ZSGF.Client.models.trade_fund_bill import TradeFundBill
from ZSGF.Client.models.voucher_detail import VoucherDetail
from typing import Optional, Set
from typing_extensions import Self

class AlipayTradeRefundResponse(BaseModel):
    """
    AlipayTradeRefundResponse
    """ # noqa: E501
    code: Optional[StrictStr] = None
    msg: Optional[StrictStr] = None
    sub_code: Optional[StrictStr] = Field(default=None, alias="subCode")
    sub_msg: Optional[StrictStr] = Field(default=None, alias="subMsg")
    body: Optional[StrictStr] = None
    is_error: Optional[StrictBool] = Field(default=None, alias="isError")
    buyer_logon_id: Optional[StrictStr] = Field(default=None, alias="buyerLogonId")
    buyer_open_id: Optional[StrictStr] = Field(default=None, alias="buyerOpenId")
    buyer_user_id: Optional[StrictStr] = Field(default=None, alias="buyerUserId")
    fund_change: Optional[StrictStr] = Field(default=None, alias="fundChange")
    gmt_refund_pay: Optional[StrictStr] = Field(default=None, alias="gmtRefundPay")
    has_deposit_back: Optional[StrictStr] = Field(default=None, alias="hasDepositBack")
    open_id: Optional[StrictStr] = Field(default=None, alias="openId")
    out_trade_no: Optional[StrictStr] = Field(default=None, alias="outTradeNo")
    pre_auth_cancel_fee: Optional[StrictStr] = Field(default=None, alias="preAuthCancelFee")
    present_refund_buyer_amount: Optional[StrictStr] = Field(default=None, alias="presentRefundBuyerAmount")
    present_refund_discount_amount: Optional[StrictStr] = Field(default=None, alias="presentRefundDiscountAmount")
    present_refund_mdiscount_amount: Optional[StrictStr] = Field(default=None, alias="presentRefundMdiscountAmount")
    refund_charge_amount: Optional[StrictStr] = Field(default=None, alias="refundChargeAmount")
    refund_charge_info_list: Optional[List[RefundChargeInfo]] = Field(default=None, alias="refundChargeInfoList")
    refund_currency: Optional[StrictStr] = Field(default=None, alias="refundCurrency")
    refund_detail_item_list: Optional[List[TradeFundBill]] = Field(default=None, alias="refundDetailItemList")
    refund_fee: Optional[StrictStr] = Field(default=None, alias="refundFee")
    refund_hyb_amount: Optional[StrictStr] = Field(default=None, alias="refundHybAmount")
    refund_preset_paytool_list: Optional[PresetPayToolInfo] = Field(default=None, alias="refundPresetPaytoolList")
    refund_settlement_id: Optional[StrictStr] = Field(default=None, alias="refundSettlementId")
    refund_voucher_detail_list: Optional[List[VoucherDetail]] = Field(default=None, alias="refundVoucherDetailList")
    send_back_fee: Optional[StrictStr] = Field(default=None, alias="sendBackFee")
    store_name: Optional[StrictStr] = Field(default=None, alias="storeName")
    trade_no: Optional[StrictStr] = Field(default=None, alias="tradeNo")
    __properties: ClassVar[List[str]] = ["code", "msg", "subCode", "subMsg", "body", "isError", "buyerLogonId", "buyerOpenId", "buyerUserId", "fundChange", "gmtRefundPay", "hasDepositBack", "openId", "outTradeNo", "preAuthCancelFee", "presentRefundBuyerAmount", "presentRefundDiscountAmount", "presentRefundMdiscountAmount", "refundChargeAmount", "refundChargeInfoList", "refundCurrency", "refundDetailItemList", "refundFee", "refundHybAmount", "refundPresetPaytoolList", "refundSettlementId", "refundVoucherDetailList", "sendBackFee", "storeName", "tradeNo"]

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
        """Create an instance of AlipayTradeRefundResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "is_error",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in refund_charge_info_list (list)
        _items = []
        if self.refund_charge_info_list:
            for _item_refund_charge_info_list in self.refund_charge_info_list:
                if _item_refund_charge_info_list:
                    _items.append(_item_refund_charge_info_list.to_dict())
            _dict['refundChargeInfoList'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in refund_detail_item_list (list)
        _items = []
        if self.refund_detail_item_list:
            for _item_refund_detail_item_list in self.refund_detail_item_list:
                if _item_refund_detail_item_list:
                    _items.append(_item_refund_detail_item_list.to_dict())
            _dict['refundDetailItemList'] = _items
        # override the default output from pydantic by calling `to_dict()` of refund_preset_paytool_list
        if self.refund_preset_paytool_list:
            _dict['refundPresetPaytoolList'] = self.refund_preset_paytool_list.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in refund_voucher_detail_list (list)
        _items = []
        if self.refund_voucher_detail_list:
            for _item_refund_voucher_detail_list in self.refund_voucher_detail_list:
                if _item_refund_voucher_detail_list:
                    _items.append(_item_refund_voucher_detail_list.to_dict())
            _dict['refundVoucherDetailList'] = _items
        # set to None if code (nullable) is None
        # and model_fields_set contains the field
        if self.code is None and "code" in self.model_fields_set:
            _dict['code'] = None

        # set to None if msg (nullable) is None
        # and model_fields_set contains the field
        if self.msg is None and "msg" in self.model_fields_set:
            _dict['msg'] = None

        # set to None if sub_code (nullable) is None
        # and model_fields_set contains the field
        if self.sub_code is None and "sub_code" in self.model_fields_set:
            _dict['subCode'] = None

        # set to None if sub_msg (nullable) is None
        # and model_fields_set contains the field
        if self.sub_msg is None and "sub_msg" in self.model_fields_set:
            _dict['subMsg'] = None

        # set to None if body (nullable) is None
        # and model_fields_set contains the field
        if self.body is None and "body" in self.model_fields_set:
            _dict['body'] = None

        # set to None if buyer_logon_id (nullable) is None
        # and model_fields_set contains the field
        if self.buyer_logon_id is None and "buyer_logon_id" in self.model_fields_set:
            _dict['buyerLogonId'] = None

        # set to None if buyer_open_id (nullable) is None
        # and model_fields_set contains the field
        if self.buyer_open_id is None and "buyer_open_id" in self.model_fields_set:
            _dict['buyerOpenId'] = None

        # set to None if buyer_user_id (nullable) is None
        # and model_fields_set contains the field
        if self.buyer_user_id is None and "buyer_user_id" in self.model_fields_set:
            _dict['buyerUserId'] = None

        # set to None if fund_change (nullable) is None
        # and model_fields_set contains the field
        if self.fund_change is None and "fund_change" in self.model_fields_set:
            _dict['fundChange'] = None

        # set to None if gmt_refund_pay (nullable) is None
        # and model_fields_set contains the field
        if self.gmt_refund_pay is None and "gmt_refund_pay" in self.model_fields_set:
            _dict['gmtRefundPay'] = None

        # set to None if has_deposit_back (nullable) is None
        # and model_fields_set contains the field
        if self.has_deposit_back is None and "has_deposit_back" in self.model_fields_set:
            _dict['hasDepositBack'] = None

        # set to None if open_id (nullable) is None
        # and model_fields_set contains the field
        if self.open_id is None and "open_id" in self.model_fields_set:
            _dict['openId'] = None

        # set to None if out_trade_no (nullable) is None
        # and model_fields_set contains the field
        if self.out_trade_no is None and "out_trade_no" in self.model_fields_set:
            _dict['outTradeNo'] = None

        # set to None if pre_auth_cancel_fee (nullable) is None
        # and model_fields_set contains the field
        if self.pre_auth_cancel_fee is None and "pre_auth_cancel_fee" in self.model_fields_set:
            _dict['preAuthCancelFee'] = None

        # set to None if present_refund_buyer_amount (nullable) is None
        # and model_fields_set contains the field
        if self.present_refund_buyer_amount is None and "present_refund_buyer_amount" in self.model_fields_set:
            _dict['presentRefundBuyerAmount'] = None

        # set to None if present_refund_discount_amount (nullable) is None
        # and model_fields_set contains the field
        if self.present_refund_discount_amount is None and "present_refund_discount_amount" in self.model_fields_set:
            _dict['presentRefundDiscountAmount'] = None

        # set to None if present_refund_mdiscount_amount (nullable) is None
        # and model_fields_set contains the field
        if self.present_refund_mdiscount_amount is None and "present_refund_mdiscount_amount" in self.model_fields_set:
            _dict['presentRefundMdiscountAmount'] = None

        # set to None if refund_charge_amount (nullable) is None
        # and model_fields_set contains the field
        if self.refund_charge_amount is None and "refund_charge_amount" in self.model_fields_set:
            _dict['refundChargeAmount'] = None

        # set to None if refund_charge_info_list (nullable) is None
        # and model_fields_set contains the field
        if self.refund_charge_info_list is None and "refund_charge_info_list" in self.model_fields_set:
            _dict['refundChargeInfoList'] = None

        # set to None if refund_currency (nullable) is None
        # and model_fields_set contains the field
        if self.refund_currency is None and "refund_currency" in self.model_fields_set:
            _dict['refundCurrency'] = None

        # set to None if refund_detail_item_list (nullable) is None
        # and model_fields_set contains the field
        if self.refund_detail_item_list is None and "refund_detail_item_list" in self.model_fields_set:
            _dict['refundDetailItemList'] = None

        # set to None if refund_fee (nullable) is None
        # and model_fields_set contains the field
        if self.refund_fee is None and "refund_fee" in self.model_fields_set:
            _dict['refundFee'] = None

        # set to None if refund_hyb_amount (nullable) is None
        # and model_fields_set contains the field
        if self.refund_hyb_amount is None and "refund_hyb_amount" in self.model_fields_set:
            _dict['refundHybAmount'] = None

        # set to None if refund_settlement_id (nullable) is None
        # and model_fields_set contains the field
        if self.refund_settlement_id is None and "refund_settlement_id" in self.model_fields_set:
            _dict['refundSettlementId'] = None

        # set to None if refund_voucher_detail_list (nullable) is None
        # and model_fields_set contains the field
        if self.refund_voucher_detail_list is None and "refund_voucher_detail_list" in self.model_fields_set:
            _dict['refundVoucherDetailList'] = None

        # set to None if send_back_fee (nullable) is None
        # and model_fields_set contains the field
        if self.send_back_fee is None and "send_back_fee" in self.model_fields_set:
            _dict['sendBackFee'] = None

        # set to None if store_name (nullable) is None
        # and model_fields_set contains the field
        if self.store_name is None and "store_name" in self.model_fields_set:
            _dict['storeName'] = None

        # set to None if trade_no (nullable) is None
        # and model_fields_set contains the field
        if self.trade_no is None and "trade_no" in self.model_fields_set:
            _dict['tradeNo'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AlipayTradeRefundResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "code": obj.get("code"),
            "msg": obj.get("msg"),
            "subCode": obj.get("subCode"),
            "subMsg": obj.get("subMsg"),
            "body": obj.get("body"),
            "isError": obj.get("isError"),
            "buyerLogonId": obj.get("buyerLogonId"),
            "buyerOpenId": obj.get("buyerOpenId"),
            "buyerUserId": obj.get("buyerUserId"),
            "fundChange": obj.get("fundChange"),
            "gmtRefundPay": obj.get("gmtRefundPay"),
            "hasDepositBack": obj.get("hasDepositBack"),
            "openId": obj.get("openId"),
            "outTradeNo": obj.get("outTradeNo"),
            "preAuthCancelFee": obj.get("preAuthCancelFee"),
            "presentRefundBuyerAmount": obj.get("presentRefundBuyerAmount"),
            "presentRefundDiscountAmount": obj.get("presentRefundDiscountAmount"),
            "presentRefundMdiscountAmount": obj.get("presentRefundMdiscountAmount"),
            "refundChargeAmount": obj.get("refundChargeAmount"),
            "refundChargeInfoList": [RefundChargeInfo.from_dict(_item) for _item in obj["refundChargeInfoList"]] if obj.get("refundChargeInfoList") is not None else None,
            "refundCurrency": obj.get("refundCurrency"),
            "refundDetailItemList": [TradeFundBill.from_dict(_item) for _item in obj["refundDetailItemList"]] if obj.get("refundDetailItemList") is not None else None,
            "refundFee": obj.get("refundFee"),
            "refundHybAmount": obj.get("refundHybAmount"),
            "refundPresetPaytoolList": PresetPayToolInfo.from_dict(obj["refundPresetPaytoolList"]) if obj.get("refundPresetPaytoolList") is not None else None,
            "refundSettlementId": obj.get("refundSettlementId"),
            "refundVoucherDetailList": [VoucherDetail.from_dict(_item) for _item in obj["refundVoucherDetailList"]] if obj.get("refundVoucherDetailList") is not None else None,
            "sendBackFee": obj.get("sendBackFee"),
            "storeName": obj.get("storeName"),
            "tradeNo": obj.get("tradeNo")
        })
        return _obj


