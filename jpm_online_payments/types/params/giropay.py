import typing
import typing_extensions
import pydantic

from .redirected_payment import RedirectedPayment, _SerializerRedirectedPayment


class Giropay(typing_extensions.TypedDict):
    """
    Giropay is German based payment method that allows customers to complete transactions online using their online banking environment, with funds debited from their bank account.
    """

    completion_time: typing_extensions.NotRequired[str]
    """
    Provides a timestamp (UTC). Designates the hour (hh), minute (mm), seconds (ss) and date (if timestamp) or year (YYYY), month (MM), and day (DD) (if date)
    """

    creation_time: typing_extensions.NotRequired[str]
    """
    Provides a timestamp (UTC). Designates the hour (hh), minute (mm), seconds (ss) and date (if timestamp) or year (YYYY), month (MM), and day (DD) (if date)
    """

    preferred_language: typing_extensions.NotRequired[str]
    """
    Language preference indicated by consumer for pages displayed. Using language tags indicated in RFC5646.
    """

    redirected_payment: typing_extensions.NotRequired[RedirectedPayment]
    """
    Redirected Payment attributes
    """


class _SerializerGiropay(pydantic.BaseModel):
    """
    Serializer for Giropay handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    completion_time: typing.Optional[str] = pydantic.Field(
        alias="completionTime", default=None
    )
    creation_time: typing.Optional[str] = pydantic.Field(
        alias="creationTime", default=None
    )
    preferred_language: typing.Optional[str] = pydantic.Field(
        alias="preferredLanguage", default=None
    )
    redirected_payment: typing.Optional[_SerializerRedirectedPayment] = pydantic.Field(
        alias="redirectedPayment", default=None
    )
