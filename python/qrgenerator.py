import qrcode
import os
def generator(text):
    #set parameters for the qr
    qr = qrcode.QRCode(
        version = 1 ,
        error_correction = qrcode.ERROR_CORRECT_L ,
        box_size = 10 ,
        border = 4
    )
    #set the content of the data
    qr.add_data(text)
    #generate the qr
    qr.make(fit = True)
    img = qr.make_image(fill_color = "black" , back_color ="white")
    filename = input("Enter  a name for the qr code: ")
    #add .png to the name to make it a png file 
    filename_extension = filename + ".png"
    #set the qr path to pictures 
    path = os.path.join(os.path.expanduser("~"), "Pictures", filename_extension)
    img.save(path)
#get the url input and call the function    
url = input("Enter the url: ")
generator(url)