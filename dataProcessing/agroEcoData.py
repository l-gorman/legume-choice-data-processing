import pandas as pd

def ExtractProjectAgroEcoData(project):
    '''
    Extracts agro-ecological data from a single legume select project

    Args:
        project (dict): A dictionary style object containing all the information for a single legume CHOICE project

    Returns: 
        dict: A single dictionary object containing key information for project agro-ecological data  
    '''

    projectID =  project["projectID"]
    projectName =  project["rawdata"]["projectInfo"]["projectName"]
    country =  project["rawdata"]["projectInfo"]["country"]
    majorRegion=project["rawdata"]["projectInfo"]["majorRegion"]
    minorRegion=project["rawdata"]["projectInfo"]["minorRegion"]
    communityName=project["rawdata"]["projectInfo"]["communityName"]
    communityType=project["rawdata"]["projectInfo"]["communityType"]
    agroEcoData = project["rawdata"]["agroEcoData"]["biofilters"]

    row={"country":country,"majorRegion":majorRegion,"minorRegion":minorRegion,"communityName":communityName,"communityType":communityType,"projectName":projectName,"projectID":projectID}


    for index in range(0,len(agroEcoData)):
        row[agroEcoData[index]["label"]]=agroEcoData[index]["value"]
    return row
def ExtractAllAgroEcoData(projects):
    agroEcoData=[]
    for project in projects:
        agroEcoData.append(ExtractProjectAgroEcoData(project=project))
    return pd.DataFrame(agroEcoData)