from selenium.webdriver.common.by import By

class EducationLocators:
    CROSS_LOCATOR = (By.XPATH, '//*[@id="_modal_24"]/div/div/div[3]')
    EDUCATION_LOCATOR = (By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[1]/div/div[1]/div/div[1]/div/section[1]/div[1]')
    WINDOW_LOCATOR = (By.XPATH, '//*[@id="root"]/div/div[2]/div')
    VKGROUP_LOCATOR = (By.XPATH, '//*[@id="_modal_24"]/div/div/div[2]/div[1]/div/div/div/section/div[1]')
    VKGROUP_MODAL_LOCATOR = (By.XPATH, '//*[@id="_modal_23"]/div/div/div[2]/div[1]/div')
    VKGROUP_H2 = (By.XPATH, '//*[@id="_modal_23"]/div/div/div[2]/div[1]/div/div/div/h2')
    VKGROUP_BUTTONS = (By.XPATH, '//*[@id="_modal_23"]/div/div/div[2]/div[1]/div/div/section')
    VKGROUP_BUTTONS_DIV = (By.CSS_SELECTOR, ':scope > div')
    VKGROUP_TUNE_POPUP = (By.XPATH, '/html/body/div[2]/div')
    VKGROUP_TUNE_BUTTON = (By.XPATH, '//*[@id="_modal_23"]/div/div/div[2]/div[1]/div/div/section/div[1]/div/div')
    VKGROUP_VIDEO = (By.XPATH, '//*[@id="_modal_22"]/div/div/div[2]/div[1]/div/div/iframe')
    VKGROUP_VIDEO_BUTTON = (By.XPATH, '//*[@id="_modal_23"]/div/div/div[2]/div[1]/div/div/section/div[2]/div/div')
    VKGROUP_COURSE_BUTTON = (By.XPATH, '//*[@id="_modal_23"]/div/div/div[2]/div[1]/div/div/section/div[3]')
    VKGROUP_HAT_SIGN = (By.XPATH, '//*[@id="_modal_24"]/div/div/div[2]/div[1]/div/div/div/section/div[1]/div/div[3]/div')
    VKGROUP_HAT_SIGN_POPUP = (By.XPATH, '/html/body/div[2]/div')
    CATALOG_LOCATOR = (By.XPATH, '//*[@id="_modal_24"]/div/div/div[2]/div[1]/div/div/div/section/div[3]')
    CATALOG_MODAL_LOCATOR = (By.XPATH, '//*[@id="_modal_23"]/div/div/div[2]/div[1]/div')
    CATALOG_BUTTONS = (By.XPATH, '//*[@id="_modal_23"]/div/div/div[2]/div[1]/div/div/section')
    CATALOG_H2 = (By.XPATH, '//*[@id="_modal_23"]/div/div/div[2]/div[1]/div/div/div/h2')
    CATALOG_BUTTONS = (By.XPATH, '//*[@id="_modal_23"]/div/div/div[2]/div[1]/div/div/section')
    CATALOG_BUTTONS_DIV = (By.CSS_SELECTOR, ':scope > div')
    CATALOG_CREATE_BTN = (By.XPATH, '//*[@id="_modal_23"]/div/div/div[2]/div[1]/div/div/section/div[1]')