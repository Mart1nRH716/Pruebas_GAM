from prophet import Prophet
import pandas as pd
# Inicializamos el modelo Prophet
m = Prophet()
df_train = pd.read_csv('train.csv')

# Añadimos regresores al modelo
m.add_regressor('temperature')
m.add_regressor('rainfall')
m.add_regressor('sunshine_fraction')
m.add_regressor('wind_speed')

# You might also want to add seasonality, holidays, etc., depending on your data
# m.add_seasonality(name='daily', period=1, fourier_order=5) # Example for daily seasonality


m.fit(df_train)

# Create a DataFrame for future predictions, including future weather data
future = m.make_future_dataframe(periods=days_to_predict)
# Add your future temperature, rainfall, sunshine_fraction, wind_speed to 'future' DataFrame
# Example: future['temperature'] = ...
# Example: future['rainfall'] = ...

forecast = m.predict(future)