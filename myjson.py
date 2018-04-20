import inspect
import requests
import json
import time
from TestSuiteSmokeTestLKA import Config


def activate_customer(customer_email):
    print(inspect.stack()[0][3])
    # url = "http://172.16.104.159:88/api/v1/customer"
    # host = "bapi.preprod.dmz.mtt.ru" # preprod
    # host = "172.16.104.159:88" # prod
    proto = Config().bapi_proto
    host = Config().bapi_host
    basic_b64 = Config().bapi_basic_b64
    url = proto + "://" + host + "/api/v1/customer"
    headers = {'content-type': 'application/json',
               'Authorization': 'Basic ' + basic_b64}
    print(url)
    print(headers)

    payload = {
        "id": "1",
        "jsonrpc": "2.0",
        "method": "activateCustomer",
        "params":
            {
                "customer_login": customer_email
            }
    }
    print(payload)
    response = requests.post(
        url, data=json.dumps(payload), headers=headers).json()
    print(response)
    assert response["result"] == {
        "success": 1
    }
    assert response["jsonrpc"]
    assert response["id"] is '1'


def update_customer_custom_fields(customer_account_number):
    """
    Метод отмечает кастомера тестовым в порте
    :param customer_account_number: лицевой счет кастомера
    :return:
    """
    print(inspect.stack()[0][3])
    url = Config().capi_host
    basic_b64 = Config().capi_basic_b64
    capi_customer_account_prefix = Config().capi_customer_account_prefix
    headers = {'Authorization': 'Basic ' + basic_b64}
    customer_account_number = capi_customer_account_prefix + customer_account_number
    print(headers)

    payload = {
            "jsonrpc": "2.0",
            "method": "updateCustomerCustomFields",
            "id": "1",
            "params": {
                "customer_name": customer_account_number,
                "custom_fields": {
                    "account_type": "test"
                }
            }
    }
    print(payload)
    response = requests.post(
        url, data=json.dumps(payload), headers=headers).json()
    print(response)
    assert response["result"] == {
        "success": 1
    }
    assert response["jsonrpc"]
    assert response["id"] is '1'


def sms_check_code(number_to_get_sms_check_code):
    """
    Метод возвращает чек код, который отправляется в виде смс на указанный при регистрации номер
    :param number_to_get_sms_check_code:
    :return:
    """
    time.sleep(5)
    print(inspect.stack()[0][3])
    time.sleep(5)
    url = Config().capi_host
    basic_b64 = Config().capi_basic_b64_for_sms_check_code
    headers = {'Authorization': 'Basic ' + basic_b64,
               'Content-Type': 'application/json'}
    print(headers)

    """ Проверка: если номер указан без семерки вначале (условие для введения номера в интерфейсе портала)
    то добавить семерку """
    if len(number_to_get_sms_check_code) is 10:
        customer_account_number = "7" + number_to_get_sms_check_code
    elif len(number_to_get_sms_check_code) is 11:
        customer_account_number = number_to_get_sms_check_code
    else:
        print(UserWarning)
        customer_account_number = number_to_get_sms_check_code

    payload = {
        "id": "1",
        "jsonrpc": "2.0",
        "method": "unitTestGetData",
        "params": {
            "what": "check_code_code",
            "params": customer_account_number
        }
    }
    print(payload)
    response = requests.post(
        url, data=json.dumps(payload), headers=headers).json()
    print(response)
    assert response["jsonrpc"]
    assert response["id"] is '1'
    return response["result"]["check_code_code"]

def delete_customer(pzv_customer_login_email):
        print(inspect.stack()[0][3])
        # url = "http://172.16.104.159:88/api/v1/customer"
        # host = "bapi.preprod.dmz.mtt.ru" # preprod
        # host = "172.16.104.159:88" # prod
        proto = Config().bapi_proto
        host = Config().bapi_host
        basic_b64 = Config().bapi_basic_b64
        url = proto + "://" + host + "/api/v1/customer"
        headers = {'content-type': 'application/json',
                   'Authorization': 'Basic ' + basic_b64}
        print(url)
        print(headers)

        payload = {
            "id": "1",
            "jsonrpc": "2.0",
            "method": "makeContractTermination",
            "params":
                {
                    "customer_login": pzv_customer_login_email
                }
        }
        print(payload)
        response = requests.post(
            url, data=json.dumps(payload), headers=headers).json()
        print(response)
        assert response["result"] == {
            "success": 1
        }
        assert response["jsonrpc"]
        assert response["id"] is '1'