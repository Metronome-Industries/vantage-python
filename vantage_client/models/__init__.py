"""Contains all the data models used in inputs/outputs"""

from .access_grant import AccessGrant
from .access_grants import AccessGrants
from .access_grants_links import AccessGrantsLinks
from .anomaly_alert import AnomalyAlert
from .anomaly_alerts import AnomalyAlerts
from .anomaly_alerts_links import AnomalyAlertsLinks
from .anomaly_notification import AnomalyNotification
from .anomaly_notifications import AnomalyNotifications
from .anomaly_notifications_links import AnomalyNotificationsLinks
from .attached_business_metric_for_cost_report import AttachedBusinessMetricForCostReport
from .attached_business_metric_for_cost_report_unit_scale import AttachedBusinessMetricForCostReportUnitScale
from .attached_cost_report_for_business_metric import AttachedCostReportForBusinessMetric
from .attached_cost_report_for_business_metric_unit_scale import AttachedCostReportForBusinessMetricUnitScale
from .audit_log import AuditLog
from .audit_log_object_changes import AuditLogObjectChanges
from .audit_logs import AuditLogs
from .audit_logs_links import AuditLogsLinks
from .banking_information import BankingInformation
from .bearer_token import BearerToken
from .billing_information import BillingInformation
from .billing_profile import BillingProfile
from .billing_profiles import BillingProfiles
from .billing_profiles_links import BillingProfilesLinks
from .billing_rule import BillingRule
from .billing_rules import BillingRules
from .billing_rules_links import BillingRulesLinks
from .budget import Budget
from .budget_alert import BudgetAlert
from .budget_alerts import BudgetAlerts
from .budget_alerts_links import BudgetAlertsLinks
from .budget_performance import BudgetPerformance
from .budget_period import BudgetPeriod
from .budgets import Budgets
from .budgets_links import BudgetsLinks
from .business_information import BusinessInformation
from .business_metric import BusinessMetric
from .business_metric_import_type import BusinessMetricImportType
from .business_metric_value import BusinessMetricValue
from .business_metric_values import BusinessMetricValues
from .business_metrics import BusinessMetrics
from .cloudwatch_dimension import CloudwatchDimension
from .cloudwatch_fields import CloudwatchFields
from .cloudwatch_fields_stat import CloudwatchFieldsStat
from .cost_alert import CostAlert
from .cost_alert_event import CostAlertEvent
from .cost_alert_event_metadata import CostAlertEventMetadata
from .cost_alert_events import CostAlertEvents
from .cost_alert_events_links import CostAlertEventsLinks
from .cost_alerts import CostAlerts
from .cost_alerts_links import CostAlertsLinks
from .cost_provider import CostProvider
from .cost_providers import CostProviders
from .cost_providers_links import CostProvidersLinks
from .cost_report import CostReport
from .cost_report_settings import CostReportSettings
from .cost_reports import CostReports
from .cost_reports_links import CostReportsLinks
from .cost_service import CostService
from .cost_services import CostServices
from .cost_services_links import CostServicesLinks
from .create_access_grant import CreateAccessGrant
from .create_access_grant_access import CreateAccessGrantAccess
from .create_anomaly_notification import CreateAnomalyNotification
from .create_azure_integration import CreateAzureIntegration
from .create_billing_profile_body import CreateBillingProfileBody
from .create_billing_rule import CreateBillingRule
from .create_billing_rule_type import CreateBillingRuleType
from .create_budget import CreateBudget
from .create_budget_alert_body import CreateBudgetAlertBody
from .create_budget_periods_item import CreateBudgetPeriodsItem
from .create_business_metric import CreateBusinessMetric
from .create_business_metric_cloudwatch_fields import CreateBusinessMetricCloudwatchFields
from .create_business_metric_cloudwatch_fields_dimensions_item import CreateBusinessMetricCloudwatchFieldsDimensionsItem
from .create_business_metric_cost_report_tokens_with_metadata_item import (
    CreateBusinessMetricCostReportTokensWithMetadataItem,
)
from .create_business_metric_cost_report_tokens_with_metadata_item_unit_scale import (
    CreateBusinessMetricCostReportTokensWithMetadataItemUnitScale,
)
from .create_business_metric_datadog_metric_fields import CreateBusinessMetricDatadogMetricFields
from .create_business_metric_values_item import CreateBusinessMetricValuesItem
from .create_cost_alert import CreateCostAlert
from .create_cost_export_body import CreateCostExportBody
from .create_cost_export_body_date_bin import CreateCostExportBodyDateBin
from .create_cost_export_body_schema import CreateCostExportBodySchema
from .create_cost_report import CreateCostReport
from .create_cost_report_business_metric_tokens_with_metadata_item import (
    CreateCostReportBusinessMetricTokensWithMetadataItem,
)
from .create_cost_report_business_metric_tokens_with_metadata_item_unit_scale import (
    CreateCostReportBusinessMetricTokensWithMetadataItemUnitScale,
)
from .create_cost_report_chart_type import CreateCostReportChartType
from .create_cost_report_date_bin import CreateCostReportDateBin
from .create_cost_report_date_interval import CreateCostReportDateInterval
from .create_cost_report_settings import CreateCostReportSettings
from .create_custom_provider_integration import CreateCustomProviderIntegration
from .create_dashboard import CreateDashboard
from .create_dashboard_date_bin import CreateDashboardDateBin
from .create_dashboard_date_interval import CreateDashboardDateInterval
from .create_dashboard_widgets_item import CreateDashboardWidgetsItem
from .create_dashboard_widgets_item_settings import CreateDashboardWidgetsItemSettings
from .create_dashboard_widgets_item_settings_display_type import CreateDashboardWidgetsItemSettingsDisplayType
from .create_financial_commitment_report import CreateFinancialCommitmentReport
from .create_financial_commitment_report_date_bucket import CreateFinancialCommitmentReportDateBucket
from .create_financial_commitment_report_date_interval import CreateFinancialCommitmentReportDateInterval
from .create_financial_commitment_report_on_demand_costs_scope import CreateFinancialCommitmentReportOnDemandCostsScope
from .create_folder import CreateFolder
from .create_gcp_integration import CreateGCPIntegration
from .create_invoice_body import CreateInvoiceBody
from .create_kubernetes_efficiency_report import CreateKubernetesEfficiencyReport
from .create_kubernetes_efficiency_report_aggregated_by import CreateKubernetesEfficiencyReportAggregatedBy
from .create_kubernetes_efficiency_report_date_bucket import CreateKubernetesEfficiencyReportDateBucket
from .create_kubernetes_efficiency_report_date_interval import CreateKubernetesEfficiencyReportDateInterval
from .create_managed_account import CreateManagedAccount
from .create_network_flow_report import CreateNetworkFlowReport
from .create_network_flow_report_date_interval import CreateNetworkFlowReportDateInterval
from .create_network_flow_report_flow_direction import CreateNetworkFlowReportFlowDirection
from .create_network_flow_report_flow_weight import CreateNetworkFlowReportFlowWeight
from .create_network_flow_report_groupings_item import CreateNetworkFlowReportGroupingsItem
from .create_report_notification import CreateReportNotification
from .create_resource_report import CreateResourceReport
from .create_saved_filter import CreateSavedFilter
from .create_segment import CreateSegment
from .create_segment_report_settings import CreateSegmentReportSettings
from .create_team import CreateTeam
from .create_team_role import CreateTeamRole
from .create_unit_costs_export_body import CreateUnitCostsExportBody
from .create_unit_costs_export_body_date_bin import CreateUnitCostsExportBodyDateBin
from .create_user_costs_upload_via_csv_data_body import CreateUserCostsUploadViaCsvDataBody
from .create_user_costs_upload_via_csv_files_body import CreateUserCostsUploadViaCsvFilesBody
from .create_user_feedback import CreateUserFeedback
from .create_virtual_tag_config import CreateVirtualTagConfig
from .create_virtual_tag_config_values_item import CreateVirtualTagConfigValuesItem
from .create_virtual_tag_config_values_item_cost_metric import CreateVirtualTagConfigValuesItemCostMetric
from .create_virtual_tag_config_values_item_cost_metric_aggregation import (
    CreateVirtualTagConfigValuesItemCostMetricAggregation,
)
from .create_workspace_body import CreateWorkspaceBody
from .create_workspace_body_exchange_rate_date import CreateWorkspaceBodyExchangeRateDate
from .dashboard import Dashboard
from .dashboard_date_bin import DashboardDateBin
from .dashboard_date_interval import DashboardDateInterval
from .dashboard_widget import DashboardWidget
from .dashboard_widget_settings import DashboardWidgetSettings
from .dashboard_widget_settings_display_type import DashboardWidgetSettingsDisplayType
from .dashboards import Dashboards
from .dashboards_links import DashboardsLinks
from .data_export import DataExport
from .data_export_manifest import DataExportManifest
from .datadog_metric_fields import DatadogMetricFields
from .download_invoice_body import DownloadInvoiceBody
from .download_invoice_body_file_type import DownloadInvoiceBodyFileType
from .errors import Errors
from .errors_links import ErrorsLinks
from .financial_commitment import FinancialCommitment
from .financial_commitment_report import FinancialCommitmentReport
from .financial_commitment_reports import FinancialCommitmentReports
from .financial_commitment_reports_links import FinancialCommitmentReportsLinks
from .financial_commitments import FinancialCommitments
from .financial_commitments_links import FinancialCommitmentsLinks
from .folder import Folder
from .folders import Folders
from .folders_links import FoldersLinks
from .forecasted_cost import ForecastedCost
from .forecasted_cost_links import ForecastedCostLinks
from .forecasted_cost_provider import ForecastedCostProvider
from .forecasted_costs import ForecastedCosts
from .forecasted_costs_links import ForecastedCostsLinks
from .get_costs_date_bin import GetCostsDateBin
from .get_costs_order import GetCostsOrder
from .get_forecasted_costs_provider import GetForecastedCostsProvider
from .get_integrations_provider import GetIntegrationsProvider
from .get_recommendations_category import GetRecommendationsCategory
from .get_tag_values_providers_item import GetTagValuesProvidersItem
from .get_tag_values_sort_direction import GetTagValuesSortDirection
from .get_tags_providers_item import GetTagsProvidersItem
from .get_tags_sort_direction import GetTagsSortDirection
from .get_unit_costs_date_bin import GetUnitCostsDateBin
from .get_unit_costs_order import GetUnitCostsOrder
from .integration import Integration
from .integration_status import IntegrationStatus
from .integrations import Integrations
from .integrations_links import IntegrationsLinks
from .invoice import Invoice
from .invoices import Invoices
from .invoices_links import InvoicesLinks
from .kubernetes_efficiency_report import KubernetesEfficiencyReport
from .kubernetes_efficiency_reports import KubernetesEfficiencyReports
from .kubernetes_efficiency_reports_links import KubernetesEfficiencyReportsLinks
from .managed_account import ManagedAccount
from .managed_accounts import ManagedAccounts
from .managed_accounts_links import ManagedAccountsLinks
from .me import Me
from .network_flow_report import NetworkFlowReport
from .network_flow_reports import NetworkFlowReports
from .network_flow_reports_links import NetworkFlowReportsLinks
from .price import Price
from .price_details import PriceDetails
from .prices import Prices
from .prices_links import PricesLinks
from .product import Product
from .product_details import ProductDetails
from .products import Products
from .products_links import ProductsLinks
from .provider_resource import ProviderResource
from .recommendation import Recommendation
from .recommendation_action import RecommendationAction
from .recommendations import Recommendations
from .recommendations_links import RecommendationsLinks
from .report_notification import ReportNotification
from .report_notification_change import ReportNotificationChange
from .report_notification_frequency import ReportNotificationFrequency
from .report_notifications import ReportNotifications
from .report_notifications_links import ReportNotificationsLinks
from .resource import Resource
from .resource_cost import ResourceCost
from .resource_report import ResourceReport
from .resource_report_columns import ResourceReportColumns
from .resource_reports import ResourceReports
from .resource_reports_links import ResourceReportsLinks
from .resources import Resources
from .resources_links import ResourcesLinks
from .saved_filter import SavedFilter
from .saved_filters import SavedFilters
from .saved_filters_links import SavedFiltersLinks
from .segment import Segment
from .segment_report_settings import SegmentReportSettings
from .segments import Segments
from .segments_links import SegmentsLinks
from .tag import Tag
from .tag_value import TagValue
from .tag_values import TagValues
from .tags import Tags
from .tags_links import TagsLinks
from .team import Team
from .teams import Teams
from .teams_links import TeamsLinks
from .unit_cost import UnitCost
from .unit_cost_links import UnitCostLinks
from .unit_costs import UnitCosts
from .unit_costs_links import UnitCostsLinks
from .update_access_grant import UpdateAccessGrant
from .update_access_grant_access import UpdateAccessGrantAccess
from .update_anomaly_alert import UpdateAnomalyAlert
from .update_anomaly_notification import UpdateAnomalyNotification
from .update_billing_profile_body import UpdateBillingProfileBody
from .update_billing_rule import UpdateBillingRule
from .update_budget import UpdateBudget
from .update_budget_alert_body import UpdateBudgetAlertBody
from .update_budget_periods_item import UpdateBudgetPeriodsItem
from .update_business_metric import UpdateBusinessMetric
from .update_business_metric_cloudwatch_fields import UpdateBusinessMetricCloudwatchFields
from .update_business_metric_cloudwatch_fields_dimensions_item import UpdateBusinessMetricCloudwatchFieldsDimensionsItem
from .update_business_metric_cost_report_tokens_with_metadata_item import (
    UpdateBusinessMetricCostReportTokensWithMetadataItem,
)
from .update_business_metric_cost_report_tokens_with_metadata_item_unit_scale import (
    UpdateBusinessMetricCostReportTokensWithMetadataItemUnitScale,
)
from .update_business_metric_datadog_metric_fields import UpdateBusinessMetricDatadogMetricFields
from .update_business_metric_values_csv_data_body import UpdateBusinessMetricValuesCSVDataBody
from .update_business_metric_values_csv_files_body import UpdateBusinessMetricValuesCSVFilesBody
from .update_business_metric_values_item import UpdateBusinessMetricValuesItem
from .update_cost_alert import UpdateCostAlert
from .update_cost_report import UpdateCostReport
from .update_cost_report_business_metric_tokens_with_metadata_item import (
    UpdateCostReportBusinessMetricTokensWithMetadataItem,
)
from .update_cost_report_business_metric_tokens_with_metadata_item_unit_scale import (
    UpdateCostReportBusinessMetricTokensWithMetadataItemUnitScale,
)
from .update_cost_report_chart_type import UpdateCostReportChartType
from .update_cost_report_date_bin import UpdateCostReportDateBin
from .update_cost_report_date_interval import UpdateCostReportDateInterval
from .update_cost_report_settings import UpdateCostReportSettings
from .update_dashboard import UpdateDashboard
from .update_dashboard_date_bin import UpdateDashboardDateBin
from .update_dashboard_date_interval import UpdateDashboardDateInterval
from .update_dashboard_widgets_item import UpdateDashboardWidgetsItem
from .update_dashboard_widgets_item_settings import UpdateDashboardWidgetsItemSettings
from .update_dashboard_widgets_item_settings_display_type import UpdateDashboardWidgetsItemSettingsDisplayType
from .update_financial_commitment_report import UpdateFinancialCommitmentReport
from .update_financial_commitment_report_date_bucket import UpdateFinancialCommitmentReportDateBucket
from .update_financial_commitment_report_date_interval import UpdateFinancialCommitmentReportDateInterval
from .update_financial_commitment_report_on_demand_costs_scope import UpdateFinancialCommitmentReportOnDemandCostsScope
from .update_folder import UpdateFolder
from .update_kubernetes_efficiency_report import UpdateKubernetesEfficiencyReport
from .update_kubernetes_efficiency_report_aggregated_by import UpdateKubernetesEfficiencyReportAggregatedBy
from .update_kubernetes_efficiency_report_date_bucket import UpdateKubernetesEfficiencyReportDateBucket
from .update_kubernetes_efficiency_report_date_interval import UpdateKubernetesEfficiencyReportDateInterval
from .update_managed_account import UpdateManagedAccount
from .update_managed_account_billing_information_attributes import UpdateManagedAccountBillingInformationAttributes
from .update_managed_account_business_information_attributes import UpdateManagedAccountBusinessInformationAttributes
from .update_managed_account_business_information_attributes_metadata import (
    UpdateManagedAccountBusinessInformationAttributesMetadata,
)
from .update_managed_account_business_information_attributes_metadata_custom_fields_item import (
    UpdateManagedAccountBusinessInformationAttributesMetadataCustomFieldsItem,
)
from .update_network_flow_report import UpdateNetworkFlowReport
from .update_network_flow_report_date_interval import UpdateNetworkFlowReportDateInterval
from .update_network_flow_report_flow_direction import UpdateNetworkFlowReportFlowDirection
from .update_network_flow_report_flow_weight import UpdateNetworkFlowReportFlowWeight
from .update_network_flow_report_groupings_item import UpdateNetworkFlowReportGroupingsItem
from .update_report_notification import UpdateReportNotification
from .update_resource_report import UpdateResourceReport
from .update_saved_filter import UpdateSavedFilter
from .update_segment import UpdateSegment
from .update_segment_report_settings import UpdateSegmentReportSettings
from .update_tag import UpdateTag
from .update_team import UpdateTeam
from .update_team_role import UpdateTeamRole
from .update_virtual_tag_config import UpdateVirtualTagConfig
from .update_virtual_tag_config_values_item import UpdateVirtualTagConfigValuesItem
from .update_virtual_tag_config_values_item_cost_metric import UpdateVirtualTagConfigValuesItemCostMetric
from .update_virtual_tag_config_values_item_cost_metric_aggregation import (
    UpdateVirtualTagConfigValuesItemCostMetricAggregation,
)
from .update_workspace_body import UpdateWorkspaceBody
from .update_workspace_body_currency import UpdateWorkspaceBodyCurrency
from .update_workspace_body_exchange_rate_date import UpdateWorkspaceBodyExchangeRateDate
from .user import User
from .user_costs_upload import UserCostsUpload
from .user_costs_uploads import UserCostsUploads
from .user_costs_uploads_links import UserCostsUploadsLinks
from .user_feedback import UserFeedback
from .users import Users
from .users_links import UsersLinks
from .virtual_tag_config import VirtualTagConfig
from .virtual_tag_config_value import VirtualTagConfigValue
from .virtual_tag_config_value_cost_metric import VirtualTagConfigValueCostMetric
from .virtual_tag_config_value_cost_metric_aggregation import VirtualTagConfigValueCostMetricAggregation
from .virtual_tag_configs import VirtualTagConfigs
from .workspace import Workspace
from .workspaces import Workspaces
from .workspaces_links import WorkspacesLinks

__all__ = (
    "AccessGrant",
    "AccessGrants",
    "AccessGrantsLinks",
    "AnomalyAlert",
    "AnomalyAlerts",
    "AnomalyAlertsLinks",
    "AnomalyNotification",
    "AnomalyNotifications",
    "AnomalyNotificationsLinks",
    "AttachedBusinessMetricForCostReport",
    "AttachedBusinessMetricForCostReportUnitScale",
    "AttachedCostReportForBusinessMetric",
    "AttachedCostReportForBusinessMetricUnitScale",
    "AuditLog",
    "AuditLogObjectChanges",
    "AuditLogs",
    "AuditLogsLinks",
    "BankingInformation",
    "BearerToken",
    "BillingInformation",
    "BillingProfile",
    "BillingProfiles",
    "BillingProfilesLinks",
    "BillingRule",
    "BillingRules",
    "BillingRulesLinks",
    "Budget",
    "BudgetAlert",
    "BudgetAlerts",
    "BudgetAlertsLinks",
    "BudgetPerformance",
    "BudgetPeriod",
    "Budgets",
    "BudgetsLinks",
    "BusinessInformation",
    "BusinessMetric",
    "BusinessMetricImportType",
    "BusinessMetrics",
    "BusinessMetricValue",
    "BusinessMetricValues",
    "CloudwatchDimension",
    "CloudwatchFields",
    "CloudwatchFieldsStat",
    "CostAlert",
    "CostAlertEvent",
    "CostAlertEventMetadata",
    "CostAlertEvents",
    "CostAlertEventsLinks",
    "CostAlerts",
    "CostAlertsLinks",
    "CostProvider",
    "CostProviders",
    "CostProvidersLinks",
    "CostReport",
    "CostReports",
    "CostReportSettings",
    "CostReportsLinks",
    "CostService",
    "CostServices",
    "CostServicesLinks",
    "CreateAccessGrant",
    "CreateAccessGrantAccess",
    "CreateAnomalyNotification",
    "CreateAzureIntegration",
    "CreateBillingProfileBody",
    "CreateBillingRule",
    "CreateBillingRuleType",
    "CreateBudget",
    "CreateBudgetAlertBody",
    "CreateBudgetPeriodsItem",
    "CreateBusinessMetric",
    "CreateBusinessMetricCloudwatchFields",
    "CreateBusinessMetricCloudwatchFieldsDimensionsItem",
    "CreateBusinessMetricCostReportTokensWithMetadataItem",
    "CreateBusinessMetricCostReportTokensWithMetadataItemUnitScale",
    "CreateBusinessMetricDatadogMetricFields",
    "CreateBusinessMetricValuesItem",
    "CreateCostAlert",
    "CreateCostExportBody",
    "CreateCostExportBodyDateBin",
    "CreateCostExportBodySchema",
    "CreateCostReport",
    "CreateCostReportBusinessMetricTokensWithMetadataItem",
    "CreateCostReportBusinessMetricTokensWithMetadataItemUnitScale",
    "CreateCostReportChartType",
    "CreateCostReportDateBin",
    "CreateCostReportDateInterval",
    "CreateCostReportSettings",
    "CreateCustomProviderIntegration",
    "CreateDashboard",
    "CreateDashboardDateBin",
    "CreateDashboardDateInterval",
    "CreateDashboardWidgetsItem",
    "CreateDashboardWidgetsItemSettings",
    "CreateDashboardWidgetsItemSettingsDisplayType",
    "CreateFinancialCommitmentReport",
    "CreateFinancialCommitmentReportDateBucket",
    "CreateFinancialCommitmentReportDateInterval",
    "CreateFinancialCommitmentReportOnDemandCostsScope",
    "CreateFolder",
    "CreateGCPIntegration",
    "CreateInvoiceBody",
    "CreateKubernetesEfficiencyReport",
    "CreateKubernetesEfficiencyReportAggregatedBy",
    "CreateKubernetesEfficiencyReportDateBucket",
    "CreateKubernetesEfficiencyReportDateInterval",
    "CreateManagedAccount",
    "CreateNetworkFlowReport",
    "CreateNetworkFlowReportDateInterval",
    "CreateNetworkFlowReportFlowDirection",
    "CreateNetworkFlowReportFlowWeight",
    "CreateNetworkFlowReportGroupingsItem",
    "CreateReportNotification",
    "CreateResourceReport",
    "CreateSavedFilter",
    "CreateSegment",
    "CreateSegmentReportSettings",
    "CreateTeam",
    "CreateTeamRole",
    "CreateUnitCostsExportBody",
    "CreateUnitCostsExportBodyDateBin",
    "CreateUserCostsUploadViaCsvDataBody",
    "CreateUserCostsUploadViaCsvFilesBody",
    "CreateUserFeedback",
    "CreateVirtualTagConfig",
    "CreateVirtualTagConfigValuesItem",
    "CreateVirtualTagConfigValuesItemCostMetric",
    "CreateVirtualTagConfigValuesItemCostMetricAggregation",
    "CreateWorkspaceBody",
    "CreateWorkspaceBodyExchangeRateDate",
    "Dashboard",
    "DashboardDateBin",
    "DashboardDateInterval",
    "Dashboards",
    "DashboardsLinks",
    "DashboardWidget",
    "DashboardWidgetSettings",
    "DashboardWidgetSettingsDisplayType",
    "DatadogMetricFields",
    "DataExport",
    "DataExportManifest",
    "DownloadInvoiceBody",
    "DownloadInvoiceBodyFileType",
    "Errors",
    "ErrorsLinks",
    "FinancialCommitment",
    "FinancialCommitmentReport",
    "FinancialCommitmentReports",
    "FinancialCommitmentReportsLinks",
    "FinancialCommitments",
    "FinancialCommitmentsLinks",
    "Folder",
    "Folders",
    "FoldersLinks",
    "ForecastedCost",
    "ForecastedCostLinks",
    "ForecastedCostProvider",
    "ForecastedCosts",
    "ForecastedCostsLinks",
    "GetCostsDateBin",
    "GetCostsOrder",
    "GetForecastedCostsProvider",
    "GetIntegrationsProvider",
    "GetRecommendationsCategory",
    "GetTagsProvidersItem",
    "GetTagsSortDirection",
    "GetTagValuesProvidersItem",
    "GetTagValuesSortDirection",
    "GetUnitCostsDateBin",
    "GetUnitCostsOrder",
    "Integration",
    "Integrations",
    "IntegrationsLinks",
    "IntegrationStatus",
    "Invoice",
    "Invoices",
    "InvoicesLinks",
    "KubernetesEfficiencyReport",
    "KubernetesEfficiencyReports",
    "KubernetesEfficiencyReportsLinks",
    "ManagedAccount",
    "ManagedAccounts",
    "ManagedAccountsLinks",
    "Me",
    "NetworkFlowReport",
    "NetworkFlowReports",
    "NetworkFlowReportsLinks",
    "Price",
    "PriceDetails",
    "Prices",
    "PricesLinks",
    "Product",
    "ProductDetails",
    "Products",
    "ProductsLinks",
    "ProviderResource",
    "Recommendation",
    "RecommendationAction",
    "Recommendations",
    "RecommendationsLinks",
    "ReportNotification",
    "ReportNotificationChange",
    "ReportNotificationFrequency",
    "ReportNotifications",
    "ReportNotificationsLinks",
    "Resource",
    "ResourceCost",
    "ResourceReport",
    "ResourceReportColumns",
    "ResourceReports",
    "ResourceReportsLinks",
    "Resources",
    "ResourcesLinks",
    "SavedFilter",
    "SavedFilters",
    "SavedFiltersLinks",
    "Segment",
    "SegmentReportSettings",
    "Segments",
    "SegmentsLinks",
    "Tag",
    "Tags",
    "TagsLinks",
    "TagValue",
    "TagValues",
    "Team",
    "Teams",
    "TeamsLinks",
    "UnitCost",
    "UnitCostLinks",
    "UnitCosts",
    "UnitCostsLinks",
    "UpdateAccessGrant",
    "UpdateAccessGrantAccess",
    "UpdateAnomalyAlert",
    "UpdateAnomalyNotification",
    "UpdateBillingProfileBody",
    "UpdateBillingRule",
    "UpdateBudget",
    "UpdateBudgetAlertBody",
    "UpdateBudgetPeriodsItem",
    "UpdateBusinessMetric",
    "UpdateBusinessMetricCloudwatchFields",
    "UpdateBusinessMetricCloudwatchFieldsDimensionsItem",
    "UpdateBusinessMetricCostReportTokensWithMetadataItem",
    "UpdateBusinessMetricCostReportTokensWithMetadataItemUnitScale",
    "UpdateBusinessMetricDatadogMetricFields",
    "UpdateBusinessMetricValuesCSVDataBody",
    "UpdateBusinessMetricValuesCSVFilesBody",
    "UpdateBusinessMetricValuesItem",
    "UpdateCostAlert",
    "UpdateCostReport",
    "UpdateCostReportBusinessMetricTokensWithMetadataItem",
    "UpdateCostReportBusinessMetricTokensWithMetadataItemUnitScale",
    "UpdateCostReportChartType",
    "UpdateCostReportDateBin",
    "UpdateCostReportDateInterval",
    "UpdateCostReportSettings",
    "UpdateDashboard",
    "UpdateDashboardDateBin",
    "UpdateDashboardDateInterval",
    "UpdateDashboardWidgetsItem",
    "UpdateDashboardWidgetsItemSettings",
    "UpdateDashboardWidgetsItemSettingsDisplayType",
    "UpdateFinancialCommitmentReport",
    "UpdateFinancialCommitmentReportDateBucket",
    "UpdateFinancialCommitmentReportDateInterval",
    "UpdateFinancialCommitmentReportOnDemandCostsScope",
    "UpdateFolder",
    "UpdateKubernetesEfficiencyReport",
    "UpdateKubernetesEfficiencyReportAggregatedBy",
    "UpdateKubernetesEfficiencyReportDateBucket",
    "UpdateKubernetesEfficiencyReportDateInterval",
    "UpdateManagedAccount",
    "UpdateManagedAccountBillingInformationAttributes",
    "UpdateManagedAccountBusinessInformationAttributes",
    "UpdateManagedAccountBusinessInformationAttributesMetadata",
    "UpdateManagedAccountBusinessInformationAttributesMetadataCustomFieldsItem",
    "UpdateNetworkFlowReport",
    "UpdateNetworkFlowReportDateInterval",
    "UpdateNetworkFlowReportFlowDirection",
    "UpdateNetworkFlowReportFlowWeight",
    "UpdateNetworkFlowReportGroupingsItem",
    "UpdateReportNotification",
    "UpdateResourceReport",
    "UpdateSavedFilter",
    "UpdateSegment",
    "UpdateSegmentReportSettings",
    "UpdateTag",
    "UpdateTeam",
    "UpdateTeamRole",
    "UpdateVirtualTagConfig",
    "UpdateVirtualTagConfigValuesItem",
    "UpdateVirtualTagConfigValuesItemCostMetric",
    "UpdateVirtualTagConfigValuesItemCostMetricAggregation",
    "UpdateWorkspaceBody",
    "UpdateWorkspaceBodyCurrency",
    "UpdateWorkspaceBodyExchangeRateDate",
    "User",
    "UserCostsUpload",
    "UserCostsUploads",
    "UserCostsUploadsLinks",
    "UserFeedback",
    "Users",
    "UsersLinks",
    "VirtualTagConfig",
    "VirtualTagConfigs",
    "VirtualTagConfigValue",
    "VirtualTagConfigValueCostMetric",
    "VirtualTagConfigValueCostMetricAggregation",
    "Workspace",
    "Workspaces",
    "WorkspacesLinks",
)
