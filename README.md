[![Build Status](https://www.travis-ci.com/vantage-sh/vantage-python.svg?branch=main)](https://www.travis-ci.com/vantage-sh/vantage-python)

# Vantage Python Client

![Vantage Picture](https://uploads-ssl.webflow.com/5f9ba05ba40d6414f341df34/5f9bb1764b6670c6f7739564_moutain-scene.svg)

[Vantage](http://vantage.sh/) is a cloud cost transparency platform. This is the official Python client for the [Vantage API](http://vantage.readme.io/). You can use the API to get EC2 instance price and product information through a few simple-to-use API calls. The data offered through this API is heavily inspired from data avaiable from [ec2instances.info](http://ec2instances.info/). The feedback we get from users is that this API is significantly easier than learning and using AWS Pricing APIs. We have plans to expand the data available through this API in the future.

## Need Help?

Feel free to join us in our [community Slack](https://join.slack.com/t/vantagecommunity/shared_invite/zt-oey52myv-gq4AWRKkX25kjp1UGziPTw) in the #api channel. We're happy to chat and help. You're also welcome to email support@vantage.sh or ping [@JoinVantage](https://twitter.com/joinvantage) on Twitter and we're happy to give assistance. Lastly, we monitor issues on this repo if you have any feature requests or issues.

## Installation

The easiest way to get going is to install the client through PIP:

```shell
pip install vantage-client
```

Then import the package:
```python
import vantage
```

## Generate a Free API Token
The Vantage API is provided completely for free but requires an API token to use. To generate a free API token, follow these steps:

* Head to [http://vantage.sh/](http://vantage.sh/)
* Register a free account and confirm your email
* When you're asked _"What would you like to do first?"_ click _"Access Cloud Pricing API"_
* Create an API token from the account profile page and you're all set

You'll only need to do this once and you can use your API token for all usage going forward.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import vantage
from vantage.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = vantage.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = vantage.AccessGrantsApi(vantage.ApiClient(configuration))
create_access_grant = vantage.CreateAccessGrant() # CreateAccessGrant |

try:
    api_response = api_instance.create_access_grant(create_access_grant)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessGrantsApi->create_access_grant: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.vantage.sh/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccessGrantsApi* | [**create_access_grant**](docs/AccessGrantsApi.md#create_access_grant) | **POST** /access_grants |
*AccessGrantsApi* | [**delete_access_grant**](docs/AccessGrantsApi.md#delete_access_grant) | **DELETE** /access_grants/{access_grant_token} |
*AccessGrantsApi* | [**get_access_grant**](docs/AccessGrantsApi.md#get_access_grant) | **GET** /access_grants/{access_grant_token} |
*AccessGrantsApi* | [**get_access_grants**](docs/AccessGrantsApi.md#get_access_grants) | **GET** /access_grants |
*AccessGrantsApi* | [**update_access_grant**](docs/AccessGrantsApi.md#update_access_grant) | **PUT** /access_grants/{access_grant_token} |
*AnomalyAlertsApi* | [**get_anomaly_alert**](docs/AnomalyAlertsApi.md#get_anomaly_alert) | **GET** /anomaly_alerts/{anomaly_alert_token} |
*AnomalyAlertsApi* | [**get_anomaly_alerts**](docs/AnomalyAlertsApi.md#get_anomaly_alerts) | **GET** /anomaly_alerts |
*AnomalyAlertsApi* | [**update_anomaly_alert**](docs/AnomalyAlertsApi.md#update_anomaly_alert) | **PUT** /anomaly_alerts/{anomaly_alert_token} |
*AnomalyNotificationsApi* | [**create_anomaly_notification**](docs/AnomalyNotificationsApi.md#create_anomaly_notification) | **POST** /anomaly_notifications |
*AnomalyNotificationsApi* | [**delete_anomaly_notification**](docs/AnomalyNotificationsApi.md#delete_anomaly_notification) | **DELETE** /anomaly_notifications/{anomaly_notification_token} |
*AnomalyNotificationsApi* | [**get_anomaly_notification**](docs/AnomalyNotificationsApi.md#get_anomaly_notification) | **GET** /anomaly_notifications/{anomaly_notification_token} |
*AnomalyNotificationsApi* | [**get_anomaly_notifications**](docs/AnomalyNotificationsApi.md#get_anomaly_notifications) | **GET** /anomaly_notifications |
*AnomalyNotificationsApi* | [**update_anomaly_notification**](docs/AnomalyNotificationsApi.md#update_anomaly_notification) | **PUT** /anomaly_notifications/{anomaly_notification_token} |
*BillingRulesApi* | [**create_billing_rule**](docs/BillingRulesApi.md#create_billing_rule) | **POST** /billing_rules |
*BillingRulesApi* | [**delete_billing_rule**](docs/BillingRulesApi.md#delete_billing_rule) | **DELETE** /billing_rules/{billing_rule_token} |
*BillingRulesApi* | [**get_billing_rule**](docs/BillingRulesApi.md#get_billing_rule) | **GET** /billing_rules/{billing_rule_token} |
*BillingRulesApi* | [**get_billing_rules**](docs/BillingRulesApi.md#get_billing_rules) | **GET** /billing_rules |
*BillingRulesApi* | [**update_billing_rule**](docs/BillingRulesApi.md#update_billing_rule) | **PUT** /billing_rules/{billing_rule_token} |
*BudgetAlertsApi* | [**create_budget_alert**](docs/BudgetAlertsApi.md#create_budget_alert) | **POST** /budget_alerts |
*BudgetAlertsApi* | [**delete_budget_alert**](docs/BudgetAlertsApi.md#delete_budget_alert) | **DELETE** /budget_alerts/{budget_alert_token} |
*BudgetAlertsApi* | [**get_budget_alert**](docs/BudgetAlertsApi.md#get_budget_alert) | **GET** /budget_alerts/{budget_alert_token} |
*BudgetAlertsApi* | [**get_budget_alerts**](docs/BudgetAlertsApi.md#get_budget_alerts) | **GET** /budget_alerts |
*BudgetAlertsApi* | [**update_budget_alert**](docs/BudgetAlertsApi.md#update_budget_alert) | **PUT** /budget_alerts/{budget_alert_token} |
*BudgetsApi* | [**create_budget**](docs/BudgetsApi.md#create_budget) | **POST** /budgets |
*BudgetsApi* | [**delete_budget**](docs/BudgetsApi.md#delete_budget) | **DELETE** /budgets/{budget_token} |
*BudgetsApi* | [**get_budget**](docs/BudgetsApi.md#get_budget) | **GET** /budgets/{budget_token} |
*BudgetsApi* | [**get_budgets**](docs/BudgetsApi.md#get_budgets) | **GET** /budgets |
*BudgetsApi* | [**update_budget**](docs/BudgetsApi.md#update_budget) | **PUT** /budgets/{budget_token} |
*BusinessMetricsApi* | [**create_business_metric**](docs/BusinessMetricsApi.md#create_business_metric) | **POST** /business_metrics |
*BusinessMetricsApi* | [**delete_business_metric**](docs/BusinessMetricsApi.md#delete_business_metric) | **DELETE** /business_metrics/{business_metric_token} |
*BusinessMetricsApi* | [**get_business_metric**](docs/BusinessMetricsApi.md#get_business_metric) | **GET** /business_metrics/{business_metric_token} |
*BusinessMetricsApi* | [**get_business_metric_values**](docs/BusinessMetricsApi.md#get_business_metric_values) | **GET** /business_metrics/{business_metric_token}/values |
*BusinessMetricsApi* | [**get_business_metrics**](docs/BusinessMetricsApi.md#get_business_metrics) | **GET** /business_metrics |
*BusinessMetricsApi* | [**update_business_metric**](docs/BusinessMetricsApi.md#update_business_metric) | **PUT** /business_metrics/{business_metric_token} |
*BusinessMetricsApi* | [**update_business_metric_values_csv**](docs/BusinessMetricsApi.md#update_business_metric_values_csv) | **PUT** /business_metrics/{business_metric_token}/values.csv |
*CostsApi* | [**create_cost_report**](docs/CostsApi.md#create_cost_report) | **POST** /cost_reports |
*CostsApi* | [**create_dashboard**](docs/CostsApi.md#create_dashboard) | **POST** /dashboards |
*CostsApi* | [**delete_cost_report**](docs/CostsApi.md#delete_cost_report) | **DELETE** /cost_reports/{cost_report_token} |
*CostsApi* | [**delete_dashboard**](docs/CostsApi.md#delete_dashboard) | **DELETE** /dashboards/{dashboard_token} |
*CostsApi* | [**get_cost_report**](docs/CostsApi.md#get_cost_report) | **GET** /cost_reports/{cost_report_token} |
*CostsApi* | [**get_cost_reports**](docs/CostsApi.md#get_cost_reports) | **GET** /cost_reports |
*CostsApi* | [**get_costs**](docs/CostsApi.md#get_costs) | **GET** /costs |
*CostsApi* | [**get_dashboard**](docs/CostsApi.md#get_dashboard) | **GET** /dashboards/{dashboard_token} |
*CostsApi* | [**get_dashboards**](docs/CostsApi.md#get_dashboards) | **GET** /dashboards |
*CostsApi* | [**get_forecasted_costs**](docs/CostsApi.md#get_forecasted_costs) | **GET** /cost_reports/{cost_report_token}/forecasted_costs |
*CostsApi* | [**update_cost_report**](docs/CostsApi.md#update_cost_report) | **PUT** /cost_reports/{cost_report_token} |
*CostsApi* | [**update_dashboard**](docs/CostsApi.md#update_dashboard) | **PUT** /dashboards/{dashboard_token} |
*DashboardsApi* | [**create_dashboard**](docs/DashboardsApi.md#create_dashboard) | **POST** /dashboards |
*DashboardsApi* | [**delete_dashboard**](docs/DashboardsApi.md#delete_dashboard) | **DELETE** /dashboards/{dashboard_token} |
*DashboardsApi* | [**get_dashboard**](docs/DashboardsApi.md#get_dashboard) | **GET** /dashboards/{dashboard_token} |
*DashboardsApi* | [**get_dashboards**](docs/DashboardsApi.md#get_dashboards) | **GET** /dashboards |
*DashboardsApi* | [**update_dashboard**](docs/DashboardsApi.md#update_dashboard) | **PUT** /dashboards/{dashboard_token} |
*FinancialCommitmentReportsApi* | [**create_financial_commitment_report**](docs/FinancialCommitmentReportsApi.md#create_financial_commitment_report) | **POST** /financial_commitment_reports |
*FinancialCommitmentReportsApi* | [**delete_financial_commitment_report**](docs/FinancialCommitmentReportsApi.md#delete_financial_commitment_report) | **DELETE** /financial_commitment_reports/{financial_commitment_report_token} |
*FinancialCommitmentReportsApi* | [**get_financial_commitment_report**](docs/FinancialCommitmentReportsApi.md#get_financial_commitment_report) | **GET** /financial_commitment_reports/{financial_commitment_report_token} |
*FinancialCommitmentReportsApi* | [**get_financial_commitment_reports**](docs/FinancialCommitmentReportsApi.md#get_financial_commitment_reports) | **GET** /financial_commitment_reports |
*FinancialCommitmentReportsApi* | [**update_financial_commitment_report**](docs/FinancialCommitmentReportsApi.md#update_financial_commitment_report) | **PUT** /financial_commitment_reports/{financial_commitment_report_token} |
*FinancialCommitmentsApi* | [**get_financial_commitments**](docs/FinancialCommitmentsApi.md#get_financial_commitments) | **GET** /financial_commitments |
*FoldersApi* | [**create_folder**](docs/FoldersApi.md#create_folder) | **POST** /folders |
*FoldersApi* | [**delete_folder**](docs/FoldersApi.md#delete_folder) | **DELETE** /folders/{folder_token} |
*FoldersApi* | [**get_folder**](docs/FoldersApi.md#get_folder) | **GET** /folders/{folder_token} |
*FoldersApi* | [**get_folders**](docs/FoldersApi.md#get_folders) | **GET** /folders |
*FoldersApi* | [**update_folder**](docs/FoldersApi.md#update_folder) | **PUT** /folders/{folder_token} |
*IntegrationsApi* | [**create_azure_integration**](docs/IntegrationsApi.md#create_azure_integration) | **POST** /integrations/azure |
*IntegrationsApi* | [**create_custom_provider_integration**](docs/IntegrationsApi.md#create_custom_provider_integration) | **POST** /integrations/custom_provider |
*IntegrationsApi* | [**create_gcp_integration**](docs/IntegrationsApi.md#create_gcp_integration) | **POST** /integrations/gcp |
*IntegrationsApi* | [**create_user_costs_upload_via_csv**](docs/IntegrationsApi.md#create_user_costs_upload_via_csv) | **POST** /integrations/{integration_token}/costs.csv |
*IntegrationsApi* | [**delete_integration**](docs/IntegrationsApi.md#delete_integration) | **DELETE** /integrations/{integration_token} |
*IntegrationsApi* | [**delete_user_costs_upload**](docs/IntegrationsApi.md#delete_user_costs_upload) | **DELETE** /integrations/{integration_token}/costs/{user_costs_upload_token} |
*IntegrationsApi* | [**get_integration**](docs/IntegrationsApi.md#get_integration) | **GET** /integrations/{integration_token} |
*IntegrationsApi* | [**get_integrations**](docs/IntegrationsApi.md#get_integrations) | **GET** /integrations |
*IntegrationsApi* | [**get_user_costs_uploads**](docs/IntegrationsApi.md#get_user_costs_uploads) | **GET** /integrations/{integration_token}/costs |
*IntegrationsApi* | [**update_integration**](docs/IntegrationsApi.md#update_integration) | **PUT** /integrations/{integration_token} |
*KubernetesEfficiencyReportsApi* | [**create_kubernetes_efficiency_report**](docs/KubernetesEfficiencyReportsApi.md#create_kubernetes_efficiency_report) | **POST** /kubernetes_efficiency_reports |
*KubernetesEfficiencyReportsApi* | [**delete_kubernetes_efficiency_report**](docs/KubernetesEfficiencyReportsApi.md#delete_kubernetes_efficiency_report) | **DELETE** /kubernetes_efficiency_reports/{kubernetes_efficiency_report_token} |
*KubernetesEfficiencyReportsApi* | [**get_kubernetes_efficiency_report**](docs/KubernetesEfficiencyReportsApi.md#get_kubernetes_efficiency_report) | **GET** /kubernetes_efficiency_reports/{kubernetes_efficiency_report_token} |
*KubernetesEfficiencyReportsApi* | [**get_kubernetes_efficiency_reports**](docs/KubernetesEfficiencyReportsApi.md#get_kubernetes_efficiency_reports) | **GET** /kubernetes_efficiency_reports |
*KubernetesEfficiencyReportsApi* | [**update_kubernetes_efficiency_report**](docs/KubernetesEfficiencyReportsApi.md#update_kubernetes_efficiency_report) | **PUT** /kubernetes_efficiency_reports/{kubernetes_efficiency_report_token} |
*ManagedAccountsApi* | [**create_managed_account**](docs/ManagedAccountsApi.md#create_managed_account) | **POST** /managed_accounts |
*ManagedAccountsApi* | [**delete_managed_account**](docs/ManagedAccountsApi.md#delete_managed_account) | **DELETE** /managed_accounts/{managed_account_token} |
*ManagedAccountsApi* | [**get_managed_account**](docs/ManagedAccountsApi.md#get_managed_account) | **GET** /managed_accounts/{managed_account_token} |
*ManagedAccountsApi* | [**get_managed_accounts**](docs/ManagedAccountsApi.md#get_managed_accounts) | **GET** /managed_accounts |
*ManagedAccountsApi* | [**update_managed_account**](docs/ManagedAccountsApi.md#update_managed_account) | **PUT** /managed_accounts/{managed_account_token} |
*NetworkFlowReportsApi* | [**create_network_flow_report**](docs/NetworkFlowReportsApi.md#create_network_flow_report) | **POST** /network_flow_reports |
*NetworkFlowReportsApi* | [**delete_network_flow_report**](docs/NetworkFlowReportsApi.md#delete_network_flow_report) | **DELETE** /network_flow_reports/{network_flow_report_token} |
*NetworkFlowReportsApi* | [**get_network_flow_report**](docs/NetworkFlowReportsApi.md#get_network_flow_report) | **GET** /network_flow_reports/{network_flow_report_token} |
*NetworkFlowReportsApi* | [**get_network_flow_reports**](docs/NetworkFlowReportsApi.md#get_network_flow_reports) | **GET** /network_flow_reports |
*NetworkFlowReportsApi* | [**update_network_flow_report**](docs/NetworkFlowReportsApi.md#update_network_flow_report) | **PUT** /network_flow_reports/{network_flow_report_token} |
*PingApi* | [**ping**](docs/PingApi.md#ping) | **GET** /ping |
*PricesApi* | [**get_price**](docs/PricesApi.md#get_price) | **GET** /products/{product_id}/prices/{id} |
*PricesApi* | [**get_prices**](docs/PricesApi.md#get_prices) | **GET** /products/{product_id}/prices |
*PricesApi* | [**get_product**](docs/PricesApi.md#get_product) | **GET** /products/{id} |
*PricesApi* | [**get_products**](docs/PricesApi.md#get_products) | **GET** /products |
*RecommendationsApi* | [**get_recommendation**](docs/RecommendationsApi.md#get_recommendation) | **GET** /recommendations/{recommendation_token} |
*RecommendationsApi* | [**get_recommendation_resource**](docs/RecommendationsApi.md#get_recommendation_resource) | **GET** /recommendations/{recommendation_token}/resources/{resource_token} |
*RecommendationsApi* | [**get_recommendation_resources**](docs/RecommendationsApi.md#get_recommendation_resources) | **GET** /recommendations/{recommendation_token}/resources |
*RecommendationsApi* | [**get_recommendations**](docs/RecommendationsApi.md#get_recommendations) | **GET** /recommendations |
*ReportNotificationsApi* | [**create_report_notification**](docs/ReportNotificationsApi.md#create_report_notification) | **POST** /report_notifications |
*ReportNotificationsApi* | [**delete_report_notification**](docs/ReportNotificationsApi.md#delete_report_notification) | **DELETE** /report_notifications/{report_notification_token} |
*ReportNotificationsApi* | [**get_report_notification**](docs/ReportNotificationsApi.md#get_report_notification) | **GET** /report_notifications/{report_notification_token} |
*ReportNotificationsApi* | [**get_report_notifications**](docs/ReportNotificationsApi.md#get_report_notifications) | **GET** /report_notifications |
*ReportNotificationsApi* | [**update_report_notification**](docs/ReportNotificationsApi.md#update_report_notification) | **PUT** /report_notifications/{report_notification_token} |
*ResourceReportsApi* | [**create_resource_report**](docs/ResourceReportsApi.md#create_resource_report) | **POST** /resource_reports |
*ResourceReportsApi* | [**delete_resource_report**](docs/ResourceReportsApi.md#delete_resource_report) | **DELETE** /resource_reports/{resource_report_token} |
*ResourceReportsApi* | [**get_resource_report**](docs/ResourceReportsApi.md#get_resource_report) | **GET** /resource_reports/{resource_report_token} |
*ResourceReportsApi* | [**get_resource_reports**](docs/ResourceReportsApi.md#get_resource_reports) | **GET** /resource_reports |
*ResourceReportsApi* | [**update_resource_report**](docs/ResourceReportsApi.md#update_resource_report) | **PUT** /resource_reports/{resource_report_token} |
*ResourcesApi* | [**get_report_resources**](docs/ResourcesApi.md#get_report_resources) | **GET** /resources |
*ResourcesApi* | [**get_resource**](docs/ResourcesApi.md#get_resource) | **GET** /resources/{resource_token} |
*SavedFiltersApi* | [**create_saved_filter**](docs/SavedFiltersApi.md#create_saved_filter) | **POST** /saved_filters |
*SavedFiltersApi* | [**delete_saved_filter**](docs/SavedFiltersApi.md#delete_saved_filter) | **DELETE** /saved_filters/{saved_filter_token} |
*SavedFiltersApi* | [**get_saved_filter**](docs/SavedFiltersApi.md#get_saved_filter) | **GET** /saved_filters/{saved_filter_token} |
*SavedFiltersApi* | [**get_saved_filters**](docs/SavedFiltersApi.md#get_saved_filters) | **GET** /saved_filters |
*SavedFiltersApi* | [**update_saved_filter**](docs/SavedFiltersApi.md#update_saved_filter) | **PUT** /saved_filters/{saved_filter_token} |
*SegmentsApi* | [**create_segment**](docs/SegmentsApi.md#create_segment) | **POST** /segments |
*SegmentsApi* | [**delete_segment**](docs/SegmentsApi.md#delete_segment) | **DELETE** /segments/{segment_token} |
*SegmentsApi* | [**get_segment**](docs/SegmentsApi.md#get_segment) | **GET** /segments/{segment_token} |
*SegmentsApi* | [**get_segments**](docs/SegmentsApi.md#get_segments) | **GET** /segments |
*SegmentsApi* | [**update_segment**](docs/SegmentsApi.md#update_segment) | **PUT** /segments/{segment_token} |
*TagsApi* | [**get_tag_values**](docs/TagsApi.md#get_tag_values) | **GET** /tags/{key}/values |
*TagsApi* | [**get_tags**](docs/TagsApi.md#get_tags) | **GET** /tags |
*TagsApi* | [**update_tag**](docs/TagsApi.md#update_tag) | **PUT** /tags |
*TeamsApi* | [**create_team**](docs/TeamsApi.md#create_team) | **POST** /teams |
*TeamsApi* | [**delete_team**](docs/TeamsApi.md#delete_team) | **DELETE** /teams/{team_token} |
*TeamsApi* | [**get_team**](docs/TeamsApi.md#get_team) | **GET** /teams/{team_token} |
*TeamsApi* | [**get_teams**](docs/TeamsApi.md#get_teams) | **GET** /teams |
*TeamsApi* | [**update_team**](docs/TeamsApi.md#update_team) | **PUT** /teams/{team_token} |
*UsersApi* | [**get_user**](docs/UsersApi.md#get_user) | **GET** /users/{user_token} |
*UsersApi* | [**get_users**](docs/UsersApi.md#get_users) | **GET** /users |
*VirtualTagsApi* | [**create_virtual_tag_config**](docs/VirtualTagsApi.md#create_virtual_tag_config) | **POST** /virtual_tag_configs |
*VirtualTagsApi* | [**delete_virtual_tag_config**](docs/VirtualTagsApi.md#delete_virtual_tag_config) | **DELETE** /virtual_tag_configs/{token} |
*VirtualTagsApi* | [**get_virtual_tag_config**](docs/VirtualTagsApi.md#get_virtual_tag_config) | **GET** /virtual_tag_configs/{token} |
*VirtualTagsApi* | [**get_virtual_tag_configs**](docs/VirtualTagsApi.md#get_virtual_tag_configs) | **GET** /virtual_tag_configs |
*VirtualTagsApi* | [**update_virtual_tag_config**](docs/VirtualTagsApi.md#update_virtual_tag_config) | **PUT** /virtual_tag_configs/{token} |
*WorkspacesApi* | [**create_workspace**](docs/WorkspacesApi.md#create_workspace) | **POST** /workspaces |
*WorkspacesApi* | [**delete_workspace**](docs/WorkspacesApi.md#delete_workspace) | **DELETE** /workspaces/{workspace_token} |
*WorkspacesApi* | [**get_workspace**](docs/WorkspacesApi.md#get_workspace) | **GET** /workspaces/{workspace_token} |
*WorkspacesApi* | [**get_workspaces**](docs/WorkspacesApi.md#get_workspaces) | **GET** /workspaces |
*WorkspacesApi* | [**update_workspace**](docs/WorkspacesApi.md#update_workspace) | **PUT** /workspaces/{workspace_token} |


## Documentation For Models

 - [AccessGrant](docs/AccessGrant.md)
 - [AccessGrants](docs/AccessGrants.md)
 - [AnomalyAlert](docs/AnomalyAlert.md)
 - [AnomalyAlerts](docs/AnomalyAlerts.md)
 - [AnomalyNotification](docs/AnomalyNotification.md)
 - [AnomalyNotifications](docs/AnomalyNotifications.md)
 - [AttachedBusinessMetricForCostReport](docs/AttachedBusinessMetricForCostReport.md)
 - [AttachedCostReportForBusinessMetric](docs/AttachedCostReportForBusinessMetric.md)
 - [BillingRule](docs/BillingRule.md)
 - [BillingRules](docs/BillingRules.md)
 - [Budget](docs/Budget.md)
 - [BudgetAlert](docs/BudgetAlert.md)
 - [BudgetAlerts](docs/BudgetAlerts.md)
 - [BudgetPerformance](docs/BudgetPerformance.md)
 - [BudgetPeriod](docs/BudgetPeriod.md)
 - [Budgets](docs/Budgets.md)
 - [BusinessMetric](docs/BusinessMetric.md)
 - [BusinessMetricValue](docs/BusinessMetricValue.md)
 - [BusinessMetricValues](docs/BusinessMetricValues.md)
 - [BusinessMetrics](docs/BusinessMetrics.md)
 - [Cost](docs/Cost.md)
 - [CostReport](docs/CostReport.md)
 - [CostReports](docs/CostReports.md)
 - [Costs](docs/Costs.md)
 - [CreateAccessGrant](docs/CreateAccessGrant.md)
 - [CreateAnomalyNotification](docs/CreateAnomalyNotification.md)
 - [CreateAzureIntegration](docs/CreateAzureIntegration.md)
 - [CreateBillingRule](docs/CreateBillingRule.md)
 - [CreateBudget](docs/CreateBudget.md)
 - [CreateBudgetPeriods](docs/CreateBudgetPeriods.md)
 - [CreateBusinessMetric](docs/CreateBusinessMetric.md)
 - [CreateBusinessMetricCostReportTokensWithMetadata](docs/CreateBusinessMetricCostReportTokensWithMetadata.md)
 - [CreateBusinessMetricValues](docs/CreateBusinessMetricValues.md)
 - [CreateCostReport](docs/CreateCostReport.md)
 - [CreateCostReportBusinessMetricTokensWithMetadata](docs/CreateCostReportBusinessMetricTokensWithMetadata.md)
 - [CreateCostReportSettings](docs/CreateCostReportSettings.md)
 - [CreateCustomProviderIntegration](docs/CreateCustomProviderIntegration.md)
 - [CreateDashboard](docs/CreateDashboard.md)
 - [CreateDashboardSettings](docs/CreateDashboardSettings.md)
 - [CreateDashboardWidgets](docs/CreateDashboardWidgets.md)
 - [CreateFinancialCommitmentReport](docs/CreateFinancialCommitmentReport.md)
 - [CreateFolder](docs/CreateFolder.md)
 - [CreateGCPIntegration](docs/CreateGCPIntegration.md)
 - [CreateKubernetesEfficiencyReport](docs/CreateKubernetesEfficiencyReport.md)
 - [CreateManagedAccount](docs/CreateManagedAccount.md)
 - [CreateNetworkFlowReport](docs/CreateNetworkFlowReport.md)
 - [CreateReportNotification](docs/CreateReportNotification.md)
 - [CreateResourceReport](docs/CreateResourceReport.md)
 - [CreateSavedFilter](docs/CreateSavedFilter.md)
 - [CreateSegment](docs/CreateSegment.md)
 - [CreateSegmentReportSettings](docs/CreateSegmentReportSettings.md)
 - [CreateTeam](docs/CreateTeam.md)
 - [CreateVirtualTagConfig](docs/CreateVirtualTagConfig.md)
 - [CreateVirtualTagConfigCostMetric](docs/CreateVirtualTagConfigCostMetric.md)
 - [CreateVirtualTagConfigCostMetricAggregation](docs/CreateVirtualTagConfigCostMetricAggregation.md)
 - [CreateVirtualTagConfigValues](docs/CreateVirtualTagConfigValues.md)
 - [Dashboard](docs/Dashboard.md)
 - [DashboardWidget](docs/DashboardWidget.md)
 - [DashboardWidgetSettings](docs/DashboardWidgetSettings.md)
 - [Dashboards](docs/Dashboards.md)
 - [Errors](docs/Errors.md)
 - [FinancialCommitment](docs/FinancialCommitment.md)
 - [FinancialCommitmentReport](docs/FinancialCommitmentReport.md)
 - [FinancialCommitmentReports](docs/FinancialCommitmentReports.md)
 - [FinancialCommitments](docs/FinancialCommitments.md)
 - [Folder](docs/Folder.md)
 - [Folders](docs/Folders.md)
 - [Integration](docs/Integration.md)
 - [Integrations](docs/Integrations.md)
 - [KubernetesEfficiencyReport](docs/KubernetesEfficiencyReport.md)
 - [KubernetesEfficiencyReports](docs/KubernetesEfficiencyReports.md)
 - [ManagedAccount](docs/ManagedAccount.md)
 - [ManagedAccounts](docs/ManagedAccounts.md)
 - [NetworkFlowReport](docs/NetworkFlowReport.md)
 - [NetworkFlowReports](docs/NetworkFlowReports.md)
 - [Price](docs/Price.md)
 - [Prices](docs/Prices.md)
 - [Product](docs/Product.md)
 - [Products](docs/Products.md)
 - [ProviderResource](docs/ProviderResource.md)
 - [Recommendation](docs/Recommendation.md)
 - [RecommendationAction](docs/RecommendationAction.md)
 - [Recommendations](docs/Recommendations.md)
 - [ReportNotification](docs/ReportNotification.md)
 - [ReportNotifications](docs/ReportNotifications.md)
 - [Resource](docs/Resource.md)
 - [ResourceCost](docs/ResourceCost.md)
 - [ResourceReport](docs/ResourceReport.md)
 - [ResourceReports](docs/ResourceReports.md)
 - [Resources](docs/Resources.md)
 - [SavedFilter](docs/SavedFilter.md)
 - [SavedFilters](docs/SavedFilters.md)
 - [Segment](docs/Segment.md)
 - [SegmentReportSettings](docs/SegmentReportSettings.md)
 - [Segments](docs/Segments.md)
 - [Tag](docs/Tag.md)
 - [TagValue](docs/TagValue.md)
 - [TagValues](docs/TagValues.md)
 - [Tags](docs/Tags.md)
 - [Team](docs/Team.md)
 - [Teams](docs/Teams.md)
 - [UpdateAccessGrant](docs/UpdateAccessGrant.md)
 - [UpdateAnomalyAlert](docs/UpdateAnomalyAlert.md)
 - [UpdateAnomalyNotification](docs/UpdateAnomalyNotification.md)
 - [UpdateBillingRule](docs/UpdateBillingRule.md)
 - [UpdateBudget](docs/UpdateBudget.md)
 - [UpdateBusinessMetric](docs/UpdateBusinessMetric.md)
 - [UpdateCostReport](docs/UpdateCostReport.md)
 - [UpdateCostReportSettings](docs/UpdateCostReportSettings.md)
 - [UpdateDashboard](docs/UpdateDashboard.md)
 - [UpdateFinancialCommitmentReport](docs/UpdateFinancialCommitmentReport.md)
 - [UpdateFolder](docs/UpdateFolder.md)
 - [UpdateKubernetesEfficiencyReport](docs/UpdateKubernetesEfficiencyReport.md)
 - [UpdateManagedAccount](docs/UpdateManagedAccount.md)
 - [UpdateNetworkFlowReport](docs/UpdateNetworkFlowReport.md)
 - [UpdateReportNotification](docs/UpdateReportNotification.md)
 - [UpdateResourceReport](docs/UpdateResourceReport.md)
 - [UpdateSavedFilter](docs/UpdateSavedFilter.md)
 - [UpdateSegment](docs/UpdateSegment.md)
 - [UpdateTag](docs/UpdateTag.md)
 - [UpdateTeam](docs/UpdateTeam.md)
 - [UpdateVirtualTagConfig](docs/UpdateVirtualTagConfig.md)
 - [User](docs/User.md)
 - [UserCostsUpload](docs/UserCostsUpload.md)
 - [UserCostsUploads](docs/UserCostsUploads.md)
 - [Users](docs/Users.md)
 - [VirtualTagConfig](docs/VirtualTagConfig.md)
 - [VirtualTagConfigValue](docs/VirtualTagConfigValue.md)
 - [VirtualTagConfigValueCostMetric](docs/VirtualTagConfigValueCostMetric.md)
 - [VirtualTagConfigValueCostMetricAggregation](docs/VirtualTagConfigValueCostMetricAggregation.md)
 - [VirtualTagConfigs](docs/VirtualTagConfigs.md)
 - [Workspace](docs/Workspace.md)
 - [Workspaces](docs/Workspaces.md)


## Documentation For Authorization


## oauth2

- **Type**: OAuth
- **Flow**: application
- **Authorization URL**:
- **Scopes**:
 - **read**: Grants read access
 - **write**: Grants write access


## Author

support@vantage.sh

