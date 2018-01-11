from suds.client import Client

from payex.config import PRODUCTION_URL, STAGING_URL
from payex.handlers import BaseHandler


class PxOrderHandler(BaseHandler):
    """
    Base handler for PxOrder methods.
    """

    def __call__(self, *args, **kwargs):

        # Set the parameters on object
        for key, value in kwargs.iteritems():
            setattr(self, key, value)

        # Which WDSL URL to use
        if self._service.production:
            self._wdsl_url = PRODUCTION_URL + 'pxorder/pxorder.asmx?WSDL'
        else:
            self._wdsl_url = STAGING_URL + 'pxorder/pxorder.asmx?WSDL'
        # Initialize the client with the WDSL schema
        self._client = Client(self._wdsl_url)


###################
# METHOD HANDLERS #
###################

class PxOrderInitialize8Handler(PxOrderHandler):
    """
    Reference:
    http://www.payexpim.com/technical-reference/pxorder/initialize8/
    """

    field_order = [
        'accountNumber',
        'purchaseOperation',
        'price',
        'priceArgList',
        'currency',
        'vat',
        'orderID',
        'productNumber',
        'description',
        'clientIPAddress',
        'clientIdentifier',
        'additionalValues',
        'externalID',
        'returnUrl',
        'view',
        'agreementRef',
        'cancelUrl',
        'clientLanguage',
    ]

    def __call__(self, *args, **kwargs):
        super(PxOrderInitialize8Handler, self).__call__(*args, **kwargs)

        # Set endpoint and send request
        self._endpoint = self._client.service.Initialize8

        return self._send_request()


class PxOrderAddSingleOrderLine2(PxOrderHandler):
    """
    Reference:
    http://www.payexpim.com/technical-reference/pxorder/addsingleorderline2/
    """

    field_order = [
        'accountNumber',
        'orderRef',
        'itemNumber',
        'itemDescription1',
        'itemDescription2',
        'itemDescription3',
        'itemDescription4',
        'itemDescription5',
        'quantity',
        'amount',
        'vatPrice',
        'vatPercent'
    ]

    def __call__(self, *args, **kwargs):
        super(PxOrderAddSingleOrderLine2, self).__call__(*args, **kwargs)

        # Set endpoint and send request
        self._endpoint = self._client.service.AddSingleOrderLine2

        return self._send_request()


class PxOrderCompleteHandler(PxOrderHandler):
    """
    Reference:
    http://www.payexpim.com/technical-reference/pxorder/complete-2/
    """

    field_order = [
        'accountNumber',
        'orderRef',
    ]

    def __call__(self, *args, **kwargs):
        super(PxOrderCompleteHandler, self).__call__(*args, **kwargs)

        # Set endpoint and send request
        self._endpoint = self._client.service.Complete

        return self._send_request()


class PxOrderCheck2Handler(PxOrderHandler):
    field_order = [
        'accountNumber',
        'transactionNumber',
    ]

    def __call__(self, *args, **kwargs):
        super(PxOrderCompleteHandler, self).__call__(*args, **kwargs)

        # Set endpoint and send request
        self._endpoint = self._client.service.Check2

        return self._send_request()

class PxOrderCapture5Handler(PxOrderHandler):
    """
    Reference:
    http://www.payexpim.com/technical-reference/pxorder/capture5/
    """

    field_order = [
        'accountNumber',
        'transactionNumber',
        'amount',
        'orderId',
        'vatAmount',
        'additionalValues',
    ]

    def __call__(self, *args, **kwargs):
        super(PxOrderCapture5Handler, self).__call__(*args, **kwargs)

        # Set endpoint and send request
        self._endpoint = self._client.service.Capture5

        return self._send_request()


class PxOrderGetTransactionDetails2Handler(PxOrderHandler):
    """
    Reference:
    http://www.payexpim.com/technical-reference/pxorder/gettransactiondetails2/
    """

    field_order = [
        'accountNumber',
        'transactionNumber'
    ]

    def __call__(self, *args, **kwargs):
        super(PxOrderGetTransactionDetails2Handler, self).__call__(*args, **kwargs)

        # Set endpoint and send request
        self._endpoint = self._client.service.GetTransactionDetails2

        return self._send_request()


class PxCancel2Handler(PxOrderHandler):
    """
    Reference:
    http://www.payexpim.com/technical-reference/pxorder/cancel2/
    """

    field_order = [
        'accountNumber',
        'transactionNumber'
    ]

    def __call__(self, *args, **kwargs):
        super(PxCancel2Handler, self).__call__(*args, **kwargs)

        # Set endpoint and send request
        self._endpoint = self._client.service.Cancel2

        return self._send_request()
