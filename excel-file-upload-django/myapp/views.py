from django.shortcuts import render
import openpyxl

import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd




def index(request):
    if "GET" == request.method:
        return render(request, 'myapp/index.html', {})
    else:
        excel_file = request.FILES["excel_file"]

        # you may put validations here to check extension or file size

        wb = openpyxl.load_workbook(excel_file)

        # getting all sheets
        sheets = wb.sheetnames
        print(sheets)

        # getting a particular sheet
        worksheet = wb["Sheet1"]
        print(worksheet)

        # getting active sheet
        active_sheet = wb.active
        print(active_sheet)

        # reading a cell
        print(worksheet["A1"].value)

        excel_data = list()
        # iterating over the rows and
        # getting value from each cell in row
        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))
                print(cell.value)
            excel_data.append(row_data)
        
        context = data_processing_box(excel_data)
        
        
        return render(request, 'myapp/index.html', {'context':json.dumps(context)})


def data_processing_box(excel_data):

    #存title
    title = excel_data[0]
    data = excel_data.copy()
    del data[0]
    #將
    df = pd.DataFrame(data, columns=title, dtype='float64')
    title.remove('SQU_NO')
    title.remove('BIRTHDAY')
    title.remove('GLU')
    title.remove('PRO')
    context=[]
    for num in range(len(title)):
        count = np.sum(df[title[num]].values == "None")
        print(count)
        df[title[num]] = df[title[num]].replace('None',"")
        df[title[num]] = pd.to_numeric(df[title[num]], errors='ignore')
        tmp = {}
        tmp['title'] = title[num]
        tmp['Q'] = []
        tmp['Q'].append(df[title[num]].quantile(0))
        tmp['Q'].append(df[title[num]].quantile(0.25))
        tmp['Q'].append(df[title[num]].quantile(0.5))
        tmp['Q'].append(df[title[num]].quantile(0.75))
        tmp['Q'].append(df[title[num]].quantile(1))
        tmp['sum']= str(len(df[title[num]])-count)
        context.append(tmp)
    print(context)
    return context

    #print(context['HEIGHT_Q0'])

    #df['HEIGHT'] = df['HEIGHT'].replace('None',"")
    #df['HEIGHT'] = pd.to_numeric(df['HEIGHT'], errors='ignore')
    #print (df['BLP'])
    #print(len(df['HEIGHT']))
    #print(df.sort_values(by=['HEIGHT']))
    #print(title)
    #print(df.dtypes)
    #print(df['BLP'].sort_values())
    #print(len(excel_data))
    #print("  ")
    #print(len(excel_data))
    #抓每個值來做圖表
    #for row in range(len(excel_data[0])):
        #for col in range(len(excel_data)):
            #print()
    # = excel_data.sort(key = sortSecond)
    #a=np.array(excel_data)
    #a=np.array(a[1:,3] , dtype=float)
    #print(np.sort(a, axis=None))
    #a = [5, 1, 4, 7, 2, 1]
    #print (excel_data.sort(key = sortSecond))
    #print(sorted(excel_data[1:,3]))        
            
            
            
            #print(row , col)
            #print(excel_data[row][col])

#def sortSecond(val): 
    #return val[1:,5]




