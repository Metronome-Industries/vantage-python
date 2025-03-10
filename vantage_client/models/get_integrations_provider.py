from enum import Enum


class GetIntegrationsProvider(str, Enum):
    AWS = "aws"
    AZURE = "azure"
    CLICKHOUSE = "clickhouse"
    CONFLUENT = "confluent"
    CORALOGIX = "coralogix"
    CUSTOM_PROVIDER = "custom_provider"
    DATABRICKS = "databricks"
    DATADOG = "datadog"
    FASTLY = "fastly"
    GCP = "gcp"
    GITHUB = "github"
    GRAFANA = "grafana"
    KUBERNETES = "kubernetes"
    LINODE = "linode"
    MONGO = "mongo"
    NEW_RELIC = "new_relic"
    OPENCOST = "opencost"
    OPEN_AI = "open_ai"
    ORACLE = "oracle"
    PLANETSCALE = "planetscale"
    SNOWFLAKE = "snowflake"
    TEMPORAL = "temporal"

    def __str__(self) -> str:
        return str(self.value)
