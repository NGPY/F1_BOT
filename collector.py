import gspread
from oauth2client.service_account import ServiceAccountCredentials

class GoogleSheetCollector():
    
    def __init__(self):
        
        scope =["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json",scope)
        client = gspread.authorize(creds)
        sheet = client.open("F1").sheet1
        tempData = sheet.get_all_values()
        
        self.data = []
        
        instructions = {'team':0,
                        'name':1,
                        'div':2,
                        'points':3}

        for row in tempData:
            tempDict = {}
            for item in instructions:              
                tempDict.update({item:row[instructions[item]]})          
            self.data.append(tempDict)
            
        
        
    def getDataCell(self, cell):
        
        row = int(''.join([i for i in cell if i.isnumeric()])) - 2
        col = ord(''.join([i for i in cell if not i.isnumeric()])) - 65# only works for A-Z      
        key = list(self.data[row])[col]
        return self.data[row][key]
        
    def getDataColRow(self, col, row):
    
        key = list(self.data[row - 2])[col - 1]
        
        print()
        
        return self.data[row - 2][key]
    
    def Row(self, row):
        return self.data[row - 1]
        
          
        
        