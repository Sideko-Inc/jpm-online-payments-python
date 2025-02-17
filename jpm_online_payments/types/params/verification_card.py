import typing
import typing_extensions
import pydantic

from .authentication import Authentication, _SerializerAuthentication
from .card_type_indicators import CardTypeIndicators, _SerializerCardTypeIndicators
from .expiry import Expiry, _SerializerExpiry
from .network_response import NetworkResponse, _SerializerNetworkResponse
from .payment_token import PaymentToken, _SerializerPaymentToken
from .payment_authentication_request import (
    PaymentAuthenticationRequest,
    _SerializerPaymentAuthenticationRequest,
)


class VerificationCard(typing_extensions.TypedDict):
    """
    Card payment instrument for card verification
    """

    account_number: typing_extensions.NotRequired[str]
    """
    The card or token number.
    """

    account_number_type: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "DEVICE_TOKEN",
            "NETWORK_TOKEN",
            "PAN",
            "SAFETECH_PAGE_ENCRYPTION",
            "SAFETECH_TOKEN",
        ]
    ]
    """
    Specifies the type of payment method used by the account number in payment transaction.
    """

    authentication: typing_extensions.NotRequired[Authentication]
    """
    The authentication object allows you to opt in to additional security features like 3-D Secure
    """

    card_type: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "AP",
            "AX",
            "CC",
            "CR",
            "CZ",
            "DC",
            "DI",
            "EP",
            "IM",
            "JC",
            "MC",
            "MR",
            "NP",
            "PP",
            "SP",
            "VI",
            "VR",
        ]
    ]
    """
    Abbreviation of card name
    """

    card_type_indicators: typing_extensions.NotRequired[CardTypeIndicators]
    """
    The card type indicators provide additional information about the card. For example, if the card is a prepaid card and thus less likely to         support recurring payments or if the card is a healthcare or commercial  card.
    """

    card_type_name: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "ACCEL_PINLESS",
            "AMERICAN_EXPRESS",
            "CHASENET_CREDIT",
            "CHASENET_SIGNATURE_DEBIT",
            "CHINA_UNION_PAY",
            "DINERS_CLUB",
            "DISCOVER",
            "EFTPOS_PINLESS",
            "INTERNATIONAL_MAESTRO",
            "JCB",
            "MASTERCARD",
            "MASTERCARD_RESTRICTED_DEBIT",
            "NYCE_PINLESS",
            "PULSE_PINLESS",
            "STAR_PINLESS",
            "VISA",
            "VISA_RESTRICTED_DEBIT",
        ]
    ]
    """
    Name of the payment network.
    """

    cvv: typing_extensions.NotRequired[str]
    """
    Card verification value (CVV/CV2)
    """

    encryption_integrity_check: typing_extensions.NotRequired[str]
    """
    The alphanumeric string generated by voltage to verify the soundness of the encrypted key used by merchant and payment process. The merchant passed this in the API call. The backend process validates the subscriber id and format matches - between the merchant request for a key and the UPG request
    """

    expiry: typing_extensions.NotRequired[Expiry]
    """
    Expiration date
    """

    is_bill_payment: typing_extensions.NotRequired[bool]
    """
    Indicates whether or not the transaction is identified as a bill payment, prearranged between the cardholder and the merchant.
    """

    masked_account_number: typing_extensions.NotRequired[str]
    """
    Identifies a concealed number associated with the card number recognized by various payment systems. This is typically concealed by storing only the first 6 and/or last 4 digits of the payment account number or some variation.
    """

    merchant_sales_channel_name: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "INTERACTIVE_VOICE_RESPONSE", "INTERNET", "MAIL_ORDER_TELEPHONE_ORDER"
        ]
    ]
    """
    Label given to a merchant client of the Firm's medium for reaching its customers and facilitating and/or performing sales of its merchandise or services.
    """

    network_response: typing_extensions.NotRequired[NetworkResponse]
    """
    Response information from payment network
    """

    original_network_transaction_id: typing_extensions.NotRequired[str]
    """
    When submitting a merchant-initiated payment, submit the networkTransactionId received from the first payment in this field.
    """

    payment_tokens: typing_extensions.NotRequired[typing.List[PaymentToken]]
    """
    List of payment tokens for the transaction
    """

    token_service_response_code: typing_extensions.NotRequired[str]
    """
    Short explanation of response Code
    """

    verification_authentication_request: typing_extensions.NotRequired[
        PaymentAuthenticationRequest
    ]
    """
    Request Authentication during payment process
    """

    wallet_provider: typing_extensions.NotRequired[
        typing_extensions.Literal["APPLE_PAY", "GOOGLE_PAY"]
    ]
    """
    Identifies the organization who manages the e-wallet for a consumer. The actual e-wallet management responsibilities may include hosting, accessing, communicating, and/or updating all or some of the customer data associated with the e-wallet.  An E-wallet is an application that is created on the mobile device to interact with the Point of Sale (POS) device as a catalyst for a transaction. This value may be sent to the Firm (as in Visa Tokenization) or created by the Firm.
    """


class _SerializerVerificationCard(pydantic.BaseModel):
    """
    Serializer for VerificationCard handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    account_number: typing.Optional[str] = pydantic.Field(
        alias="accountNumber", default=None
    )
    account_number_type: typing.Optional[
        typing_extensions.Literal[
            "DEVICE_TOKEN",
            "NETWORK_TOKEN",
            "PAN",
            "SAFETECH_PAGE_ENCRYPTION",
            "SAFETECH_TOKEN",
        ]
    ] = pydantic.Field(alias="accountNumberType", default=None)
    authentication: typing.Optional[_SerializerAuthentication] = pydantic.Field(
        alias="authentication", default=None
    )
    card_type: typing.Optional[
        typing_extensions.Literal[
            "AP",
            "AX",
            "CC",
            "CR",
            "CZ",
            "DC",
            "DI",
            "EP",
            "IM",
            "JC",
            "MC",
            "MR",
            "NP",
            "PP",
            "SP",
            "VI",
            "VR",
        ]
    ] = pydantic.Field(alias="cardType", default=None)
    card_type_indicators: typing.Optional[_SerializerCardTypeIndicators] = (
        pydantic.Field(alias="cardTypeIndicators", default=None)
    )
    card_type_name: typing.Optional[
        typing_extensions.Literal[
            "ACCEL_PINLESS",
            "AMERICAN_EXPRESS",
            "CHASENET_CREDIT",
            "CHASENET_SIGNATURE_DEBIT",
            "CHINA_UNION_PAY",
            "DINERS_CLUB",
            "DISCOVER",
            "EFTPOS_PINLESS",
            "INTERNATIONAL_MAESTRO",
            "JCB",
            "MASTERCARD",
            "MASTERCARD_RESTRICTED_DEBIT",
            "NYCE_PINLESS",
            "PULSE_PINLESS",
            "STAR_PINLESS",
            "VISA",
            "VISA_RESTRICTED_DEBIT",
        ]
    ] = pydantic.Field(alias="cardTypeName", default=None)
    cvv: typing.Optional[str] = pydantic.Field(alias="cvv", default=None)
    encryption_integrity_check: typing.Optional[str] = pydantic.Field(
        alias="encryptionIntegrityCheck", default=None
    )
    expiry: typing.Optional[_SerializerExpiry] = pydantic.Field(
        alias="expiry", default=None
    )
    is_bill_payment: typing.Optional[bool] = pydantic.Field(
        alias="isBillPayment", default=None
    )
    masked_account_number: typing.Optional[str] = pydantic.Field(
        alias="maskedAccountNumber", default=None
    )
    merchant_sales_channel_name: typing.Optional[
        typing_extensions.Literal[
            "INTERACTIVE_VOICE_RESPONSE", "INTERNET", "MAIL_ORDER_TELEPHONE_ORDER"
        ]
    ] = pydantic.Field(alias="merchantSalesChannelName", default=None)
    network_response: typing.Optional[_SerializerNetworkResponse] = pydantic.Field(
        alias="networkResponse", default=None
    )
    original_network_transaction_id: typing.Optional[str] = pydantic.Field(
        alias="originalNetworkTransactionId", default=None
    )
    payment_tokens: typing.Optional[typing.List[_SerializerPaymentToken]] = (
        pydantic.Field(alias="paymentTokens", default=None)
    )
    token_service_response_code: typing.Optional[str] = pydantic.Field(
        alias="tokenServiceResponseCode", default=None
    )
    verification_authentication_request: typing.Optional[
        _SerializerPaymentAuthenticationRequest
    ] = pydantic.Field(alias="verificationAuthenticationRequest", default=None)
    wallet_provider: typing.Optional[
        typing_extensions.Literal["APPLE_PAY", "GOOGLE_PAY"]
    ] = pydantic.Field(alias="walletProvider", default=None)
