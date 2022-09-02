# from PIL import Image
import qrcode
import qrcode.image.svg
import os

def make_qr_quote(data,name,dirname):
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=2)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=(150,151,54), back_color="white")
    os.makedirs(f"./result/{dirname}/{dirname}/", exist_ok=True)
    img.save(f"./result/{dirname}/{dirname}/{name}.png")
    # return img.get_image()


def make_qr_svg_quote(data,name,dirname):
    qr = qrcode.QRCode(image_factory=qrcode.image.svg.SvgPathImage)
    qr.add_data(data)
    qr.make(fit=True)
    # img = qr.make_image(fill='#000000')

    img = qr.make_image(fill='#969736')
    os.makedirs(f"./result/{dirname}/{dirname}_qr_images/", exist_ok=True)
    img.save(f"./result/{dirname}/{dirname}_qr_images/{name}.svg")


def make_AR_qr_svg_quote(data,name,dirname):
    qr = qrcode.QRCode(image_factory=qrcode.image.svg.SvgPathImage)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='#d12027')
    os.makedirs(f"./result/{dirname}/{dirname}_qr_images/", exist_ok=True)
    img.save(f"./result/{dirname}/{dirname}_qr_images/{name}.svg")


def v_card(dirname, company, first_name, last_name, title, email, office_number = "" , mobile_number = "", address = None, zip_code = None):
    if company == "GetixHealth":
        make_qr_svg_quote(f'''BEGIN:VCARD
VERSION:3.0

N: {last_name}; {first_name}

FN: {first_name} {last_name}

TITLE: {title}

ORG: {company} 

LANG: en-US

URL: www.{company}.com

EMAIL: {email}      

TEL;TYPE=voice,work,pref:{office_number}

TEL;TYPE=voice,CELL,pref:{mobile_number} 

ADR;TYPE=dom,work,postal,parcel:;;{address};;{zip_code};

END:VCARD ''',first_name + " " + last_name, dirname)

    else:
        make_AR_qr_svg_quote(f'''BEGIN:VCARD
VERSION:3.0

N: {last_name}; {first_name}

FN: {first_name} {last_name}

TITLE: {title}

ORG: {company} 

LANG: en-US

URL: www.{company}.com

EMAIL: {email}      

TEL;TYPE=voice,work,pref:{office_number}

TEL;TYPE=voice,CELL,pref:{mobile_number} 

ADR;TYPE=dom,work,postal,parcel:;;{address};;{zip_code};

END:VCARD ''',first_name + " " + last_name, dirname)
