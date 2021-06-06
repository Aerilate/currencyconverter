# :dollar: Currency-Converter :dollar:
Currency converter reads in a CSV file as input and converts prices of a specific column to another currency.
  
  
## Input
The input is a CSV with one column having prices to convert. The first row will be ignored in any calculations.
  
  
## Usage
To see all script options and their descriptions, enter the command:
```bash
python currency_convert --help
```
  
  
### Examples
Specify the multiplier to convert rates at:
```bash
python currency_convert --field 2 --multiplier 1.5
```
This will multiply each price at column 2 by 1.5.
  
  
## Testing
Tests are located in `currency_convert.test.py`. To run tests, enter the command:
```bash
python currency_convert.test.py
```
