from selenium import webdriver
from SubmitPage import Field, Color

def test_zipcode_red():
   browser = webdriver.Chrome()
   field_page = Field(browser)
   field_page.first_name('Иван')
   field_page.last_name('Петров')
   field_page.address('Ленина, 55-3')
   field_page.city('Москва')
   field_page.country('Россия')
   field_page.job('QA')
   field_page.company('SkyPro')
   field_page.click()

   color_page = Color(browser)
   zip_code = color_page.color_zip()
   assert zip_code == "rgba(132, 32, 41, 1)"

def test_green():
   browser = webdriver.Chrome()
   pole_page = Field(browser)
   pole_page.first_name('Иван')
   pole_page.last_name('Петров')
   pole_page.address('Ленина, 55-3')
   pole_page.city('Москва')
   pole_page.country('Россия')
   pole_page.job('QA')
   pole_page.company('SkyPro')
   pole_page.click()

   color_page = Color(browser)
   first_name = color_page.color_first_name()
   assert first_name == "rgba(15, 81, 50, 1)"
   last_name = color_page.color_last_name()
   assert last_name == "rgba(15, 81, 50, 1)"
   address = color_page.color_address()
   assert address == "rgba(15, 81, 50, 1)"
   city = color_page.color_city()
   assert city == "rgba(15, 81, 50, 1)"
   country = color_page.color_country()
   assert country == "rgba(15, 81, 50, 1)"
   job = color_page.color_job_position()
   assert job == "rgba(15, 81, 50, 1)"
   company = color_page.color_company()
   assert company == "rgba(15, 81, 50, 1)"
