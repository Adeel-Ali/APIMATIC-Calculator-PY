# Getting Started
## How to Build


You must have Python greater than 2.7 installed in your system to build and run your SDK files. 
The generated code has dependencies over external libraries like nose, jsonpickle, etc. These dependencies are defined in the ```requirements.txt``` file that comes with the SDK. 
To resolve these dependencies, we use the PIP Dependency manager. Install it by following steps at https://pip.pypa.io/en/stable/installing/

The paths of Python and PIP must be properly set in the environment variables. Open command prompt and type ```pip --version```. 
This should display the current version of the PIP Dependency Manager installed if the installation was successful.

* Using command line, navigate to the directory containing the generated files (including ```requirements.txt```) for the SDK. 
Run the command ```pip install -r requirements.txt```. This should install all the required dependencies.

![Building SDK - Step 1](http://apidocs.io/illustration/python?step=installDependencies&workspaceFolder=APIMATIC Calculator-Python)


## How to Use

The following section explains how to use the APIMATICCalculator library in a new project.

#### 1. Open Project in an IDE
Open an IDE for Python like PyCharm. The basic workflow presented here is also applicable if you prefer using a different editor or IDE.

![Open project in PyCharm - Step 1](http://apidocs.io/illustration/python?step=pyCharm)

Click on ```Open``` in PyCharm to browse to your generated SDK directory and then click ```OK```.

![Open project in PyCharm - Step 2](http://apidocs.io/illustration/python?step=openProject0&workspaceFolder=APIMATIC Calculator-Python)     

The project files will be displayed in the side bar as follows:

![Open project in PyCharm - Step 3](http://apidocs.io/illustration/python?step=openProject1&workspaceFolder=APIMATIC Calculator-Python&projectName=apimaticcalculatorlib)     


#### 2. Add a new Test Project
Create a new directory by right clicking on the solution name as shown below:

![Add a new project in PyCharm - Step 1](http://apidocs.io/illustration/python?step=createDirectory&workspaceFolder=APIMATIC Calculator-Python&projectName=apimaticcalculatorlib)

Name the directory as "test"

![Add a new project in PyCharm - Step 2](http://apidocs.io/illustration/python?step=nameDirectory)
   
Add a python file to this project with the name "testsdk"

![Add a new project in PyCharm - Step 3](http://apidocs.io/illustration/python?step=createFile&workspaceFolder=APIMATIC Calculator-Python&projectName=apimaticcalculatorlib)

Name it "testsdk"

![Add a new project in PyCharm - Step 4](http://apidocs.io/illustration/python?step=nameFile)

In your python file you will be required to import the generated python library using the following code lines
   ```Python
   from apimaticcalculatorlib.apimaticcalculator_client import *
   ```
![Add a new project in PyCharm - Step 4](http://apidocs.io/illustration/python?step=projectFiles&workspaceFolder=APIMATIC Calculator-Python&libraryName=apimaticcalculatorlib.apimaticcalculator_client&projectName=apimaticcalculatorlib)

After this you can add code to initialize the client library and acquire the instance of a Controller class. Sample code to initialize the client library and using controller methods is given in the subsequent sections.


#### 3. Run the Test Project
To run the file within your test project, right click on your Python file inside your Test project and click on ```Run```

![Run Test Project - Step 1](http://apidocs.io/illustration/python?step=runProject&workspaceFolder=APIMATIC Calculator-Python&libraryName=apimaticcalculatorlib.apimaticcalculator_client&projectName=apimaticcalculatorlib)


## How to Test

You can test the generated SDK and the server with automatically generated test
cases. unittest is used as the testing framework and nose is used as the test
runner. You can run the tests as follows:

  1. From terminal/cmd navigate to the root directory of the SDK.
  2. Invoke 'nosetests'

## Initialization

#### Initialization

API client can be initialized as following.

```python

client = APIMATICCalculatorClient()
```

# Class Reference
## <a name="list_of_controllers"></a>List of Controllers

* [SimpleCalculatorController](#simple_calculator_controller)

## <a name="simple_calculator_controller"></a>![Class: ](http://apidocs.io/img/class.png ".SimpleCalculatorController") SimpleCalculatorController


#### Get controller instance
An instance of the ``` SimpleCalculatorController ``` class can be accessed from the API Client.
```python
 simple_calculator_client = client.simple_calculator
```

### <a name="get_calculate"></a>![Method: ](http://apidocs.io/img/method.png ".SimpleCalculatorController.get_calculate") get_calculate

> Calculates the expression using the specified operation.

```python
def get_calculate(self,
                      options=dict())
```

#### Parameters: 

| Parameter | Tags | Description |
|-----------|------|-------------|
| operation |  ``` Required ```  | The operator to apply on the variables |
| x |  ``` Required ```  | The LHS value |
| y |  ``` Required ```  | The RHS value |



#### Example Usage:
```python
collect = {}

operation = OperationTypeEnum.SUM
collect['operation'] = operation

x = 5
collect['x'] = x

y = 6
collect['y'] = y


result = simple_calculator_client.get_calculate(collect)

```





[Back to List of Controllers](#list_of_controllers)


