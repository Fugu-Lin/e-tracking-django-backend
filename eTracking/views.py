
# from .models.etracking import ECTracker
import uuid
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from models.etracking import ECTracker
import json
import os

ECTRACKER = ECTracker("C:\\Program Files\\Tesseract-OCR\\tesseract.exe")
@csrf_exempt
def search(request):
    data = json.load(request)
    results = []
    for order in data["fileds"]:
        result = ""
        try:
            uid    = uuid.uuid4()
            result = ECTRACKER.tracker(order['orderNumber'], autoVerify=True, uid=uid)
            results.append(result)
            os.remove("./img_"+str(uid)+".jpg")
            print(result)
        except:
            result = "搜尋結果有誤，請重新檢查輸入的資料是否正確"
        json_data = json.dumps(results)
        print(json_data)
    return HttpResponse(json_data, content_type='application/json')
