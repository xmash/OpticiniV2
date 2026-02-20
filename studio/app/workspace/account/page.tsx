"use client";

import Link from "next/link";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import {
  User,
  Settings,
  Lock,
  CreditCard,
} from "lucide-react";

const quickAccessItems = [
  {
    title: "Profile",
    description: "Update your profile, contact details, and preferences.",
    href: "/workspace/profile",
    icon: User,
  },
  {
    title: "Settings",
    description: "Monitoring, notifications, and application settings.",
    href: "/workspace/settings",
    icon: Settings,
  },
  {
    title: "Site Security",
    description: "Authentication, 2FA, session, and security options.",
    href: "/workspace/security",
    icon: Lock,
  },
  {
    title: "Financials",
    description: "Payment methods, subscriptions, and billing.",
    href: "/workspace/financials",
    icon: CreditCard,
  },
];

export default function AccountPage() {
  return (
    <div className="space-y-6">
      <div>
        <h1 className="app-page-title">Account</h1>
        <p className="text-muted-foreground mt-1">
          Manage your account, profile, security, and billing.
        </p>
      </div>

      <p className="text-sm text-slate-600 max-w-2xl">
        Update your profile and preferences, configure security and notifications, and manage payment and subscription settings.
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
