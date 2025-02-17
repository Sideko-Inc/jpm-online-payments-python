import typing
import typing_extensions
import pydantic

from .account_holder import AccountHolder
from .information import Information
from .installment import Installment
from .mandate import Mandate
from .merchant import Merchant
from .verification_payment_method_type import VerificationPaymentMethodType
from .risk import Risk
from .sub_merchant_supplemental_data import SubMerchantSupplementalData
from .payment_authentication_result import PaymentAuthenticationResult


class VerificationResponse(pydantic.BaseModel):
    """
    Response information for verification API calls
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    account_holder: typing.Optional[AccountHolder] = pydantic.Field(
        alias="accountHolder", default=None
    )
    """
    Card owner properties
    """
    account_on_file: typing.Optional[
        typing_extensions.Literal["NOT_STORED", "STORED", "TO_BE_STORED"]
    ] = pydantic.Field(alias="accountOnFile", default=None)
    """
    Indicates whether payment method is stored by merchant. Possible values:STORED - Use if already stored and current payment is either cardholder-initiated stored payment or subsequent recurring or installment transaction. NOT_STORED - Use when payment method obtained for purpose of single payment. TO_BE_STORED - Use when consumer is intentionally storing their payment method after this payment for subsequent recurring or stored payments.
    """
    approval_code: typing.Optional[str] = pydantic.Field(
        alias="approvalCode", default=None
    )
    """
    Approval code provided by the issuing bank.
    """
    currency: typing_extensions.Literal[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "ISK",
        "JMD",
        "JPY",
        "KES",
        "KHR",
        "KMF",
        "KRW",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRU",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SEK",
        "SGD",
        "SHP",
        "SLL",
        "SOS",
        "SRD",
        "STN",
        "SZL",
        "THB",
        "TJS",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XCD",
        "XOF",
        "XPF",
        "YER",
        "ZAR",
        "ZMW",
    ] = pydantic.Field(
        alias="currency",
    )
    """
    Describes the currency type of the transaction
    """
    host_message: str = pydantic.Field(
        alias="hostMessage",
    )
    """
    Message received from Issuer, network or processor. Can be blank
    """
    host_reference_id: typing.Optional[str] = pydantic.Field(
        alias="hostReferenceId", default=None
    )
    """
    Identifies unique identifier generated by the acquirer processing system and return to merchant for reference purposes.
    """
    information: typing.Optional[Information] = pydantic.Field(
        alias="information", default=None
    )
    """
    A list of informational messages
    """
    initiator_type: typing.Optional[
        typing_extensions.Literal["CARDHOLDER", "MERCHANT"]
    ] = pydantic.Field(alias="initiatorType", default=None)
    """
    Describes the initiator of the transaction for the stored credential framework (MIT/CIT)
    """
    installment: typing.Optional[Installment] = pydantic.Field(
        alias="installment", default=None
    )
    """
    Object containing information in the file
    """
    mandate: typing.Optional[Mandate] = pydantic.Field(alias="mandate", default=None)
    """
    Agreement information between the consumer, debtor bank (checking account of the consumer) and the merchant for debit funds.
    """
    merchant: typing.Optional[Merchant] = pydantic.Field(alias="merchant", default=None)
    """
    Information about the merchant
    """
    merchant_order_number: typing.Optional[str] = pydantic.Field(
        alias="merchantOrderNumber", default=None
    )
    """
    A unique merchant assigned identifier for the confirmation of goods and/or services purchased. The merchant order provides the merchant a reference to the prices, quantity and description of goods and/or services to be delivered for all transactions included in the sale.
    """
    payment_method_type: VerificationPaymentMethodType = pydantic.Field(
        alias="paymentMethodType",
    )
    """
    Object with one of the payment method type applicable for verification processing
    """
    recurring_sequence: typing.Optional[
        typing_extensions.Literal["FIRST", "SUBSEQUENT"]
    ] = pydantic.Field(alias="recurringSequence", default=None)
    """
    Identifies whether payment is the first in a series of recurring payments or a subsequent payment. Required for recurring billing.
    """
    request_id: str = pydantic.Field(
        alias="requestId",
    )
    """
    Merchant identifier for the request. The value must be unique.
    """
    response_code: str = pydantic.Field(
        alias="responseCode",
    )
    """
    Short explanation for response status
    """
    response_message: str = pydantic.Field(
        alias="responseMessage",
    )
    """
    Long explanation of response code
    """
    response_status: typing_extensions.Literal["DENIED", "ERROR", "SUCCESS"] = (
        pydantic.Field(
            alias="responseStatus",
        )
    )
    """
    Indicates whether API request resulted in success, error, or denial.
    """
    risk: typing.Optional[Risk] = pydantic.Field(alias="risk", default=None)
    """
    Response information for transactions
    """
    sub_merchant_supplemental_data: typing.Optional[SubMerchantSupplementalData] = (
        pydantic.Field(alias="subMerchantSupplementalData", default=None)
    )
    """
    Additional data provided by merchant for reference purposes.
    """
    transaction_date: typing.Optional[str] = pydantic.Field(
        alias="transactionDate", default=None
    )
    """
    Designates the hour, minute, seconds and date (if timestamp) or year, month, and date (if date) when the transaction (monetary or non-monetary) occurred.
    """
    transaction_id: str = pydantic.Field(
        alias="transactionId",
    )
    """
    Identifier of a transaction.
    """
    transaction_routing_override_list: typing.Optional[
        typing.List[typing_extensions.Literal["CIELO", "GETNET", "REDECARD", "STONE"]]
    ] = pydantic.Field(alias="transactionRoutingOverrideList", default=None)
    """
    List of transaction routing providers where the transaction be routed preferred by the merchant .
    """
    verification_authentication_result: typing.Optional[PaymentAuthenticationResult] = (
        pydantic.Field(alias="verificationAuthenticationResult", default=None)
    )
    """
    Cardholder Authentication Result from the Payment request.
    """
