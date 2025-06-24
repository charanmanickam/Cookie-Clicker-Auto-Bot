import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup Chrome with stealth
options = uc.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.headless = False  # Show browser window

driver = uc.Chrome(options=options)

# Open Cookie Clicker
driver.get("https://orteil.dashnet.org/cookieclicker/")

# Wait for and click English language option
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'English')]"))
)
driver.find_element(By.XPATH, "//*[contains(text(),'English')]").click()

# Wait for the big cookie to appear
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "bigCookie"))
)

cookie = driver.find_element(By.ID, "bigCookie")
cookies_id = "cookies"

# Product IDs
product_prefix = "product"
product_price_prefix = "productPrice"
total_products = 4  # Cursor to Mine

# Track current upgrade tier
current_product = 0

# Main loop
while True:
    for _ in range(30):
        cookie.click()

    # Get cookies count
    cookies_text = driver.find_element(By.ID, cookies_id).text.split(" ")[0]
    cookies_count = int(cookies_text.replace(",", ""))

    try:
        # Get current product price
        current_price_text = driver.find_element(By.ID, product_price_prefix + str(current_product)).text.replace(",", "")
        if not current_price_text.isdigit():
            continue
        current_price = int(current_price_text)

        # Check if next product exists and its price
        if current_product + 1 < total_products:
            next_price_text = driver.find_element(By.ID, product_price_prefix + str(current_product + 1)).text.replace(",", "")
            if next_price_text.isdigit():
                next_price = int(next_price_text)
                if current_price >= next_price:
                    current_product += 1  # Move to next upgrade

        # Buy current product if affordable
        if cookies_count >= current_price:
            driver.find_element(By.ID, product_prefix + str(current_product)).click()

    except Exception:
        pass  # Skip errors

    time.sleep(0.0001)


    



