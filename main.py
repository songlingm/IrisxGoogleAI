from hear import *
from speak import*
from datetime import date, datetime, time

speak("Xin chào mọi người, mình là trợ lý ảo Iris")

while True:

    you = hear()

    if you == None:
        speak("Mình chưa nghe được bạn nói, bạn nói lại được không ?")
    elif "hôm nay" in you or "bây giờ"in you :
        now = datetime.now()
        if "mấy giờ" in you:
            t = now.strftime("%H h, %M phút, %S giây")
            speak(t)
        if "ngày bao nhiêu" in you:
            t = now.strftime("Hôm nay là ngày %d, tháng %m, năm %Y")
            speak(t)
    elif "chủ tịch" in you and "việt nam" in you and "đầu tiên" in you:
        speak("Chủ tịch Hồ Chí Minh nha bạn")
    elif "con người" in you:
        speak("Mình chỉ là trợ lý ảo thôi")
    elif "bạn tên là gì" in you:
        speak("Mình tên là Iris !")
    elif "tạm biệt" in you:
        speak("Tạm biệt, hẹn gặp lại bạn sau !!!")
        break    
