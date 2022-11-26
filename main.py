import json
from datetime import date


#helper functions
def CreateWorkOrderLog(_IOT,_FrameNumber, _Proity):
    creation_date = str(date.today())
    work_order_log_data = {
        f"workorder-{_FrameNumber}": {
        "IOT_number" : _IOT,
        "Frame Number" : _FrameNumber,
        "Bike Priority" : _Proity,
        "date_created" :  creation_date,
        "Bike issues" : [],
        "Completed_issues" : [],
        "Notes" : ""
        }
    }

    json_string = json.dumps(work_order_log_data)

    return json_string

#user command line input indicator
uci = (' \n' + '>')
log_db_filepath = 'Resources/worklogdatabase.json'

def Showall():
    print("Show all Menu")
    #read db
    json_data = []
    with open(log_db_filepath, 'r') as readfile:
        json_data = readfile.readline()
        decoded_data = json.loads(json_data)
        for index, workorder in enumerate(decoded_data):
            print(f"{workorder} at index {index}")
        #print(f"{type(decoded_data)} Data: {decoded_data[1]}") # change this to 1 to show other data
        print(len(decoded_data))
def Search():
    print("Search Menu")

def Edit():
    print("Edit Menu")

def Create():
    print("Create Work Order Log..")

    iot_number = input("type IOT number:" + uci)
    frame_number = input("type bike frame number:" + uci)
    bike_prority = input("Bike Priority. h = High, m = Medium, l = Low" + uci)

    json_data = []
    decoded_data = []
    try:
        with open(log_db_filepath , 'r') as readfile:
            json_data.append(readfile.readline())
            for data in json_data:
                decoded_data.append(json.loads(data))
            #left off working on reading file.
    except FileNotFoundError:
        print("Data Base file not found creating new DB File...")
    finally:
        with open(log_db_filepath ,'w') as writefile:
            Work_Order_Data = CreateWorkOrderLog( iot_number,frame_number,bike_prority)
            decoded_data.append(Work_Order_Data)
            #for data ... left off here
            json_data.append(Work_Order_Data)
            json.dump(json_data, writefile)
            print("succesfully saved work order.")

def MainMenu():
    user_selection = input("Type an option:" + '\n' + "Create ,Edit ,Search, Show all or exit" + uci)
    if 'create' in user_selection:
        Create()
    elif 'exit' in user_selection:
        exit()
    elif 'show' in user_selection and 'all' in user_selection:
        Showall()
    elif 'edit' in user_selection:
        Edit()
    elif 'search' in user_selection:
        Search()
    else:
        print("Enter a valid Command")

while True:
    MainMenu()
