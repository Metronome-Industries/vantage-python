from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors import Errors
from ...models.segment import Segment
from ...types import Response


def _get_kwargs(
    segment_token: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/segments/{segment_token}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Errors, Segment]]:
    if response.status_code == 204:
        response_204 = Segment.from_dict(response.json())

        return response_204
    if response.status_code == 404:
        response_404 = Errors.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Errors, Segment]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    segment_token: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Errors, Segment]]:
    """Delete a Segment.

    Args:
        segment_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, Segment]]
    """

    kwargs = _get_kwargs(
        segment_token=segment_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    segment_token: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Errors, Segment]]:
    """Delete a Segment.

    Args:
        segment_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Errors, Segment]
    """

    return sync_detailed(
        segment_token=segment_token,
        client=client,
    ).parsed


async def asyncio_detailed(
    segment_token: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Errors, Segment]]:
    """Delete a Segment.

    Args:
        segment_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, Segment]]
    """

    kwargs = _get_kwargs(
        segment_token=segment_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    segment_token: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Errors, Segment]]:
    """Delete a Segment.

    Args:
        segment_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Errors, Segment]
    """

    return (
        await asyncio_detailed(
            segment_token=segment_token,
            client=client,
        )
    ).parsed
