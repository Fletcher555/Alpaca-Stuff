# Simple error handling script that will be used repeatedly throughout the coding to ensure that inputs have correct
# form to pass back


class TestInputs:
    # This code will have many different variables with different datatypes which will all be passed into the same
    # function which will check if they fit
    # To use this class import it and then go like this testinputs = testInputs(inputType) and then
    # testinputs.test(input) where the inputType is type such as 'stock' or 'datetime' or other and input is the var
    # Format for this is as such stock.FILENAME so for 'Create any chart with SQL' it would be
    # stock.createAnyChartWithSQL
    createAnyChartWithSQLStock = ['GME', 'TSLA', 'CCJ', 'SPY', 'AAPL', 'MSFT', 'FB', 'NVDA', 'GOOG', 'BB', 'AMC',
                                  'PLTR', 'DASH', 'MMM', 'DIS', 'KO', '1']
    createAnyChartWithSQLDataDensity = ['5min', '15min', '45min', '1h', '1day', '5day', 'Custom', '1']

    success = False

    def tester(self, inputPassed, inputArray):
        for x in inputArray:
            if inputPassed == x:
                self.success = True

        if not self.success:
            return False
        else:
            return True
