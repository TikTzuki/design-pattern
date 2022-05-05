from enum import auto

from fastapi_utils.enums import StrEnum


class EPosition(StrEnum):
    U1 = auto()
    "Nhóm sản phẩm"
    U2 = auto()
    "Thông tin pháp lý"
    U2_BO = auto()
    "Người vay"
    U2_CB = auto()
    "Người đồng vay"
    U2_CE = auto()
    "Người liên hệ"
    U2_CP = auto()
    "Người đồng trả nợ"
    U2_MA = auto()
    "Người hôn phối"
    U2_OT = auto()
    "Đối tượng khác"
    U2_RE = auto()
    "Người liên quan theo QDPL"
    U3 = auto()
    "Thông tin CIC"
    U3_OI = auto()
    "Quan hệ tại các tổ chức tín dụng khác"
    U3_OI_BO = auto()
    "Người vay"
    U3_OI_CB = auto()
    "Người đồng vay"
    U3_OI_CP = auto()
    "Người đồng trả nợ"
    U3_OI_MA = auto()
    "Người hôn phối"
    U3_OI_OT = auto()
    "Đối tượng khác"
    U3_OI_RE = auto()
    "Người liên quan theo QDPL"
    U3_SC = auto()
    "Khoản vay hiện hữu tại SCB"
    U3_SC_BO = auto()
    "Người vay"
    U3_SC_CB = auto()
    "Người đồng vay"
    U3_SC_CP = auto()
    "Người đồng trả nợ"
    U3_SC_MA = auto()
    "Người hôn phối"
    U3_SC_OT = auto()
    "Đối tượng khác"
    U3_SC_RE = auto()
    "Người liên quan theo QDPL"
    U4 = auto()
    "Thông tin khoản vay"
    U4_CP = auto()
    "Nhu cầu vốn và phương án vay vốn"
    U4_OB = auto()
    "Hoạt động sản xuất kinh doanh"
    U4_OB_BH = auto()
    "Pháp lý hộ kinh doanh"
    U4_OB_FA = auto()
    "Phân tích tài chính"
    U4_PR = auto()
    "Thông tin sản phẩm chương trình vay"
    U5 = auto()
    "Nguồn thu nhập"
    U5_BA = auto()
    "Cân đối thu nhập - chi phí"
    U5_BO = auto()
    "Người vay"
    U5_BO_AS = auto()
    "Cho thuê tài sản"
    U5_BO_BU = auto()
    "Hoạt động của hộ kinh doanh"
    U5_BO_CO = auto()
    "Doanh nghiệp do khách hàng làm chủ"
    U5_BO_DE = auto()
    "Lãi tiền gởi / Giấy tờ có giá"
    U5_BO_OT = auto()
    "Nguồn thu khác"
    U5_BO_PE = auto()
    "Lương hưu trí"
    U5_BO_SL = auto()
    "Nguồn lương"
    U5_BO_ST = auto()
    "Cổ tức / Lợi nhuận"
    U5_CB = auto()
    "Người đồng vay"
    U5_CB_AS = auto()
    "Cho thuê tài sản"
    U5_CB_BU = auto()
    "Hoạt động của hộ kinh doanh"
    U5_CB_CO = auto()
    "Doanh nghiệp do khách hàng làm chủ"
    U5_CB_DE = auto()
    "Lãi tiền gởi / Giấy tờ có giá"
    U5_CB_OT = auto()
    "Nguồn thu khác"
    U5_CB_PE = auto()
    "Lương hưu trí"
    U5_CB_SL = auto()
    "Nguồn lương"
    U5_CB_ST = auto()
    "Cổ tức / Lợi nhuận"
    U5_CP = auto()
    "Người đồng trả nợ"
    U5_CP_AS = auto()
    "Cho thuê tài sản"
    U5_CP_BU = auto()
    "Hoạt động của hộ kinh doanh"
    U5_CP_CO = auto()
    "Doanh nghiệp do khách hàng làm chủ"
    U5_CP_DE = auto()
    "Lãi tiền gởi / Giấy tờ có giá"
    U5_CP_OT = auto()
    "Nguồn thu khác"
    U5_CP_PE = auto()
    "Lương hưu trí"
    U5_CP_SL = auto()
    "Nguồn lương"
    U5_CP_ST = auto()
    "Cổ tức / Lợi nhuận"
    U5_MA = auto()
    "Người hôn phối"
    U5_MA_AS = auto()
    "Cho thuê tài sản"
    U5_MA_BU = auto()
    "Hoạt động của hộ kinh doanh"
    U5_MA_CO = auto()
    "Doanh nghiệp do khách hàng làm chủ"
    U5_MA_DE = auto()
    "Lãi tiền gởi / Giấy tờ có giá"
    U5_MA_OT = auto()
    "Nguồn thu khác"
    U5_MA_PE = auto()
    "Lương hưu trí"
    U5_MA_SL = auto()
    "Nguồn lương"
    U5_MA_ST = auto()
    "Cổ tức / Lợi nhuận"
    U5_OT = auto()
    "Đối tượng khác"
    U5_OT_AS = auto()
    "Cho thuê tài sản"
    U5_OT_BU = auto()
    "Hoạt động của hộ kinh doanh"
    U5_OT_CO = auto()
    "Doanh nghiệp do khách hàng làm chủ"
    U5_OT_DE = auto()
    "Lãi tiền gởi / Giấy tờ có giá"
    U5_OT_OT = auto()
    "Nguồn thu khác"
    U5_OT_PE = auto()
    "Lương hưu trí"
    U5_OT_SL = auto()
    "Nguồn lương"
    U5_OT_ST = auto()
    "Cổ tức / Lợi nhuận"
    U5_PA = auto()
    "Khả năng trả nợ gốc lãi"
    U6 = auto()
    "Tài sản bảo đảm"
    U7 = auto()
    "Hồ sơ khác"
    U7_AM = auto()
    "Phân tích và biện pháp hạn chế rủi ro"
    U7_EX = auto()
    "Thông tin ngoại lệ"
    U8 = auto()
    "XHTDNB"
    U9 = auto()
    "Biểu mẫu"
