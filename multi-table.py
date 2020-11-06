import matplotlib.pyplot as plt
import openpyxl
import pandas as pd

# 将表格根据日期拆分成多个工作表
# str = object保留excel表数据原格式，防止保存excel时数值以科学计数格式保存造成信息丢失
df = pd.DataFrame(pd.read_excel('D:\\subdata.xlsx', sheet_name='Sheet1', dtype=object))

writer = pd.ExcelWriter('D:\\subdata.xlsx')

# 在原工作簿基础上新增工作表
wb = openpyxl.load_workbook('D:\\subdata.xlsx')
writer.book = wb

for groupname, groupdf in df.groupby('日期'):
    groupdf.to_excel(writer, sheet_name=groupname, index=False)

writer.save()
writer.close()
wb.close()
