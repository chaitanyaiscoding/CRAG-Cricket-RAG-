#we making the sample data into a paricular format of Content and Metadata

import pandas as pd
import os

RAW_DATA_PATH = os.path.join("data", "raw", "ipl_sample.csv")


def load_raw_data():
    df = pd.read_csv(RAW_DATA_PATH)
    return df


def convert_to_documents(df):
    documents = []

    for _, row in df.iterrows():
        doc = {
            "content": row["summary"],
            "metadata": {
                "match": row["match"],
                "tournament": row["tournament"],
                "year": int(row["year"]),
                "stage": row["stage"]
            }
        }
        documents.append(doc)

    return documents
