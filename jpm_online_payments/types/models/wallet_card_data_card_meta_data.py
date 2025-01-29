import typing
import pydantic


class WalletCardDataCardMetaData(pydantic.BaseModel):
    """
    Card data, including its expiration date and suffix, for the card related to the merchant token.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        extra="allow",
    )

    __pydantic_extra__: typing.Dict[str, str]
