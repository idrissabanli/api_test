import requests


def test_create_blog():
    post_valid_data = {
        "title": "Blog 25",
        "short_description": "Blog description 2",
        "content": "Blog content 2",
        "blogger_full_name": "Blogger 2"
    }
    
    response_valid_data = requests.post("http://35.225.243.133/blogs/", data=post_valid_data)
    
    res_valid_data_json = response_valid_data.json()

    print('created blog', res_valid_data_json)
    create_blog_id = res_valid_data_json['id']
    
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

    # response_get = requests.get('http://35.225.243.133/blogs/')

    # # print('get request response data', )
    # blogs = response_get.json() # ['blog1', 'blog 2', 'blog 3']

    # for blog in blogs:
    #     print('blog === ', blog )

    blog_get = requests.get(f'http://35.225.243.133/blogs/{create_blog_id}')
    blog_data = blog_get.json()
    # print('blog =', blog_get.json())

    assert blog_get.status_code == 200
    assert blog_data['title'] == post_valid_data['title'] and blog_data['short_description'] == post_valid_data['short_description'] and blog_data['content'] == post_valid_data['content'] and blog_data['blogger_full_name'] == post_valid_data['blogger_full_name']

    put_blog_data = {
        "title": "Blog 30",
        "short_description": "Blog description 30",
        "content": "Blog content 30",
        "blogger_full_name": "Blogger 30"
    }
    changed_blog = requests.put(f'http://35.225.243.133/blogs/{create_blog_id}/', data=put_blog_data)
    changed_blog_data = changed_blog.json()
    assert changed_blog.status_code == 200
    assert changed_blog_data['title'] == put_blog_data['title']

    patch_blog_data = {
        "title": "Blog 51",
    }
    changed_blog = requests.patch(f'http://35.225.243.133/blogs/{create_blog_id}/', data=patch_blog_data)
    changed_blog_data = changed_blog.json()
    assert changed_blog.status_code == 200
    assert changed_blog_data['title'] == patch_blog_data['title']

    blog_delete = requests.delete(f'http://35.225.243.133/blogs/{create_blog_id}/')

    assert blog_delete.status_code == 204





# test_create_blog()


