# Surpress warnings:
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn

Module 1: Importing Data Sets
Download the dataset by running the cell below.

from pyodide.http import pyfetch

async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())

filepath='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/FinalModule_Coursera/data/kc_house_data_NaN.csv'

await download(filepath, "housing.csv")
file_name="housing.csv"

Load the csv:
df = pd.read_csv(file_name)

We use the method head to display the first 5 columns of the dataframe.

df.head()

