from selenium.webdriver import Firefox, FirefoxOptions, FirefoxProfile


def build_driver():
    profile = _build_profile()
    options = _build_options()

    return Firefox(profile, options=options)


def _build_profile() -> FirefoxProfile:
    profile = FirefoxProfile()
    profile.set_preference('http.response.timeout', 30)
    profile.set_preference('dom.max_script_run_time', 40)

    return profile


def _build_options() -> FirefoxOptions:
    options = FirefoxOptions()
    options.headless = True
    options.log.level = "trace"

    return options
