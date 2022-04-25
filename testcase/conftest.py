from testcase.__init__ import *


@pytest.fixture(scope="session")
def tool_instance():
    ym = YamlTools()
    rsp = Request()
    conf = DoConf(constant.globe_conf_dir)
    log = DoLogs(__name__)
    yield conf, ym, rsp,log


@pytest.fixture(scope="class")
def get_driver(tool_instance):
    """
    登陸
    :return:
    """
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", tool_instance[1].read_yaml(constant.dev_desired_caps_dir))
    yield driver, tool_instance
    driver.close_app()


@pytest.fixture(scope="class")
def login_driver(tool_instance):
    """
    登陸
    :return:
    """
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", tool_instance[1].read_yaml(constant.dev_desired_caps_dir))
    # Login(driver).login(tool_instance[0].get_value("data", "user"), tool_instance[0].get_value("data", "pwd"))
    yield driver, tool_instance
    driver.close_app()

