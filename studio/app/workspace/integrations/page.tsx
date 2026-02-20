"use client";

import Link from "next/link";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import {
  Search,
  MessageSquare,
  CreditCard,
  BarChart3,
  ShieldCheck,
  Package,
} from "lucide-react";

const quickAccessItems = [
  {
    title: "Discovery Integrations",
    description: "Connect discovery sources and sync data for asset inventory.",
    href: "/workspace/discovery/integrations",
    icon: Search,
  },
  {
    title: "Communication",
    description: "Email, Slack, and other notification integrations.",
    href: "/workspace/communication",
    icon: MessageSquare,
  },
  {
    title: "Financials",
    description: "Payment providers, Stripe, PayPal, and billing integrations.",
    href: "/workspace/financials",
    icon: CreditCard,
  },
  {
    title: "Google Analytics",
    description: "Connect Google Analytics for site and product analytics.",
    href: "/workspace/google-analytics",
    icon: BarChart3,
  },
  {
    title: "Compliance Tools",
    description: "Configure scanners and evidence collection tools for compliance.",
    href: "/workspace/compliance/tools",
    icon: ShieldCheck,
  },
  {
    title: "WordPress",
    description: "WordPress and CMS integrations.",
    href: "/workspace/wordpress",
    icon: Package,
  },
];

export default function IntegrationsPage() {
  return (
    <div className="space-y-6">
      <div>
        <h1 className="app-page-title">Integrations</h1>
        <p className="text-muted-foreground mt-1">
          Connect and manage third-party services, data sources, and tools.
        </p>
      </div>

      <p className="text-sm text-slate-600 max-w-2xl">
        Configure discovery sources, communication channels, payment providers, analytics, and compliance tools from one place.
      </p>

      <div className="grid gap-4 md:grid-cols-2 xl:grid-cols-3">
        {quickAccessItems.map((item) => {
          const Icon = item.icon;
          return (
            <Card key={item.href} className="border border-palette-accent-1">
              <CardHeader className="flex flex-row items-center gap-3">
                <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-palette-accent-2/40">
                  <Icon className="h-5 w-5 text-palette-primary" />
                </div>
                <CardTitle className="text-base text-slate-900">{item.title}</CardTitle>
              </CardHeader>
              <CardContent className="space-y-4">
                <p className="text-sm text-slate-600">{item.description}</p>
                <Button asChild variant="outline" className="w-full">
                  <Link href={item.href}>Open {item.title}</Link>
                </Button>
              </CardContent>
            </Card>
          );
        })}
      </div>
    </div>
  );
}
