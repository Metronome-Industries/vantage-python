from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.budget_alert import BudgetAlert
from ...models.errors import Errors
from ...models.update_budget_alert_files_body import UpdateBudgetAlertFilesBody
from ...models.update_budget_alert_json_body import UpdateBudgetAlertJsonBody
from ...types import Response


def _get_kwargs(
    budget_alert_token: str,
    *,
    body: Union[
        UpdateBudgetAlertJsonBody,
        UpdateBudgetAlertFilesBody,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/budget_alerts/{budget_alert_token}",
    }

    if isinstance(body, UpdateBudgetAlertJsonBody):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdateBudgetAlertFilesBody):
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
    if response.status_code == 404:
        response_404 = Errors.from_dict(response.json())

        return response_404
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
    budget_alert_token: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateBudgetAlertJsonBody,
        UpdateBudgetAlertFilesBody,
    ],
) -> Response[Union[BudgetAlert, Errors]]:
    """Updates an existing BudgetAlert.

    Args:
        budget_alert_token (str):
        body (UpdateBudgetAlertJsonBody):
        body (UpdateBudgetAlertFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BudgetAlert, Errors]]
    """

    kwargs = _get_kwargs(
        budget_alert_token=budget_alert_token,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    budget_alert_token: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateBudgetAlertJsonBody,
        UpdateBudgetAlertFilesBody,
    ],
) -> Optional[Union[BudgetAlert, Errors]]:
    """Updates an existing BudgetAlert.

    Args:
        budget_alert_token (str):
        body (UpdateBudgetAlertJsonBody):
        body (UpdateBudgetAlertFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BudgetAlert, Errors]
    """

    return sync_detailed(
        budget_alert_token=budget_alert_token,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    budget_alert_token: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateBudgetAlertJsonBody,
        UpdateBudgetAlertFilesBody,
    ],
) -> Response[Union[BudgetAlert, Errors]]:
    """Updates an existing BudgetAlert.

    Args:
        budget_alert_token (str):
        body (UpdateBudgetAlertJsonBody):
        body (UpdateBudgetAlertFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BudgetAlert, Errors]]
    """

    kwargs = _get_kwargs(
        budget_alert_token=budget_alert_token,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    budget_alert_token: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateBudgetAlertJsonBody,
        UpdateBudgetAlertFilesBody,
    ],
) -> Optional[Union[BudgetAlert, Errors]]:
    """Updates an existing BudgetAlert.

    Args:
        budget_alert_token (str):
        body (UpdateBudgetAlertJsonBody):
        body (UpdateBudgetAlertFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BudgetAlert, Errors]
    """

    return (
        await asyncio_detailed(
            budget_alert_token=budget_alert_token,
            client=client,
            body=body,
        )
    ).parsed
