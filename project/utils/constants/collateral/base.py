from enum import Enum

from project.utils.constants import udtm

COLL_TYPE_REAL_ESTATE = "REST"  # "ID_BAT_DONG_SAN"
COLL_TYPE_MACHINE = "DEVI"  # "ID_MAY_MOC_THIET_BI_DAY_CHUYEN_CONG_NGHE"
COLL_TYPE_TRANSPORTATION = "MEST"  # "ID_PHUONG_TIEN_VAN_TAI_DONG_SAN"
COLL_TYPE_CARGO = "GODS"  # "ID_VAT_TU_HANG_HOA"
COLL_TYPE_RIGHT_PROPERTY = "RPRO"  # "ID_QUYEN_TAI_SAN"
COLL_TYPE_STOCK = "STOC"  # "ID_CO_PHIEU_CO_PHAN"
COLL_TYPE_OTHER = "OTHE"  # "ID_TAI_SAN_KHAC"
COLL_TYPE_BALANCE = "BALC"  # Số dư TKTG, HTTG, GTCG

# Loai so huu, (tai san dam bao). Table: LOS_UDTM_LOV
OWNER_TYPE_SELF_OWNER = "SELF"  # "ID_CHINH_CHU"
OWNER_TYPE_CO_OWNER = "CO_BORROWER"  # "ID_DONG_SO_HUU"
OWNER_TYPE_THIRD_PARTY = "THIRD_PARTY"  # "ID_BEN_THU_BA"
OWNER_TYPE_MARRIAGE = "SEPARATE_PROPERTY"  # "ID_TAI_SAN_RIENG_VO_CHONG""

YES = "Y"
NO = "N"

USED_OTHER_CONTRACT_FLAG_SWITCHER = {
    True: YES,
    False: NO
}

OTHER = "OTHER"


class EValuationUnitType(str, Enum):
    """
    chọn 1 trong list:
        + ĐVKD thẩm định giá
        + TT.TĐTS thực hiện thẩm định giá
        + Thuê tổ chức ĐGĐL
    """
    CURRENT_UNIT = "APPRAISAL_BRANCH"
    VALUATION_CENTER = "APPRAISAL_CENTER"
    INDEPENDENCE_ORGANIZATION = "APPRAISAL_VALUATION"


class EValuationCenter(str, Enum):
    """
    TODO: check db
    Nếu trường "Đơn vị thực hiện" chọn "TT.TĐTS thực hiện" Xổ list chọn danh sách các Mảng TĐTS, chọn 1 trong list
    + Mảng TĐTS Hội sở
    + Mảng TĐTS Miền Bắc
    + Mảng TĐTS Miền Đông
    + Mảng TĐTS Miền Tây
    + Mảng TĐTS Hồ Chí Minh 1
    + Mảng TĐTS Hồ Chí Minh 2
    + Mảng TĐTS Miền Trung - Tây Nguyên"
    """
    OTHER = "OTHER"


class EValuationIndependenceOrganization(str, Enum):
    """
    TODO: check db
    Nếu trường "Đơn vị thực hiện" chọn "Thuê tổ chức ĐGĐL" xổ chọn danh sách công ty Thẩm định giá liên kết với SCB
    '+ Công ty CP Thẩm định giá và Đầu tư Sài Sòn Thái Dương (SGVIS)
    + Công ty CP Thẩm định giá Exim (EXIMA)
    + Công ty CP Thông tin và Thẩm định giá Tây Nam Bộ (SIAC)
    + Công ty CP Thẩm định giá BTC VALUE
    + Công ty TNHH Thẩm định giá MHD
    + Công ty TNHH Thẩm định giá Chuẩn Việt (VIETVALUE)
    + Công ty TNHH Thẩm định giá PRD
    + Công ty CP Thẩm định giá và Tư vấn Việt Nam (VNVC)
    + Công ty CP Tư vấn - Dịch vụ về Tài sản - Bất động sản DATC (DCSC)
    + Công ty TNHH Định giá Châu Á (AVC)
    + Công ty CP Định giá và Đầu tư kinh doanh Bất động sản Thịnh Vượng (Thinhvuongcorp)
    + Công ty TNHH Thẩm định giá VAS
    + Khác"
    """
    OTHER = "OTHER"


class EValuationPurpose(str, Enum):
    """
    TODO: check db
    Chọn 1 trong list các mục đích:
        + Cấp tín dụng;
        + Xử lý nợ;
        + định giá lại định kỳ;
        + Khác
    """
    OTHER = "OTHER"


class ECollateralType(str, Enum):
    """
    List danh sách Loại tài sản được nhận làm TSBĐ gồm: "BĐS"; "PTVT"; "MMTB"; "Dây chuyền công nghệ"; "Vật tư hàng hóa"; "Quyền tài sản"; "Chứng khoán"; "Tài sản khác"; "Số dư tiền gửi (TKTG/HĐTG/GTCG"
    """
    REAL_ESTATE = COLL_TYPE_REAL_ESTATE
    MACHINE = COLL_TYPE_MACHINE
    TRANSPORTATION = COLL_TYPE_TRANSPORTATION
    CARGO = COLL_TYPE_CARGO
    RIGHT_PROPERTY = COLL_TYPE_RIGHT_PROPERTY
    STOCK = COLL_TYPE_STOCK
    OTHER = COLL_TYPE_OTHER
    BALANCE = COLL_TYPE_BALANCE


class ECollateralOwnerRelationshipType(str, Enum):
    """
    Nếu chọn tài sản là chính chủ thì hiện các trường đối tượng ""chính chủ sở hữu"", tương tự với Đồng sở hữu và bên thứ ba, chỉ có thể xuất hiện 1 trong 4 tab Chính chủ/Đồng sở hữu/Bên thứ ba/tài sản riêng của vợ/chồng.
     - Chọn ""Chính chủ sở hữu"": Hiển thị thông tin của Khách hàng vay và người hôn phồi (nếu có), người đồng vay đồng thời cùng là chủ sở hữu tài sản
     - Chọn ""Đồng sở hữu"": load thông tin của Khách hàng vay và chọn nhập thêm các chủ tài sản tương ứng đã khai báo ở Step 1 (người liên quan)
     - Chọn ""Bên thứ 3"": Chọn các chủ tài sản tương ứng đã khai báo ở step 1 (người liên quan), nhập liệu các thông tin của bên thứ 3
    - Chọn ""tài sản riêng của vợ/chồng"" cho phép load thông tin của Vợ/chồng tại thông tin KH vay (các trường thông tin tương tự như ""bên thứ 3
    """
    SELF_OWNER = OWNER_TYPE_SELF_OWNER
    CO_OWNER = OWNER_TYPE_CO_OWNER
    THIRD_PARTY = OWNER_TYPE_THIRD_PARTY
    ID_MARRIAGE = OWNER_TYPE_MARRIAGE


YES_NO_QUESTION = {
    True: YES,
    False: NO
}


class CollateralUDTM(str, Enum):
    """
        Tất cả config collateral
    """

    # Loai so huu, (tai san dam bao). Table: LOS_UDTM_LOV
    COLLATERAL_OWNER_RELATIONSHIP_TYPE = udtm.COLLATERAL_OWNER_RELATIONSHIP_TYPE

    # Đơn vị thực hiện thẩm định giá
    VALUATION_UNIT_TYPE = udtm.VALUATION_UNIT_TYPE

    # Mục đích định giá
    COLLATERAL_VALUATION_PURPOSE = udtm.COLLATERAL_VALUATION_PURPOSE

    # Trạng thái bất động sản
    COLLATERAL_REAL_ESTATE_STATUS = udtm.COLLATERAL_REAL_ESTATE_STATUS

    # Loại vị trí
    COLLATERAL_LOCATION_TYPE = udtm.COLLATERAL_LOCATION_TYPE

    # Chiều rộng đường hiện hữu
    COLLATERAL_LANE_WIDTH = udtm.COLLATERAL_LANE_WIDTH

    # Loại GCN quyền sử dụng đất
    COLLATERAL_LAND_CERT_TYPE = udtm.COLLATERAL_LAND_CERT_TYPE

    # Mục đích sử dụng đất (theo thẩm định giá) của đất của bất động sản loại 1
    COLLATERAL_LAND_ASSET_VALUATION_LAND_USE_PURPOSE = udtm.COLLATERAL_LAND_ASSET_VALUATION_LAND_USE_PURPOSE

    # Mục đích sử dụng đất (theo thẩm định giá) của đất của bất động sản loại 2
    COLLATERAL_APARTMENT_VALUATION_LAND_USE_PURPOSE = udtm.COLLATERAL_APARTMENT_VALUATION_LAND_USE_PURPOSE

    # Nguồn gốc sử dụng đất theo GCN
    COLLATERAL_CERT_LAND_USE_SOURCE = udtm.COLLATERAL_CERT_LAND_USE_SOURCE

    # Hình thức sử dụng đất theo GCN
    COLLATERAL_CERT_LAND_USE_FORM = udtm.COLLATERAL_CERT_LAND_USE_FORM

    # Pháp lý CTXD
    COLLATERAL_LAND_ASSET_LEGAL = udtm.COLLATERAL_LAND_ASSET_LEGAL

    # Loại GCN quyền sở hữu CTXD/nhà ở
    COLLATERAL_CONST_CERT_TYPE = udtm.COLLATERAL_CONST_CERT_TYPE

    # Loại công trình
    COLLATERAL_LAND_ASSET_TYPE = udtm.COLLATERAL_LAND_ASSET_LEGAL

    # Tình trạng pháp lý
    COLLATERAL_APARTMENT_LEGAL_STATUS = udtm.COLLATERAL_APARTMENT_LEGAL_STATUS

    # Mục đích sử dụng đất (theo định giá)
    COLLATERAL_APARTMENT_USED_PURPOSE = udtm.COLLATERAL_APARTMENT_USED_PURPOSE

    # Loại căn hộ
    COLLATERAL_APARTMENT_TYPE = udtm.COLLATERAL_APARTMENT_TYPE

    # Tình trạng PTVT
    COLLATERAL_TRANS_STATUS = udtm.COLLATERAL_TRANS_STATUS

    # Máy móc thiết bị / Tình trạng tài sản
    COLLATERAL_MACHINE_STATUS = udtm.COLLATERAL_MACHINE_STATUS

    # Vật tư hàng hóa / Tình trạng tài sản
    COLLATERAL_CARGO_STATUS = udtm.COLLATERAL_CARGO_STATUS

    # Quyền sở hữu tài sản / Tình trạng tài sản
    COLLATERAL_RIGHT_PROPERTY_STATUS = udtm.COLLATERAL_RIGHT_PROPERTY_STATUS

    # Loại tài sản
    COLLATERAL_BALANCE_TYPE = udtm.COLLATERAL_BALANCE_TYPE
