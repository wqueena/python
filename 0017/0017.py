import xlrd
from xml.dom.minidom import Document

workbook = xlrd.open_workbook('result.xls')

#获取sheet
Data_sheet = workbook.sheets()[0]

namecols = Data_sheet.col_values(0)  #获取id list
encols = Data_sheet.col_values(2)  # 获取翻译 list

#xml doc
doc = Document()
resources = doc.createElement("resources")
doc.appendChild(resources)

for x in range(len(namecols)):
    st = doc.createElement("string")
    st.setAttribute("name", namecols[x])
    name = doc.createTextNode(encols[x])
    st.appendChild(name)
    resources.appendChild(st)

filename = "student.xml"
f = open(filename, "w")
f.write(doc.toprettyxml(indent="  "))
f.close()
