from enum import Enum


class ETransportationType(str, Enum):
    """
    Loại PTVT
    chọn 1 trong list: PTVT đường bộ; xe máy chuyên dùng; PTVT không phải đường bộ
    TABLE: LOS_MA_COLL_TYPE (PARENT_ID = 'MEST')
    """
    ROAD_TRANSPORT = "TRVE"
    MECHANIC = "SPVE"
    OTHER = "NRVE"
