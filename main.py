from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_stealth import stealth
from plyer import notification
from datetime import datetime
import getpass
import time
import sys

# === COLORS ===
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
RESET = "\033[0m"


# === LOGO ===
print(GREEN + r"""
   _____ _        _              _____       _ _       _     
  / ____| |      | |            / ____|     (_) |     | |    
 | (___ | |_ __ _| |_ _   _ ___| (___  _ __  _| |_ ___| |__  
  \___ \| __/ _` | __| | | / __|\___ \| '_ \| | __/ __| '_ \ 
  ____) | || (_| | |_| |_| \__ \____) | | | | | || (__| | | |
 |_____/ \__\__,_|\__|\__,_|___/_____/|_| |_|_|\__\___|_| |_|                        
""" + MAGENTA + "   ⛓️ Facebook Status Tracker by Nihal Cipher\n" + RESET)

# === CREDENTIALS ===
FACEBOOK_EMAIL = input(f"📧 {YELLOW}Enter Facebook Email or Phone: {RESET}")
FACEBOOK_PASSWORD = getpass.getpass(f"🔑 {YELLOW}Enter Facebook Password: {RESET}")
TARGET_USERNAME = input(f"🎯 {MAGENTA}Enter target username or profile ID: {RESET}")
LOG_FILE = "status_log.txt"

# === SELENIUM CONFIG ===
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("detach", True)

try:
    driver = webdriver.Chrome(options=chrome_options)
    stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
    )
except Exception as e:
    print(f"{RED}[FATAL] ChromeDriver Error: {e}{RESET}")
    sys.exit(1)

def login_facebook():
    print(f"{YELLOW}[*] Logging in...{RESET}")
    driver.get("https://www.facebook.com/login")
    time.sleep(3)
    driver.find_element(By.ID, "email").send_keys(FACEBOOK_EMAIL)
    driver.find_element(By.ID, "pass").send_keys(FACEBOOK_PASSWORD)
    driver.find_element(By.NAME, "login").click()
    print(f"{MAGENTA}[!] Solve CAPTCHA or 2FA if prompted... Waiting 70 seconds...{RESET}")
    time.sleep(70)
    try:
        WebDriverWait(driver, 10).until(lambda d: "checkpoint" not in d.current_url and "login" not in d.current_url)
        print(f"{GREEN}[+] Login successful!{RESET}")
    except TimeoutException:
        print(f"{RED}[!] Login failed or session not validated.{RESET}")
        driver.quit()
        sys.exit(1)

def go_to_messenger():
    print(f"{YELLOW}[*] Opening chat with {TARGET_USERNAME}...{RESET}")
    try:
        driver.get(f"https://www.facebook.com/messages/t/{TARGET_USERNAME}")
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        print(f"{GREEN}[+] Messenger chat loaded.{RESET}")
    except Exception as e:
        print(f"{RED}[!] Error loading Messenger: {e}{RESET}")

def get_status():
    try:
        container = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[aria-label*='Conversation']")))
        if container.find_elements(By.XPATH, ".//span[contains(text(),'Active now')]"):
            return "online"
        return "offline"
    except Exception:
        return "unknown"

def notify(status):
    try:
        notification.notify(
            title="StatusSnitch Update",
            message=f"{TARGET_USERNAME} is now {status.upper()}",
            timeout=3
        )
    except:
        print(f"{RED}[!] Notification failed.{RESET}")

def log_status(status):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {TARGET_USERNAME} is {status}\n"
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as log:
            log.write(entry)
        print(f"{MAGENTA}{entry.strip()}{RESET}")
    except Exception as e:
        print(f"{RED}[!] Failed to write log: {e}{RESET}")

def check_session_alive():
    return "login" not in driver.current_url

def monitor(interval=60):
    print(f"{CYAN}[*] Monitoring started. Press Ctrl+C to stop.{RESET}")
    last_status = None
    fail_count = 0
    last_refresh = time.time()
    last_notify = time.time()

    while True:
        if not check_session_alive():
            print(f"{RED}[!] Session expired. Re-logging...{RESET}")
            login_facebook()
            go_to_messenger()
            continue

        try:
            status = get_status()

            if status == "unknown":
                fail_count += 1
                print(f"{YELLOW}[~] Unable to detect status ({fail_count}){RESET}")
                if fail_count >= 5:
                    go_to_messenger()
                    fail_count = 0
                continue

            if status != last_status:
                notify(status)
                log_status(status)
                last_status = status
                last_notify = time.time()
            elif time.time() - last_notify >= 300:
                notify(status)
                log_status(status)
                last_notify = time.time()

            if time.time() - last_refresh >= interval:
                driver.refresh()
                print(f"{BLUE}[🔄] Page refreshed{RESET}")
                last_refresh = time.time()
                continue
            print(f"{GREEN}[+] {TARGET_USERNAME} is currently {status.upper()}{RESET}")

            time.sleep(5)

        except KeyboardInterrupt:
            print(f"\n{GREEN}[*] Monitoring stopped by user.{RESET}")
            break
        except Exception as e:
            print(f"{RED}[!] Error during monitoring: {e}{RESET}")
            time.sleep(5)

# === RUN ===
try:
    login_facebook()
    go_to_messenger()
    monitor()
except Exception as e:
    print(f"{RED}[FATAL] {e}{RESET}")
finally:
    driver.quit()
    print(f"{GREEN}[*] Exiting...{RESET}")
# === END OF SCRIPT ===
    sys.exit(0)

    
