import typing
import typing_extensions

from jpm_online_payments.core import (
    AsyncBaseClient,
    QueryParams,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    encode_param,
    to_encodable,
    type_utils,
)
from jpm_online_payments.types import models, params


class RefundsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def get(
        self,
        *,
        merchant_id: str,
        request_id: str,
        request_identifier: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.RefundResponse:
        """
        Get a specific refund transaction by request Id

        Get a specific refund transaction by request Id.

        GET /refunds

        Args:
            merchant-id: Identifier for the merchant account
            request-id: Merchant identifier for the request. The value must be unique.
            requestIdentifier: The request identifier for the previous attempted transaction to query by.
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.refunds.get(
            merchant_id="991234567890",
            request_id="10cc0270-7bed-11e9-a188-1763956dd7f6",
            request_identifier="12cc0270-7bed-11e9-a188-1763956dd7f6",
        )
        ```

        """
        _query: QueryParams = {}
        _query["requestIdentifier"] = encode_param(request_identifier, False)
        _header: typing.Dict[str, str] = {}
        _header["merchant-id"] = str(encode_param(merchant_id, False))
        _header["request-id"] = str(encode_param(request_id, False))
        return self._base_client.request(
            method="GET",
            path="/refunds",
            auth_names=["auth"],
            query_params=_query,
            headers=_header,
            cast_to=models.RefundResponse,
            request_options=request_options or default_request_options(),
        )

    def get_by_id(
        self,
        *,
        id: str,
        merchant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.RefundResponse:
        """
        Get a specific refund transaction by transaction Id

        Get a specific refund transaction by transaction Id

        GET /refunds/{id}

        Args:
            id: Identifier for the transaction
            merchant-id: Identifier for the merchant account
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.refunds.get_by_id(
            id="12cc0270-7bed-11e9-a188-1763956dd7f6", merchant_id="991234567890"
        )
        ```

        """
        _header: typing.Dict[str, str] = {}
        _header["merchant-id"] = str(encode_param(merchant_id, False))
        return self._base_client.request(
            method="GET",
            path=f"/refunds/{id}",
            auth_names=["auth"],
            headers=_header,
            cast_to=models.RefundResponse,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        merchant: params.Merchant,
        merchant_id: str,
        request_id: str,
        account_holder: typing.Union[
            typing.Optional[params.AccountHolder], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        account_on_file: typing.Union[
            typing.Optional[
                typing_extensions.Literal["NOT_STORED", "STORED", "TO_BE_STORED"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        amount: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        capture_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        currency: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
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
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        initiator_type: typing.Union[
            typing.Optional[typing_extensions.Literal["CARDHOLDER", "MERCHANT"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        mandate: typing.Union[
            typing.Optional[params.Mandate], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        merchant_defined: typing.Union[
            typing.Optional[params.MerchantDefined], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        merchant_order_number: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        payment_metadata_list: typing.Union[
            typing.Optional[typing.List[params.PaymentMetadata]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        payment_method_type: typing.Union[
            typing.Optional[params.RefundPaymentMethodType], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        payment_request_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        point_of_interaction: typing.Union[
            typing.Optional[params.PointOfInteraction], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        restaurant_addenda: typing.Union[
            typing.Optional[params.RestaurantAddenda], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        retail_addenda: typing.Union[
            typing.Optional[params.RetailAddenda], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        statement_descriptor: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        sub_merchant_supplemental_data: typing.Union[
            typing.Optional[params.SubMerchantSupplementalData], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.RefundResponse:
        """
        Create a refund

        Creates a refund request and returns funds to the consumer. 1. For refund associated with a previous payment, send transactionReferenceId. 2. For standalone refunds, send order and payment objects.

        POST /refunds

        Args:
            accountHolder: Card owner properties
            accountOnFile: Indicates whether payment method is stored by merchant. Possible values:STORED - Use if already stored and current payment is either cardholder-initiated stored payment or subsequent recurring or installment transaction. NOT_STORED - Use when payment method obtained for purpose of single payment. TO_BE_STORED - Use when consumer is intentionally storing their payment method after this payment for subsequent recurring or stored payments.
            amount: Total monetary value of the payment including all taxes and fees.
            captureId: Identifies a unique occurrence of a payment settlement request when the authorization is complete and the transaction is ready for settlement. The transaction can no longer be edited but can be voided.
            currency: Describes the currency type of the transaction
            initiatorType: Describes the initiator of the transaction for the stored credential framework (MIT/CIT)
            mandate: Agreement information between the consumer, debtor bank (checking account of the consumer) and the merchant for debit funds.
            merchantDefined: merchant defined data field that it will pass through to reporting.
            merchantOrderNumber: A unique merchant assigned identifier for the confirmation of goods and/or services purchased. The merchant order provides the merchant a reference to the prices, quantity and description of goods and/or services to be delivered for all transactions included in the sale.
            paymentMetadataList: Payment Metadata List
            paymentMethodType: Object with one of the payment method type applicable for refund processing
            paymentRequestId: Identifies a unique occurrence of an payment processing request from merchant that is associated with a purchase of goods and/or services. A payment request consist of authorization, captures and refunds.
            pointOfInteraction: In store payment Information
            restaurantAddenda: Restaurant Addenda
            retailAddenda: Industry-specific attributes.
            statementDescriptor: Merchant name to appear on account holder statement. If not provided, defaults to merchant profile descriptor value.  To send both company identifier and transaction-specific information, use one of these formats: Option 1 ? 3-byte company identifier * 18-byte descriptor (example: XYZ*PAYMENT1OF3) Option 2 ? 7-byte company identifier * 14-byte descriptor (example: XYZCOMP*PAYMENT1OF3) Option 3 ? 12-byte company identifier * 9-byte descriptor (example: XYZCOMPANY1*PAYMT1OF3)
            subMerchantSupplementalData: Additional data provided by merchant for reference purposes.
            merchant: Information about the merchant
            merchant-id: Identifier for the merchant account
            request-id: Merchant identifier for the request. The value must be unique.
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.refunds.create(
            merchant={
                "merchant_software": {
                    "company_name": "Payment Company",
                    "product_name": "Application Name",
                }
            },
            merchant_id="000017904371",
            request_id="10cc0270-7bed-11e9-a188-1763956dd7f6",
        )
        ```

        """
        _header: typing.Dict[str, str] = {}
        _header["merchant-id"] = str(encode_param(merchant_id, False))
        _header["request-id"] = str(encode_param(request_id, False))
        _json = to_encodable(
            item={
                "account_holder": account_holder,
                "account_on_file": account_on_file,
                "amount": amount,
                "capture_id": capture_id,
                "currency": currency,
                "initiator_type": initiator_type,
                "mandate": mandate,
                "merchant_defined": merchant_defined,
                "merchant_order_number": merchant_order_number,
                "payment_metadata_list": payment_metadata_list,
                "payment_method_type": payment_method_type,
                "payment_request_id": payment_request_id,
                "point_of_interaction": point_of_interaction,
                "restaurant_addenda": restaurant_addenda,
                "retail_addenda": retail_addenda,
                "statement_descriptor": statement_descriptor,
                "sub_merchant_supplemental_data": sub_merchant_supplemental_data,
                "merchant": merchant,
            },
            dump_with=params._SerializerRefund,
        )
        return self._base_client.request(
            method="POST",
            path="/refunds",
            auth_names=["auth"],
            headers=_header,
            json=_json,
            cast_to=models.RefundResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncRefundsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def get(
        self,
        *,
        merchant_id: str,
        request_id: str,
        request_identifier: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.RefundResponse:
        """
        Get a specific refund transaction by request Id

        Get a specific refund transaction by request Id.

        GET /refunds

        Args:
            merchant-id: Identifier for the merchant account
            request-id: Merchant identifier for the request. The value must be unique.
            requestIdentifier: The request identifier for the previous attempted transaction to query by.
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.refunds.get(
            merchant_id="991234567890",
            request_id="10cc0270-7bed-11e9-a188-1763956dd7f6",
            request_identifier="12cc0270-7bed-11e9-a188-1763956dd7f6",
        )
        ```

        """
        _query: QueryParams = {}
        _query["requestIdentifier"] = encode_param(request_identifier, False)
        _header: typing.Dict[str, str] = {}
        _header["merchant-id"] = str(encode_param(merchant_id, False))
        _header["request-id"] = str(encode_param(request_id, False))
        return await self._base_client.request(
            method="GET",
            path="/refunds",
            auth_names=["auth"],
            query_params=_query,
            headers=_header,
            cast_to=models.RefundResponse,
            request_options=request_options or default_request_options(),
        )

    async def get_by_id(
        self,
        *,
        id: str,
        merchant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.RefundResponse:
        """
        Get a specific refund transaction by transaction Id

        Get a specific refund transaction by transaction Id

        GET /refunds/{id}

        Args:
            id: Identifier for the transaction
            merchant-id: Identifier for the merchant account
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.refunds.get_by_id(
            id="12cc0270-7bed-11e9-a188-1763956dd7f6", merchant_id="991234567890"
        )
        ```

        """
        _header: typing.Dict[str, str] = {}
        _header["merchant-id"] = str(encode_param(merchant_id, False))
        return await self._base_client.request(
            method="GET",
            path=f"/refunds/{id}",
            auth_names=["auth"],
            headers=_header,
            cast_to=models.RefundResponse,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        merchant: params.Merchant,
        merchant_id: str,
        request_id: str,
        account_holder: typing.Union[
            typing.Optional[params.AccountHolder], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        account_on_file: typing.Union[
            typing.Optional[
                typing_extensions.Literal["NOT_STORED", "STORED", "TO_BE_STORED"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        amount: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        capture_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        currency: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
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
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        initiator_type: typing.Union[
            typing.Optional[typing_extensions.Literal["CARDHOLDER", "MERCHANT"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        mandate: typing.Union[
            typing.Optional[params.Mandate], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        merchant_defined: typing.Union[
            typing.Optional[params.MerchantDefined], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        merchant_order_number: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        payment_metadata_list: typing.Union[
            typing.Optional[typing.List[params.PaymentMetadata]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        payment_method_type: typing.Union[
            typing.Optional[params.RefundPaymentMethodType], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        payment_request_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        point_of_interaction: typing.Union[
            typing.Optional[params.PointOfInteraction], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        restaurant_addenda: typing.Union[
            typing.Optional[params.RestaurantAddenda], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        retail_addenda: typing.Union[
            typing.Optional[params.RetailAddenda], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        statement_descriptor: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        sub_merchant_supplemental_data: typing.Union[
            typing.Optional[params.SubMerchantSupplementalData], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.RefundResponse:
        """
        Create a refund

        Creates a refund request and returns funds to the consumer. 1. For refund associated with a previous payment, send transactionReferenceId. 2. For standalone refunds, send order and payment objects.

        POST /refunds

        Args:
            accountHolder: Card owner properties
            accountOnFile: Indicates whether payment method is stored by merchant. Possible values:STORED - Use if already stored and current payment is either cardholder-initiated stored payment or subsequent recurring or installment transaction. NOT_STORED - Use when payment method obtained for purpose of single payment. TO_BE_STORED - Use when consumer is intentionally storing their payment method after this payment for subsequent recurring or stored payments.
            amount: Total monetary value of the payment including all taxes and fees.
            captureId: Identifies a unique occurrence of a payment settlement request when the authorization is complete and the transaction is ready for settlement. The transaction can no longer be edited but can be voided.
            currency: Describes the currency type of the transaction
            initiatorType: Describes the initiator of the transaction for the stored credential framework (MIT/CIT)
            mandate: Agreement information between the consumer, debtor bank (checking account of the consumer) and the merchant for debit funds.
            merchantDefined: merchant defined data field that it will pass through to reporting.
            merchantOrderNumber: A unique merchant assigned identifier for the confirmation of goods and/or services purchased. The merchant order provides the merchant a reference to the prices, quantity and description of goods and/or services to be delivered for all transactions included in the sale.
            paymentMetadataList: Payment Metadata List
            paymentMethodType: Object with one of the payment method type applicable for refund processing
            paymentRequestId: Identifies a unique occurrence of an payment processing request from merchant that is associated with a purchase of goods and/or services. A payment request consist of authorization, captures and refunds.
            pointOfInteraction: In store payment Information
            restaurantAddenda: Restaurant Addenda
            retailAddenda: Industry-specific attributes.
            statementDescriptor: Merchant name to appear on account holder statement. If not provided, defaults to merchant profile descriptor value.  To send both company identifier and transaction-specific information, use one of these formats: Option 1 ? 3-byte company identifier * 18-byte descriptor (example: XYZ*PAYMENT1OF3) Option 2 ? 7-byte company identifier * 14-byte descriptor (example: XYZCOMP*PAYMENT1OF3) Option 3 ? 12-byte company identifier * 9-byte descriptor (example: XYZCOMPANY1*PAYMT1OF3)
            subMerchantSupplementalData: Additional data provided by merchant for reference purposes.
            merchant: Information about the merchant
            merchant-id: Identifier for the merchant account
            request-id: Merchant identifier for the request. The value must be unique.
            request_options: Additional options to customize the HTTP request

        Returns:
            Success

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.refunds.create(
            merchant={
                "merchant_software": {
                    "company_name": "Payment Company",
                    "product_name": "Application Name",
                }
            },
            merchant_id="000017904371",
            request_id="10cc0270-7bed-11e9-a188-1763956dd7f6",
        )
        ```

        """
        _header: typing.Dict[str, str] = {}
        _header["merchant-id"] = str(encode_param(merchant_id, False))
        _header["request-id"] = str(encode_param(request_id, False))
        _json = to_encodable(
            item={
                "account_holder": account_holder,
                "account_on_file": account_on_file,
                "amount": amount,
                "capture_id": capture_id,
                "currency": currency,
                "initiator_type": initiator_type,
                "mandate": mandate,
                "merchant_defined": merchant_defined,
                "merchant_order_number": merchant_order_number,
                "payment_metadata_list": payment_metadata_list,
                "payment_method_type": payment_method_type,
                "payment_request_id": payment_request_id,
                "point_of_interaction": point_of_interaction,
                "restaurant_addenda": restaurant_addenda,
                "retail_addenda": retail_addenda,
                "statement_descriptor": statement_descriptor,
                "sub_merchant_supplemental_data": sub_merchant_supplemental_data,
                "merchant": merchant,
            },
            dump_with=params._SerializerRefund,
        )
        return await self._base_client.request(
            method="POST",
            path="/refunds",
            auth_names=["auth"],
            headers=_header,
            json=_json,
            cast_to=models.RefundResponse,
            request_options=request_options or default_request_options(),
        )
