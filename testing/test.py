import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from pyvirtualdisplay import Display

# virtual display initialization
display = Display(visible=0, size=(800, 800))
display.start()

# chromedriver autoinstaller
chromedriver_autoinstaller.install()

chrome_options = webdriver.ChromeOptions()

options = [
    "--windows-size=1200,1200",
    "--ignore-certificate-errors"
]

for option in options:
    chrome_options.add_argument(option)

class TestFormElements():
    @classmethod
    def setup_class(cls):
        # Chrome driver initialization with chrome_options
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.get("http://localhost:5000")

    @classmethod
    def teardown_class(cls):
        # close browser after test
        cls.driver.quit()

    def test_label_name(self):
        # find label name element and its value
        name_label = self.driver.find_element(By.XPATH, "//label[@for='nama']")
        assert name_label.text == "Nama Lengkap:", "Name Check Failed"

    def test_nim_label(self):
        # find label NIM element and its value
        nim_label = self.driver.find_element(By.XPATH, "//label[@for='nim']")
        assert nim_label.text == "Nomor Induk Mahasiswa:", "NIM Check Failed"

    def course_label(self):
        # find label course element and its value
        course_label = self.driver.find_element(By.XPATH, "//label[@for='mata_kuliah']")
        assert course_label.text == "Mata Kuliah:", "Course Check Failed"

    def program_label(self):
        # find label program element and its value
        program_label = self.driver.find_element(By.XPATH, "//label[@for='jurusan']")
        assert program_label.text == "Jurusan:", "Program Check Failed"

# run pytest when this file is not imported
if __name__ == "__main__":
    pytest.main()
