from instagram import Instagram


SEARCH = ""

MESSAGE = "hello"

USER_NAME = ""
PASSWORD = ""

CHROME_DRIVER_PATH = "/Users/Admin/Chrome driver/chromedriver.exe"

instagram = Instagram(CHROME_DRIVER_PATH, USER_NAME, PASSWORD)

instagram.search(SEARCH)
