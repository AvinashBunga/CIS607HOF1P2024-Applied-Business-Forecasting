install.packages("readxl")
library(readxl)

# Load the necessary library
library(readxl)

# Load the dataset
file_path <- "/Users/avinash/Desktop/CIS/CIS607/Unit2/Assignment/py/USA_AppleData_TimeDifferences.xlsx"
usa_data <- read_excel(file_path)

# View the first few rows of the dataset to confirm it's loaded correctly
head(usa_data)

# Perform a one-sample t-test
# Hypothesized mean (e.g., 365 days for annual release)
hypothesized_mean <- 365
t_test_result <- t.test(usa_data$`Time Between Releases (days)`, mu = hypothesized_mean)

# Print the t-test results
print(t_test_result)
