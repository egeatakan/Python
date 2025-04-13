import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    # Her çalışana maaşının %10'u kadar bonus ekleyelim
    employees['Bonus'] = employees['Salary'] * 0.10
    return employees

# Çalışan bilgilerini kullanıcıdan alma
def get_employee_data():
    employees = []
    
    while True:
        name = input("Çalışan ismini girin (veya 'q' ile çıkış yapın): ")
        if name.lower() == 'q':
            break
        
        try:
            salary = float(input(f"{name} için maaşı girin: "))
            employees.append({"Name": name, "Salary": salary})
        except ValueError:
            print("Lütfen geçerli bir maaş değeri girin.")
    
    return pd.DataFrame(employees)

# Çalışan bilgilerini al
employees_df = get_employee_data()

# Bonusları hesapla ve sonucu göster
if not employees_df.empty:
    updated_employees = createBonusColumn(employees_df)
    print(updated_employees)
else:
    print("Çalışan verisi girilmedi.")