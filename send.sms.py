import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint


def main():
    configuration = sib_api_v3_sdk.Configuration()
    # Clé API fourni unique
    configuration.api_key['api-key'] = 'YOUR API KEY'

    api_instance = sib_api_v3_sdk.TransactionalSMSApi(sib_api_v3_sdk.ApiClient(configuration))
    send_transac_sms = sib_api_v3_sdk.SendTransacSms(
        sender="string", recipient="string", content="string",
        type="string", web_url="https://snowlab.fr/notifyUrl"
    )

    try:
        api_response = api_instance.send_transac_sms(send_transac_sms)
        pprint(api_response)
    except ApiException as e:
        print(f"Exception when calling TransactionalSMSApi->send_transac_sms: {e}\n")

if __name__ == '__main__':
    main()