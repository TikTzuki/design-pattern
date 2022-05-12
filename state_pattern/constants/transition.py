from enum import auto
from fastapi_utils.enums import StrEnum
class ETransition(StrEnum):
	approving_approve_disbursement = auto()
	"Đem hồ sơ đi giải ngân"
	approving_close_closed = auto()
	"Đóng hồ sơ"
	approving_return_init_init = auto()
	"Trả hồ sơ"
	controlling_apply_approve_approving = auto()
	"Trình hồ sơ"
	controlling_close_closed = auto()
	"Đóng hồ sơ"
	init_apply_control_controlling = auto()
	"Trình hồ sơ"
	init_close_closed = auto()
	"Đóng hồ sơ"
	s1_a1_start_event_save_init = auto()
	"None"