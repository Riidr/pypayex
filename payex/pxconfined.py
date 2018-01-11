from suds.client import Client

from payex.config import PRODUCTION_URL, STAGING_URL
from payex.handlers import BaseHandler


class PxConfidentHandler(BaseHandler):
    """
    Base handler for PxAgreement methods.
    """

    def __call__(self, *args, **kwargs):

        # Set the parameters on object
        for key, value in kwargs.iteritems():
            setattr(self, key, value)

        # Which WDSL URL to use
        if self._service.production:

            self._wdsl_url = PRODUCTION_URL + 'pxconfined/pxorder.asmx?WSDL'
        else:
            self._wdsl_url = STAGING_URL + 'PxConfined/Pxorder.asmx?WSDL'

        # Initialize the client with the WDSL schema
        self._client = Client(self._wdsl_url)


###################
# METHOD HANDLERS #
###################

class PxPreparePurchaseCC3Handler(PxConfidentHandler):
    """
    Reference:
    http://www.payexpim.com/technical-reference/pxconfined/preparepurchasecc/
    """

    field_order = [
        'accountNumber',
        'orderRef',
        'cardNumber',
        'cardNumberExpireMonth',
        'cardNumberExpireYear',
        'cardNumberCVC',
        'cardHolderName',
    ]

    def __call__(self, *args, **kwargs):
        super(PxPreparePurchaseCC3Handler, self).__call__(*args, **kwargs)

        # Set endpoint and send request
        self._endpoint = self._client.service.PreparePurchaseCC

        return self._send_request()


class PxPurchaseCC3Handler(PxConfidentHandler):
    """
    Reference:
    http://www.payexpim.com/technical-reference/pxconfined/preparepurchasecc/
    """

    field_order = [
        'accountNumber',
        'orderRef',
        'transactionType',
        'cardNumber',
        'cardNumberExpireMonth',
        'cardNumberExpireYear',
        'cardNumberCVC',
        'cardHolderName',
    ]

    def __call__(self, *args, **kwargs):
        super(PxPurchaseCC3Handler, self).__call__(*args, **kwargs)

        # Set endpoint and send request
        self._endpoint = self._client.service.PurchaseCC

        return self._send_request()