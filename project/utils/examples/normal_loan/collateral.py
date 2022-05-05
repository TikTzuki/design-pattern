from datetime import datetime

from project.utils import functions

_price_cert_uuid = functions.generate_uuid()
_price_cert_asset_uuid = functions.generate_uuid()
_COLLATERAL_LTV_EXAMPLE_POST = {
    "rows": [
        {
            "coll_price_cert_uuid": _price_cert_uuid,
            "coll_price_cert_asset_uuid": _price_cert_asset_uuid,
            "loan_credit": 1_000,
            "temp_calc_value": 1_000,
            "max_ltv_value": 90,
            "max_loan_credit": 1_0000,
            "safely_debit": 1_000,
            "ltv_value": 80,
            "uuid": None,
        },
    ],
    "uuid": functions.generate_uuid()
}

_COLLATERAL_LTV_EXAMPLE_GET = {
    "current_ltv": {
        "rows": [
            {
                "coll_price_cert_uuid": "eaa52f0a-cd64-4e30-b28b-5c50eb07a588",
                "coll_price_cert_asset_uuid": "3b8c78b9-36eb-43ac-a0b9-6996988424dc",
                "loan_credit": 1000,
                "temp_calc_value": 1000,
                "max_ltv_value": 90,
                "max_loan_credit": 10000,
                "safely_debit": 1000,
                "ltv_value": 80,
                "uuid": "f6225055-8e0f-44fc-bca5-30e00d45cf43"
            }
        ],
        "uuid": "701e8e88-16fb-4cc8-b2f2-53319f702e0d",
        "title": "Bảng tính LTV 2022-04-18T23:25:35.158872",
        "is_activated": True,
        "updated_by": "TUNN",
        "updated_at": 1650299179.542654
    },
    "logs": [
        {
            "title": "Bảng tính LTV 2022-04-18T23:25:35.158872",
            "rows": [
                {
                    "coll_price_cert_uuid": "eaa52f0a-cd64-4e30-b28b-5c50eb07a588",
                    "coll_price_cert_asset_uuid": "3b8c78b9-36eb-43ac-a0b9-6996988424dc",
                    "loan_credit": 1000,
                    "temp_calc_value": 1000,
                    "max_ltv_value": 90,
                    "max_loan_credit": 10000,
                    "safely_debit": 1000,
                    "ltv_value": 80,
                    "uuid": "f6225055-8e0f-44fc-bca5-30e00d45cf43"
                }
            ],
            "is_activated": True,
            "updated_by": "TUNN",
            "updated_at": 1650299179.542654,
            "uuid": "701e8e88-16fb-4cc8-b2f2-53319f702e0d"
        },
        {
            "title": "Bảng tính LTV 2022-04-18T23:25:41.930857",
            "rows": [
                {
                    "coll_price_cert_uuid": "eaa52f0a-cd64-4e30-b28b-5c50eb07a588",
                    "coll_price_cert_asset_uuid": "3b8c78b9-36eb-43ac-a0b9-6996988424dc",
                    "loan_credit": 1000,
                    "temp_calc_value": 1000,
                    "max_ltv_value": 90,
                    "max_loan_credit": 10000,
                    "safely_debit": 1000,
                    "ltv_value": 80,
                    "uuid": "6fd44d93-7339-4a08-9879-9dc5b9413c49"
                }
            ],
            "is_activated": False,
            "updated_by": "TUNN",
            "updated_at": 1650299141.930857,
            "uuid": "ce11117a-a899-4c9b-9fbd-51457ff3ce40"
        }
    ]
}
COLLATERAL_LTV_EXAMPLES = {
    "post": {
        "value": _COLLATERAL_LTV_EXAMPLE_POST
    },
    "get": {
        "value": _COLLATERAL_LTV_EXAMPLE_GET
    }
}
COLLATERAL_APPRISE_EXAMPLES = {
    "first": {
        "is_accept": True,
        "reason": "reason to apprise collateral"
    }
}
