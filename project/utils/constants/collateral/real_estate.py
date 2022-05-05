# Loai bat dong san. Table: LOS_MA_COLL_TYPE
from decimal import Decimal
from enum import Enum

REAL_ESTATE_TYPE_MARKET = "MARK"  # "ID_SAP_CHO_O_TTTM"
REAL_ESTATE_TYPE_LAND_ASSET = "LAND"  # "ID_DAT_NHA_RIENG_LE"
REAL_ESTATE_TYPE_APARTMENT = "APPA"  # "ID_CAN_HO_CHUNG_CU"

# Tinh trang tai san dam bao
COLLATERAL_STATUS_TYPE_BUSINESS = "RE_BUSINESS"
COLLATERAL_STATUS_TYPE_COMPOSITE = "RE_MIXED"
COLLATERAL_STATUS_TYPE_NONE_BUSINESS = "RE_NOT_BUSINESS"

COLL_MIN_PERCENTAGE_REAL_ESTATE_LAND_ASSET = Decimal("0")
COLL_MIN_PERCENTAGE_REAL_ESTATE_APARTMENT = Decimal("0")
COLL_MIN_PERCENTAGE_REAL_ESTATE_MARKET = Decimal("0")
COLL_MIN_PERCENTAGE_TRANS = Decimal("0")
COLL_MIN_PERCENTAGE_MACHINE = Decimal("0")
COLL_MIN_PERCENTAGE_CARGO = Decimal("0")
COLL_MIN_PERCENTAGE_RIGHT_PROPERTY = Decimal("0")
COLL_MIN_PERCENTAGE_STOCK = Decimal("0")
COLL_MIN_PERCENTAGE_OTHER = Decimal("0")
COLL_MIN_PERCENTAGE_BALANCE = Decimal("0")

COLL_MAX_PERCENTAGE_REAL_ESTATE_LAND_ASSET = Decimal("100")
COLL_MAX_PERCENTAGE_REAL_ESTATE_APARTMENT = Decimal("80")
COLL_MAX_PERCENTAGE_REAL_ESTATE_MARKET = Decimal("80")
COLL_MAX_PERCENTAGE_TRANS = Decimal("80")
COLL_MAX_PERCENTAGE_MACHINE = Decimal("80")
COLL_MAX_PERCENTAGE_CARGO = Decimal("80")
COLL_MAX_PERCENTAGE_RIGHT_PROPERTY = Decimal("80")
COLL_MAX_PERCENTAGE_STOCK = Decimal("80")
COLL_MAX_PERCENTAGE_OTHER = Decimal("80")
COLL_MAX_PERCENTAGE_BALANCE = Decimal("80")


class ECollateralMinPercentage(Decimal, Enum):
    """
    Tỉ lệ cho vay tối thiểu
    """
    REAL_ESTATE_LAND_ASSET = COLL_MIN_PERCENTAGE_REAL_ESTATE_LAND_ASSET
    REAL_ESTATE_APARTMENT = COLL_MIN_PERCENTAGE_REAL_ESTATE_APARTMENT
    REAL_ESTATE_MARKET = COLL_MIN_PERCENTAGE_REAL_ESTATE_MARKET
    TRANS = COLL_MIN_PERCENTAGE_TRANS
    MACHINE = COLL_MIN_PERCENTAGE_MACHINE
    CARGO = COLL_MIN_PERCENTAGE_CARGO
    RIGHT_PROPERTY = COLL_MIN_PERCENTAGE_RIGHT_PROPERTY
    STOCK = COLL_MIN_PERCENTAGE_STOCK
    OTHER = COLL_MIN_PERCENTAGE_OTHER
    BALANCE = COLL_MIN_PERCENTAGE_BALANCE


class ECollateralMaxPercentage(Decimal, Enum):
    """
    Tỉ lệ cho vay tối đa theo quy định
    """
    REAL_ESTATE_LAND_ASSET = COLL_MAX_PERCENTAGE_REAL_ESTATE_LAND_ASSET
    REAL_ESTATE_APARTMENT = COLL_MAX_PERCENTAGE_REAL_ESTATE_APARTMENT
    REAL_ESTATE_MARKET = COLL_MAX_PERCENTAGE_REAL_ESTATE_MARKET
    TRANS = COLL_MAX_PERCENTAGE_TRANS
    MACHINE = COLL_MAX_PERCENTAGE_MACHINE
    CARGO = COLL_MAX_PERCENTAGE_CARGO
    RIGHT_PROPERTY = COLL_MAX_PERCENTAGE_RIGHT_PROPERTY
    STOCK = COLL_MAX_PERCENTAGE_STOCK
    OTHER = COLL_MAX_PERCENTAGE_OTHER
    BALANCE = COLL_MAX_PERCENTAGE_BALANCE


class ERealEstateStatus(str, Enum):
    """
    Trạng thái bất động sản:
    "BĐS có kinh doanh";
    "BĐS không kinh doanh";
    "BĐS hỗn hợp"
    TABLE: UDTM (FIELD_NAME = COLL_RE_STATUS)
    """
    BUSINESS = COLLATERAL_STATUS_TYPE_BUSINESS
    NON_BUSINESS = COLLATERAL_STATUS_TYPE_NONE_BUSINESS
    COMPOSITE = COLLATERAL_STATUS_TYPE_COMPOSITE


class ECollateralRealEstateType(str, Enum):
    """
    Loại bất động sản:
    Table: LOS_MA_COLL_TYPE
    Loại 1: - QSDĐ là đất và/hoặc Nhà riêng lẻ;
    - QSDĐ là đất thuê trong KCN;
    - Nhà nhiều hộ, nhiều tầng;
    - QSDĐ là đất thuê ngoài KCN;
    - QSDĐ là đất có nguồn gốc vừa giao vừa thuê ngoài KCN;
    - Bất động sản khác.
    - Dự án;
    Loại 2:
    - Quyền sở hữu căn hộ chung cư;
    - Căn hộ chung cư đã hình thành nhưng chưa được cấp GCN;
    - Căn hộ hình thành trong tương lai;
    Loại 3:
    - Sạp chợ/Ô TTTM;
    """
    MARKET = REAL_ESTATE_TYPE_MARKET
    LAND_ASSET = REAL_ESTATE_TYPE_LAND_ASSET
    APARTMENT = REAL_ESTATE_TYPE_APARTMENT


""" LAND """


class ECertificateLandUseSource(str, Enum):
    """
    Nguồn gốc sử dụng đất theo GCN
    "Chọn 1 trong list:
    + Nhà nước giao đất có thu tiền sử dụng đất
    + Nhà nước giao đất không thu tiền sử dụng đất
    + Nhà nước công nhận quyền sử dụng đất
    + Nhà nước công nhận quyền sử dụng đất như Nhà nước giao đất có thu tiền sử dụng đất
    + Nhà nước công nhận quyền sử dụng đất như Nhà nước giao đất không thu tiền sử dụng đất
    + Nhà nước công nhận QSDĐ như Nhà nước giao đất có thu tiền sử dụng đất
    + Nhà nước công nhận QSDĐ như Nhà nước giao đất không thu tiền sử dụng đất
    + Công nhận QSDĐ như giao đất không thu tiền sử dụng đất
    + Công nhận QSDĐ như giao đất có thu tiền sử dụng đất
    + Nhận chuyển nhượng đất được Công nhận QSDĐ như giao đất có thu tiền sử dụng đất
    + Nhận chuyển nhượng đất được Công nhận QSDĐ như giao đất không thu tiền sử dụng đất
    + Được tặng cho đất được Công nhận QSDĐ như giao đất có thu tiền sử dụng đất.
    + Được tặng cho đất được Công nhận QSDĐ như giao đất không thu tiền sử dụng đất
    + Khác"
    """
    OTHER = "LS_14"


""" LAND ASSET """


class ELandAssetLegal(str, Enum):
    """
    Pháp lý CTXD
    chọn 1 trong list: Không có CTXD; Đã được công nhận QSH CTXD; có GPXD; Không có GPXD; khác
    TABLE: LOS_UDTM_LOV WHERE (FIELD_NAME = 'COLL_RE_CONS_LEGAL')
    """
    NON_LAND_ASSET = "NO_ALLBUILD_CERT"  # Không có GPXD
    RECOGNIZE_LAND_ASSET_RIGHT_PROPERTY = "ACCEPTOWN"  # Đã được công nhận QSH CTXD
    HAS_CONSTRUCTION_PERMIT = "ALLBUILD_CERT"  # Có GPXD
    NON_CONSTRUCTION_PERMIT = "NOCONST"  # Không có CTXD
    OTHER = "OTHER"


""" APARTMENT """
