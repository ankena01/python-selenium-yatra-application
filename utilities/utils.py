import logging
import pandas as pd

class Utils:


    def custom_logger(loglevel = logging.DEBUG):


        # create logger (set logging level)

        logger = logging.getLogger(__name__)        
    
        logger.setLevel(loglevel)

        # create console handler / file handler
        
        fh = logging.FileHandler('.\Logs\demofile.log' , mode='a')      # Default mode is append. we can use write mode to overwrite        

        # create formatter (how you want your logs to be formatted)
        
        formatter_fh = logging.Formatter('%(asctime)s : %(filename)s : %(name)s - %(levelname)s : %(message)s' , datefmt='%m/%d/%Y %I:%M:%S %p')
        
        # add formatter to console handler / file handler (Display formmatted messages on console / file)
        
        fh.setFormatter(formatter_fh)
        # add console handler / file handler to logger
        
        logger.addHandler(fh)

        return logger

        
    def read_data_from_excel(file_path):
        
        df = pd.read_excel(file_path,sheet_name="Sheet1")
        #print(df)
        row_count = len(df)
        data_list=[]

        for i in range(0, row_count):
            row = [] 
            for x in df.iloc[i]:
                row.append(x)
            data_list.append(row)
        #print(data_list)
        return data_list
        
    def read_data_from_csv(file_path):
        
        df = pd.read_csv(file_path)
        #print(df)
        row_count = len(df)
        data_list=[]

        for i in range(0, row_count):
            row = [] 
            for x in df.iloc[i]:
                row.append(x)
            data_list.append(row)
        #print(data_list)
        return data_list    
        

    def feature_sdet_1(self):
        print("Feature created by sdet 1 to merge with main branch")
        
    def merge_conflict(self):
        pass

