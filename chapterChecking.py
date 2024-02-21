import os
import re
import pandas as pd
from datetime import date, datetime



def localChecking():
    folder = 'C:\\Users\\thain\\Downloads\\mangas\\down\\downloads'

    log_datetime = []
    name = []
    latestChapter = []

    files = os.listdir(folder)
    for file in files:
        chapterFolder = folder + "\\" + file
        chapters = os.listdir(chapterFolder)
        # print(chapters)
        if len(chapters) == 1:
            for chapter in chapters:
                numChapter = re.search(r'\d+', chapter).group()
                name.append(file)
                latestChapter.append(numChapter)
                log_datetime.append(f'{datetime.today()}')
        else:
                numChapter = re.search(r'\d+', chapters[-1]).group()
                name.append(file)
                latestChapter.append(numChapter)
                log_datetime.append(f'{datetime.today()}')


    
    df = pd.DataFrame({
         'name': name,
         'latestChapter': latestChapter
    })

    df_log = pd.DataFrame({
        'log': log_datetime,
        'name': name,
        'latestChapter': latestChapter
    })

    df.to_csv(f'coffeemanga.csv', index=False)
    print('create update file successfully')

    # CREATE LOG

    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")

    # Create the filename using the formatted datetime
    filename = f"./log/log_{formatted_datetime}.csv"

    # Save the DataFrame to CSV
    df_log.to_csv(filename, index=False)

    print(f"Save log successfully: {filename}")

        


def chapterChecking():
    localChecking()
    print('done')

    

