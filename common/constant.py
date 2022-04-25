import os

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

conf_test_dir = os.path.join(root_dir, 'config', 'conf_test.cfg')

conf_uat_dir = os.path.join(root_dir, 'config', 'conf_uat.cfg')

conf_prod_dir = os.path.join(root_dir, 'config', 'conf_prod.cfg')

globe_conf_dir = os.path.join(root_dir, 'config', 'globe_conf.cfg')

excel_dir = os.path.join(root_dir, 'datas', 'user_cases.xlsx')

report_dir = os.path.join(root_dir, 'report')

data_dir = os.path.join(root_dir, 'datas')

log_dir = os.path.join(root_dir, 'log')

screenshots_dir = os.path.join(root_dir, 'outputs\screenshots')

file_dir = os.path.join(root_dir, 'datas', 'web安全测试模板.docx')

dev_desired_caps_dir = os.path.join(root_dir, 'datas', 'desired_caps.yaml')

dev_desired_caps_tea_dir = os.path.join(root_dir, 'datas', 'desired_caps_tea.yaml')

house_add_data_dir = os.path.join(root_dir, 'datas', 'add_house_data.yaml')

house_list_data_dir = os.path.join(root_dir, 'datas', 'house_list_data.yaml')
