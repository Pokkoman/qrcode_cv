import requests
lot_id = "612f4a5cea87150021469d96"
url_reqcode = r"https://cocoon-server.herokuapp.com/v1/parking-lot/booking-info-from-userid"
url_checkin = r"https://cocoon-server.herokuapp.com/v1/parking-lot/check-in"
myobj = {"lotId": lot_id,"userId": None}
myobj_num = {"lotId": lot_id,"vehiclePlateNumber": None}

def req_code(user_id): 
    num = None
    myobj["userId"] = user_id

    x = requests.post(url_reqcode, data = myobj)
    if str(x.status_code) == "200":
        data = x.json()
        print(data)
        num = data["vehiclePlateNumber"]

        return x.status_code,num 
    else:
        return x.status_code, num

def check(num):

    myobj_num["vehiclePlateNumber"] = num
    print(myobj_num)
    x = requests.post(url_checkin, data = myobj_num)
    data = x.json()
    
    msg = data["message"]

    return msg
    


