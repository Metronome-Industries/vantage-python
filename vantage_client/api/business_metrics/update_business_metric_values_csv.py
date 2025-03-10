from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.business_metric import BusinessMetric
from ...models.errors import Errors
from ...models.update_business_metric_values_csv_data_body import UpdateBusinessMetricValuesCSVDataBody
from ...models.update_business_metric_values_csv_files_body import UpdateBusinessMetricValuesCSVFilesBody
from ...types import Response


def _get_kwargs(
    business_metric_token: str,
    *,
    body: Union[
        UpdateBusinessMetricValuesCSVDataBody,
        UpdateBusinessMetricValuesCSVFilesBody,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/business_metrics/{business_metric_token}/values.csv",
    }

    if isinstance(body, UpdateBusinessMetricValuesCSVDataBody):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, UpdateBusinessMetricValuesCSVFilesBody):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[BusinessMetric, Errors]]:
    if response.status_code == 201:
        response_201 = BusinessMetric.from_dict(response.json())

        return response_201
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
) -> Response[Union[BusinessMetric, Errors]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    business_metric_token: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateBusinessMetricValuesCSVDataBody,
        UpdateBusinessMetricValuesCSVFilesBody,
    ],
) -> Response[Union[BusinessMetric, Errors]]:
    """Updates the values for an existing BusinessMetric from a CSV file.

    Args:
        business_metric_token (str):
        body (UpdateBusinessMetricValuesCSVDataBody):
        body (UpdateBusinessMetricValuesCSVFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BusinessMetric, Errors]]
    """

    kwargs = _get_kwargs(
        business_metric_token=business_metric_token,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    business_metric_token: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateBusinessMetricValuesCSVDataBody,
        UpdateBusinessMetricValuesCSVFilesBody,
    ],
) -> Optional[Union[BusinessMetric, Errors]]:
    """Updates the values for an existing BusinessMetric from a CSV file.

    Args:
        business_metric_token (str):
        body (UpdateBusinessMetricValuesCSVDataBody):
        body (UpdateBusinessMetricValuesCSVFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BusinessMetric, Errors]
    """

    return sync_detailed(
        business_metric_token=business_metric_token,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    business_metric_token: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateBusinessMetricValuesCSVDataBody,
        UpdateBusinessMetricValuesCSVFilesBody,
    ],
) -> Response[Union[BusinessMetric, Errors]]:
    """Updates the values for an existing BusinessMetric from a CSV file.

    Args:
        business_metric_token (str):
        body (UpdateBusinessMetricValuesCSVDataBody):
        body (UpdateBusinessMetricValuesCSVFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BusinessMetric, Errors]]
    """

    kwargs = _get_kwargs(
        business_metric_token=business_metric_token,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    business_metric_token: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateBusinessMetricValuesCSVDataBody,
        UpdateBusinessMetricValuesCSVFilesBody,
    ],
) -> Optional[Union[BusinessMetric, Errors]]:
    """Updates the values for an existing BusinessMetric from a CSV file.

    Args:
        business_metric_token (str):
        body (UpdateBusinessMetricValuesCSVDataBody):
        body (UpdateBusinessMetricValuesCSVFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BusinessMetric, Errors]
    """

    return (
        await asyncio_detailed(
            business_metric_token=business_metric_token,
            client=client,
            body=body,
        )
    ).parsed
