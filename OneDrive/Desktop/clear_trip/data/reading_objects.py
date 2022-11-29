from library_.config import Config
import xlrd
path = Config.Data_Path

def read_locators():
    workbook =xlrd.open_workbook(Config.Data_Path)
    worksheet = workbook.sheet_by_name("OfferPage")
    rows = worksheet.nrows
    print(rows)
    d = {}

    for i in range(1,rows):
        row = worksheet.row_values(i)
        print(row)
        d[row[0]] = (row[1],row[2])
    return d

print(read_locators())