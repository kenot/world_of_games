import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_scores_service(url):
    try:
        # Setup Selenium WebDriver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        # Open the web page
        driver.get(url)

        # Locate the score element
        score_element = driver.find_element(By.ID, "score")

        # Extract and convert the score text to an integer
        score = int(score_element.text)

        # Check if the score is between 1 and 1000
        return 1 <= score <= 1000

    except Exception as e:
        print(f"Error during test: {e}")
        return False

    finally:
        # Close the browser after the test
        driver.quit()


def main():
    # URL of the running web service
    url = "http://localhost:5000"

    # Run the test
    test_passed = test_scores_service(url)

    # Exit with 0 if test passed, -1 if it failed
    sys.exit(0 if test_passed else -1)


if __name__ == "__main__":
    main()
