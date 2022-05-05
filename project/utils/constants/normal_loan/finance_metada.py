from enum import Enum

TYPE_CALCULATION_FINANCE_META = 'CALCULATOR'  # Loại tính toán
TYPE_CLONE_DATA_FINANCE_META = 'CLONE_DATA'  # Clone dữ liệu
TYPE_CONDITION_OBJ_REF_FINANCE_META = 'CONDITION_REF_OBJ'  # Loại tính toán dựa theo điểu kiện dữ liệu


class ECalTypeFinanceMeta(str, Enum):
    id_calculation = TYPE_CALCULATION_FINANCE_META
    id_clone_data = TYPE_CLONE_DATA_FINANCE_META
    id_condition_obj_ref = TYPE_CONDITION_OBJ_REF_FINANCE_META


TYPE_CASH_FLOW_INPUT = 'INPUT'  # Phải trả khách hàng
TYPE_CASH_FLOW_OUTPUT = 'OUTPUT'  # Phải thu khách hàng


class EAverageCashFlowType(str, Enum):
    id_input = TYPE_CASH_FLOW_INPUT
    id_output = TYPE_CASH_FLOW_OUTPUT


METADATA_GROUP_ID_1 = 1
METADATA_GROUP_ID_2 = 2
METADATA_GROUP_ID_3 = 3
METADATA_GROUP_ID_4 = 4

METADATA_GROUP_TYPE = {
    METADATA_GROUP_ID_1: 'business_result_list',  # field trong schema,
    METADATA_GROUP_ID_2: 'asset_balance_capital_list',
    METADATA_GROUP_ID_3: 'business_finance_cash_flow_info',
    METADATA_GROUP_ID_4: 'credit_limit_info'
}

FIELD_TYPE_TOTAL_ASSETS = 'TOTAL_ASSETS'  # field tổng tài sản
FIELD_CAPITAL = 'CAPITAL'  # field Nguồn vốn


class EFieldTypeFinanceMeta(str, Enum):
    id_total_assets = FIELD_TYPE_TOTAL_ASSETS
    id_capital = FIELD_CAPITAL
