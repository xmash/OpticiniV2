"""
Canonical navigation options from All APPS doc.
Single source of truth for app sections, purpose, and sub-options with descriptions.
Used by get_navigation() to build the sidebar structure.
"""

# Icon names must match frontend iconMap (lucide-react): LayoutDashboard, Search, Gauge,
# Activity, BarChart3, Shield, FileText, Settings, TrendingUp, Database, Network, etc.

NAV_APPS_FROM_DOC = [
    {
        "id": "discovery",
        "title": "Discovery",
        "icon": "Search",
        "purpose": "Know what exists across local, hybrid, and cloud.",
        "items": [
            {"id": "discovery_overview", "title": "Overview", "description": "Entry point for discovery metrics and inventory.", "path": "/workspace/discovery/overview", "icon": "LayoutDashboard"},
            {"id": "discovery_asset_inventory", "title": "Asset Inventory", "description": "Single view of all discovered assets across environments.", "path": "/workspace/discovery/asset-inventory", "icon": "Database"},
            {"id": "discovery_network", "title": "Network Discovery", "description": "Discover and map network devices and topology.", "path": "/workspace/discovery/network-discovery", "icon": "Network"},
            {"id": "discovery_cloud", "title": "Cloud Assets", "description": "Discover and classify cloud resources (AWS, Azure, GCP, etc.).", "path": "/workspace/discovery/cloud-assets", "icon": "Cloud"},
            {"id": "discovery_app_mapping", "title": "Application Mapping", "description": "Map applications, services, and their relationships.", "path": "/workspace/discovery/application-mapping", "icon": "MapPin"},
            {"id": "discovery_dependency", "title": "Dependency Mapping", "description": "Visualize dependencies between assets and services.", "path": "/workspace/discovery/dependency-mapping", "icon": "TrendingUp"},
            {"id": "discovery_tagging", "title": "Tagging & Classification", "description": "Tag and classify assets for organization and filtering.", "path": "/workspace/discovery/tagging", "icon": "FileText"},
            {"id": "discovery_ownership", "title": "Ownership", "description": "Assign and track asset and application ownership.", "path": "/workspace/discovery/ownership", "icon": "Users"},
            {"id": "discovery_integrations", "title": "Integrations", "description": "Connect discovery sources and sync data.", "path": "/workspace/discovery/integrations", "icon": "Plug"},
            {"id": "discovery_reports", "title": "Reports", "description": "Discovery coverage, gaps, and audit reports.", "path": "/workspace/discovery/reports", "icon": "BarChart3"},
        ],
    },
    {
        "id": "health",
        "title": "Health",
        "icon": "Activity",
        "purpose": "Operational reliability and system vitality.",
        "items": [
            {"id": "health_overview", "title": "Overview", "description": "Entry point for health metrics and system status.", "path": "/workspace/health/overview", "icon": "LayoutDashboard"},
            {"id": "health_infrastructure", "title": "Infrastructure Health", "description": "Health status of servers, VMs, and infrastructure.", "path": "/workspace/health/infrastructure", "icon": "Monitor"},
            {"id": "health_service", "title": "Service Health", "description": "Status of applications and business services.", "path": "/workspace/health/service-health", "icon": "Activity"},
            {"id": "health_dependency", "title": "Dependency Health", "description": "Health of dependent systems and integrations.", "path": "/workspace/health/dependency-health", "icon": "TrendingUp"},
            {"id": "health_availability", "title": "Availability", "description": "Uptime, SLA tracking, and availability trends.", "path": "/workspace/health/availability", "icon": "Clock"},
            {"id": "health_capacity", "title": "Capacity", "description": "Capacity usage and headroom across resources.", "path": "/workspace/health/capacity", "icon": "Gauge"},
            {"id": "health_utilization", "title": "Resource Utilization", "description": "CPU, memory, disk, and network utilization.", "path": "/workspace/health/resource-utilization", "icon": "BarChart3"},
            {"id": "health_incident_signals", "title": "Incident Signals", "description": "Signals and events that may indicate incidents.", "path": "/workspace/health/incident-signals", "icon": "Activity"},
            {"id": "health_alerts", "title": "Alerts", "description": "Active alerts and alerting rules.", "path": "/workspace/health/alerts", "icon": "Activity"},
            {"id": "health_reports", "title": "Reports", "description": "Health summaries, trends, and SLA reports.", "path": "/workspace/health/reports", "icon": "BarChart3"},
        ],
    },
    {
        "id": "security",
        "title": "Security",
        "icon": "Shield",
        "purpose": "Continuous security posture and exposure visibility.",
        "items": [
            {"id": "security_overview", "title": "Overview", "description": "Entry point for security posture and key metrics.", "path": "/workspace/security/overview", "icon": "LayoutDashboard"},
            {"id": "security_vulnerabilities", "title": "Vulnerabilities", "description": "Known vulnerabilities and patch status.", "path": "/workspace/security/vulnerabilities", "icon": "Shield"},
            {"id": "security_threat_detection", "title": "Threat Detection", "description": "Detected threats and suspicious activity.", "path": "/workspace/security/threat-detection", "icon": "Shield"},
            {"id": "security_identity_access", "title": "Identity & Access", "description": "Users, roles, permissions, and access reviews.", "path": "/workspace/security/identity-access", "icon": "Lock"},
            {"id": "security_exposure", "title": "Exposure Monitoring", "description": "Exposed ports, services, and attack surface.", "path": "/workspace/security/exposure-monitoring", "icon": "Monitor"},
            {"id": "security_endpoint", "title": "Endpoint Security", "description": "Endpoint protection and hardening status.", "path": "/workspace/security/endpoint-security", "icon": "Shield"},
            {"id": "security_cloud_posture", "title": "Cloud Security Posture", "description": "Cloud misconfigurations and best practices.", "path": "/workspace/security/cloud-security-posture", "icon": "Cloud"},
            {"id": "security_network", "title": "Network Security", "description": "Network segmentation, firewall, and traffic analysis.", "path": "/workspace/security/network-security", "icon": "Network"},
            {"id": "security_incidents", "title": "Security Incidents", "description": "Security events and incident tracking.", "path": "/workspace/security/incidents", "icon": "Activity"},
            {"id": "security_reports", "title": "Reports", "description": "Security posture, compliance, and incident reports.", "path": "/workspace/security/reports", "icon": "BarChart3"},
        ],
    },
    {
        "id": "configuration",
        "title": "Configuration",
        "icon": "Settings",
        "purpose": "Baselines, drift detection, and system integrity.",
        "items": [
            {"id": "configuration_overview", "title": "Overview", "description": "Entry point for configuration and drift metrics.", "path": "/workspace/configuration/overview", "icon": "LayoutDashboard"},
            {"id": "configuration_baselines", "title": "Configuration Baselines", "description": "Defined baselines and desired state.", "path": "/workspace/configuration/baselines", "icon": "FileText"},
            {"id": "configuration_drift", "title": "Drift Detection", "description": "Current vs baseline drift and deviations.", "path": "/workspace/configuration/drift-detection", "icon": "Activity"},
            {"id": "configuration_policy", "title": "Policy Enforcement", "description": "Configuration policies and enforcement status.", "path": "/workspace/configuration/policy-enforcement", "icon": "Shield"},
            {"id": "configuration_iac", "title": "Infrastructure as Code", "description": "IaC templates and deployment state.", "path": "/workspace/configuration/iac", "icon": "FileText"},
            {"id": "configuration_settings", "title": "System Settings", "description": "Key system and application settings.", "path": "/workspace/configuration/settings", "icon": "Settings"},
            {"id": "configuration_version", "title": "Version Tracking", "description": "Configuration version history and changes.", "path": "/workspace/configuration/version-tracking", "icon": "Clock"},
            {"id": "configuration_approval", "title": "Approval Workflows", "description": "Approval gates for configuration changes.", "path": "/workspace/configuration/approval-workflows", "icon": "ShieldCheck"},
            {"id": "configuration_remediation", "title": "Remediation", "description": "Remediation actions and automation.", "path": "/workspace/configuration/remediation", "icon": "Wrench"},
            {"id": "configuration_reports", "title": "Reports", "description": "Drift, compliance, and change reports.", "path": "/workspace/configuration/reports", "icon": "BarChart3"},
        ],
    },
    {
        "id": "evidence",
        "title": "Evidence",
        "icon": "FileText",
        "purpose": "Automated audit proof and artifact management.",
        "items": [
            {"id": "evidence_overview", "title": "Overview", "description": "Entry point for evidence and audit readiness.", "path": "/workspace/evidence/overview", "icon": "LayoutDashboard"},
            {"id": "evidence_library", "title": "Evidence Library", "description": "Central store of collected evidence artifacts.", "path": "/workspace/evidence/library", "icon": "FileText"},
            {"id": "evidence_automated", "title": "Automated Collection", "description": "Evidence gathered automatically from tools and scans.", "path": "/workspace/evidence/automated-collection", "icon": "Activity"},
            {"id": "evidence_manual", "title": "Manual Uploads", "description": "Manually uploaded documents and attestations.", "path": "/workspace/evidence/manual-uploads", "icon": "FileText"},
            {"id": "evidence_mapping", "title": "Evidence Mapping", "description": "Mapping of evidence to controls and requirements.", "path": "/workspace/evidence/mapping", "icon": "MapPin"},
            {"id": "evidence_version", "title": "Version History", "description": "History and versions of evidence items.", "path": "/workspace/evidence/version-history", "icon": "Clock"},
            {"id": "evidence_expiration", "title": "Expiration Tracking", "description": "Expiration dates and renewal reminders.", "path": "/workspace/evidence/expiration-tracking", "icon": "Clock"},
            {"id": "evidence_ownership", "title": "Ownership", "description": "Owners and custodians of evidence items.", "path": "/workspace/evidence/ownership", "icon": "Users"},
            {"id": "evidence_audit_packages", "title": "Audit Packages", "description": "Packaged evidence sets for audits.", "path": "/workspace/evidence/audit-packages", "icon": "Package"},
            {"id": "evidence_reports", "title": "Reports", "description": "Evidence coverage, gaps, and audit reports.", "path": "/workspace/evidence/reports", "icon": "BarChart3"},
        ],
    },
    {
        "id": "change",
        "title": "Change",
        "icon": "TrendingUp",
        "purpose": "Change tracking and impact analysis.",
        "items": [
            {"id": "change_overview", "title": "Overview", "description": "Entry point for change activity and impact.", "path": "/workspace/change/overview", "icon": "LayoutDashboard"},
            {"id": "change_log", "title": "Change Log", "description": "Chronological log of changes across the estate.", "path": "/workspace/change/change-log", "icon": "FileText"},
            {"id": "change_deployments", "title": "Deployments", "description": "Deployment history and status.", "path": "/workspace/change/deployments", "icon": "Package"},
            {"id": "change_config", "title": "Configuration Changes", "description": "Configuration change tracking.", "path": "/workspace/change/configuration-changes", "icon": "Settings"},
            {"id": "change_infra", "title": "Infrastructure Changes", "description": "Infrastructure and environment changes.", "path": "/workspace/change/infrastructure-changes", "icon": "Database"},
            {"id": "change_approval", "title": "Approval Workflows", "description": "Change approval and sign-off.", "path": "/workspace/change/approval-workflows", "icon": "ShieldCheck"},
            {"id": "change_risk", "title": "Change Risk Scoring", "description": "Risk assessment for planned changes.", "path": "/workspace/change/risk-scoring", "icon": "Shield"},
            {"id": "change_correlation", "title": "Change-to-Incident Correlation", "description": "Link changes to incidents.", "path": "/workspace/change/incident-correlation", "icon": "Activity"},
            {"id": "change_rollbacks", "title": "Rollbacks", "description": "Rollback history and procedures.", "path": "/workspace/change/rollbacks", "icon": "Activity"},
            {"id": "change_reports", "title": "Reports", "description": "Change volume, success rate, and impact reports.", "path": "/workspace/change/reports", "icon": "BarChart3"},
        ],
    },
    {
        "id": "cost",
        "title": "Cost",
        "icon": "BarChart3",
        "purpose": "Infrastructure financial visibility (FinOps layer).",
        "items": [
            {"id": "cost_overview", "title": "Overview", "description": "Entry point for cost visibility and key metrics.", "path": "/workspace/cost/overview", "icon": "LayoutDashboard"},
            {"id": "cost_spend", "title": "Spend Analysis", "description": "Total spend breakdown and trends.", "path": "/workspace/cost/spend-analysis", "icon": "BarChart3"},
            {"id": "cost_by_asset", "title": "Cost by Asset", "description": "Cost attribution to individual assets.", "path": "/workspace/cost/by-asset", "icon": "Database"},
            {"id": "cost_by_app", "title": "Cost by Application", "description": "Cost attribution to applications and services.", "path": "/workspace/cost/by-application", "icon": "Package"},
            {"id": "cost_by_team", "title": "Cost by Team", "description": "Cost by team, project, or business unit.", "path": "/workspace/cost/by-team", "icon": "Users"},
            {"id": "cost_utilization", "title": "Utilization vs Spend", "description": "Compare usage to cost for optimization.", "path": "/workspace/cost/utilization-vs-spend", "icon": "Gauge"},
            {"id": "cost_waste", "title": "Waste Detection", "description": "Idle resources and optimization opportunities.", "path": "/workspace/cost/waste-detection", "icon": "Activity"},
            {"id": "cost_forecasting", "title": "Forecasting", "description": "Cost forecasts and projections.", "path": "/workspace/cost/forecasting", "icon": "TrendingUp"},
            {"id": "cost_budget", "title": "Budget Monitoring", "description": "Budgets, alerts, and variance.", "path": "/workspace/cost/budget-monitoring", "icon": "CreditCard"},
            {"id": "cost_reports", "title": "Reports", "description": "Cost allocation, trends, and FinOps reports.", "path": "/workspace/cost/reports", "icon": "BarChart3"},
        ],
    },
    {
        "id": "risk",
        "title": "Risk",
        "icon": "Shield",
        "purpose": "Unified business-level risk intelligence.",
        "items": [
            {"id": "risk_overview", "title": "Overview", "description": "Entry point for risk posture and key metrics.", "path": "/workspace/risk/overview", "icon": "LayoutDashboard"},
            {"id": "risk_dashboard", "title": "Risk Dashboard", "description": "Aggregated risk view and trends.", "path": "/workspace/risk/dashboard", "icon": "LayoutDashboard"},
            {"id": "risk_asset_scoring", "title": "Asset Risk Scoring", "description": "Risk scores per asset or service.", "path": "/workspace/risk/asset-scoring", "icon": "Gauge"},
            {"id": "risk_operational", "title": "Operational Risk", "description": "Risks from availability, capacity, and operations.", "path": "/workspace/risk/operational", "icon": "Activity"},
            {"id": "risk_security", "title": "Security Risk", "description": "Risks from security posture and threats.", "path": "/workspace/risk/security", "icon": "Shield"},
            {"id": "risk_compliance", "title": "Compliance Risk", "description": "Risks from compliance gaps and audits.", "path": "/workspace/risk/compliance", "icon": "ShieldCheck"},
            {"id": "risk_financial", "title": "Financial Risk", "description": "Cost and budget-related risks.", "path": "/workspace/risk/financial", "icon": "CreditCard"},
            {"id": "risk_trends", "title": "Risk Trends", "description": "How risk scores and findings trend over time.", "path": "/workspace/risk/trends", "icon": "TrendingUp"},
            {"id": "risk_register", "title": "Risk Register", "description": "Catalog of risks and mitigation status.", "path": "/workspace/risk/register", "icon": "FileText"},
            {"id": "risk_reports", "title": "Reports", "description": "Risk summaries, heat maps, and board reports.", "path": "/workspace/risk/reports", "icon": "BarChart3"},
        ],
    },
]


def build_nav_sections_from_doc():
    """Convert NAV_APPS_FROM_DOC to API shape: items have 'href' and optional 'description'/'purpose'."""
    sections = []
    for app in NAV_APPS_FROM_DOC:
        items = []
        for it in app["items"]:
            items.append({
                "id": it["id"],
                "title": it["title"],
                "href": it["path"],
                "icon": it.get("icon", "LayoutDashboard"),
                "description": it.get("description", ""),
            })
        sections.append({
            "id": app["id"],
            "title": app["title"],
            "icon": app["icon"],
            "purpose": app.get("purpose", ""),
            "items": items,
        })
    return sections
