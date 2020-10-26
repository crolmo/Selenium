# -*- coding: utf-8 -*-
import os
from Common.utils import listdir,abs_path,load_yaml
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

def get_driver_path():
    drvier_path = abs_path("../Data/driver/")
    path_list = listdir(drvier_path)
    return path_list


def select_driver(browser="Chrome"):
    driver_path = get_driver_path()
    if browser == "Chrome":
        for driver in driver_path:
            if os.path.basename(driver) == "chromedriver.exe":
                return driver


def operate_by(elements,operate_type,operate_info):
    info = ""
    if operate_type == "click":
        info = elements.click()
    elif operate_type == "send_keys":
        info = elements.send_keys(operate_info)
    elif operate_type == "submit":
        info = elements.submit(operate_info)
    elif operate_type == "get_attribute":
        info = elements.get_attribute(operate_info)
    elif operate_type == "clear":
        info = elements.clear(operate_info)
    elif operate_type == "get_property":
        info = elements.get_property(operate_info)
    elif operate_type == "select_by_index":
        info = Select(elements).select_by_index(operate_info)
    elif operate_info == "select_by_value":
        info = Select(elements).select_by_value(operate_info)
    elif operate_info == "select_by_visible_text":
        info = Select(elements).select_by_visible_text(operate_info)
    elif operate_info == "all_selected_options":
        info = Select(elements).all_selected_options
    elif operate_info == "deselect_all":
        info = Select(elements).deselect_all()
    elif operate_info == "deselect_by_index":
        info = Select(elements).deselect_by_index(operate_info)
    elif operate_info == "deselect_by_value":
        info = Select(elements).deselect_by_value(operate_info)
    elif operate_info == "deselect_by_visible_text":
        info = Select(elements).deselect_by_visible_text(operate_info)
    elif operate_info == "first_selected_option":
        info = Select(elements).first_selected_option
    if info:
        return info


def get_element_info(driver,operate):
    format_keys(operate)
    element_info = operate["element_info"]
    find_type = operate["find_type"]
    operate_type = operate["operate_type"]
    operate_info = operate["operate_info"]
    elements = ""
    if find_type == "id":
        elements = driver.find_element_by_id(element_info)
    elif find_type == "ids":
        elements = driver.find_elements_by_id(element_info)
    elif find_type == "xpath":
        elements = driver.find_element_by_xpath(element_info)
    elif find_type == "xpaths":
        elements = driver.find_elements_by_xpath(element_info)
    elif find_type == "link_text":
        elements = driver.find_element_by_link_text(element_info)
    elif find_type == "partial_link_text":
        elements = driver.find_element_by_partial_link_text(element_info)
    elif find_type == "partial_link_texts":
        elements = driver.find_elements_by_partial_link_text(element_info)
    elif find_type == "name":
        elements = driver.find_element_by_name(element_info)
    elif find_type == "names":
        elements = driver.find_elements_by_name(element_info)
    elif find_type == "tag_name":
        elements = driver.find_element_by_tag_name(element_info)
    elif find_type == "tag_names":
        elements = driver.find_elements_by_tag_name(element_info)
    elif find_type == "class_name":
        elements = driver.find_element_by_class_name(element_info)
    elif find_type == "class_names":
        elements = driver.find_elements_by_class_name(element_info)
    elif find_type == "css_selector":
        elements = driver.find_element_by_css_selector(element_info)
    elif find_type == "css_selectors":
        elements = driver.find_elements_by_css_selector(element_info)
    info = operate_by(elements, operate_type, operate_info)

    return info


def get_driver_info(driver,operate):
    format_keys(operate)
    find_type = operate["find_type"]
    operate_type = operate["operate_type"]
    operate_info = operate["operate_info"]
    info = ""

    if operate_type == "open":
        driver.get(operate_info)
    elif operate_type == "maximize_window":
        driver.maximize_window()
    elif operate_type == "close":
        driver.close()
    elif operate_type == "quit":
        driver.quit()
    elif operate_type == "refresh":
        driver.refresh()
    elif operate_type == "back":
        driver.back()
    elif operate_type == "forward":
        driver.forward()
    elif operate_type == "title":
        info = driver.title
    elif operate_type == "current_url":
        info = driver.current_url
    elif operate_type == "page_source":
        info = driver.page_source
    elif operate_type == "current_window_handle":
        info = driver.current_window_handle
    elif operate_type == "window_handles":
        info = driver.window_handles
    elif operate_type == "fullscreen_window":
        info = driver.fullscreen_window
    elif operate_type == "minimize_window":
        info = driver.minimize_window
    elif operate_type == "switch_to_active_element":
        info = driver.switch_to_active_element
    elif operate_type == "switch_to_window":
        info = driver.switch_to_window(operate_info)
    elif operate_type == "switch_to_frame":
        info = driver.switch_to_frame(operate_info)
    elif operate_type == "switch_to_default_content":
        info = driver.switch_to_default_content
    elif operate_type == "switch_to_alert":
        info = driver.switch_to_alert
    elif operate_type == "get_cookies":
        info = driver.get_cookies
    elif operate_type == "get_cookie":
        info = driver.get_cookie(operate_info)
    elif operate_type == "delete_cookie":
        info = driver.delete_cookie(operate_info)
    elif operate_type == "delete_all_cookies":
        info = driver.delete_all_cookies
    elif operate_type == "add_cookie":
        info = driver.add_cookie(operate_info)
    elif operate_type == "implicitly_wait":
        info = driver.implicitly_wait(operate_info)
    elif operate_type == "set_script_timeout":
        info = driver.set_script_timeout(operate_info)
    elif operate_type == "set_page_load_timeout":
        info = driver.set_page_load_timeout(operate_info)
    elif operate_type == "get_screenshot_as_file":
        info = driver.get_screenshot_as_file(operate_info)
    elif operate_type == "desired_capabilities":
        info = driver.desired_capabilities
    elif operate_type == "save_screenshot":
        info = driver.save_screenshot(operate_info)
    elif operate_type == "get_screenshot_as_png":
        info = driver.get_screenshot_as_png
    elif operate_type == "get_screenshot_as_base64":
        info = driver.get_screenshot_as_base64
    elif operate_type == "set_window_size":
        info = driver.set_window_size(operate_info["width"],operate_info["height"],operate_info["windowHandle"])
    elif operate_type == "get_window_size":
        info = driver.get_window_size(operate_info)
    elif operate_type == "set_window_position":
        info = driver.set_window_position(operate_info["x"],operate_info["y"],operate_info["windowHandle"])
    elif operate_type == "get_window_position":
        info = driver.get_window_position(operate_info)
    elif operate_type == "get_window_rect":
        info = driver.get_window_rect
    elif operate_type == "get_log":
        info = driver.get_log(operate_info)

    return info


def get_element(driver,operate):
    format_keys(operate)
    element_info = operate["element_info"]
    find_type = operate["find_type"]
    elements = ""
    if find_type == "id":
        elements = driver.find_element_by_id(element_info)
    elif find_type == "ids":
        elements = driver.find_elements_by_id(element_info)
    elif find_type == "xpath":
        elements = driver.find_element_by_xpath(element_info)
    elif find_type == "xpaths":
        elements = driver.find_elements_by_xpath(element_info)
    elif find_type == "link_text":
        elements = driver.find_element_by_link_text(element_info)
    elif find_type == "partial_link_text":
        elements = driver.find_element_by_partial_link_text(element_info)
    elif find_type == "partial_link_texts":
        elements = driver.find_elements_by_partial_link_text(element_info)
    elif find_type == "name":
        elements = driver.find_element_by_name(element_info)
    elif find_type == "names":
        elements = driver.find_elements_by_name(element_info)
    elif find_type == "tag_name":
        elements = driver.find_element_by_tag_name(element_info)
    elif find_type == "tag_names":
        elements = driver.find_elements_by_tag_name(element_info)
    elif find_type == "class_name":
        elements = driver.find_element_by_class_name(element_info)
    elif find_type == "class_names":
        elements = driver.find_elements_by_class_name(element_info)
    elif find_type == "css_selector":
        elements = driver.find_element_by_css_selector(element_info)
    elif find_type == "css_selectors":
        elements = driver.find_elements_by_css_selector(element_info)
    return elements


def get_mouse_info(driver,operate):
    format_keys(operate)
    operate_type = operate["operate_type"]
    operate_info = operate["operate_info"]
    element = get_element(driver,operate)
    info = ""
    if operate_type == "move_to_element":
        info = ActionChains(driver).move_to_element(element)
    elif operate_type == "perform":
        info = ActionChains(driver).perform()
    elif operate_type == "reset_actions":
        info = ActionChains(driver).reset_actions()
    elif operate_type == "click":
        info = ActionChains(driver).click(element)
    elif operate_type == "click_and_hold":
        info = ActionChains(driver).click_and_hold(element)
    elif operate_type == "context_click":
        info = ActionChains(driver).context_click(element)
    elif operate_type == "double_click":
        info = ActionChains(driver).double_click(element)
    elif operate_type == "drag_and_drop":
        source = element
        target = get_element(driver,operate_info)
        info = ActionChains(driver).drag_and_drop(source,target)
    elif operate_type == "drag_and_drop_by_offset":
        source = element
        info = ActionChains(driver).drag_and_drop_by_offset(source,operate_info["xoffset"],operate_info["yoffset"])
    elif operate_type == "key_down":
        info = ActionChains(driver).key_down(element)
    elif operate_type == "key_up":
        info = ActionChains(driver).key_up(element)
    elif operate_type == "move_by_offset":
        info = ActionChains(driver).move_by_offset(operate_info["xoffset"],operate_info["yoffset"])
    elif operate_type == "move_to_element_with_offset":
        info = ActionChains(driver).move_to_element_with_offset(element,operate_info["xoffset"],operate_info["yoffset"])
    elif operate_type == "pause":
        info = ActionChains(driver).pause(operate_info)
    elif operate_type == "release":
        info = ActionChains(driver).release(element)
    elif operate_type == "send_keys":
        info = ActionChains(driver).send_keys(operate_info)
    elif operate_type == "send_keys_to_element":
        info = ActionChains(driver).send_keys_to_element(element,operate_info)

    return info


def format_keys(operate):
    operate_type = operate["operate_type"]
    operate_info = operate["operate_info"]
    if operate_type == "send_keys" or operate_type == "send_keys_to_element":
        if operate_info == "NULL":
            operate["operate_info"] = Keys.NULL
        elif operate_info == "CANCEL":
            operate["operate_info"] = Keys.CANCEL
        elif operate_info == "HELP":
            operate["operate_info"] = Keys.HELP
        elif operate_info == "BACKSPACE":
            operate["operate_info"] = Keys.BACKSPACE
        elif operate_info == "BACK_SPACE":
            operate["operate_info"] = Keys.BACK_SPACE
        elif operate_info == "TAB":
            operate["operate_info"] = Keys.TAB
        elif operate_info == "CLEAR":
            operate["operate_info"] = Keys.CLEAR
        elif operate_info == "RETURN":
            operate["operate_info"] = Keys.RETURN
        elif operate_info == "ENTER":
            operate["operate_info"] = Keys.ENTER
        elif operate_info == "SHIFT":
            operate["operate_info"] = Keys.SHIFT
        elif operate_info == "LEFT_SHIFT":
            operate["operate_info"] = Keys.LEFT_SHIFT
        elif operate_info == "CONTROL":
            operate["operate_info"] = Keys.CONTROL
        elif operate_info == "LEFT_CONTROL":
            operate["operate_info"] = Keys.LEFT_CONTROL
        elif operate_info == "ALT":
            operate["operate_info"] = Keys.ALT
        elif operate_info == "LEFT_ALT":
            operate["operate_info"] = Keys.LEFT_ALT
        elif operate_info == "PAUSE":
            operate["operate_info"] = Keys.PAUSE
        elif operate_info == "ESCAPE":
            operate["operate_info"] = Keys.ESCAPE
        elif operate_info == "SPACE":
            operate["operate_info"] = Keys.SPACE
        elif operate_info == "PAGE_UP":
            operate["operate_info"] = Keys.PAGE_UP
        elif operate_info == "PAGE_DOWN":
            operate["operate_info"] = Keys.PAGE_DOWN
        elif operate_info == "END":
            operate["operate_info"] = Keys.END
        elif operate_info == "HOME":
            operate["operate_info"] = Keys.HOME
        elif operate_info == "LEFT":
            operate["operate_info"] = Keys.LEFT
        elif operate_info == "ARROW_LEFT":
            operate["operate_info"] = Keys.ARROW_LEFT
        elif operate_info == "UP":
            operate["operate_info"] = Keys.UP
        elif operate_info == "ARROW_UP":
            operate["operate_info"] = Keys.ARROW_UP
        elif operate_info == "RIGHT":
            operate["operate_info"] = Keys.RIGHT
        elif operate_info == "ARROW_RIGHT":
            operate["operate_info"] = Keys.ARROW_RIGHT
        elif operate_info == "DOWN":
            operate["operate_info"] = Keys.DOWN
        elif operate_info == "ARROW_DOWN":
            operate["operate_info"] = Keys.ARROW_DOWN
        elif operate_info == "INSERT":
            operate["operate_info"] = Keys.INSERT
        elif operate_info == "DELETE":
            operate["operate_info"] = Keys.DELETE
        elif operate_info == "SEMICOLON":
            operate["operate_info"] = Keys.SEMICOLON
        elif operate_info == "EQUALS":
            operate["operate_info"] = Keys.EQUALS
        elif operate_info == "NUMPAD0":
            operate["operate_info"] = Keys.NUMPAD0
        elif operate_info == "NUMPAD1":
            operate["operate_info"] = Keys.NUMPAD1
        elif operate_info == "NUMPAD2":
            operate["operate_info"] = Keys.NUMPAD2
        elif operate_info == "NUMPAD3":
            operate["operate_info"] = Keys.NUMPAD3
        elif operate_info == "NUMPAD4":
            operate["operate_info"] = Keys.NUMPAD4
        elif operate_info == "NUMPAD5":
            operate["operate_info"] = Keys.NUMPAD5
        elif operate_info == "NUMPAD6":
            operate["operate_info"] = Keys.NUMPAD6
        elif operate_info == "NUMPAD7":
            operate["operate_info"] = Keys.NUMPAD7
        elif operate_info == "NUMPAD8":
            operate["operate_info"] = Keys.NUMPAD8
        elif operate_info == "NUMPAD9":
            operate["operate_info"] = Keys.NUMPAD9
        elif operate_info == "MULTIPLY":
            operate["operate_info"] = Keys.MULTIPLY
        elif operate_info == "ADD":
            operate["operate_info"] = Keys.ADD
        elif operate_info == "SEPARATOR":
            operate["operate_info"] = Keys.SEPARATOR
        elif operate_info == "SUBTRACT":
            operate["operate_info"] = Keys.SUBTRACT
        elif operate_info == "DECIMAL":
            operate["operate_info"] = Keys.DECIMAL
        elif operate_info == "DIVIDE":
            operate["operate_info"] = Keys.DIVIDE
        elif operate_info == "F1":
            operate["operate_info"] = Keys.F1
        elif operate_info == "F2":
            operate["operate_info"] = Keys.F2
        elif operate_info == "F3":
            operate["operate_info"] = Keys.F3
        elif operate_info == "F4":
            operate["operate_info"] = Keys.F4
        elif operate_info == "F5":
            operate["operate_info"] = Keys.F5
        elif operate_info == "F6":
            operate["operate_info"] = Keys.F6
        elif operate_info == "F7":
            operate["operate_info"] = Keys.F7
        elif operate_info == "F8":
            operate["operate_info"] = Keys.F8
        elif operate_info == "F9":
            operate["operate_info"] = Keys.F9
        elif operate_info == "F10":
            operate["operate_info"] = Keys.F10
        elif operate_info == "F11":
            operate["operate_info"] = Keys.F11
        elif operate_info == "F12":
            operate["operate_info"] = Keys.F12
        elif operate_info == "META":
            operate["operate_info"] = Keys.META
        elif operate_info == "COMMAND":
            operate["operate_info"] = Keys.COMMAND


def check_keys(operate):
    mathod = operate["mathod"]
    find_type = operate["find_type"]
    operate_type = operate["operate_type"]
    info = list()
    seleniumobj = load_yaml(abs_path("../Config/Common/seleniumobj.yml"))
    if mathod not in seleniumobj["mathod"]:
        info.append("Error:Method is illegal: {}".format(operate))
    else:
        if mathod == "element" or mathod == "get_element":
            if find_type not in seleniumobj["find_type"]:
                info.append("Error:find_type is illegal: {}".format(operate))
        else:
            if operate_type not in seleniumobj["operate_type"]:
                info.append("Error:operate_type is illegal: {}".format(operate))
    return info