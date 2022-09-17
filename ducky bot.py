import tkinter as tk
from tkinter import font
import requests
import time

# THE BRAINS #

# key bank
key_storage = ['E8NP-XQVW-X3T2-Z7R8',
'2HU0-9MCO-KT89-PFPR',
'6RBG-UPUK-34XJ-B0R2',
'06O4-3HIQ-4Z6H-4WQ8',
'TAM2-MERT-4R0I-HW89',
'TDO9-5UJ8-G4HO-VXIL',
'1EK5-DG63-Z5ML-AX9M',
'9IQD-U20R-VFQZ-RR61',
'GVFG-CVWA-RUB6-ZKGR',
'GXR6-UACA-ZWFD-80CP',
'RJ99-YG27-LJ2V-U1MB',
'J4XO-2Z41-G653-UE8C', 
'85OT-XOU6-NSV4-V5JG',
'6QH6-MEVZ-LYLC-7ODP',
'H6NE-R4WJ-LWPB-QSN1',
'D2PT-J9R0-J74Y-6EU0',
'GKF8-527K-1U2B-U9NZ',
'AA9I-UMO5-O1AI-7T1U',
'YQ0R-CCP1-E2S6-VHVR',
'IF5P-CKFM-AF1L-UTW1',
'0MKP-L2II-8S7I-DI6I',
'E1V7-TU7S-0RUS-31Q3',
'VFIL-S7YK-NKPG-B9RH',
'LT72-VKFI-VR88-Q80M',
'87FB-PANJ-11PD-T8O0',
'6QV2-FK1J-3OEV-N8DZ',
'2I7K-W8PM-816X-O45E',
'HZUL-HLFJ-T5ZW-DE4G',
'S573-N4WA-9SZY-EUBE',
'HLTT-VPC9-AD60-L5UM',
'GB86-8ORU-3Y14-05L9',
'RX2Q-YOP7-7283-DD0Z',
'NYUI-TG42-BGTS-CAMV',
'89OZ-QK6C-SAG7-D50A',
'QELO-YF8V-SQHY-2T9N',
'5AWG-YWHC-GW0F-5YMV',
'FEJ5-WQT2-4I55-A8SA',
'R8KA-MAJR-GSRE-W3Z0',
'8EVR-OQ12-C4FS-ID36',
'3YT4-B9CW-MHUW-IZZL',
'BA9D-5OWI-TKA4-H9X6',
'D962-BYWP-6E9L-7C49',
'0TBA-FJYU-Z8AK-186N',
'V49E-OU9A-XYF9-CRA3',
'51EZ-J118-T5IH-EY1O',
'EDH7-ACDT-M8SH-3TMF',
'XQ9U-4EAU-ER4R-IBNG',
'RBGP-CUTJ-IQWM-7BTM',
'V8Y4-QCAQ-5D5F-FWF7',
'QP4G-Y8YP-PEUH-C5TX',
'MZ37-IMCA-25DA-03NU',
'3YSG-4A6E-MQTS-I4XT',
'B57A-7Y5E-QZ2N-NY4S',
'TFMK-WWQH-TMY9-01EG',
'P2PK-0AUY-4EK0-9IG2',
'EIEK-ATN4-M3X5-8TPF',
'J059-FFWL-RKF3-B4BY',
'UT6E-1BF2-4IFB-PAUZ',
'1KPN-H9QJ-E3WC-Q11G',
'F6BI-JVA4-5IUY-PA3Q',
'LRNK-3QPH-C3OE-L55S',
'2QNB-B4QX-XM8W-WJ11',
'8TWE-ST3F-U7TL-07WH',
'5DKB-X9TX-T1H3-OB9L',
'82YQ-8XRL-6MFW-LYM6',
'ZNAH-NF3O-RD6V-O36S',
'PXG8-0V4L-XWUX-R76W',
'S7NC-8DPT-6BJS-U22J',
'C4SG-8GKH-LNFC-PW1E',
'GR2J-6C1K-6432-SOCZ',
'A205-WVB2-95QD-L4N9',
'QJAR-56I1-QFB8-7SXK',
'X0LN-YF0C-9YLE-RI12',
'JQ7N-5A6T-A0WO-F5I3',
'T9TM-ZVQ8-5YXS-BJDS',
'YG9M-D9C2-E62P-CKG2',
'DUCL-J3M5-KWG5-5LU3',
'ETNE-53F6-CVL5-YVZS',
'THDR-TBAB-MS9X-618D',
'CB1S-E5KJ-AFZA-IGIP',
'FE6N-772C-5JDW-QQOB',
'QLFI-ZLW7-9PXQ-F89Y',
'KTLZ-JTX2-YBZ2-WZFZ',
'00M6-40R5-LYCD-FMKJ',
'CRSH-4S88-F3N9-ZDWH',
'6JJJ-6L72-ZEGJ-O6Z4',
'1Q25-R8D0-E5NG-7F6W',
'L5TB-X8OG-LLX1-9NKC',
'QUT3-VW2W-05AV-TBGB',
'NK8I-610I-DR4W-HITG',
'DOJT-2CG7-XQ7F-ZWGH',
'EAJS-V7AZ-19UP-AG5P',
'O619-P3VB-RLQZ-M5H8',
'1BAL-KNO4-DC9B-28JJ',
'0VWR-ITIL-S40Q-TIS3',
'3SWY-L29D-DWMZ-70R5',
'9DSL-HM01-G33G-ORFV',
'48HJ-A5MN-APOY-IO4G',
'GTRI-SQJ6-03QM-MOTG',
'1CYV-7NVC-6QS7-FXEI', 'XXXX-XXXX-XXXX-XXXX']


def viewing():
    # defining
    user_key = entry1.get()
    listing = entry2.get()
    views = entry3.get()
    # process
    log_response["text"] = ""
    errorFound = False
    if user_key in key_storage:
            valid = "key is valid!" #STATUS # COLOR CHANGE
            status_output["text"] = valid
            status_output.config(bg='#28ff02') # green
            # url error
            if "http" not in listing:
                pre = "Your url is incorrect. \nMake sure the it includes https:// ! \n"
                log_response["text"] += pre + "\n"
                errorrr = "Error!" # COLOR CHANGE
                status_output["text"] = errorrr
                status_output.config(bg='#ff1500') # red
                errorFound = True
            # number error
            if not str(views).isnumeric():
                error = "Make sure that your views is \na number greater than or equal to 1"
                log_response["text"] += error + "\n"
                errorrr = "Error!" # COLOR CHANGE
                status_output["text"] = errorrr
                status_output.config(bg='#ff1500') # red
                errorFound = True
            else:
                views = int(views)
            if errorFound:
                return
            # process
            views_output = ""
            for i in range(views):
                r = requests.get(listing)
                views_output = "1 view added"
                win.update()
                #text.set(views_output)
                log_response["text"] += views_output + "\n"
            #sucess
            if views == 1:
                view_success = entry3.get() + " " + "view successfully added!" #STATUS # COLOR CHANGE
                status_output.config(bg='#28ff02') # green
            else:
                view_success = entry3.get() + " " + "views successfully added!" #STATUS # COLOR CHANGE
                status_output.config(bg='#28ff02') # green
            status_output["text"] = view_success
            
    else:
        display = "There was an error! \nCheck to see if your key is correct!" #STATUS 
        log_response["text"] += display
        errorrr = "Error!" # COLOR CHANGE
        status_output["text"] = errorrr
        status_output.config(bg='#ff1500') # red

# add error

#####
#####
#####



### SETTINGS ###

# create instance
win = tk.Tk()

# title
win.title("DuckyTools")

# window
win.resizable(False, False)
win.geometry("700x500")



### OBJECTS + BACKGROUNDS ###

# frame
frame = tk.Frame(win, bg='#070B52', bd=5)
frame.place(relx=0, rely=0, relwidth=1, relheight=1)

photo = tk.PhotoImage(file='ducky.logo.png')

# logo background
logo_background = tk.Label(win, bg='#000000', image=photo)
logo_background.place(relx=0, rely=0.01, relwidth=0.2, relheight=0.2)

# label
title = tk.Label(win, text="DuckyTool's Ebay View Bot", bg='#A8C0CA', bd=10, font=('Arial', 28, 'bold'), fg='#FFFFFF')
title.place(relx=0.19, rely=0.05, relwidth=0.78, relheight=0.11)

# background entrys
background_entry = tk.Label(win, bg='#A8C0CA')
background_entry.place(relx=0.028, rely=0.22, relwidth=0.44, relheight=0.73)

# key entry background
key_background = tk.Label(win, bg='#000000')
key_background.place(relx=0.047, rely=0.318, relwidth=0.405, relheight=0.135)

# key entry fake
entry1_fake = tk.Label(win, bg='#78D88F')
entry1_fake.place(relx=0.048, rely=0.32, relwidth=0.4, relheight=0.13)

# key entry real
entry1 = tk.Entry(win, bg='#78D88F', font=('Arial', 11), bd=0)
entry1.place(relx=0.055, rely=0.32, relwidth=0.393, relheight=0.13)

# key label background
key_background_2 = tk.Label(win, bg='#000000')
key_background_2.place(relx=0.047, rely=0.245, relwidth=0.405, relheight=0.055)

# key label
key_label = tk.Label(win, text="License Key", bg='#FFFFFF', bd=10, font=('Arial', 15), fg='#000000', anchor='w')
key_label.place(relx=0.048, rely=0.248, relwidth=0.4, relheight=0.05)

# listing entry background
listing_background = tk.Label(win, bg='#000000')
listing_background.place(relx=0.047, rely=0.548, relwidth=0.405, relheight=0.135)

# listing entry fake
entry2_fake = tk.Label(win, bg='#78D88F')
entry2_fake.place(relx=0.048, rely=0.55, relwidth=0.4, relheight=0.13)

# listing entry real
entry2 = tk.Entry(win, bg='#78D88F', font=('Arial', 11), bd=0)
entry2.place(relx=0.055, rely=0.55, relwidth=0.393, relheight=0.13)

# listing label background
listing_background_2 = tk.Label(win, bg='#000000')
listing_background_2.place(relx=0.047, rely=0.478, relwidth=0.405, relheight=0.055)

# listing label
listing_label = tk.Label(win, text="Listing URL", bg='#FFFFFF', bd=10, font=('Arial', 15), fg='#000000', anchor='w')
listing_label.place(relx=0.048, rely=0.48, relwidth=0.4, relheight=0.05)

# view entry background
view_background = tk.Label(win, bg='#000000')
view_background.place(relx=0.047, rely=0.778, relwidth=0.405, relheight=0.135)

# view entry fake
entry3_fake = tk.Label(win, bg='#78D88F')
entry3_fake.place(relx=0.048, rely=0.78, relwidth=0.4, relheight=0.13)

# view entry real
entry3 = tk.Entry(win, bg='#78D88F', font=('Arial', 11), bd=0)
entry3.place(relx=0.055, rely=0.78, relwidth=0.393, relheight=0.13)

# view label background
view_background_2 = tk.Label(win, bg='#000000')
view_background_2.place(relx=0.047, rely=0.705, relwidth=0.405, relheight=0.06)

# view label
key_label = tk.Label(win, text="Number of Views", bg='#FFFFFF', bd=10, font=('Arial', 15), fg='#000000', anchor='w')
key_label.place(relx=0.048, rely=0.707, relwidth=0.4, relheight=0.055)

# Start button
start_button = tk.Button(win, text='Start', bg='#F5A8FC', font=('Arial', 16), cursor="hand2", relief="flat", bd=3, command=viewing)
start_button.place(relx=0.49, rely=0.875, relwidth=0.48, relheight=0.075)

# background log response
background_entry = tk.Label(win, bg='#A8C0CA')
background_entry.place(relx=0.49, rely=0.32, relwidth=0.48, relheight=0.54)

# boarder log response
boarder_entry = tk.Label(win, bg='#000000')
boarder_entry.place(relx=0.5065, rely=0.34, relwidth=0.447, relheight=0.5)

# Log response
log_response = tk.Label(win, bg='#78D88F', font=('Arial', 10), anchor='nw', justify='left')
log_response.place(relx=0.51, rely=0.345, relwidth=0.44, relheight=0.49)

# Status Output
status_output = tk.Label(win, bg='#e9ff6c', font=('Arial', 16, 'bold'))
status_output.place(relx=0.49, rely=0.22, relwidth=0.48, relheight=0.075)

IDLE = "Idle" #STATUS # COLOR CHANGE
status_output["text"] = IDLE

### MORE SETTINGS ###

# start
win.mainloop()
