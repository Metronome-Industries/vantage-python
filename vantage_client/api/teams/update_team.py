from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors import Errors
from ...models.team import Team
from ...models.update_team import UpdateTeam
from ...types import Response


def _get_kwargs(
    team_token: str,
    *,
    body: UpdateTeam,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/teams/{team_token}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Errors, Team]]:
    if response.status_code == 200:
        response_200 = Team.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = Errors.from_dict(response.json())

        return response_400
    if response.status_code == 403:
        response_403 = Errors.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = Errors.from_dict(response.json())

        return response_404
    if response.status_code == 422:
        response_422 = Errors.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Errors, Team]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    team_token: str,
    *,
    client: AuthenticatedClient,
    body: UpdateTeam,
) -> Response[Union[Errors, Team]]:
    """Update a Team.

    Args:
        team_token (str):
        body (UpdateTeam): Update a Team.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, Team]]
    """

    kwargs = _get_kwargs(
        team_token=team_token,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    team_token: str,
    *,
    client: AuthenticatedClient,
    body: UpdateTeam,
) -> Optional[Union[Errors, Team]]:
    """Update a Team.

    Args:
        team_token (str):
        body (UpdateTeam): Update a Team.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Errors, Team]
    """

    return sync_detailed(
        team_token=team_token,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    team_token: str,
    *,
    client: AuthenticatedClient,
    body: UpdateTeam,
) -> Response[Union[Errors, Team]]:
    """Update a Team.

    Args:
        team_token (str):
        body (UpdateTeam): Update a Team.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, Team]]
    """

    kwargs = _get_kwargs(
        team_token=team_token,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    team_token: str,
    *,
    client: AuthenticatedClient,
    body: UpdateTeam,
) -> Optional[Union[Errors, Team]]:
    """Update a Team.

    Args:
        team_token (str):
        body (UpdateTeam): Update a Team.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Errors, Team]
    """

    return (
        await asyncio_detailed(
            team_token=team_token,
            client=client,
            body=body,
        )
    ).parsed
