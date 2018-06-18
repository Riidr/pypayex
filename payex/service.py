from payex.pxagreement import (
        PxCreateAgreement3Handler, PxAutoPay2Handler, PxAutoPay3Handler, PxDeleteAgreementHandler,
        PxAgreementCheckHandler
        )
from payex.pxorder import (
    PxOrderInitialize8Handler, PxOrderCompleteHandler, PxOrderCapture5Handler,
    PxOrderGetTransactionDetails2Handler, PxCancel2Handler, PxOrderCheck2Handler,
    PxOrderAddSingleOrderLine2, PxOrderCredit5Handler)

class Payex(object):
    """
    Base Payex service, with handlers.
    """
    
    def __init__(self, merchant_number, encryption_key, production=False, force_url=None):
        
        # Set account credentials
        self.accountNumber = merchant_number
        self.encryption_key = encryption_key
        self.production = production
        self.force_url = force_url

        # Add agreement handlers
        self.add_resource('create_agreement', PxCreateAgreement3Handler)
        self.add_resource('delete_agreement', PxDeleteAgreementHandler)
        self.add_resource('check_agreement', PxAgreementCheckHandler)
        self.add_resource('autopay', PxAutoPay2Handler)
        self.add_resource('autopay3', PxAutoPay3Handler)

        
        # Add order handlers
        self.add_resource('initialize', PxOrderInitialize8Handler)
        self.add_resource('complete', PxOrderCompleteHandler)
        self.add_resource('capture', PxOrderCapture5Handler)
        self.add_resource('credit', PxOrderCredit5Handler)
        self.add_resource('cancel', PxCancel2Handler)
        self.add_resource('get_transaction_details', PxOrderGetTransactionDetails2Handler)
        self.add_resource('check', PxOrderCheck2Handler)
        self.add_resource('order_line', PxOrderAddSingleOrderLine2)

    def add_resource(self, name, handler):
        """
        Initializes the handler with this service instance.
        """
        
        setattr(self, name, handler(self))
