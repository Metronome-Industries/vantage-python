from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors import Errors
from ...models.segment import Segment
from ...models.update_segment import UpdateSegment
from ...types import Response


def _get_kwargs(
    segment_token: str,
    *,
    body: UpdateSegment,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/segments/{segment_token}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Errors | Segment | None:
    if response.status_code == 200:
        response_200 = Segment.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Errors.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = Errors.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Errors | Segment]:
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
    body: UpdateSegment,
) -> Response[Errors | Segment]:
    """Update segment

     Update a Segment.

    Args:
        segment_token (str):
        body (UpdateSegment): Update a Segment.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Errors | Segment]
    """

    kwargs = _get_kwargs(
        segment_token=segment_token,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    segment_token: str,
    *,
    client: AuthenticatedClient,
    body: UpdateSegment,
) -> Errors | Segment | None:
    """Update segment

     Update a Segment.

    Args:
        segment_token (str):
        body (UpdateSegment): Update a Segment.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Errors | Segment
    """

    return sync_detailed(
        segment_token=segment_token,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    segment_token: str,
    *,
    client: AuthenticatedClient,
    body: UpdateSegment,
) -> Response[Errors | Segment]:
    """Update segment

     Update a Segment.

    Args:
        segment_token (str):
        body (UpdateSegment): Update a Segment.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Errors | Segment]
    """

    kwargs = _get_kwargs(
        segment_token=segment_token,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    segment_token: str,
    *,
    client: AuthenticatedClient,
    body: UpdateSegment,
) -> Errors | Segment | None:
    """Update segment

     Update a Segment.

    Args:
        segment_token (str):
        body (UpdateSegment): Update a Segment.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Errors | Segment
    """

    return (
        await asyncio_detailed(
            segment_token=segment_token,
            client=client,
            body=body,
        )
    ).parsed
