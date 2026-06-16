import pandas as pd
import os


def save_prediction(
    plant,
    disease,
    confidence,
    prediction_time
):

    file_name = "prediction_history.csv"

    data = {
        "Date": [prediction_time],
        "Plant": [plant],
        "Disease": [disease],
        "Confidence": [round(confidence, 2)]
    }

    new_row = pd.DataFrame(data)

    if os.path.exists(file_name):

        existing = pd.read_csv(file_name)

        updated = pd.concat(
            [existing, new_row],
            ignore_index=True
        )

        updated.to_csv(file_name, index=False)

    else:

        new_row.to_csv(file_name, index=False)