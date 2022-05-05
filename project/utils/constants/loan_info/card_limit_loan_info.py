from enum import Enum

TYPE_CALCULATION = 'CALCULATION'  # Loại tính toán
TYPE_CONDITION_REF_OBJ = 'CONDITION_REF_OBJ'  # Loại điều kiện có quan hệ
TYPE_CONDITION_NOT_REF_OBJ = 'CONDITION_NOT_REF_OBJ'  # Loại điều kiện không có quan hệ
TYPE_CALCULATION_TOTAL_CHILD = 'CALCULATION_TOTAL_CHILD'  # Loại tính tổng đối tượng con
TYPE_CLONE_DATA = "CLONE_DATA"  # Loại clone dữ liệu
TYPE_CONDITION_DEPENDS_VALUE = "CONDITION_DEPENDS_VALUE"  # Loại điều kiện phụ thuộc vào giá trị
TYPE_CONDITION_REF_OBJ_INPUT_VALUE = "CONDITION_REF_OBJ_INPUT_VALUE"  # Loại điều kiện phụ thuộc vào giá trị nhập vào
TYPE_CALCULATION_CONDITION = "CALCULATION_CONDITION_REF_OBJ"  # Loại tính toán phụ thuộc vào giá trị nhập vào và so sánh điều kiện của kết quả tính toán


class ECalculationType(str, Enum):
    id_calculation = TYPE_CALCULATION
    id_calculation_total_child = TYPE_CALCULATION_TOTAL_CHILD
    id_condition_ref_obj = TYPE_CONDITION_REF_OBJ
    id_condition_not_ref_obj = TYPE_CONDITION_NOT_REF_OBJ
    id_clone_data = TYPE_CLONE_DATA
    id_condition_depends_value = TYPE_CONDITION_DEPENDS_VALUE
    id_condition_ref_obj_input_value = TYPE_CONDITION_REF_OBJ_INPUT_VALUE
    id_calculation_condition = TYPE_CALCULATION_CONDITION


TABLE_LOS_CREDIT_INSTITUTION = 'LOS_CREDIT_INSTITUTION'  # table các ngân hàng khác SCB
TABLE_LOS_STTM_BRANCH = 'LOS_STTM_BRANCH'  # table ngân hàng SCB
TABLE_LOS_UDTM_LOV = 'LOS_UDTM_LOV'  # table common data
TABLE_LOS_COLL_TYPE = 'LOS_MA_COLL_TYPE'  # table master loại tài sản đảm bảo


class ECalculationTable(str, Enum):
    id_credit_institution = TABLE_LOS_CREDIT_INSTITUTION
    id_sttm_branch = TABLE_LOS_STTM_BRANCH
    id_udtm_lov = TABLE_LOS_UDTM_LOV
    id_coll_type = TABLE_LOS_COLL_TYPE


DROPLIST_ITEM_COEFF_SALARY = 'COEFF_SALARY'  # hệ số lương


class EDropListItem(str, Enum):
    id_coeff = DROPLIST_ITEM_COEFF_SALARY


TYPE_INFO_DETAILS = 'DETAILS'  # loại thông tin chi tiết
TYPE_INFO_CRITERIA = "CRITERIA"  # loại thông tin tiêu chí


class ETypeInfo(str, Enum):
    id_details = TYPE_INFO_DETAILS
    id_criteria = TYPE_INFO_CRITERIA


KEY_NO_OBJECT = "no_object"  # key không có đối tượng
KEY_DETAILS = 'details'  # key thông tin chi tiết
KEY_CRITERIA = 'criteria'  # key thông tin tiêu chí


class EKeyComponent(str, Enum):
    id_key_no_object = KEY_NO_OBJECT
    id_key_details = KEY_DETAILS
    id_key_criteria = KEY_CRITERIA


COMPONENT_INPUT = "INPUT"
COMPONENT_SELECT = "SELECT"


class ETypeComponent(str, Enum):
    id_input = COMPONENT_INPUT
    id_select = COMPONENT_SELECT


FIELD_TYPE_OBJECT_LIMIT = 'OBJECT_LIMIT'  # Hạn mức tối đa theo đối tượng
FIELD_TYPE_UNIT_LIMIT = 'UNIT_LIMIT'  # Hạn mức tổng đơn vị đề xuất


class ETypeField(str, Enum):  # Phân biệt field item: Hạn mức tối đa theo đối tượng, Hạn mức tổng đơn vị đề, ...
    id_object_limit = FIELD_TYPE_OBJECT_LIMIT
    id_unit_limit = FIELD_TYPE_UNIT_LIMIT
