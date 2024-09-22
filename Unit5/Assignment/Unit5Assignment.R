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



# Step 3: Apply K-means clustering with the chosen number of clusters (e.g., 3 clusters)
optimal_clusters <- 3  # Based on the Elbow plot

# Apply K-means clustering
kmeans_model <- kmeans(train_data[, c("Open", "High", "Low", "Close")], centers = optimal_clusters, nstart = 25)

# Add the cluster assignments to the training data
train_data$Cluster <- as.factor(kmeans_model$cluster)

# Display the cluster centroids
print("Cluster Centroids:")
print(kmeans_model$centers)


# Load ggplot2 for visualization
library(ggplot2)

# Scatter plot of Open vs. Close, colored by cluster
ggplot(train_data, aes(x = Open, y = Close, color = Cluster)) +
  geom_point() +
  labs(title = "K-means Clustering of Scaled Training Data", x = "Open", y = "Close") +
   theme_minimal()



# Load necessary libraries
library(readr)

# Step 1: Load the scaled testing data
test_data_path <- "/Users/avinash/Desktop/CIS/CIS607/Unit5/Assignment/USDINRX_Test_Scaled.csv"
test_data <- read_csv(test_data_path)

# Display the first few rows of the testing data
head(test_data)

# Step 2: Extract only the relevant columns for prediction
X_test <- test_data[, c("Open", "High", "Low", "Close")]

# Step 3: Use the K-means centroids to predict the nearest cluster for each test data point
# Define a function to calculate the nearest cluster based on centroids
predict_cluster <- function(new_data, centroids) {
  apply(new_data, 1, function(row) {
    distances <- apply(centroids, 1, function(centroid) {
      sum((row - centroid)^2)
    })
    return(which.min(distances))
  })
}

# Apply the function to predict clusters for the test data
test_data$Predicted_Cluster <- as.factor(predict_cluster(as.matrix(X_test), kmeans_model$centers))

# Display the first few rows of the test data with the predicted clusters
print("Testing Data with Predicted Clusters:")
print(head(test_data))

# Optional: Visualize the predicted clusters on the test data
library(ggplot2)
ggplot(test_data, aes(x = Open, y = Close, color = Predicted_Cluster)) +
  geom_point() +
  labs(title = "Predicted Clusters for Testing Data", x = "Open", y = "Close") +
  theme_minimal()

