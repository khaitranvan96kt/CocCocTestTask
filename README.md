# CocCocTestTask
# Authors: Trần Văn Khải
# Gmail: khai.tranvan.96.kt@gmail.com
# Sdt: 01663435301
# Work: PTIT

Ý tưởng: Ta có hai chuỗi A và B. Ta tìm các vị trí mà ký tự của A bằng ký tự ở B.
Ví dụ như : A = 'aLbm' và B = 'abLm'
 -- Ta gọi a và b là 2 mảng chứa các vị trí thỏa mãn.
 => a = [0,1,3] và b = [0,2,3]  
 Ta luôn có: len(a) = len(b)
 Ta suy ra được sô lần cần copy = len(a) = len(b)
 Từ a và b t sẽ dựa vào đó tính số lần Replace, Delete, Insert.
 
 