import json


def json_deserialize(data, expect_type=None):
    """
       :param data: data to deserialize
       :param expect_type:
       :return: deserialized data is returned as a python dictionary
       """
    try:
        data = json.loads(data)
    except (TypeError, json.decoder.JSONDecodeError):
        pass

    if expect_type is not None and not isinstance(data, expect_type):
        raise ValueError(f"Got {type(data)} but expected {expect_type}.")

    return data
