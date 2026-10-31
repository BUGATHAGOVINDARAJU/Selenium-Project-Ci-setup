from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import undetected_chromedriver as uc
#from selenium_stealth import stealth  # <-- Added for anti-bot bypass
from config.config import Config
from utils.logger import Logger

logger = Logger.get_logger(__name__)

class WebDriverFactory:
    
    @staticmethod
    def get_driver(browser_name=None):
        browser = browser_name or Config.BROWSER
        browser = browser.lower()
        
        logger.info(f"Initializing {browser} driver (Headless: {Config.HEADLESS})")
        
        if browser == 'chrome':
            return WebDriverFactory._get_chrome_driver()
        elif browser == 'firefox':
            return WebDriverFactory._get_firefox_driver()
        elif browser == 'edge':
            return WebDriverFactory._get_edge_driver()
        else:
            raise ValueError(f"Unsupported browser: {browser}")


    @staticmethod
    def _get_chrome_driver():
        options = uc.ChromeOptions()
        
        if Config.HEADLESS:
            options.add_argument('--headless')
        
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36')

        # FIX: Explicitly force it to download and use the version 149 driver
        driver = uc.Chrome(options=options, version_main=149)
        
        WebDriverFactory._configure_driver(driver)
        return driver
    
    # @staticmethod
    # def _get_chrome_driver():
        # CRITICAL: Must use uc.ChromeOptions(), not webdriver.ChromeOptions()
        options = uc.ChromeOptions()
        
        if Config.HEADLESS:
            # undetected-chromedriver handles headless processing natively
            options.add_argument('--headless')
        
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        
        # Spoof a completely standard User Agent
        options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36')

        # uc handles browser patching internally. No Service or ChromeDriverManager needed here.
        driver = uc.Chrome(options=options)
        
        WebDriverFactory._configure_driver(driver)
        return driver
    # @staticmethod
    # def _get_chrome_driver():
    #     options = webdriver.ChromeOptions()
        
    #     if Config.HEADLESS:
    #         # 'headless=new' preserves browser fingerprint integrity better than standard '--headless'
    #         options.add_argument('--headless=new')
        
    #     options.add_argument('--disable-blink-features=AutomationControlled')
    #     options.add_argument('--no-sandbox')
    #     options.add_argument('--disable-dev-shm-usage')
    #     options.add_argument('--disable-gpu')
    #     options.add_argument('--window-size=1920,1080')
        
    #     # FIX: Added 'enable-automation' to hide the automated browser banner/flags
    #     options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])
    #     options.add_experimental_option('useAutomationExtension', False)
        
    #     # FIX: Spoof a genuine desktop user agent to avoid looking like a bare script
    #     options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36')
        
    #     service = ChromeService(ChromeDriverManager().install())
    #     driver = webdriver.Chrome(service=service, options=options)
        
    #     # FIX: Apply stealth masking to patch navigator.webdriver, plugins, and webgl properties
    #     stealth(driver,
    #             languages=["en-US", "en"],
    #             vendor="Google Inc.",
    #             platform="Win32",
    #             webgl_vendor="Intel Inc.",
    #             renderer="Intel Iris OpenGL Engine",
    #             fix_hairline=True)
        
    #     WebDriverFactory._configure_driver(driver)
    #     return driver
    
    @staticmethod
    def _get_firefox_driver():
        options = webdriver.FirefoxOptions()
        
        if Config.HEADLESS:
            options.add_argument('--headless')
        
        options.add_argument('--width=1920')
        options.add_argument('--height=1080')
        
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
        
        WebDriverFactory._configure_driver(driver)
        return driver
    
    @staticmethod
    def _get_edge_driver():
        options = webdriver.EdgeOptions()
        
        if Config.HEADLESS:
            options.add_argument('--headless=new')
        
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--window-size=1920,1080')
        
        # Mirroring Chrome's automation exclusions for Edge (since it's Chromium-based)
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        options.add_experimental_option('useAutomationExtension', False)
        
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service, options=options)
        
        WebDriverFactory._configure_driver(driver)
        return driver
    
    # @staticmethod
    # def _configure_driver(driver):
    #     driver.implicitly_wait(Config.IMPLICIT_WAIT)
    #     driver.set_page_load_timeout(Config.PAGE_LOAD_TIMEOUT)
    #     driver.maximize_window()
    #     logger.info("WebDriver configured successfully")

    @staticmethod
    def _configure_driver(driver):
        driver.implicitly_wait(Config.IMPLICIT_WAIT)
        driver.set_page_load_timeout(Config.PAGE_LOAD_TIMEOUT)
        
        # SAFE WRAPPER: Prevents startup crashes caused by anti-bot window hooks
        try:
            driver.maximize_window()
        except Exception as e:
            logger.warning(f"Failed to maximize window, bypassing to prevent hook crash: {str(e)}")
            
        logger.info("WebDriver configured successfully")