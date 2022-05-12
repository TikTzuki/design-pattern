from enum import auto
from fastapi_utils.enums import StrEnum
class EState(StrEnum):
	approving = auto()
	"Hồ sơ đang phê duyệt"
	closed = auto()
	"Hồ sơ đã đóng"
	controlling = auto()
	"Hồ sơ đang kiểm soát"
	disbursement = auto()
	"Hồ sơ được giải ngân"
	init = auto()
	"Khai báo hồ sơ"
	s1_a1_start_event = auto()
	"s1_a1_start_event"