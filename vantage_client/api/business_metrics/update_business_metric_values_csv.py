from http import HTTPStatus
from typing import Any

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
    body: UpdateBusinessMetricValuesCSVDataBody | UpdateBusinessMetricValuesCSVFilesBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/business_metrics/{business_metric_token}/values.csv",
    }

    if isinstance(body, UpdateBusinessMetricValuesCSVDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, UpdateBusinessMetricValuesCSVFilesBody):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BusinessMetric | Errors | None:
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
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BusinessMetric | Errors]:
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
    body: UpdateBusinessMetricValuesCSVDataBody | UpdateBusinessMetricValuesCSVFilesBody,
) -> Response[BusinessMetric | Errors]:
    """Update business metric values from CSV

     Updates the values for an existing BusinessMetric from a CSV file.

    Args:
        business_metric_token (str):
        body (UpdateBusinessMetricValuesCSVDataBody):
        body (UpdateBusinessMetricValuesCSVFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BusinessMetric | Errors]
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
    body: UpdateBusinessMetricValuesCSVDataBody | UpdateBusinessMetricValuesCSVFilesBody,
) -> BusinessMetric | Errors | None:
    """Update business metric values from CSV

     Updates the values for an existing BusinessMetric from a CSV file.

    Args:
        business_metric_token (str):
        body (UpdateBusinessMetricValuesCSVDataBody):
        body (UpdateBusinessMetricValuesCSVFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BusinessMetric | Errors
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
    body: UpdateBusinessMetricValuesCSVDataBody | UpdateBusinessMetricValuesCSVFilesBody,
) -> Response[BusinessMetric | Errors]:
    """Update business metric values from CSV

     Updates the values for an existing BusinessMetric from a CSV file.

    Args:
        business_metric_token (str):
        body (UpdateBusinessMetricValuesCSVDataBody):
        body (UpdateBusinessMetricValuesCSVFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BusinessMetric | Errors]
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
    body: UpdateBusinessMetricValuesCSVDataBody | UpdateBusinessMetricValuesCSVFilesBody,
) -> BusinessMetric | Errors | None:
    """Update business metric values from CSV

     Updates the values for an existing BusinessMetric from a CSV file.

    Args:
        business_metric_token (str):
        body (UpdateBusinessMetricValuesCSVDataBody):
        body (UpdateBusinessMetricValuesCSVFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BusinessMetric | Errors
    """

    return (
        await asyncio_detailed(
            business_metric_token=business_metric_token,
            client=client,
            body=body,
        )
    ).parsed
