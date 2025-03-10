from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.budget_alert import BudgetAlert
from ...models.create_budget_alert_files_body import CreateBudgetAlertFilesBody
from ...models.create_budget_alert_json_body import CreateBudgetAlertJsonBody
from ...models.errors import Errors
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        CreateBudgetAlertJsonBody,
        CreateBudgetAlertFilesBody,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/budget_alerts",
    }

    if isinstance(body, CreateBudgetAlertJsonBody):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateBudgetAlertFilesBody):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[BudgetAlert, Errors]]:
    if response.status_code == 201:
        response_201 = BudgetAlert.from_dict(response.json())

        return response_201
    if response.status_code == 400:
        response_400 = Errors.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[BudgetAlert, Errors]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateBudgetAlertJsonBody,
        CreateBudgetAlertFilesBody,
    ],
) -> Response[Union[BudgetAlert, Errors]]:
    """Create a Budget Alert.

    Args:
        body (CreateBudgetAlertJsonBody):
        body (CreateBudgetAlertFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BudgetAlert, Errors]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateBudgetAlertJsonBody,
        CreateBudgetAlertFilesBody,
    ],
) -> Optional[Union[BudgetAlert, Errors]]:
    """Create a Budget Alert.

    Args:
        body (CreateBudgetAlertJsonBody):
        body (CreateBudgetAlertFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BudgetAlert, Errors]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateBudgetAlertJsonBody,
        CreateBudgetAlertFilesBody,
    ],
) -> Response[Union[BudgetAlert, Errors]]:
    """Create a Budget Alert.

    Args:
        body (CreateBudgetAlertJsonBody):
        body (CreateBudgetAlertFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BudgetAlert, Errors]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateBudgetAlertJsonBody,
        CreateBudgetAlertFilesBody,
    ],
) -> Optional[Union[BudgetAlert, Errors]]:
    """Create a Budget Alert.

    Args:
        body (CreateBudgetAlertJsonBody):
        body (CreateBudgetAlertFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BudgetAlert, Errors]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
