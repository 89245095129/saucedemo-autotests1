from utils.driver import DriverFactory

print("Тестирую...")
driver = DriverFactory.get_driver()
driver.get("https://google.com")
print(f"Заголовок: {driver.title}")
driver.quit()
print(" Готово!")
