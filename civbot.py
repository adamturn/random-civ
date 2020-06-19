# third-party


class CivBot(object):

    def __init__(self):
        print("[CivBot]$ :)")
        self.driver = None

    def configure_firefox():
        fp = webdriver.FirefoxProfile()
        fp.set_preference("browser.download.folderList", 2)
        fp.set_preference("browser.download.manager.showWhenStarting", False)
        fp.set_preference("browser.download.dir", download_dir)
        fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv")

        return fp

    def instantiate_driver(profile):
        options = Options()
        # options.add_argument("--headless")
        driver = webdriver.Firefox(
            firefox_profile=profile,
            options=options,
            executable_path="/home/adam/utils/geckodriver-v0.26.0-linux64/geckodriver"
        )
        return driver



def main():

    fp = CivBot.configure_firefox()
    #   creating driver instance
    driver = CivBot.instantiate_driver(profile=fp)

    # ------------------------ NAVIGATION ------------------------------
    #   driving to the web page
    print("~ Surfing the Web ~")
    driver.get("https://live.clarksons.net/wfr2/fleet")

    #   accepts cookie policy
    time.sleep(random_wait_base + (random.randint(1, 10) / 10))
    print("Cookie time!")
    try:
        cookie_button = driver.find_element_by_id("cookieAgreeButton")
        cookie_button.click()
        print("Cookies accepted.")
    except:
        print("Could not find cookie button! :(")

    #   logs in
    print("Entering login information...")
    time.sleep(random_wait_base + (random.randint(1, 10) / 10))
    username = driver.find_element_by_id("usernameText")
    username.clear()
    username.send_keys("johns.lang@clipperdata.com")
    time.sleep(random_wait_base + (random.randint(1, 10) / 10))
    password = driver.find_element_by_id("passwordText")
    password.clear()
    password.send_keys("syd4t4clipper")
    print("Logging in...")
    password.send_keys(Keys.RETURN)


    return None


if __name__ == "__main__":
    main()
