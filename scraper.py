from selenium import webdriver 
from selenium.webdriver.chrome.options import Options


YOUTUBE_TRENDING_URL = 'https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl'

def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver =webdriver.Chrome(options=chrome_options)
  return driver

if __name__ == "__main__":
  print ('Creating driver')
  driver = get_driver()

print('Fetching the page')
driver.get(YOUTUBE_TRENDING_URL)
print ('Get the video divs')
driver.find_elements_by_class_name(VIDEO_DIV_CLASS)

print('Page title:', driver.title)