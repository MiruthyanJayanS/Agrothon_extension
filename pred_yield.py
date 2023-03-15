dist_list = ['AHMEDNAGAR', 'AKOLA', 'AMRAVATI', 'AURANGABAD', 'BEED', 'BHANDARA', 'BULDHANA', 'CHANDRAPUR', 'DHULE', 'GADCHIROLI', 'GONDIA', 'HINGOLI', 'JALGAON', 'JALNA', 'KOLHAPUR', 'LATUR', 'NAGPUR', 'NANDED', 'NANDED', 'NASHIK', 'OSMANABAD', 'PARBHANI', 'PUNE', 'SANGLI', 'SATARA', 'SATARA', 'THANE', 'WARDHA', 'WASHIM', 'YAVATMAL']
crop_list = ['Jowar', 'Bajra', 'Wheat']
soil_list = ['chalky', 'clay', 'loamy', 'sandy', 'silty']
def predict_yield(district,Crop,Area,soil_type):
    import requests

    # Define the API endpoint
    url = 'http://localhost:5000/api/yield'

    # Define the request body as a dictionary
    data = {"district":district,"Crop":Crop,"Area":Area,"soil_type":soil_type}

    # Send a POST request to the API endpoint with the request body as JSON
    response = requests.post(url, json=data)

    # Check the response status code
    if response.status_code == 200:
        # Parse the response JSON and extract the result field
        result = response.json()['prediction']
        return result
    else:
        print("Error:", response.text)

print(predict_yield('AHMEDNAGAR','Jowar',51,'loamy'))
