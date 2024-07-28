# Machine-Learning-API-using-FastAPI-with-Sepsis-Data



### Overview
This analysis embarks on the exploration of a dataset containing essential medical and demographic information of patients in an Intensive Care Unit (ICU). The primary objective is to leverage this dataset to develop a predictive model that can effectively identify individuals at risk of developing sepsis during their ICU stay. By doing so, healthcare professionals can receive early warnings, allowing them to initiate timely interventions and potentially save lives






### Background
In the healthcare industry the early detection and management of critical medical conditions can significantly impact patient outcomes and improve the quality of care. One such life-threatening condition is sepsis, which is the body's extreme response to an infection. Sepsis happens when an infection you arleady have triggers a chain reaction throughout the body. Prompt identification and intervention in cases of sepsis are pivotal in preventing its progression and reducing mortality rates. This analysis embarks on the exploration of a dataset containing essential medical and demographic information of patients in an Intensive Care Unit (ICU). The primary objective is to leverage this dataset to develop a predictive model that can effectively identify individuals at risk of developing sepsis during their ICU stay. By doing so, healthcare professionals can receive early warnings, allowing them to initiate timely interventions and potentially save lives


### Project Ojectives
- Perform hypothesis testing to reject or fail to reject the null hypothesis
- Develop and train a build a model that more accurately predicts the unit sales for thousands of items sold at different Favorita stores.
- Evaluate the model's performance using appropriate metrics.
- Fine-tune the model parameters to optimize performance.
- To simplofy deployment and usage, including a Dockerfile that streamlines the setup process and ensures the necessary dependencies are installed.




### Data Dictionary
<table>
  <tr>
    <th>Column Name</th>
    <th>Attribute/Target</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>ID</td>
    <td>N/A</td>
    <td>Unique number to represent patient ID</td>
  </tr>
  <tr>
    <td>PRG</td>
    <td>Attribute1</td>
    <td>Plasma glucose</td>
  </tr>
  <tr>
    <td>PL</td>
    <td>Attribute 2</td>
    <td>Blood Work Result-1 (mu U/ml)</td>
  </tr>
  <tr>
    <td>PR</td>
    <td>Attribute 3</td>
    <td>Blood Pressure (mm Hg)</td>
  </tr>
  <tr>
    <td>SK</td>
    <td>Attribute 4</td>
    <td>Blood Work Result-2 (mm)</td>
  </tr>
  <tr>
    <td>TS</td>
    <td>Attribute 5</td>
    <td>Blood Work Result-3 (mu U/ml)</td>
  </tr>
  <tr>
    <td>M11</td>
    <td>Attribute 6</td>
    <td>Body mass index (weight in kg/(height in m)^2)</td>
  </tr>
  <tr>
    <td>BD2</td>
    <td>Attribute 7</td>
    <td>Blood Work Result-4 (mu U/ml)</td>
  </tr>
  <tr>
    <td>Age</td>
    <td>Attribute 8</td>
    <td>Patients age (years)</td>
  </tr>
  <tr>
    <td>Insurance</td>
    <td>N/A</td>
    <td>If a patient holds a valid insurance card</td>
  </tr>
  <tr>
    <td>Sepssis</td>
    <td>Target</td>
    <td>Positive: if a patient in ICU will develop sepsis, and Negative: otherwise</td>
  </tr>
</table>


### Deliverables 
1. A jupyter notebook for training a classification model
2. A classification Model
3. An API App built with FastApi
4. A Streamlit app that make calls to the build and hosted API
5. A Dockerfile for easy deployment 



### Installation 
Clone the repository to your local machine:


        git clone https://github.com/FloJoLaryea/Machine-Learning-API-using-FastAPI-with-Sepsis-Data

Navigate to the project directory:

        cd Machine-Learning-API-using-FastAPI-with-Sepsis-Data
Create a new virtual environment and activate the virtual:

- Windows:

        python -m venv venv; venv\Scripts\activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt  

- Linux & MacOs:

        python3 -m venv venv; source venv/bin/activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt

*API*

To execute the API, follow these steps:
After all requirement have been install

At the root of your repository in your terminal
`root :: Machine-Learning-API-using-FastAPI-with-Sepsis-Data> ...`
run the command:


            uvicorn api:app --reload 

OR

            python api/api.py




*Streamlit App*

To execute the App, follow these steps:
After all requirement have been install

At the root of your repository in your terminal
`root :: Machine-Learning-API-using-FastAPI-with-Sepsis-Data> ...`
run the command:


            streamlit run main.py



<img src="https://github.com/FloJoLaryea/Machine-Learning-API-using-FastAPI-with-Sepsis-Data/blob/main/gif.gif?raw=true" width="600" height="400" />


*API Endpoints* 

1. **/**: This Endpoint display a welcome message-” Welcome to the Sepsis API...”.
2. **/Get Status**: Checks status of the API
3. **/predict_sepsis/random_forest_classifier**: Recieve inputs and returns a single prediction using random forest model.
4. **/predict_sepsis/gradient_boost**: Recieve inputs and returns a single prediction using gradient boost model


## Running The Docker Images from Dockerhub

To run the Docker images on your local machine, follow these steps.

### Prerequisites

In order to run this project, you need:

- Python installed on your machine

### Steps

1. **Install Docker**

   If you haven't already installed Docker, you can download and install it from the [official Docker website](https://www.docker.com/get-started). Follow the installation instructions specific to your operating system.

2. **Pull the Docker Images**

   Open your terminal or command prompt and pull the required Docker images from Dockerhub using the following commands:

   ``` sh
   docker pull flojo24/sepsis-predict-api:v1.0     
   docker pull flojo24/sepsis-predict-client:v1.0 
   ```

  ``` sh
   docker run -d --name mycontainer -p 8000:8000 flojo24/sepsis-predict-api:v1.0
   docker run -d --name mycontainer -p 8000:8000 flojo24/sepsis-predict-client:v1.0
   ```


## Authors
- Florence Josephina Laryea
- florencelaryea@gmail.com

- [Link to my article on Medium](https://medium.com/@florencelaryea88/sepsis-prediction-with-fastapi-e088c8934d78)





## Acknowledgements

Much of our sincere gratitude goes to our instructors Racheal Appiah-Kubi for unwavering support, and invaluable mentorship throughout the course of this project.

Her expertise, dedication, and commitment to our learning journey have been instrumental in shaping our understanding and skills in data analysis
