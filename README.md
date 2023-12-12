# qwertypy

My personal utilities library.

## Installation

```bash
pip install qwertypy
```

### Upgrade

```bash
pip install --upgrade qwertypy
```

## Usage

-   Try on colab: [Click here](https://colab.research.google.com/drive/1SK96YfBgIPY-CKNfvQxvBKkJnNA7fSCe?usp=sharing)

### `qwertypy.greetings`

```py
import qwertypy.greetings as qpyGreetings

print(qpyGreetings.hello())
```

### `qwertypy.tickertape`

#### `qwertypy.tickertape.companies`

```py
import qwertypy.tickertape.companies as ttCompanies

topCompanies = ttCompanies.getTopCompanies()
print("TOP = ", len(topCompanies))
# print("ALL = ", len(ttCompanies.getAllCompanies()))

ttName = "reliance-industries-RELI"
companyInfo = ttCompanies.getCompanyInfo(ttName)
print(companyInfo)
```

#### `qwertypy.tickertape.financials`

```py
import qwertypy.tickertape.financials as ttFinancials

ttName = "reliance-industries-RELI"
for statementType in ttFinancials.statementTypes:
    statement = ttFinancials.getStatement(ttName, statementType)
    print(statementType, type(statement))
```

### `qwertypy.data_analysis`

### `qwertypy.data_analysis.regression`

```py
import qwertypy.data_analysis.regression as qpyRegression

xTrain = [1, 2, 3, 4, 5, 6]
yTrain = [2, 4, 6, 8, 10, 12]
model = qpyRegression.QpyLinearRegression(xTrain, yTrain)
model.train()
yPredict = model.getPrediction()
print("yPredict: ", yPredict)

xPredict2 = [10, 11]
yExpected = [20, 22]
yPredict2 = model.getPrediction(xPredict2)
print("yPredict2: ", yPredict2)
```
