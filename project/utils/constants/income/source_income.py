from enum import Enum

# loại nguồn thu nhập
SOURCE_INCOME_TYPE_SALARY = 'SALARY'  # NGUỒN LƯƠNG
SOURCE_INCOME_TYPE_GROUP_ASSET = 'ASSET_RENT'  # TÀI SẢN CHO THUÊ
SOURCE_INCOME_TYPE_BUSINESS_HOUSEHOLD = 'BUSINESS'  # HOẠT ĐỘNG CỦA HỘ KINH DOANH
SOURCE_INCOME_TYPE_COMPANY = 'COMPANY'  # DOANH NGHIỆP DO KHÁCH HÀNG LÀM CHỦ
SOURCE_INCOME_TYPE_STOCK = 'STOCK'  # CỔ TỨC LỢI NHUẬN
SOURCE_INCOME_TYPE_DEPOSIT = 'DIR'  # LÃI TIỀN GỬI / GIẤY TỜ CÓ GIÁ TRỊ
SOURCE_INCOME_TYPE_PENSION = 'PENSION'  # LƯƠNG HƯU TRÍ
SOURCE_INCOME_TYPE_OTHER = 'OTHERS'  # TÀI SẢN KHÁC
SOURCE_INCOME_TYPE_REAL_ESTATE = 'REAL_ESTATE'  # BẤT ĐỘNG SẢN
SOURCE_INCOME_TYPE_ASSET_TRANSPORTATION = 'TRANSPORT'  # PHƯƠNG TIỆN VẬN TẢI CHO THUÊ
SOURCE_INCOME_TYPE_ASSET_OTHER = 'OTHER'  # TÀI SẢN CHO THUÊ KHÁC

# loại hình doanh nghiệp
BUSINESS_TYPE = "BUSINESS_TYPE"
BUSINESS_TYPE_1MLC = "1MLC"  # CÔNG TY TNHH 1 THÀNH VIÊN
BUSINESS_TYPE_2MLC = "2MLC"  # CÔNG TY TNHH 2 THÀNH VIÊN TRỞ LÊN
BUSINESS_TYPE_JSC = "JSC"  # CÔNG TY CỔ PHẦN
BUSINESS_TYPE_PARS = "PARS"  # CÔNG TY HỢP DAN
BUSINESS_TYPE_SOLS = "SOLS"  # DOANG NGHIỆP TƯ NHÂN
BUSINESS_TYPE_BUSP = "BUSP"  # HỘ KINH DOANH
BUSINESS_TYPE_FORC = "FORC"  # CÔNG TY CÓ VỐN NƯỚC NGOÀI
BUSINESS_TYPE_GRPC = "GRPC"  # CÔNG TY LIÊN DOANH

# khu vực hoạt động
BUSINESS_TYPE_SH = 'BUSINESS_TYPE_SH'
BUSINESS_TYPE_SH_STATEOWNED = "STATEOWNED"  # NHÀ NƯỚC
BUSINESS_TYPE_SH_SOLE = "SOLE"  # TƯ NHÂN
BUSINESS_TYPE_SH_FOREOWNED = "FOREOWNED"  # NƯỚC NGOÀI

# phương thức nhận lương
DISBURSEMENT = "DISBURSEMENT"
DISBURSEMENT_CASH = "CASH"  # TIỀN MẶT
DISBURSEMENT_TRANS = "TRANS"  # CHUYỂN KHOẢN

# tần xuất thu nhập
FREQUENCE = 'FREQUENCE'
FREQUENCY_REGULARLY_TYPE = "FREQ"  # THƯỜNG XUYÊN
FREQUENCY_IRREGULARLY_TYPE = "INFREQ"  # KHÔNG THƯỜNG XUYÊN

# loại tài sản cho thuê
ASSET_RENT_TYPE_REAL_ESTATE = "REAL_ESTATE"  # BẤT ĐỘNG SẢN CHO THUÊ
ASSET_RENT_TYPE_TRANSPORT = "TRANSPORT"  # PHƯƠNG TIỆN VẬN TẢI CHO THUÊ
ASSET_RENT_TYPE_OTHER = "OTHER"  # TÀI SẢN CHO THUÊ KHÁC

# đồng ý phong tỏa
ACCEPT_STATUS = "ACCEPT_STATUS"
ACCEPT_STATUS_ACCEPT = "ACCEPT"  # ĐỒNG Ý
ACCEPT_STATUS_UNACCEPT = "UNACCEPT"  # KHÔNG ĐỒNG Ý

#  nhận xét khả năng trả nợ gốc lãi
ACCEPT_FLAG_GURANTEE = "GURANTEE"  # đảm bảo
ACCEPT_FLAG_NOT_GURANTEE = "NOT_GURANTEE"  # không đảm bảo

# loại hợp đồng lao động
CONTRACT_TERM = 'CONTRACT_TERM'
CONTRACT_TERM_PROBATIONARY = 'PROBATIONARY'  # THỬ VIỆC
CONTRACT_TERM_TERM = 'TERM'  # CÓ THỜI HẠN

#  thuộc sở hữu và sử dụng
OWNER_PROPERTY = 'OWNER_PROPERTY'
OWNER_PROPERTY_OWNER = 'OWNER'  # SỞ HỮU RIÊNG
OWNER_PROPERTY_RENT = 'RENT'  # THUÊ

# thuộc sở hữu
RENTAL_OWNER_PROPERTY = 'RENTAL_OWNER_PROPERTY'

# loại hình doanh nghiệp
TYPE_BUSINESS_HOUSEHOLD = 'INCOME_SOURE_TYPE'

ACCEPT_FLAG = 'ACCEPT_FLAG'

# tình trang làm việc
WORK_STATUS = 'WORK_SCHEDULE'
WORK_STATUS_FULL_TIME = 'FULLTIME'
WORK_STATUS_PART_TIME = 'PART_TIME'

# số tiền tối thiểu phải thanh toán
MIN_PAYMENT = 'MIN_PAYMENT'
MIN_PAYMENT_PERCENT = 'MIN_PAYMENT_PERCENT'
MIN_PAYMENT_VALUE = 'MIN_PAYMENT_VALUE'

# loại chi phí
COST_LIVING = 'COST_LIVING'  # phí sinh hoạt gia đình
COST_LOAN = 'COST_LOAN'  # chi phí cho các khoản vay khác ( vay thường )
COST_CREDIT = 'COST_CREDIT'  # Chi Phí trả gốc, lãi KV không gồm nhu cầu vay lần này (VNĐ)
COST_OTHER = 'COST_OTHER'  # Chi phí khác (VNĐ)
COST_HOUSEHOLD_EXPENDITURE = 'COST_HOUSEHOLD_EXPENDITURE'  # Chi tiêu bình quân tháng (VNĐ)

# tỉ lệ nguồn thu nhập
RATIO_REGULARLY = 100
RATIO_IRREGULARLY = 30

# LOAI TAI LIEU
SALARY_TYPE = 20
OTHER_INCOME_TYPE = 27

# NGUOI DAI DIEN HO KINH DOANH
SELF = 'SELF'
MARRIAGE = 'MARRIAGE'


class ESourceIncome(Enum):
    id_source_income_salary = SOURCE_INCOME_TYPE_SALARY
    id_source_income_group_asset = SOURCE_INCOME_TYPE_GROUP_ASSET
    id_source_income_business_household = SOURCE_INCOME_TYPE_BUSINESS_HOUSEHOLD
    id_source_income_company = SOURCE_INCOME_TYPE_COMPANY
    id_source_income_stock = SOURCE_INCOME_TYPE_STOCK
    id_source_income_deposit = SOURCE_INCOME_TYPE_DEPOSIT
    id_source_income_pension = SOURCE_INCOME_TYPE_PENSION
    id_source_income_other = SOURCE_INCOME_TYPE_OTHER
    id_source_income_real_real_estate = SOURCE_INCOME_TYPE_REAL_ESTATE
    id_source_income_asset_transportation = SOURCE_INCOME_TYPE_ASSET_TRANSPORTATION
    id_source_income_asset_other = SOURCE_INCOME_TYPE_ASSET_OTHER


class EBusinessTypeSh(Enum):
    id_business_type_sh_stateowned = BUSINESS_TYPE_SH_STATEOWNED
    id_business_type_sh_sole = BUSINESS_TYPE_SH_SOLE
    id_business_type_sh_foreowned = BUSINESS_TYPE_SH_FOREOWNED


class EFrequency(Enum):
    id_frequency_freq = FREQUENCY_REGULARLY_TYPE
    id_frequency_infreq = FREQUENCY_IRREGULARLY_TYPE


class EDisbursement(Enum):
    id_disbursement_cash = DISBURSEMENT_CASH
    id_disbursement_trans = DISBURSEMENT_TRANS


class EAssetRentType(Enum):
    id_asset_real_estate = ASSET_RENT_TYPE_REAL_ESTATE
    id_asset_transport = ASSET_RENT_TYPE_TRANSPORT
    id_asset_other = ASSET_RENT_TYPE_OTHER


class EBusinessType(Enum):
    id_business_type_1mlc = BUSINESS_TYPE_1MLC
    id_business_type_mlc = BUSINESS_TYPE_2MLC
    id_business_type_jsc = BUSINESS_TYPE_JSC
    id_business_type_pars = BUSINESS_TYPE_PARS
    id_business_type_sols = BUSINESS_TYPE_SOLS
    id_business_type_busp = BUSINESS_TYPE_BUSP
    id_business_type_forc = BUSINESS_TYPE_FORC
    id_business_type_grpc = BUSINESS_TYPE_GRPC


class EAcceptStatus(Enum):
    id_accept_status_accept = ACCEPT_STATUS_ACCEPT
    id_accept_status_unaccept = ACCEPT_STATUS_UNACCEPT


class EAcceptFlagGurantee(Enum):
    id_accept_flag_gurantee = ACCEPT_FLAG_GURANTEE
    id_accept_flag_not_gurantee = ACCEPT_FLAG_NOT_GURANTEE


class EContractTerm(Enum):
    id_contract_term_probationary = CONTRACT_TERM_PROBATIONARY
    id_contract_term_term = CONTRACT_TERM_TERM


class EOwnerPropertyOwner(Enum):
    id_owner_property_owner = OWNER_PROPERTY_OWNER
    id_owner_property_rent = OWNER_PROPERTY_RENT


KEY_SALARY = 'salary'
KEY_ASSET_RENT = 'asset_rent'
KEY_BUSINESS_HOUSEHOLD = 'business_household'
KEY_COMPANY = 'company'
KEY_STOCK = 'stock'
KEY_DEPOSIT = 'deposit'
KEY_PENSION = 'pension'
KEY_OTHER = 'other_income'
# # loại người vay
TYPE_BORROWER = 'borrower'  # NGƯỜI VAY
TYPE_CO_BORROWER = 'co_borrower'  # NGƯỜI ĐỒNG VAY
TYPE_SPOUSE = 'marriage'  # NGƯỜI HÔN PHỐI
TYPE_CO_PAYER = 'co_payer'  # NGƯỜI ĐỒNG TRẢ NỢ
# CUSTOMER_TYPE_LAW_RLT = "LAW_RLT"  # ĐỐI LIÊN HỆ THEO QUY ĐỊNH PHÁP LUẬT
# CUSTOMER_TYPE_RELATED = "RELATED"  # NGƯỜI LIÊN HỆ
