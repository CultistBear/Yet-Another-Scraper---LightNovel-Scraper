import os
import time
from pathlib import Path

os.system("color")

#global variables:
#DownloadPath
#LightNovelName
#ChoosenNovel
#Choice
ChapterLinks=[]
NovelLinks=[]
NovelTitles=[]

#Edit the Data Below to support your custom source

import ReadLightNovelorg

Sources=["https://www.readlightnovel.org/"]

SourcesSearchFunction={
    1:ReadLightNovelorg.Search
    }

SourcesChapterLinksFunction={
    1:ReadLightNovelorg.ChapterRange
}

SourcesDownloadFunction={
    1:ReadLightNovelorg.Download
}

#End of variables needed to be able to edited to support custom sources.

#Function to Choose the source to scrape the light novels from 
def SourceChoosing():
    try:
        for i in Sources:
            print("[",Sources.index(i)+1,"]",i,"\n")
        global Choice
        Choice=int(input("\033[0;32mChoose a source for downloading Light Novel: \033[0;37m"))
    except:
        print("\033[0;31mInvalid Input. Try Again.\033[0;37m")
        time.sleep(2)
        print("\n"*3)
        SourceChoosing()
    else:
        if 0<Choice<=len(Sources):
            SourcesSearchFunction[Choice](LightNovelName)
            SeriesListing()
        else:
            print("\033[0;31mInput outside the range. Try again.\033[0;37m")
            time.sleep(2)
            print("\n"*3)
            SourceChoosing()

#Function that just lists all the light novels found using search string
def SeriesListing():
    if len(NovelTitles)==0:
        print("\033[0;31mThere were no results. Please search again\033[0;37m")
        time.sleep(2)
        print("\n"*3)
        Start()
    else:
        print()
        for i in NovelTitles:
            print("[",NovelTitles.index(i)+1,"]",i,"\n")
        ChoosingLightNovelIndex()

#Function to choose one of the light novels to download after search
def ChoosingLightNovelIndex():
    try:
        ChoiceNovel=int(input("\033[0;32mChoose the index of the Light Novel to download: \033[0;37m"))
    except:
        print("\033[0;31mInvalid Input. Try Again.\033[0;37m")
        time.sleep(2)
        print("\n"*3)    
        SeriesListing()
    else:
        if 0<ChoiceNovel<=len(NovelLinks):
            global ChoosenNovel
            ChoosenNovel=NovelTitles[ChoiceNovel-1]
            SourcesChapterLinksFunction[Choice](NovelLinks[ChoiceNovel-1])
            StartingChaptersIndex()
        else:
            print("\033[0;31mInput outside the range. Try again.\033[0;37m")
            time.sleep(2)
            print("\n"*3)
            SeriesListing()

#Function for choosing the Starting index of the chapter range to download
def StartingChaptersIndex():
    try:
        print("\033[0;32m\nTotal Chapters: \033[0;37m",len(ChapterLinks))
        ChapterStartingIndex=int(input("\033[0;32mEnter Starting index of chapter(s) to download (1 - %s): \033[0;37m" %(len(ChapterLinks))))
    except:
            print("\033[0;31mInvalid Input. Try again.\033[0;37m")
            time.sleep(2)
            print("\n"*3)
            StartingChaptersIndex()
    else:
        if 1<=ChapterStartingIndex<=len(ChapterLinks):
            EndingChaptersIndex(ChapterStartingIndex)
        else:
            print("\033[0;31mInput outside the range. Try again.\033[0;37m")
            time.sleep(2)
            print("\n"*3)
            StartingChaptersIndex()
            
#Function for choosing the Ending index of the chapter range to download
def EndingChaptersIndex(ChapterStartingIndex):
    try:
        ChapterEndingIndex=int(input("\033[0;32mEnter Ending index of chapter(s) to download (%s - %s): \033[0;37m" %(ChapterStartingIndex,len(ChapterLinks))))
    except:
        print("\033[0;31mInvalid Input. Try again.\033[0;37m")
        time.sleep(2)
        print("\n"*3)
        StartingChaptersIndex()
    else:
        if ChapterStartingIndex<=ChapterEndingIndex<=len(ChapterLinks):
            ChoosingSaveLocation(ChapterStartingIndex,ChapterEndingIndex)
        else:
            print("\033[0;31mInput outside the range. Try again.\033[0;37m")
            time.sleep(2)
            print("\n"*3)
            StartingChaptersIndex()

#Function to ask the user for save location of light novels and check the validity of path
def ChoosingSaveLocation(Beginning,Ending):
    try:
        global DownloadPath
        DownloadPath = str(Path.home() / "Downloads")
        ChoiceLocation=str(input('''\033[0;32m\nThe default save location for downloads is \033[0;37m%s\033[0;32m 
Keep in mind that a folder will be created at this location, where the light novel files will be downloaded.
If you wish to continue with this folder, enter \033[0;37mY\033[0;32m, otherwise enter \033[0;37mN\033[0;32m: \033[0;37m''' %DownloadPath))
    except:
            print("\033[0;31mInvalid Input. Try again.\033[0;37m")
            time.sleep(2)
            print("\n"*3) 
            ChoosingSaveLocation(Beginning,Ending) 
    else:
        if ChoiceLocation.lower()=="y":
            if os.path.isdir(DownloadPath)==True:
                DownloadingFunction(Beginning,Ending,DownloadPath)
            else:
                print("\033[0;31mThere were some problems reaching the location of the path. Input another Location.\033[0;37m")
                time.sleep(2)
                print("\n"*3) 
                ChoosingSaveLocation(Beginning,Ending)
        elif ChoiceLocation.lower()=="n":
            DownloadPath=input("\033[0;32m\nEnter the Desired Location for Downloads: \033[0;37m")
            if os.path.isdir(DownloadPath)==True:
                DownloadingFunction(Beginning,Ending,DownloadPath)
            else:
                print("\033[0;31mLocation does not exist or is a file. Input a valid directory.\033[0;37m")
                time.sleep(2)
                print("\n"*3) 
                ChoosingSaveLocation(Beginning,Ending)
        else:
            print("\033[0;31mInvalid Input. Try again.\033[0;37m")
            time.sleep(2)
            print("\n"*3) 
            ChoosingSaveLocation(Beginning,Ending)   

#Function Makes a folder at the download location to store the downloaded light novels and checks for write permissions and finally starts the download 
def DownloadingFunction(Beginning,Ending,Location):
    FinalPath=os.path.join(Location, ChoosenNovel)
    PermError=0
    try:
        os.mkdir(FinalPath)
        print("\033[0;32m\nFolder created with path %s.\033[0;37m\n\n" %FinalPath) 
    except FileExistsError:
        print("\033[0;32m\nFolder Exists at %s.\033[0;37m\n\n" %FinalPath)
        pass
    except PermissionError:
        print("\033[0;31mInsufficient Permissions to make a folder in that location. Please enter a new path\033[0;37m")
        time.sleep(2)
        print("\n"*3)
        PermError=1
        pass
    finally:
        if PermError==1:
            ChoosingSaveLocation(Beginning,Ending)
        else:
            for i in range(Beginning-1,Ending):
                SourcesDownloadFunction[Choice](ChapterLinks[i],FinalPath)
            raise SystemExit("\033[0;32m\nAll Files Downloaded Successfully\033[0;37m")

#Function Starts the Program
def Start():
    global LightNovelName
    LightNovelName=input("\033[0;32mEnter The Name of Light Novel you wish to download: \033[0;37m")
    print()
    SourceChoosing()

Start()
