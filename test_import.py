print("=== Тест импорта ===")
try:
    from utils.driver import DriverFactory
    print(" DriverFactory импортируется успешно!")
    
    # Пробуем создать драйвер
    driver = DriverFactory.get_driver("chrome")
    print(" Драйвер создан!")
    
    # Тестируем
    driver.get("https://www.google.com")
    print(f" Chrome работает! Заголовок: {driver.title}")
    
    driver.quit()
    print(" Все работает!")
    
except Exception as e:
    print(f" Ошибка: {type(e).__name__}: {e}")
