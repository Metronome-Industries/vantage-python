from enum import Enum


class GetForecastedCostsProvider(str, Enum):
    ALL = "all"
    AWS = "aws"
    AZURE = "azure"
    AZURE_CSP = "azure_csp"
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
    KUBERNETES_AGENT = "kubernetes_agent"
    LINODE = "linode"
    MONGO = "mongo"
    NEW_RELIC = "new_relic"
    OPENCOST = "opencost"
    OPEN_AI = "open_ai"
    ORACLE = "oracle"
    PLANETSCALE = "planetscale"
    SNOWFLAKE = "snowflake"
    TEMPORAL = "temporal"
    TWILIO = "twilio"

    def __str__(self) -> str:
        return str(self.value)
