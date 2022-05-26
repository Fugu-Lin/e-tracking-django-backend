# e-tracking-django-backend

統一超商交貨便貨態查詢(包含 OCR 自動辨識驗證碼)

此repository與https://github.com/Fugu-Lin/e-tracking-angular-frontend 為一組全端的專案，可搭配服用。  
  
以下為系統的展示網址：  
http://54.179.188.161:4200/

本功能中的models 是從 https://github.com/ThanatosDi/E-Tracking Fork過來的。  
在此版本中更改了self.session = requests.Session()在new ECTracker就initialize的問題，  
解決了沒辦法在django連續要求資料的問題，  
並同時在ocr.py中對影像加入MaxFilter與MinFilter的方法增加OCR辨識的穩定性。  
不過偶爾還是會不準確，之後有空再自己training一個專用的model XD。



