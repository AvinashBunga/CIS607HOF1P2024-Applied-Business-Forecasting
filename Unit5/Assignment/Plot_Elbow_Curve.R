# Load necessary libraries
library(readr)  # For reading CSV files

# Load the scaled training data
train_data_path <- "/Users/avinash/Desktop/CIS/CIS607/Unit5/Assignment/USDINRX_Train_Scaled.csv"
train_data <- read_csv(train_data_path)

# Display the first few rows of the data to check if it's loaded correctly
head(train_data)


# Set seed for reproducibility
set.seed(42)

# Initialize a vector to store WCSS (Within-Cluster Sum of Squares)
wcss <- vector()

# Calculate WCSS for 1 to 10 clusters
for (i in 1:10) {
  kmeans_model <- kmeans(train_data[, c("Open", "High", "Low", "Close")], centers = i, nstart = 25)
  wcss[i] <- kmeans_model$tot.withinss
}

# Plot the Elbow curve
plot(1:10, wcss, type = "b", pch = 19, frame = FALSE,
     xlab = "Number of Clusters", ylab = "WCSS (Within-Cluster Sum of Squares)",
     main = "Elbow Method for Optimal Clusters")
