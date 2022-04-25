import pytest
from common.base_context import BaseContext
from appium import webdriver
from common import constant
from common.ConfTools import DoConf
from common.LogTools import DoLogs
from common.yaml_tools import YamlTools
from page_object.login_obj import Login
from page_object.index_obj import Index
from page_object.add_house_obj import AddHouse
from page_object.house_list_obj import HouseList
from common import context
from common.HttpRequest import Request
