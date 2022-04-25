import datetime

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time
from common import constant, LogTools


class BaseContext:

    def __init__(self, driver):
        self.driver = driver
        self.log = LogTools.DoLogs(__name__)

    def save_web_screenshot(self, img_doc):
        """
        封装一个截图的方法
        :param img_doc:
        :return:
        """
        now_time = time.strftime("%Y-%m-%d %H-%M-%S")  # 获取当前时间并以字符串返回
        filename = "{}_{}".format(img_doc, now_time)
        try:
            self.driver.save_screenshot(constant.screenshots_dir + '/' + filename + '.png')
            self.log.mylog.debug("截图成功，图片保存在{}".format(constant.screenshots_dir + '/' + filename))
        except Exception as e:
            self.log.mylog.error("截图失败")
            raise e

    def wait_element_visible(self, loc, img_doc, timeout=20, polling=0.5):
        """
        封装一个等待元素可见的方法
        :param loc:
        :param img_doc:
        :param timeout:
        :param polling:
        :return:
        """
        flag = None
        try:
            self.log.mylog.debug("等待元素{}可见。".format(loc))
            WebDriverWait(self.driver, timeout, poll_frequency=polling).until(EC.visibility_of_element_located(loc))
            flag = True
        except TimeoutException as e:
            self.log.mylog.error("等待元素可见超时")
            self.save_web_screenshot(img_doc)
            flag = False
            # raise e
        finally:
            return flag

    def get_element(self, loc, img_doc):
        """
        封装一个获取元素对象的方法
        :param loc:
        :param img_doc:
        :return:
        """
        try:
            self.log.mylog.debug("查找并{}中的元素{}".format(img_doc, loc))
            ele = self.driver.find_element(*loc)
            return ele
        except Exception as e:
            self.log.mylog.error("元素没有找到")
            self.save_web_screenshot(img_doc)
            raise e

    def get_elements(self, loc, img_doc):
        """
        封装一个获取元素对象的方法
        :param loc:
        :param img_doc:
        :return:
        """
        try:
            self.log.mylog.debug("查找{}中的元素{}".format(img_doc, loc))
            eles = self.driver.find_elements(*loc)
            return eles
        except Exception as e:
            self.log.mylog.error("元素没有找到")
            self.save_web_screenshot(img_doc)
            raise e

    def input_text(self, loc, *args, img_doc=''):
        """
        封装一个输入的方法
        :param loc:
        :param args:
        :param img_doc:
        :param timeout:
        :param frequency:
        :return:
        """
        self.wait_element_visible(loc, img_doc)
        ele = self.get_element(loc, img_doc)
        try:
            self.log.mylog.debug("给元素{}输入{}".format(loc, *args))
            ele.clear()
            ele.send_keys(*args)
        except Exception as e:
            self.log.mylog.error("输入操作失败")
            self.save_web_screenshot(img_doc)
            raise e

    def click_element(self, loc, img_doc, timeout=20, frequency=0.5):
        """
        封装一个点击元素的方法
        :param loc:
        :param img_doc:
        :param timeout:
        :param frequency:
        :return:
        """
        self.wait_element_visible(loc, img_doc, timeout, frequency)
        ele = self.get_element(loc, img_doc)
        try:
            self.log.mylog.debug("你需要点击的元素是{}".format(loc))
            ele.click()
        except Exception as e:
            self.log.mylog.error("点击元素失败")
            self.save_web_screenshot(img_doc)
            raise e

    def click_first_element(self, loc, img_doc, index=1, timeout=20, frequency=0.5):
        """
        封装点击列表第一个元素
        :param loc:元素定位
        :param loc:元素集下标，默认从1开始
        :param img_doc:
        :param timeout:
        :param frequency:
        :return:
        """
        self.wait_element_visible(loc, img_doc, timeout, frequency)
        ele = self.get_elements(loc, img_doc)[index]
        try:
            self.log.mylog.debug("你需要点击的元素是{}".format(loc))
            ele.click()
        except Exception as e:
            self.log.mylog.error("点击元素失败")
            self.save_web_screenshot(img_doc)
            raise e

    def get_text(self, loc, img_doc):
        """
        封装一个获取页面文本的方法
        :param loc:
        :param img_doc:
        :return:
        """
        ele = self.get_element(loc, img_doc)
        try:
            text = ele.text
            self.log.mylog.debug("获取元素{}的文本值为：{}".format(loc, text))
            return text
        except Exception as e:
            self.log.mylog.error("获取文本失败")
            self.save_web_screenshot(img_doc)
            raise e

    def enter_iframe(self, loc, img_doc):
        """
        封装一个切换iframe的方法
        :param loc:
        :param img_doc:
        :return:
        """
        # 方法一
        # self.wait_element_visible(loc, img_doc)
        # ele = self.get_element(loc, img_doc)
        # try:
        #     self.driver.switch_to.frame(ele)
        #     self.log.mylog.debug("切入iframe成功")
        # except Exception as e:
        #     self.log.mylog.debug("切入iframe失败")
        #     self.save_web_screenshot(img_doc)
        #     raise e
        # 方法二
        try:
            WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it(loc))  # 等待元素可见后在切入iframe
            self.log.mylog.debug("切入iframe成功")
        except Exception as e:
            self.log.mylog.error("切入iframe失败")
            self.save_web_screenshot(img_doc)
            raise e

    def exit_iframe(self):
        """
        封装一个退出iframe的方法
        :return:
        """
        try:
            self.driver.switch_to.default_content()
            self.log.mylog.debug("退出iframe成功")
        except Exception as e:
            self.log.mylog.error("退出iframe失败")
            raise e

    def select_option(self, loc, option, img_doc, var="value"):
        """
        封装一个下拉框选择的方法
        :param loc:
        :param option:下拉框的文本值
        :param img_doc:
        :param img_doc:
        """
        ele = self.get_element(loc, img_doc)  # 得到select的元素对象
        try:
            s = Select(ele)
            if var == "value":
                s.select_by_value(option)
            elif var == "text":
                s.select_by_visible_text(option)
            self.log.mylog.debug("下拉框选择成功")
        except Exception as e:
            self.log.mylog.error("下拉框选择失败")
            self.save_web_screenshot(img_doc)
            raise e

    def close_alert(self):
        """
        封装一个关闭弹出框的方法
        :return:
        """
        try:
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())  # 等待alert出现
            alert = self.driver.switch_to.alert  # 切入alert
            alert.accept()  # 确定弹出框
            self.log.mylog.debug("弹出框关闭")
        except Exception as e:
            self.log.mylog.error("弹出框未关闭")
            raise e

    def mouse_xuanfu(self, loc, img_doc):
        """
        封装一个鼠标悬浮的操作
        :param loc:
        :param img_doc:
        :return:
        """
        try:
            self.wait_element_visible(loc, img_doc)
            ele = self.get_element(loc, img_doc)
            ac = ActionChains(self.driver)
            ac.move_to_element(ele).click().perform()
            self.log.mylog.debug("文件夹选中成功")
        except Exception:
            self.log.mylog.error("文件夹选中失败")
            self.save_web_screenshot(img_doc)

    def mouse_double_click(self, loc, img_doc):
        """
        封装一个鼠标双击操作
        :param loc:
        :param img_doc:
        :return:
        """
        try:
            self.wait_element_visible(loc, img_doc)
            ele = self.get_element(loc, img_doc)
            ac = ActionChains(self.driver)
            ac.double_click(on_element=ele).perform()
            self.log.mylog.debug("左键双击成功")
        except Exception:
            self.log.mylog.error("左键双击失败")
            self.save_web_screenshot(img_doc)

    def hold_mouse_and_slide(self, loc, loc1, img_doc):
        """
        点击左键并移动一段距离后释放
        :param loc: 
        :param loc1:
        :param img_doc:
        :return:
        """
        try:
            self.wait_element_visible(loc, img_doc)
            ele = self.get_element(loc, img_doc)
            ele1 = self.get_element(loc1, img_doc)
            ac = ActionChains(self.driver)
            # ac.click_and_hold(on_element=ele).move_to_element(on_element=ele1).release().perform()
            ac.drag_and_drop(ele, ele1).perform()
            self.log.mylog.debug("点击左键并移动成功")
        except Exception:
            self.log.mylog.error("点击左键并移动失败")
            self.save_web_screenshot(img_doc)

    def add_date(self, ele, value, num=1):
        """
        日期控件改成可输入
        :param ele:
        :param value:
        :return:
        """
        if num == 1:
            js = 'var a = document.getElementById("{0}");' \
                 'a.readOnly = false;' \
                 'a.value = "{1}"'.format(ele, value)
            self.driver.execute_script(js)
        elif num == 2:
            js = 'var a = document.getElementsByName("{0}");' \
                 'a[0].readonly = false;' \
                 'a[0].value = "{1}"'.format(ele, value)
            self.driver.execute_script(js)
        else:
            print("num没有匹配上")

    def execute_js(self, roomId, startDate, endDate):
        """
        执行js
        :param roomId:
        :param startDate:
        :param endDate:
        :return:
        """
        self.driver.execute_script('openApplyCreate("{0}", "{1}", "{2}", '')'.format(roomId, startDate, endDate))

    def get_datetime(self, N):
        """
        获取当前时间后的指定时间
        :param N: 自定义整数
        :return:
        """
        datetime1 = datetime.datetime.now()
        datetime2 = datetime.timedelta(hours=N)
        datetime3 = (datetime1 + datetime2).strftime("%Y-%m-%d %H:%M")
        return datetime3

    def go_back(self, num):
        """
        调用系统返回按钮
        :param num: 指定返回次数
        :return:
        """
        for i in range(num):
            self.driver.keyevent(4)
        time.sleep(2)

    def get_page_content(self):
        """
        获取当前页面的源码
        :return:
        """
        return self.driver.page_source

    def switch_to_window(self, *args, is_search=False):
        """
        切换最新窗口
        :param args:关键字路径路径
        :param is_search:是否通过路径搜索
        :return:
        """
        # WebDriverWait(self.driver, 20, poll_frequency=0.5).until(EC.number_of_windows_to_be(2))  # 等待窗口数量大于2
        handles = self.driver.window_handles
        if is_search:
            self.check_url(args[0])
        else:
            self.driver.switch_to.window(handles[-1])

    def switch_to_context(self, app_type="student"):
        """
        切换最新上下文
        :param app_type:当前app类型
        :return:
        """
        if app_type == "OA":
            self.driver.switch_to.context("WEBVIEW_cn.doocom.WeMustDEV")
        else:
            # self.driver.switch_to.context(self.driver.contexts[-1])
            self.driver.switch_to.context("WEBVIEW_cn.doocom.wemustcampusbeta")

    def get_current_url(self):
        """
        获取当前页面的url
        :return:
        """
        return self.driver.current_url

    def switch_to_native(self):
        """
        切换至原生
        :return:
        """
        self.driver.switch_to.context("NATIVE_APP")

    def click_coordinate(self, x, y):
        """
        通过坐标点击元素
        :param x:元素的x坐标的百分比
        :param y:元素的y坐标的百分比
        :return:x
        """
        # self.log.mylog.error(f"x的绝对坐标为:{x}")
        # self.log.mylog.error(f"y的绝对坐标为:{y}")
        size = self.driver.get_window_size()
        # self.log.mylog.error("当前屏幕的尺寸为:{}".format(size["width"]))
        # self.log.mylog.error("当前屏幕的尺寸为:{}".format(size["height"]))
        x1 = int(size["width"] * x)
        y1 = int(size["height"] * y)
        # self.log.mylog.error(f"x1的相对坐标为:{x1}")
        # self.log.mylog.error(f"y1的相对坐标为:{y1}")
        self.driver.tap([(x1, y1), (x1, y1)], duration=300)
        return self

    def swipe_page(self, value, loc, img_doc):
        """
        滑动页面，直到出现指定的值后停止滑动
        :param value:需要查找的值
        :param loc:定位
        :param img_doc:备注
        :return:
        """
        old_page = None
        new_page = self.driver.page_source
        size = self.driver.get_window_size()
        while True:
            if old_page == new_page:  # 此处表示滑动到底部了
                break
            else:
                if new_page.find(value) != -1:
                    self.click_element(loc, img_doc)
                    time.sleep(1)
                    break
                else:
                    """
                    如果当前页面没有发现application_name，更新旧页面继续滑动
                    """
                    old_page = new_page
                    # self.driver.swipe(size["width"] * 0.5, size["height"] * 0.9, size["width"] * 0.5,
                    #                   size["height"] * 0.5, duration=500)
                    self.driver.swipe(size["width"] * 0.5, size["height"] * 0.9, size["width"] * 0.5,
                                      size["height"] * 0.5)
                    time.sleep(5)
                    new_page = self.driver.page_source
                    continue

    def wait_element_presence(self, loc, img_doc, timeout=5, polling=0.1):
        """
        封装一个元素是否存在
        :param loc:
        :param img_doc:
        :param timeout:
        :param polling:
        :return:
        """
        try:
            WebDriverWait(self.driver, timeout, poll_frequency=polling).until(EC.presence_of_element_located(loc))
            self.log.mylog.debug("元素{}存在。".format(loc))
        except TimeoutException as e:
            self.log.mylog.error("元素不存在")
            self.save_web_screenshot(img_doc)
            raise e

    def get_contexts(self):
        """
        获取所有上下文
        :return:
        """
        return self.driver.contexts

    def get_context(self):
        """
        获取当前上下文
        :return:
        """
        return self.driver.context

    def get_window_handles(self):
        """
        获取所有句柄
        :return:
        """
        return self.driver.window_handles

    def get_current_window_handle(self):
        """
        获取当前句柄
        :return:
        """
        return self.driver.current_window_handle

    def js_click(self, loc, img_doc):
        """
        使用js进行点击
        :param loc:
        :param img_doc:
        :return:
        """
        ele = self.get_element(loc, img_doc)
        self.driver.execute_script("arguments[0].click();", ele)

    def key_enter(self, loc, img_doc):
        """
        键盘回车
        :param loc:
        :param img_doc:
        :return:
        """
        ele = self.get_element(loc, img_doc)
        ele.send_keys(Keys.ENTER)

    def check_url(self, *args):
        """
        切换当前每一个句柄，然后查看当前url是否包含指定的关键词
        :param args: url关键词
        :return:
        """
        handles = self.driver.window_handles
        for handle in handles:
            self.driver.switch_to.window(handle)
            url = self.driver.current_url
            if url.find(args[0]) != -1:
                break
            else:
                continue

    def _get_element_location(self, loc, ele=None):
        """
           获取元素的中心坐标并返回
        :param loc: 元素定位
        :param ele: 元素对象
        :return: tuple(x,y)
        """
        # self.log.mylog.error("当前窗口的宽高：{}".format(self.driver.get_window_size()))
        # self.log.mylog.error("当前窗口的大小：{}".format(self.driver.get_window_rect()))
        # self.log.mylog.error("ele的值为：{}".format(ele))
        if not ele:
            ele = self.driver.find_element(*loc)
        # location获取元素左上角的坐标
        location = ele.location
        # self.log.mylog.error("location的值为：{}".format(location))
        # 获取页面滑动的距离
        distance = self._get_scroll_top()
        # self.log.mylog.error("滚动的距离为：{}".format(distance))
        location['y'] = location['y'] - distance
        # size获取元素的宽和高
        size = ele.size
        # 获取元素的中心坐标
        # self.log.mylog.error("size的值为：{}".format(size))
        #  此处乘2是因为页面固定元素的宽度了，而不是实际占屏幕的宽度
        x1 = int(location['x'] + size['width'] * 0.5) * 2
        y1 = int(location['y'] + size['height'] * 0.5) * 2 + 1498 - 1330
        # self.log.mylog.error("x1的值为：{0},y1的值为:{1}".format(x1, y1))
        return x1, y1

    def _page_scroll(self, loc, ele=None):
        """
        拖动页面至指定元素
        :param loc: 元素定位
        :param ele: 元素对象
        :return:
        """
        if not ele:
            ele = self.driver.find_element(*loc)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", ele)

    def _cap(self, loc, ele=None):
        """
        触摸点击元素
        :param loc:
        :param ele: 元素对象
        :return:
        """
        location = self._get_element_location(loc, ele=ele)
        self.driver.tap([location, location], duration=300)

    def scroll_cap(self, loc):
        """
        滚动页面并模拟手点击元素，
        这里获取ele对象是为了page_scroll和get_element_location、cap三个方法每次都要获取元素对象而浪费大量时间
        :param loc:
        :return:
        """
        ele = self.driver.find_element(*loc)
        self._page_scroll(loc, ele=ele)
        self._cap(loc, ele=ele)

    @staticmethod
    def update_content(param, loc):
        """
        替换元素定位中的固定文本
        :param param:需要替换的文本
        :param loc:原字符串
        :return:返回新的元素定位
        """
        import re
        # p = u"[\u4e00-\u9fa5]+"
        p = '#(.*?)#'
        new_loc = eval(re.sub(p, param, str(loc), count=1))
        return new_loc

    def start_activity_app(self, app_package, app_activity):
        """
        从后台调起APP
        :param app_activity:
        :param app_package
        :return:
        """
        self.driver.start_activity(app_package, app_activity)
        return self

    def app_background(self, seconds):
        """
        将app置于后台
        :param seconds:生存多少秒
        :return:
        """
        self.driver.background_app(seconds)

    def CloseApp(self):
        self.driver.close_app()

    def _get_scroll_top(self):
        """
        获取页面滚动距离
        :return: 返回滚动距离
        """
        js = "var scroll_top = 0; " \
             "if (document.documentElement && document.documentElement.scrollTop) " \
             "{ scroll_top = document.documentElement.scrollTop;}" \
             "else if (document.body) " \
             "{scroll_top = document.body.scrollTop;}" \
             "return scroll_top;"
        return self.driver.execute_script(js)

    def press_home_button(self):
        """
        调用系统home按钮
        :return:
        """
        self.driver.keyevent(3)
