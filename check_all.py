print("=== ПРОВЕРКА ===")

# 1. Проверка драйвера
try:
    with open("utils/driver.py", "r") as f:
        content = f.read()
        print("1. Файл driver.py существует")
        
        if "class DriverFactory" in content:
            print("    Содержит DriverFactory")
        else:
            print("    НЕТ DriverFactory")
            
        if "def get_driver" in content:
            print("    Содержит get_driver")
        else:
            print("    НЕТ get_driver")
            
except Exception as e:
    print(f"1.  Ошибка: {e}")

# 2. Проверка импорта
try:
    from utils.driver import DriverFactory
    print("2.  DriverFactory импортируется")
    
    # 3. Тестируем драйвер
    driver = DriverFactory.get_driver()
    print("3.  Драйвер создан")
    
    driver.get("https://www.saucedemo.com")
    print(f"4.  Сайт открыт: {driver.title}")
    
    driver.quit()
    print("5.  Все работает!")
    
except Exception as e:
    print(f" Ошибка при тесте: {type(e).__name__}: {e}")

print("=== ЗАВЕРШЕНО ===")
