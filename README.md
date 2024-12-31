# Bengaluru Home Price Prediction

This project predicts the price of homes in Bengaluru based on various features such as area, number of bathrooms, number of bedrooms (BHK), and location. The model is deployed as a web application using Streamlit.

## Web Application

You can access the live web application [here](https://bengaluruhomepriceprediction.streamlit.app/).

## Features

- Predicts home prices based on input features.
- User-friendly interface built with Streamlit.
- Dropdown menu for selecting locations.
- Easy-to-use input fields for area, number of bathrooms, and BHK.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:

    ```sh
    git clone https://github.com/your-username/bengaluru-home-price-prediction.git
    ```

2. Navigate to the project directory:

    ```sh
    cd bengaluru-home-price-prediction
    ```

3. Create and activate a virtual environment (optional but recommended):

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

4. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

5. Run the Streamlit app:

    ```sh
    streamlit run app.py
    ```

## Usage

1. Open the Streamlit web application.
2. Enter the area in square feet.
3. Select the number of bathrooms.
4. Select the number of bedrooms (BHK).
5. Choose the location from the dropdown menu.
6. Click on the "Predict Price" button to get the predicted home price.

## Files

- `app.py`: The main Streamlit application file.
- `banglore_home_prices_model.pickle`: The trained machine learning model.
- `bengaluru_home_price_prediction_columns_data.pkl`: The data file containing column names and other necessary information.
- `requirements.txt`: The file listing all the dependencies required for this project.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or create a pull request.

## License

This project is licensed under the Apache License 2.0 License. See the [LICENSE](LICENSE) file for details.
