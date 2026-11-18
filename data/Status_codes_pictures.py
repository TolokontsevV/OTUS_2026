import requests


STATUS_CODE = [
    (200, requests.codes.ok),  # OK
    (300, requests.codes.multiple_choices),  # Multiple Choices
    (400, requests.codes.bad_request),  # Bad Request
    (418, requests.codes.im_a_teapot),  # im a teapot
    (404, requests.codes.not_found),  # Not Found
    (500, requests.codes.internal_server_error),  # Internal Server Error
    (511, requests.codes.network_authentication)  # Network Authentication Required
]

pictures = [
    ('https://images.dog.ceo/breeds/affenpinscher/n02110627_12077.jpg'),
    ('https://images.dog.ceo/breeds/affenpinscher/n02110627_6869.jpg'),
    ('https://images.dog.ceo/breeds/affenpinscher/n02110627_12556.jpg'),
    ('https://images.dog.ceo/breeds/affenpinscher/n02110627_8071.jpg')
]

user_id = [
    (1),
    (2),
    (3),
    (4)
]

brewery_id = [
    ("ae7b3174-8be8-4d53-a3a5-9b8240970eea"),
    ("aa7cbe9b-3a0f-4888-9884-6186b0042b55"),
    ("1034754f-abf9-4b42-bd6d-37e110ba4b1a"),
    ("907826b3-6902-4d28-a5e2-f73084bebeed"),
    ("5128df48-79fc-4f0f-8b52-d06be54d0cec")
]

filtered_params =[
    ('by_city'),
    ('by_country'),
    ('by_dist'),
    ('by_ids'),
    ('by_name'),
    ('by_state'),
    ('by_postal'),
    ('by_type')
]

search = [
    ('6198876453'),
    ('micro'),
    ('planning'),
    ('8589995728'),
    ('California')
]