from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_cost_export_body import CreateCostExportBody
from ...models.errors import Errors
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateCostExportBody,
    groupings: Union[Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_groupings: Union[Unset, list[str]] = UNSET
    if not isinstance(groupings, Unset):
        json_groupings = groupings

    params["groupings"] = json_groupings

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/costs/data_exports",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Errors]]:
    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202
    if response.status_code == 400:
        response_400 = Errors.from_dict(response.json())

        return response_400
    if response.status_code == 402:
        response_402 = Errors.from_dict(response.json())

        return response_402
    if response.status_code == 404:
        response_404 = Errors.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, Errors]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateCostExportBody,
    groupings: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Any, Errors]]:
    """Generate a DataExport of costs.

    Args:
        groupings (Union[Unset, list[str]]):
        body (CreateCostExportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Errors]]
    """

    kwargs = _get_kwargs(
        body=body,
        groupings=groupings,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: CreateCostExportBody,
    groupings: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[Any, Errors]]:
    """Generate a DataExport of costs.

    Args:
        groupings (Union[Unset, list[str]]):
        body (CreateCostExportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Errors]
    """

    return sync_detailed(
        client=client,
        body=body,
        groupings=groupings,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateCostExportBody,
    groupings: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Any, Errors]]:
    """Generate a DataExport of costs.

    Args:
        groupings (Union[Unset, list[str]]):
        body (CreateCostExportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Errors]]
    """

    kwargs = _get_kwargs(
        body=body,
        groupings=groupings,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateCostExportBody,
    groupings: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[Any, Errors]]:
    """Generate a DataExport of costs.

    Args:
        groupings (Union[Unset, list[str]]):
        body (CreateCostExportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Errors]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            groupings=groupings,
        )
    ).parsed
