# Set up cross-validation settings
train_control <- trainControl(method = "cv", number = 10)  # 10-fold cross-validation

# Train the model using cross-validation with corrected column names
cv_model <- train(y_train ~ duration + days_left + airline_AirAsia + airline_Indigo + 
                    airline_GO_FIRST + source_city_Bangalore + source_city_Chennai + 
                    source_city_Delhi + source_city_Hyderabad + source_city_Kolkata + 
                    departure_time_Afternoon + departure_time_Early_Morning + 
                    departure_time_Evening + stops_one + stops_two_or_more + 
                    arrival_time_Afternoon + arrival_time_Early_Morning + 
                    arrival_time_Late_Night + arrival_time_Morning + 
                    destination_city_Bangalore + destination_city_Delhi + 
                    destination_city_Hyderabad + destination_city_Kolkata + 
                    class_Business, 
                  data = X_train, method = "lm", trControl = train_control)

# Print cross-validation results
print(cv_model)
