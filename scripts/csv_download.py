import requests
import os
def download():
    url = 'https://data.sfgov.org/api/views/tpp3-epx2/rows.csv?accessType=DOWNLOAD'

    response = requests.get(url)

    with open(os.getenv('DATA_DIR')+'/raw/schools.csv', 'w') as outfile:
        for line in response.text:
            outfile.write(line)
