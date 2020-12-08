import csv


def make_json(csvfile):
    """ Helper function to read and process CSV data

    Parameters
    ----------
    csvfile
        CSV file containing the data to be posted

    Returns
    -------
    data: dict
        Dictionary with each row of csvfile nested as a dictinary

    """

    data = []
    with open(csvfile, encoding='utf-8') as csvf:
        csvreader = csv.DictReader(csvf)
        for rows in csvreader:
            data.append(rows)

    return data
