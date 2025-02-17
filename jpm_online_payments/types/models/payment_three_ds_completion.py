import typing
import typing_extensions
import pydantic


class PaymentThreeDsCompletion(pydantic.BaseModel):
    """
    ThreeDS Completion information from payment call.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    acs_transaction_id: typing.Optional[str] = pydantic.Field(
        alias="acsTransactionId", default=None
    )
    """
    This data element provides additional information to the ACS to determine the best approach for handling a request. The field is limited to 36 characters containing ACS Transaction ID for a prior authenticated transaction (for example, the first  recurring transaction that was authenticated with the cardholder).
    """
    authentication_status_reason_text: typing.Optional[str] = pydantic.Field(
        alias="authenticationStatusReasonText", default=None
    )
    """
    Long explanation of the Authentication Status
    """
    challenge_authentication_method: typing.Optional[
        typing_extensions.Literal[
            "APP_OTP",
            "KBA",
            "KEY_FOB",
            "OOB_BIOMETRICS",
            "OOB_LOGIN",
            "OOB_OTHER",
            "OTHER",
            "OTP_OTHER",
            "PUSH_CONFIRMATION",
            "SMS_OTP",
            "STATIC_PASSCODE",
        ]
    ] = pydantic.Field(alias="challengeAuthenticationMethod", default=None)
    """
    Information about how the 3DS Requestor authenticated the cardholder for the challenge request.
    """
    challenge_authentication_type: typing.Optional[
        typing_extensions.Literal["DECOUPLED", "DYNAMIC", "OOB", "STATIC"]
    ] = pydantic.Field(alias="challengeAuthenticationType", default=None)
    """
    Indicates the category of authentication request the Issuer will use to challenge the Cardholder in a three domain secure authentication process.
    """
    electronic_commerce_indicator: typing.Optional[str] = pydantic.Field(
        alias="electronicCommerceIndicator", default=None
    )
    """
    Describes the Electronic Commerce Indicator used in cardholder authentication on a network token
    """
    three_ds_authentication_value: typing.Optional[str] = pydantic.Field(
        alias="threeDSAuthenticationValue", default=None
    )
    """
    Payment System-specific value provided by the Access Control Server (ACS)  or the DS using an algorithm defined by Payment System. Authentication Value may be used to provide proof of authentication.
    """
    three_ds_directory_server_transaction_id: typing.Optional[str] = pydantic.Field(
        alias="threeDSDirectoryServerTransactionId", default=None
    )
    """
    Universally unique transaction identifier to identify a single transaction generated by the Three Domain Secure Server. This value has 36 characters in a format defined in IETF RFC 4122.
    """
    three_ds_transaction_status: typing.Optional[
        typing_extensions.Literal["A", "C", "D", "I", "N", "R", "U", "Y"]
    ] = pydantic.Field(alias="threeDSTransactionStatus", default=None)
    """
    Indicates whether a transaction qualifies as an authenticated transaction. The accepted values are: Y -> Authentication / Account verification successful N -> Not authenticated / Account not verified; Transaction denied U -> Authentication / Account verification could not be performed; technical or other problem C -> In order to complete the authentication, a challenge is required R -> Authentication / Account verification Rejected. Issuer is rejecting authentication/verification and request that authorization not be attempted A -> Attempts processing performed; Not authenticated / verified, but a proof of attempt authentication / verification is provided The following values are also accepted if the 3DS Server has initiated authentication with EMV 3DS 2.2.0 version or greater: D -> In order to complete the authentication, a challenge is required. Decoupled Authentication confirmed. I -> Informational Only; 3DS Requestor challenge preference acknowledged
    """
    three_ds_version: typing.Optional[str] = pydantic.Field(
        alias="threeDSVersion", default=None
    )
    """
    Codifies the version of the Three Domain Secure (3-D Secure or 3DS) software that is used by the merchant. 3DS is a protocol designed to be an additional multi-factor security layer and is performed for online debit and credit card authorization requests. The acquirer domain initiates the transaction for 3DS authentication. The interoperability domain sends a message to the corresponding issuing bank based on the Bank Identification Number (BIN) range. The issuing bank domain authenticates the card user.
    """
    update_timestamp: typing.Optional[str] = pydantic.Field(
        alias="updateTimestamp", default=None
    )
    """
    Designates the hour, minute, and second in a specific day when the record was last modified.
    """
