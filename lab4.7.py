def BMI(w,h):
    h1  = h / 100
    b = w / (h1 * h1)
    print("BMI: %.2f" %b)
    return b

w = float(input("Weight: "))
h = float(input("Height: "))

b = BMI(w,h)

if(b >30):
    print("อยู่ในเกณฑ์ : อ้วนมาก / โรคอ้วนระดับ3\nภาวะเสี่ยงต่อโรค : อันตรายระดับ 3")
elif(b >= 25 and b <=29.90):
    print("อยู่ในเกณฑ์ : อ้วน / โรคอ้วนระดับ2\nภาวะเสี่ยงต่อโรค : อันตรายระดับ 2")
elif(b >= 23 and b <=24.90):    
    print("อยู่ในเกณฑ์ : ท้วม / โรคอ้วนระดับ1\nภาวะเสี่ยงต่อโรค : อันตรายระดับ 1")
elif(b >= 18.50 and b <=22.90):
    print("อยู่ในเกณฑ์ : ปกติ (สุขภาพดี)\nภาวะเสี่ยงต่อโรค : เท่าคนปกติ")
else:
    print("อยู่ในเกณฑ์ : น้ำหนักน้อย / ผอม\nภาวะเสี่ยงต่อโรค : มากกว่าคนปกติ")

