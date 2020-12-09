# Example 1: POST request

Let's try to add the first two books from our mock data. Copy-paste the following data it into Postman workspace for making requests.

[{"title": "Animal Farm", "author": "George Orwell", "publisher": "Signet", "published_year": "1996"},
 {"title": "Physics & Philosophy", "author": "Werner Hesinberg", "publisher": "Penguin", "published_year": "2007"}]

Make a POST request on the API server. (Make sure you have input data format selected as raw/JSON in the Body, you can also select Beautify to make it look pretty)

Since our data conforms to type and there are no missing values in any field, this results in success. We can verify this by making GET request as /books/id (id = 1, 2). You can also explicitly check these entries have appeared into the database file.

# Example 2: POST request

Let's try to add the third book now

[{"title": "Catch-22", "author": "Joseph Heller", "publisher": "Random House", "published_year": "XYZ"}]

Make a POST request. We get an output like this:

{
    "0": {
        "error": {
            "published_year": [
                "Not a valid integer."
            ]
        },
        "status code": 400
    }
}

The POST request results in failure. This is because in the published_year field, we have XYZ, which is not a valid year.

# Example 3: POST request 

Let's try to add the fourth book now

[{"title": "The Code Book", "author": "Simon Singh", "publisher": "", "published_year": "2002"}]

Make a POST request. We get an output like this:

{
    "0": {
        "error": {
            "publisher": [
                "Field should not be empty."
            ]
        },
        "status code": 400
    }
}

Once again, this request results in an error. Our API doesn't like it when we leave a field empty! 

# Example 4: POST request 

Let's try to add the last book now

[{"title": "Unfinished", "author": "Prateek Goel", "publisher": "", "published_year": "2030"}]

Make a POST request. We get an output like this:

{
    "0": {
        "error": {
            "publisher": [
				"Futuristic books are not yet allowed."
            ]
        },
        "status code": 400
    }
}

It again results in an error. Our API doesn't like that we are trying to add books to the database which will (supposedly) be published in future. That's fair! 
