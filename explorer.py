from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_mint_address(commit_hash):
    # Set up the WebDriver
    driver = webdriver.Chrome()

    # Open the Ordinals explorer
    driver.get("http://0.0.0.0:9001")

    # Wait for the input field to be present
    wait = WebDriverWait(driver, 10)
    input_field = wait.until(EC.presence_of_element_located((By.NAME, "query")))

    # Enter the commit hash and submit the form
    input_field.send_keys(commit_hash)
    input_field.send_keys(Keys.RETURN)

    # Wait for the address element to be present
    # XPath to find <dd> element after <dt> with text "address"
    address_element = wait.until(EC.presence_of_element_located((By.XPATH, "//dt[text()='address']/following-sibling::dd")))
    mint_address = address_element.text

    driver.quit()
    return mint_address

# Example usage
# commit_hash = "3bcf15e8c4b57b0792311924477735a4fa811b7b90d35277641020473a17a5df"  # Replace with your actual commit hash
# mint_address = get_mint_address(commit_hash)
# print(f"Mint Address: {mint_address}")
