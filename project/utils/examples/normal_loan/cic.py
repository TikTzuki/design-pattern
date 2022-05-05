from datetime import datetime

CIC_API_GET_EXAMPLE = {
    "name": "Nguyen Tran Phong Vu",
    "total_balance": "2_729_720_000",
    "total_collateral_value": "1_000_720_000",
    "highest_debt_group": "MEDIUM",
    "flex_cube_date": datetime(2021, 5, 20).timestamp(),
    "identities": [
        {
            "identity_type": "CMND",
            "identity_number": "343525968",
            "loan_last_update_date": datetime(2021, 5, 12).timestamp(),
            "card_last_update_date": datetime(2021, 5, 12).timestamp(),
            "loan_wrapper": [
                {
                    "institution_id": 1,
                    "institution_name": "Ngan hang hsbc",
                    "loans": [
                        {
                            "credit_term": "12",
                            "debt": 5_000,
                            "debt_group": "MEDIUM",
                            "credit_limit": 10_000
                        }
                    ]
                },
            ],
            "card_wrapper": [
                {
                    "institution_id": 1,
                    "institution_name": "Ngan hang hsbc",
                    "cards": [
                        {
                            "credit_name": "The tin dung",
                            "debt": 5_000,
                            "debt_group": "MEDIUM",
                            "credit_limit": 10_000,
                        }
                    ]
                }
            ],
            "collateral_wrapper": [
                {
                    "name": "",
                    "collateral_type": "",
                    "collateral_value": "",
                }
            ],
            "highest_debt_last_twelve_months": 1_000_000,
            "credit_card_liability": 3_000_000,
            "liability_note": "Tinh theo 5% han muc tin dung"
        }
    ]
}
CIC_API_POST_EXAMPLE = {
    "name": "Nguyen Tran Phong Vu",
    "total_balance": "2_729_720_000",
    "total_collateral_value": "1_000_720_000",
    "highest_debt_group": "MEDIUM",
    "flex_cube_date": datetime(2021, 5, 20).timestamp(),
    "identities": [
        {
            "identity_type": "CMND",
            "identity_number": "343525968",
            "loan_last_update_date": datetime(2021, 5, 12).timestamp(),
            "card_last_update_date": datetime(2021, 5, 12).timestamp(),
            "loan_wrapper": [
                {
                    "institution_id": 1,
                    "institution_name": "Ngan hang hsbc",
                    "loans": [
                        {
                            "credit_term": "12",
                            "debt": 5_000,
                            "debt_group": "MEDIUM",
                            "credit_limit": 10_000,
                            "is_early_loan_settlement": "Y"
                        }
                    ]
                },
            ],
            "card_wrapper": [
                {
                    "institution_id": 1,
                    "institution_name": "Ngan hang hsbc",
                    "cards": [
                        {
                            "credit_name": "The tin dung",
                            "debt": 5_000,
                            "debt_group": "MEDIUM",
                            "credit_limit": 10_000,
                        }
                    ]
                }
            ],
            "collateral_wrapper": [
                {
                    "name": "",
                    "collateral_type": "",
                    "collateral_value": "",
                }
            ],
            "highest_debt_last_twelve_months": 1_000_000,
            "credit_card_liability": 3_000_000,
            "liability_note": "Tinh theo 5% han muc tin dung"
        }
    ],
    "is_satisfied": "Y",
    "note": "ghi chu"
}
