import pandas as pd
from functions import v_card
import shutil

#importing CSV into pandas and setting ID as the index for the dataframe
# df = pd.read_csv(
#     "Business Card Request (2).csv",
#     index_col="ID")

def do_everything(csv):
    pd.options.display.max_columns = 100
    df = pd.read_csv(csv,index_col="ID")

    columns_to_drop = ["Requested By",
    "Shipping Address",
    "Supervisor",
    "Quantity ",
    "Quote Amount",
    "Actual Amount",
    "PO Number",
    "Attachments",
    "Supervisor Sign-off status",
    "Procurement Status on PO Number",
    "Shipping Address: Country/Region",
    "Shipping Address: State",
    "Shipping Address: City",
    "Shipping Address: Postal Code",
    "Shipping Address: Street",
    "Shipping Address: Coordinates",
    "Shipping Address: Name",
    "Suite/Apt/P.O. Number",
    "Proof to Review",
    "Modified", 
    "Created", 
    "Modified By", 
    "Notes to Designer",
    "Business Address on Business Card"]
    df = df.drop(columns_to_drop,axis=1)
    # setting all N/A values to 0 to change data type from float to int for both Office and Mobile number
    df["Office Number"] = df["Office Number"].fillna(0).astype(int)
    df["Mobile Number (optional)"] = df["Mobile Number (optional)"].fillna(0).astype(int)

    #splitting full name into first and last name
    for i,r in df.iterrows():
        df.loc[i,"First Name"] = r["Name"].split()[0]
        df.loc[i,"Last Name"] = r["Name"].split()[-1]
    df['Business Address on Business Card: Address'] = df['Business Address on Business Card: Address'].fillna(value="")
    df['Business Address on Business Card: Address 2'] = df['Business Address on Business Card: Address 2'].fillna(value="")
    df['Business Address on Business Card: City '] = df['Business Address on Business Card: City '].fillna(value="")
    df['Business Address on Business Card: State'] = df['Business Address on Business Card: State'].fillna(value="")

    df["Preferred Last Name"] = df["Preferred Last Name"].fillna(value="")
    df["Preferred First Name"] = df["Preferred First Name"].fillna(value="")


    path = "Users:elisantibanez:Documents:new_businesscards:qr_images:"

    #making QR Codes. Setting an if statement depending on preferred name or not. 
    for i,r in df.iterrows():

        # print([type(r['Business Address on Business Card: Address 2']), type(r['Business Address on Business Card: City ']), type(r['Business Address on Business Card: State'])])
        
        if r["Office Number"] and r["Mobile Number (optional)"] != 0: 

            #both numbers and has a preferred name
            if r["Do you have a preferred name?"] == "Yes":
                v_card(
                    company= r["GetixHealth or ARstrat "],
                    first_name = r["Preferred First Name"],
                    last_name = r["Preferred Last Name"],
                    title = r["Title"],
                    email = r["Email"],
                    office_number = r["Office Number"],
                    mobile_number = r["Mobile Number (optional)"],
                    address = r['Business Address on Business Card: Address'] + ", " + r['Business Address on Business Card: Address 2'] + " " + r['Business Address on Business Card: City '] + " " +  r['Business Address on Business Card: State'],
                    zip_code = r['Business Address on Business Card: ZIP'])
                    
                df.loc[i,"#image"] = path + r["Preferred First Name"] + " " + r["Preferred Last Name"] + ".svg"

            #both numbers and has NO preferred name
            else:
                v_card(
                    company= r["GetixHealth or ARstrat "],
                    first_name = r["First Name"],
                    last_name = r["Last Name"],
                    title = r["Title"],
                    email = r["Email"],
                    office_number = r["Office Number"],
                    mobile_number = r["Mobile Number (optional)"],
                    address = r['Business Address on Business Card: Address'] + ", " + r['Business Address on Business Card: Address 2'] + " " + r['Business Address on Business Card: City '] + " " +  r['Business Address on Business Card: State'],
                    zip_code = r['Business Address on Business Card: ZIP'])  
                
                df.loc[i,"#image"] = path + r["First Name"] + " " + r["Last Name"] + ".svg"
    
                        
        if r["Office Number"] == 0 and r["Mobile Number (optional)"] != 0:
            #Only Mobile number and has a preferred name
            if r["Do you have a preferred name?"] == "Yes":
                v_card(
                    company= r["GetixHealth or ARstrat "],
                    first_name = r["Preferred First Name"],
                    last_name = r["Preferred Last Name"],
                    title = r["Title"],
                    email = r["Email"],
                    mobile_number = r["Mobile Number (optional)"],
                    address = r['Business Address on Business Card: Address'] + ", " + r['Business Address on Business Card: Address 2'] + " " + r['Business Address on Business Card: City '] + " " +  r['Business Address on Business Card: State'],
                    zip_code = r['Business Address on Business Card: ZIP']) 
                df.loc[i,"#image"] = path + r["Preferred First Name"] + " " + r["Preferred Last Name"] + ".svg"
    

            else:
                #Only Mobile numbers and has NO preferred name
                v_card(
                    company= r["GetixHealth or ARstrat "],
                    first_name = r["First Name"],
                    last_name = r["Last Name"],
                    title = r["Title"],
                    email = r["Email"],
                    mobile_number = r["Mobile Number (optional)"],
                    address = r['Business Address on Business Card: Address'] + ", " + r['Business Address on Business Card: Address 2'] + " " + r['Business Address on Business Card: City '] + " " +  r['Business Address on Business Card: State'],
                    zip_code = r['Business Address on Business Card: ZIP'])
                
                df.loc[i,"#image"] = path + r["First Name"] + " " + r["Last Name"] + ".svg"

                    

        if r["Office Number"] != 0 and r["Mobile Number (optional)"] == 0:
            #Only Office number and has a preferred name
            if r["Do you have a preferred name?"] == "Yes":
                v_card(
                    company= r["GetixHealth or ARstrat "],
                    first_name = r["Preferred First Name"],
                    last_name = r["Preferred Last Name"],
                    title = r["Title"],
                    email = r["Email"],
                    office_number = r["Office Number"],
                    address = r['Business Address on Business Card: Address'] + ", " + r['Business Address on Business Card: Address 2'] + " " + r['Business Address on Business Card: City '] + " " +  r['Business Address on Business Card: State'],
                    zip_code = r['Business Address on Business Card: ZIP'])
                
                df.loc[i,"#image"] = path + r["Preferred First Name"] + " " + r["Preferred Last Name"] + ".svg"

                    
            #Only Office number and has No preferred name
            else:
                v_card(
                    company= r["GetixHealth or ARstrat "],
                    first_name = r["First Name"],
                    last_name = r["Last Name"],
                    title = r["Title"],
                    email = r["Email"],
                    office_number = r["Office Number"],
                    address = r['Business Address on Business Card: Address'] + ", " + r['Business Address on Business Card: Address 2'] + " " + r['Business Address on Business Card: City '] + " " +  r['Business Address on Business Card: State'],
                    zip_code = r['Business Address on Business Card: ZIP']) 
                
                df.loc[i,"#image"] = path + r["First Name"] + " " + r["Last Name"] + ".svg"


    columns_to_rename = {"Business Address on Business Card: Address": "Address",	
    "Business Address on Business Card: City": "City",	
    "Business Address on Business Card: State": "State",	
    "Business Address on Business Card: ZIP": "ZIP",	
    "Business Address on Business Card: Country": "Country",	
    "Business Address on Business Card: Address 2": "Address 2",
    "#image":"@image"}

    df = df.rename(columns=columns_to_rename)
    numbers = ["Mobile Number (optional)" ,"Office Number"]
    df[numbers] = df[numbers].astype(str)
    #setting the periods on the phone numbers
    for c in df[numbers]:
        df[c] = df[c].str[:3] + '.' + df[c].str[3:6] + '.' + df[c].str[6:]

    df.to_csv("./result/datacsv/data_14_follow_up.csv")
    df
    shutil.make_archive("test6", 'zip', "./result/")
