"""
Convert segment to number

Input:segment list,node list
Output:link list of number

Author:Hanyunxuan
Date:2018.10.19
"""


def segment_num(Node_list, segment_list1, segment_list2):
    num_list1 = len(segment_list1) * [0]
    num_list2 = len(segment_list1) * [0]
    for i in range(len(segment_list1)):
        for j in range(len(Node_list)):
            if segment_list1[i] == Node_list[j]:
                num_list1[i] = j + 1
        for j in range(len(Node_list)):
            if segment_list2[i] == Node_list[j]:
                num_list2[i] = j + 1

        # for i in range(len(num_list1)):
        #     if num_list1[i]==0:
        #         print(segment_list1[i],i)
    try:
        num_list1.index(0)
        print(segment_list1[num_list1.index(0)]+" is not in Node_list")
    except ValueError:
        pass
    try:
        num_list2.index(0)
        print(segment_list2[num_list2.index(0)]+" is not in Node_list")
    except ValueError:
        pass
    return num_list1, num_list2


if __name__ == "__main__":
    from network_generation.mysql_link import Link
    import glob
    import os
    import xlrd

    # Read node data
    [db, cursor] = Link()

    cursor.execute("SELECT (Node) FROM node")
    Node_list = [res[0] for res in cursor]

    # Read segment data
    os.chdir('E:\AllProject\全国程序基础数据')
    # FileList = glob.glob('*.xlsx')
    FileList = glob.glob('全国segment.xlsx')
    # print(FileList)
    workbook = xlrd.open_workbook(FileList[0])
    sheet1 = workbook.sheet_by_index(0)
    segment_list1 = sheet1.col_values(0)
    segment_list2 = sheet1.col_values(1)
    num_list1, num_list2 = segment_num(Node_list, segment_list1, segment_list2)
    print(len(segment_list1))
    # # Write to mysql
    # cursor = db.cursor()
    # cursor.execute("DROP TABLE IF EXISTS segment")
    #
    # sql = """CREATE TABLE segment (
    #          segment1 text,
    #          segment2 text,
    #          num1 INT,
    #          num2 INT )"""
    # cursor.execute(sql)
    #
    # for i in range(len(segment_list1)):
    #     cursor.execute("INSERT INTO segment(segment1) VALUES(%s)", [segment_list1[i]])
    #     db.commit()
    #
    # for i in range(len(segment_list1)):
    #     cursor.execute("UPDATE `segment` SET `segment`.`segment2`= %s WHERE `segment`.`segment1` = %s",
    #                    (segment_list2[i], segment_list1[i]))
    #     cursor.execute("UPDATE `segment` SET `segment`.`num1`= %s WHERE `segment`.`segment1` = %s",
    #                    (num_list1[i], segment_list1[i]))
    #     cursor.execute("UPDATE `segment` SET `segment`.`num2`= %s WHERE `segment`.`segment1` = %s",
    #                    (num_list2[i], segment_list1[i]))
    #     db.commit()
    # cursor.close()
    # db.close()

    import pandas as pd
    from pandas import ExcelWriter

    df = pd.DataFrame({'a': num_list1,
                       'b': num_list2})

    writer = ExcelWriter('aaa2.xlsx')
    df.to_excel(writer, 'Sheet1', index=False)
    writer.save()