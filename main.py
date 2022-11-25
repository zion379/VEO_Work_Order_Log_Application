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

    json_string = json.dumps(work_order_log_data, indent=4)

    return json_string

#user command line input indicator
uci = (' \n' + '>')
log_db_filepath = 'Resources/worklogdatabase.txt'


def Search():
    print("Search")

def Edit():
    print("Edit Menu:")

def Create():
    print("Create Work Order Log..")

    iot_number = input("type IOT number:" + uci)
    frame_number = input("type bike frame number:" + uci)
    bike_prority = input("Bike Priority. h = High, m = Medium, l = Low" + uci)

    with open(log_db_filepath , 'r') as readfile:
        json_data = readfile.readlines()
        decoded_data = json.loads(json_data[0])
        print(decoded_data)
        #left off working on reading file.

    with open(log_db_filepath ,'w') as writefile:
        Work_Order_Data = CreateWorkOrderLog( iot_number,frame_number,bike_prority)
        json.dump(Work_Order_Data, writefile)

def MainMenu():
    user_selection = input("Type an option:" + '\n' + "Create ,Edit ,Search or exit" + uci)

    if 'create'or 'Create' in user_selection:
        Create()
    elif 'exit' in user_selection:
        exit()

while True:
    MainMenu()
