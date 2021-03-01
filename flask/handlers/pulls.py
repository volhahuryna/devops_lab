import requests


URL = 'https://api.github.com/repos/alenaPy/devops_lab/pulls'
USERNAME = 'xxx'
PASSWORD = 'xxx'


def get_response(api_state):
    parameter = {
        'per_page': 100,
        'state': api_state
    }
    response = requests.get(URL, auth=(USERNAME, PASSWORD), params=parameter).json()
    return response


def get_outputs(state):
    outputs = []
    if state == "accepted" or state == "needs work":
        response = get_response("all")
        for item in response:
            if item["labels"]:
                if item["labels"][0]["name"] == state:
                    output = {
                        "link": item["html_url"],
                        "num": item["number"],
                        "title": item["title"]
                    }
                    outputs.append(output)
    else:
        response = get_response(state)
        for item in response:
            output = {
                "link": item["html_url"],
                "num": item["number"],
                "title": item["title"]
            }
            outputs.append(output)

    return outputs


def get_pulls(state):
    final_output = get_outputs(state)
    return final_output
