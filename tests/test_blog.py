import requests


def test_create_blog():
    post_valid_data = {
        "title": "Blog 2",
        "short_description": "Blog description 2",
        "content": "Blog content 2",
        "blogger_full_name": "Blogger 2"
    }
    
    response_valid_data = requests.post("http://35.225.243.133/blogs/", data=post_valid_data)
    
    res_valid_data_json = response_valid_data.json()

    print(response_valid_data)
    
    assert response_valid_data.status_code == 201

    post_invalid_data = {
        "short_description": "Blog description 2",
        "content": "Blog content 2",
        "blogger_full_name": "Blogger 2"
    }
    response_invalid_data = requests.post("http://35.225.243.133/blogs/", data=post_invalid_data)

    assert response_invalid_data.status_code == 400
    res_invalid_json = response_invalid_data.json()
    assert res_invalid_json["title"] == ["This field is required."]





