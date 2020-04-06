# InspireHEP API Wrapper

This project provides a simple wrapper around the [Inspire HEP](https://labs.inspirehep.net) API, main endpoints: 
 
 - literature 
 - authors
 - jobs
 - conferences
 
 ### Dependencies
 
Dependencies are minimal and can be installed with 

    pip install -r requirements.txt
    
Its recommended to work in a dedicated virtual environment.

### Usage

The wrapper 
     
    from inspirehep_api_wrapper.service.inspire_api import InspireAPI

    inspire_api = InspireAPI()

provides one method for each endpoint allowing to retrieve a given document
by specifying the unique identifier from Inspire, example:

     response = inspire_api.literature('11883')
     
To retrieve the data    
     
     response.data
     
 Additionally, InspireAPI provide a method to query any of the endpoints
 
    params = {'sort': 'mostrecent', 'size':25, 'page':1}
 
    response = inspireapi.search('literature', query = 'suppersymmetry', params)