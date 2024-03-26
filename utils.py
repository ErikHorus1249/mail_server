# import pickle
import os
import csv
import datetime


def export_csv(hostname: str, username: str, current_time_server: str):
    file_path = f"reports/non_sync_servers_{datetime.datetime.now().strftime('%d_%m_%Y')}.csv"
    
    
    # my data rows as dictionary objects
    mydict = [{'timestamp': datetime.datetime.now(), 'hostname': hostname, 'username': username, 'curent_time_server': current_time_server,},]
    
    # field names
    fields = ['timestamp', 'hostname', 'username', 'curent_time_server']
    try:
        # check exist file 
        if not os.path.isfile(file_path):
            # writing to csv file
            with open(file_path, 'a') as csvfile:
                # creating a csv dict writer object
                writer = csv.DictWriter(csvfile, fieldnames=fields)
            
                # writing headers (field names)
                writer.writeheader()
            
                # writing data rows
                writer.writerows(mydict)
                
                csvfile.close()
        else:
            # writing to csv file
            with open(file_path, 'a') as csvfile:
                # creating a csv dict writer object
                writer = csv.DictWriter(csvfile, fieldnames=fields)
            
                # writing data rows
                writer.writerows(mydict)
                
                csvfile.close()
        return True
    except Exception as error:
        print(error)
        return False
    
    
if __name__ == "__main__":
    print(export_csv("HMVGGLOBAL", "14.13.1.1"))
    