# 导入Excel第三方库xlwt,先用pip安装
import xlwt
# 新建excel
book = xlwt.Workbook(encoding='utf-8')
# 新建sheet
sheet = book.add_sheet('sheet1')
# 第一行第一列
sheet.write(0,0,'a1')
# 第二行第二列
sheet.write(1,1,'python')
sheet.write(1,2,'love')
# 保存到本地
book.save('d:\\test.xls')