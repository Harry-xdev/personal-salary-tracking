import csv


staffs_lst_default = [
('LÊ PHƯƠNG', '070032', 'TEST REQUEST', 'RD'),
('TRƯƠNG TƯ XUÂN', '080262', 'TEST REQUEST', 'RD'),
('TRƯƠNG THÀNH TAM', '080427', 'B/T', 'RD'),
('LÊ THANH TUẤN', '101339', 'TEST REQUEST', 'RD'),
('PHẠM THỊ PHƯƠNG', '172684', 'TEST REQUEST', 'RD'),
('NGUYỄN HOÀNG VIỆT', '172759', 'TEST REQUEST', 'RD'),
('NGUYỄN THỊ HỒNG YẾN', '172824', 'TEST REQUEST', 'RD'),
('BÙI ĐÌNH HỒNG PHÚC', '193273', 'TEST REQUEST', 'RD'),
('TRƯƠNG VĂN MINH', '203591', 'TEST REQUEST', 'RD'),
('NGUYỄN QUANG QUÍ', '203638', 'TEST REQUEST', 'RD'),
('NGUYỄN THỊ DIỄM MY', '213714', 'TEST REQUEST', 'RD'),
('LÊ MINH THẮNG', '223906', 'TEST REQUEST', 'RD'),
('LÊ QUỐC TRUNG', '224016', 'B/T', 'RD'),
('NGUYỄN TUẤN ANH', '224057', 'TEST REQUEST', 'RD'),
('TRẦN VĂN LƯU', '234102', 'TEST REQUEST', 'RD'),
('LÊ HUỲNH ANH KHOA', '234168', 'B/T', 'RD'),
('NGUYỄN MAI PHƯƠNG', '234170', 'TEST REQUEST', 'RD'),
('PHẠM NG NGỌC TUYẾT', '234172', 'TEST REQUEST', 'RD'),
]


def write_data_to_csv():
    with open("staffs.csv", 'w', encoding='utf-8', newline='') as file:
          writer = csv.writer(file)
          for i in staffs_lst_default:
            writer.writerow(i)
    
def import_staffs_data():
  staffs_list_2 = []
  with open('staffs.csv', 'r', encoding='utf-8', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
       staffs_list_2.append(tuple(row))
  return staffs_list_2
          
staffs = import_staffs_data()
print(staffs)