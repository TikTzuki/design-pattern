from datetime import datetime
from decimal import Decimal
from typing import Generic, Type, TypeVar, List, Dict

from pydantic import Field, condecimal

from project.core import CustomGenericModel
from project.core.schemas import CustomBaseModel
from project.utils.constants.utils import EYesNoQuestion

ConDecimal: Type[Decimal] = condecimal(decimal_places=2)
PercentageDecimal: Type[Decimal] = condecimal(decimal_places=2, ge=Decimal("0"), le=Decimal("100"))
TypeEnum = TypeVar('TypeEnum')
D = TypeVar("D", bound=ConDecimal)
S = TypeVar("S", bound=str)


class BranchRes(CustomBaseModel):
    """
    chi nhánh ngân hàng
    """
    branch_code: str
    branch_name: str
    branch_address: str
    branch_parent_code: str
    branch_tax_code: str
    branch_phone: str
    branch_status: str
    branch_region_code: str
    branch_region_name: str


class FileUtil(CustomBaseModel):
    """ schema dùng chung cho file trong các tab """
    uuid: str = Field(...)
    name: str = Field(...)
    content_type: str = Field(...)
    display_order: int = Field(None)
    created_by: str = Field(None)
    created_at: datetime = Field(None)
    updated_at: datetime = Field(None)
    updated_by: str = Field(None)
    custom_keys: Dict = Field(None)


class ValueMeasureUtil(CustomGenericModel, Generic[D]):
    """
        Schema dùng chung cho các model id, name, value. Value là gía trị số, name là đơn vị nếu có.
    """
    id: str = Field(None)
    value: D = Field(...)


class IdCodeNameEnumUtil(CustomGenericModel, Generic[TypeEnum]):
    """
        Schema dùng chung cho các model id, code, name mà code là một enum
    """
    id: str = Field(None)
    code: TypeEnum = Field(...)
    name: str = Field(None)


class IdNameUtil(CustomGenericModel, Generic[S]):
    id: S = Field(...)
    name: str = Field(None)
    other_value_flag: EYesNoQuestion = Field(None)


class IdNameUtilOpt(CustomGenericModel, Generic[S]):
    id: S = Field(None)
    name: str = Field(None)
    other_value_flag: EYesNoQuestion = Field(None)


class CountryRes(CustomBaseModel):
    country_code: str
    country_name: str


# Tỉnh, thành phố
class ProvinceRes(CustomBaseModel):
    province_code: str
    province_name: str


# Quận huyện
class DistrictRes(CustomBaseModel):
    district_code: str
    district_name: str


# Phường, xã
class WardRes(CustomBaseModel):
    ward_code: str
    ward_name: str


# Địa chỉ
class AddressRes(CustomBaseModel):
    address: str


class UdtmRes(CustomBaseModel):
    """
        Schema dùng chung cho các master data
    """
    id: str
    code: str
    name: str
    is_default: str = Field("N")


class Document(CustomBaseModel):
    document_id: int = Field(...)
    document_name: str = Field(...)
    data_file: List[FileUtil] = Field(None)
