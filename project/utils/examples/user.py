USER_INFO = {
    "user_id": "13537",
    "user_name": "tannd6",
    "full_name": "Nguyễn Duy Tân",
    "avatar": "cdm/tannd6.jpg",
    "branch": {
        "branch_code": "001",
        "branch_name": "Cống quỳnh",
        "branch_address": "Nguyễn Kiệm",
        "branch_parent_code": "string",
        "branch_tax_code": "1234",
        "branch_phone": "09123654",
        "branch_status": "status",
        "branch_region_code": "region_code",
        "branch_region_name": "region_name"
    },
    "department": {
        "id": "15888",
        "code": "P.PTUD",
        "name": "Phòng Phát triển ứng dụng"
    }
}
USER_LOGIN = {
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0YW5uZDYiLCJpYXQiOjE2MjY0MzIxNzksImV4cCI6MTY1Nzk2ODE3OSwiaXNzIjoiaHR0cHM6Ly9sb3Mtc2V2ZXIiLCJhdWQiOiJodHRwczovL2xvcy1jbGllbnQifQ.CQh5yN3i7tpGL_xVFpflUuIcODqSCn_dBInaQQKBP5Q",
    "user_info": USER_INFO,
    "global_config": {
        "countries": "VN"
    }
}
LOGIN_REQUEST = {
    "username": "BICHNTN",
    "password": "Scb@1234"
}
GLOBAL_CONFIG = {
    "countries": "VN"
}
AUTHORIZED_USER = {
    'user_info': {
        'user_id': '13537', 'user_name': 'BICHNTN', 'full_name': 'Nguyễn Thị Ngọc Bích', 'avatar': 'cdm/tannd6.jpg',
        'branch': {
            'branch_code': '122',
            'branch_name': 'PGD DINH TIEN HOANG',
            'branch_address': '41 Dinh Tien Hoang, P.3, Q.Binh Thanh',
            'branch_parent_code': '021',
            'branch_tax_code': '1234',
            'branch_phone': '0311449990',
            'branch_status': 'Y',
            'branch_region_code': 'Y',
            'branch_region_name': 'V01'
        },
        'department': {
            'id': '15888', 'code': 'P.PTUD', 'name': 'Phòng Phát triển ứng dụng'
        }
    },
    'menu_list': [
        {
            'parent_id': None,
            'menu_id': 'f51b9702-37f8-4ead-91e4-55f49a2bce51',
            'menu_name': 'los',
            'menu_code': 'LOS',
            'group_role_list': [
                {
                    'group_role_id': '76617133-d942-4d58-978a-475d0a3687d2',
                    'group_role_code': 'TRA_HO_SO',
                    'group_role_name': 'Chuyển trả hồ sơ về Kiểm soát',
                    'permission_list': [
                        {
                            'permission_id': '6400bcb5-8d5c-45c9-a457-4417a7b5e12b',
                            'permission_name': 'Chuyển trả hồ sơ về kiểm soát',
                            'permission_code': 'CT_HS_KS',
                            'active_flag': 1
                        }
                    ],
                    'is_permission': True
                },
                {
                    'group_role_id': '16499863-60ac-42e8-8ec8-d6dba95116a5', 'group_role_code': 'KHOI_TAO', 'group_role_name': 'Khởi tạo chỉnh,',
                    'permission_list': [
                        {
                            'permission_id': 'd567bd84-8579-4a71-afa3-b201fdeede61',
                            'permission_name': 'Chỉnh sửa hồ sơ',
                            'permission_code': 'CS_HS',
                            'active_flag': 1
                        },
                        {
                            'permission_id': 'd6db5ca1-fe74-4613-88c5-0e431cc792db',
                            'permission_name': 'Khởi tạo hồ sơ',
                            'permission_code': 'KHOITAO_HS', 'active_flag': 1
                        }
                    ],
                    'is_permission': True
                },
                {
                    'group_role_id': '250e3bed-02f9-4dc9-8771-a7076390e43f',
                    'group_role_code': 'KS_HO_SO',
                    'group_role_name': 'Kiểm soát hồ sơ',
                    'permission_list': [
                        {
                            'permission_id': '94a3cbd9-06d9-4be4-9e32-716c6a2ae9ed',
                            'permission_name': 'Kiểm soát hồ sơ',
                            'permission_code': 'KS_HS', 'active_flag': 1
                        }
                    ],
                    'is_permission': False
                },
                {
                    'group_role_id': 'c716975a-8bdb-4c79-bb8e-4063b6db45bf',
                    'group_role_code': 'TRA_HOKK',
                    'group_role_name': 'Chuyển trả hồ sơ về BP Khởi tạo',
                    'permission_list': [
                        {
                            'permission_id': '61fda20d-5a5a-4f1c-b87a-b0db6d267d0d',
                            'permission_name': 'Chuyển trả hồ sơ về BP Khởi tạo',
                            'permission_code': 'CT_HS_BPKT',
                            'active_flag': 1
                        }
                    ],
                    'is_permission': True
                },
                {
                    'group_role_id': 'a18920c5-7a2a-495f-9c0f-863c85d0e236',
                    'group_role_code': 'PHE_DUYET_HS_VAY',
                    'group_role_name': 'Phê duyệt hồ sơ vay',
                    'permission_list': [
                        {
                            'permission_id': 'dc93e4ce-dbdf-41e7-a22a-7ee880475745', 'permission_name': 'Phê duyệt', 'permission_code': 'PD_HS', 'active_flag': 1
                        }
                    ],
                    'is_permission': True
                }
            ]
        },
        {'parent_id': None, 'menu_id': 'be63298c-ddd3-4fa9-9609-aabe68fda3c6', 'menu_name': 'Admin', 'menu_code': 'LOS3', 'group_role_list': []},
        {'parent_id': None, 'menu_id': '33682a29-5c90-449d-85df-25889be9b7e5', 'menu_name': 'los2', 'menu_code': 'LOS1', 'group_role_list': []},
        {'parent_id': None, 'menu_id': '7cf03600-f8f1-472d-a70b-5856197a1b91', 'menu_name': 'ádasd', 'menu_code': 'testok', 'group_role_list': []}]}
